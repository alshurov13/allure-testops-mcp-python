"""
Custom Field Project Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
custom_field_project_controller_tools = [
    {
        "name": "allure_custom_field_project_findOne",
        "description": "GET /api/cfproject",
        "inputSchema": {
            "type": "object",
            "properties": {
                "customFieldId": {
                    "type": "number",
                    "description": "customFieldId"
                },
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                }
            },
            "required": [
                "customFieldId",
                "projectId"
            ]
        }
    },
    {
        "name": "allure_custom_field_project_add",
        "description": "Add custom field to projects",
        "inputSchema": {
            "type": "object",
            "properties": {
                "customFieldId": {
                    "type": "number",
                    "description": "customFieldId"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "customFieldId",
                "body"
            ]
        }
    },
    {
        "name": "allure_addToProject",
        "description": "Add custom fields to project",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
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
        "name": "allure_setDefault",
        "description": "Deprecated. Use PATCH /api/project/{projectId}/cf/{cfId} instead",
        "inputSchema": {
            "type": "object",
            "properties": {
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "body"
            ]
        }
    },
    {
        "name": "allure_custom_field_project_cfDelta",
        "description": "Find missing custom fields",
        "inputSchema": {
            "type": "object",
            "properties": {
                "toProjectId": {
                    "type": "number",
                    "description": "toProjectId"
                },
                "testCaseId": {
                    "type": "array",
                    "description": "testCaseId",
                    "items": {
                        "type": "string"
                    }
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "toProjectId",
                "body"
            ]
        }
    },
    {
        "name": "allure_findProjectsByCustomField",
        "description": "Find projects that use specified custom field",
        "inputSchema": {
            "type": "object",
            "properties": {
                "customFieldId": {
                    "type": "number",
                    "description": "customFieldId"
                },
                "query": {
                    "type": "string",
                    "description": "query"
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
                "customFieldId"
            ]
        }
    },
    {
        "name": "allure_custom_field_project_remove",
        "description": "Remove custom field from project",
        "inputSchema": {
            "type": "object",
            "properties": {
                "customFieldId": {
                    "type": "number",
                    "description": "customFieldId"
                },
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                }
            },
            "required": [
                "customFieldId",
                "projectId"
            ]
        }
    },
    {
        "name": "allure_setRequired",
        "description": "Deprecated. Use PATCH /api/project/{projectId}/cf/{cfId} instead",
        "inputSchema": {
            "type": "object",
            "properties": {
                "customFieldId": {
                    "type": "number",
                    "description": "customFieldId"
                },
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "required": {
                    "type": "boolean",
                    "description": "required"
                }
            },
            "required": [
                "customFieldId",
                "projectId",
                "required"
            ]
        }
    }
]

async def handle_custom_field_project_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle custom_field_project controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for custom_field_project not yet implemented")
