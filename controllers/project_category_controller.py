"""
Project Category Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
project_category_controller_tools = [
    {
        "name": "allure_project_category_findAll",
        "description": "GET /api/project/{projectId}/category",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                },
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
            },
            "required": [
                "projectId"
            ]
        }
    },
    {
        "name": "allure_project_category_add",
        "description": "POST /api/project/{projectId}/category",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "projectId",
                "body"
            ]
        }
    },
    {
        "name": "allure_project_category_remove",
        "description": "POST /api/project/{projectId}/category/remove",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "projectId",
                "body"
            ]
        }
    }
]

async def handle_project_category_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle project_category controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for project_category not yet implemented")
