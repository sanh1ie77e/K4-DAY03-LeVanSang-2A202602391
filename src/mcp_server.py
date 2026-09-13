"""
🔌 MODEL CONTEXT PROTOCOL (MCP) SERVER MODULE
Mô phỏng kiến trúc MCP Server (Client-Server Architecture) cung cấp công cụ chuẩn hóa.
"""

import json
import sys
from typing import Dict, Any, List
from tools import TOOLS_SCHEMA, dispatch_tool_call

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MCPAcademicServer:
    """
    Giả lập MCP Server tuân thủ chuẩn giao thức Model Context Protocol
    """
    def __init__(self, server_name: str = "vinuni-library-mcp-server"):
        self.server_name = server_name
        self.version = "2026.1.0"

        
    def list_tools(self) -> List[Dict[str, Any]]:
        """Trả về danh sách các Tools chuẩn giao thức MCP"""
        return TOOLS_SCHEMA
        
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        [TASK 2.1] HỌC VIÊN HOÀN THIỆN HÀM THỰC THI TOOL TRÊN MCP SERVER
        Thực thi request gọi Tool theo chuẩn MCP JSON-RPC
        """
        # --------------------------------------------------------------------------
        # TODO 2.1: Hoàn thiện hàm gọi Tool chuẩn MCP JSON-RPC 2.0
        # 1. Gọi dispatch_tool_call() lấy chuỗi JSON kết quả từ Tool Router
        raw_result = dispatch_tool_call(tool_name, arguments)
        # 2. Chuyển đổi chuỗi JSON sang Python Dictionary
        content = json.loads(raw_result)
        # 3. Đóng gói và trả về phản hồi chuẩn MCP JSON-RPC 2.0
        return {
            "jsonrpc": "2.0",
            "server": self.server_name,
            "tool": tool_name,
            "result": content
        }


if __name__ == "__main__":
    print("==========================================================")
    print("🔌 KIEM THU DOC LAP MCP SERVER (vinuni-library-mcp-server)")
    print("==========================================================")

    server = MCPAcademicServer()
    tools = server.list_tools()
    print(f"OK Khoi tao thanh cong MCP Server: {server.server_name} (Version: {server.version})")
    print(f"So luong Tools cong bo: {len(tools)}")

    renew_tool = next((t for t in tools if t.get("name") == "renew_book"), None)
    if renew_tool and not renew_tool.get("parameters", {}).get("properties"):
        print("PENDING [TODO 1.2]: Tool 'renew_book' chua duoc dinh nghia properties.")
    else:
        print("OK [TODO 1.2]: Tool 'renew_book' da co schema day du.")

    test_result = server.call_tool("search_book", {"book_id": "LIB-001"})
    if not test_result:
        print("PENDING [TODO 2.1]: Ham call_tool() dang tra ve rong!")
    else:
        print(f"OK [TODO 2.1]: Test dispatch tool 'search_book' thanh cong:")
        print(f"   Phan hoi JSON-RPC: {json.dumps(test_result, ensure_ascii=False)}")


