"""
Dashboard Template Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
dashboard_template_controller_tools = [
    {
        "name": "allure_dashboard_template_findAll",
        "description": "GET /api/dashboard-template",
        "inputSchema": {
            "type": "object",
            "properties": {
                "page": {
                    "type": "number",
                    "description": "Zero-based page index (0..N)"
                },
                "size": {
                    "type": "number",
                    "description": "The size of the page to be returned"
                },
                "sort": {
                    "type": "array",
                    "description": "Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.",
                    "items": {
                        "type": "string"
                    }
                }
            }
        }
    },
    {
        "name": "allure_dashboard_template_findOne",
        "description": "GET /api/dashboard-template/{id}",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                }
            },
            "required": [
                "id"
            ]
        }
    }
]

async def handle_dashboard_template_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle dashboard_template controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for dashboard_template not yet implemented")
