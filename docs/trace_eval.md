# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [Điền Họ và Tên]  
> **Mã Sinh Viên / Mã Học viên:** [Điền MSSV]  
> **Chủ đề Lựa chọn:** Đề tài 1.2 — Trợ lý Quản lý Thư viện & Tài liệu VinUni (Library Assistant)

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Hệ thống cần suy luận chuỗi hành động: Tra cứu sách trước (search_book) rồi mới quyết định gia hạn hay không (renew_book). |
| **2. Tool Interaction** | 5 / 5 | Giao tiếp 2 chiều với MCP Server (vinuni-library-mcp-server) qua JSON-RPC 2.0 để query DB sách. |
| **3. Dynamic Decision** | 4 / 5 | Kết quả trả về (NOT_FOUND, ERROR, SUCCESS) quyết định câu trả lời Final Answer tiếp theo của Agent. |
| **4. Long Horizon Goal** | 5 / 5 | Có khả năng duy trì mục tiêu xử lý các thao tác phức tạp từ người dùng qua nhiều lượt tool calls. |
| **TỔNG ĐIỂM AGENTIC FIT** | **18 / 20** | *Đề tài cực kỳ phù hợp để áp dụng kiến trúc ReAct Agent thay vì Chatbot truyền thống.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật (OpenAI GPT-4o-mini):

```json
[
  {
    "step": 1,
    "query": "Tra cuu thong tin sach co ma LIB-001.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "search_book",
    "arguments": {
      "book_id": "LIB-001"
    },
    "observation": {
      "status": "SUCCESS",
      "book_id": "LIB-001",
      "data": {
        "title": "Trí Tuệ Nhân Tạo — Tương Lai và Hiện Tại",
        "author": "PGS.TS Nguyễn Văn Linh",
        "category": "Khoa học Máy tính / AI",
        "shelf_location": "Kệ A3 - Tầng 2",
        "total_copies": 3,
        "available_copies": 2,
        "status": "Có sẵn",
        "due_date": null,
        "borrowed_by": null
      }
    }
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt (TC02, TC03, TC04, TC05).
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!

