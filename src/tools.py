"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Đề tài 1.2 — Trợ lý Quản lý Thư viện & Tài liệu VinUni.
Tra cứu vị trí sách, tình trạng mượn/trả và gia hạn tài liệu.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu thông tin sách theo mã sách
    {
        "name": "search_book",
        "description": "Tra cứu thông tin sách trong thư viện VinUni theo mã sách. Trả về tên sách, tác giả, vị trí kệ sách, tình trạng mượn/trả và ngày trả dự kiến.",
        "parameters": {
            "type": "object",
            "properties": {
                "book_id": {
                    "type": "string",
                    "description": "Mã sách cần tra cứu (ví dụ: 'LIB-001')"
                }
            },
            "required": ["book_id"]
        }
    },

    # Tool 2: Gia hạn mượn tài liệu
    {
        "name": "renew_book",
        "description": "Gia hạn thời gian mượn tài liệu trong thư viện VinUni cho thành viên. Yêu cầu mã thành viên và mã sách cần gia hạn.",
        "parameters": {
            "type": "object",
            "properties": {
                "member_id": {
                    "type": "string",
                    "description": "Mã thành viên thư viện cần gia hạn (ví dụ: 'MEM-001')"
                },
                "book_id": {
                    "type": "string",
                    "description": "Mã sách cần gia hạn mượn (ví dụ: 'LIB-002')"
                },
                "days": {
                    "type": "integer",
                    "description": "Số ngày muốn gia hạn thêm (mặc định: 14 ngày)"
                }
            },
            "required": ["member_id", "book_id"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_BOOK_DATABASE = {
    "LIB-001": {
        "title": "Trí Tuệ Nhân Tạo — Tương Lai và Hiện Tại",
        "author": "PGS.TS Nguyễn Văn Linh",
        "category": "Khoa học Máy tính / AI",
        "shelf_location": "Kệ A3 - Tầng 2",
        "total_copies": 3,
        "available_copies": 2,
        "status": "Có sẵn",
        "due_date": None,
        "borrowed_by": None
    },
    "LIB-002": {
        "title": "Học Máy Cơ Bản với Python",
        "author": "TS. Trần Thị Mai",
        "category": "Khoa học Máy tính / Machine Learning",
        "shelf_location": "Kệ B1 - Tầng 2",
        "total_copies": 2,
        "available_copies": 0,
        "status": "Đang được mượn",
        "due_date": "20/09/2026",
        "borrowed_by": "MEM-001 (Nguyễn Văn An)"
    },
    "LIB-003": {
        "title": "Deep Learning với TensorFlow và Keras",
        "author": "ThS. Lê Quang Minh",
        "category": "Khoa học Máy tính / Deep Learning",
        "shelf_location": "Kệ B2 - Tầng 2",
        "total_copies": 1,
        "available_copies": 0,
        "status": "Đang được mượn",
        "due_date": "15/09/2026",
        "borrowed_by": "MEM-002 (Trần Thị Bình)"
    },
    "LIB-004": {
        "title": "Giải tích Toán học Ứng dụng",
        "author": "GS. Phạm Văn Hùng",
        "category": "Toán học",
        "shelf_location": "Kệ C5 - Tầng 3",
        "total_copies": 5,
        "available_copies": 4,
        "status": "Có sẵn",
        "due_date": None,
        "borrowed_by": None
    }
}

MOCK_MEMBER_DATABASE = {
    "MEM-001": {"name": "Nguyễn Văn An", "class": "AI-K4", "borrowed_books": ["LIB-002"]},
    "MEM-002": {"name": "Trần Thị Bình", "class": "AI-K4", "borrowed_books": ["LIB-003"]},
}


def execute_search_book(book_id: str) -> str:
    """Thực thi tra cứu thông tin sách theo mã sách"""
    book = MOCK_BOOK_DATABASE.get(book_id.strip().upper())
    if book:
        return json.dumps({
            "status": "SUCCESS",
            "book_id": book_id,
            "data": book
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy sách có mã '{book_id}' trong hệ thống thư viện."
        }, ensure_ascii=False)


def execute_renew_book(member_id: str, book_id: str, days: int = 14) -> str:
    """Thực thi gia hạn mượn tài liệu"""
    member = MOCK_MEMBER_DATABASE.get(member_id.strip().upper())
    book = MOCK_BOOK_DATABASE.get(book_id.strip().upper())

    if not member:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy thành viên có mã '{member_id}'."
        }, ensure_ascii=False)

    if not book:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy sách có mã '{book_id}'."
        }, ensure_ascii=False)

    if book_id.strip().upper() not in member.get("borrowed_books", []):
        return json.dumps({
            "status": "ERROR",
            "message": f"Thành viên {member['name']} ({member_id}) chưa mượn sách '{book['title']}' ({book_id})."
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "renew_id": f"RNW-{member_id}-{book_id}",
        "member": member["name"],
        "book_title": book["title"],
        "book_id": book_id,
        "extended_days": days,
        "message": f"Đã gia hạn thành công! Thành viên {member['name']} gia hạn sách '{book['title']}' thêm {days} ngày."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "search_book": execute_search_book,
    "renew_book": execute_renew_book
}


def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)

