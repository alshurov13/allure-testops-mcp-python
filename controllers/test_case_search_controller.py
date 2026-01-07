"""
Test Case Search Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
test_case_search_controller_tools = [
    {
        "name": "allure_test_case_search_search",
        "description": "Find all test cases by given AQL",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "rql": {
                    "type": "string",
                    "description": "rql"
                },
                "deleted": {
                    "type": "boolean",
                    "description": "deleted"
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
                "projectId",
                "rql"
            ]
        }
    },
    {
        "name": "allure_test_case_search_validateQuery",
        "description": "Find all test cases by given AQL",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "rql": {
                    "type": "string",
                    "description": "rql"
                },
                "deleted": {
                    "type": "boolean",
                    "description": "deleted"
                }
            },
            "required": [
                "projectId",
                "rql"
            ]
        }
    }
]

async def handle_test_case_search_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle test_case_search controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for test_case_search not yet implemented")
