"""
Project Access Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
project_access_controller_tools = [
    {
        "name": "allure_deleteUsers",
        "description": "Delete collaborators from project",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                },
                "username": {
                    "type": "array",
                    "description": "username",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "projectId",
                "username"
            ]
        }
    },
    {
        "name": "allure_getProjectCollaborators",
        "description": "Get project collaborators",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                },
                "query": {
                    "type": "string",
                    "description": "query"
                },
                "permissionsSetId": {
                    "type": "array",
                    "description": "permissionsSetId",
                    "items": {
                        "type": "string"
                    }
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
        "name": "allure_addProjectCollaborators",
        "description": "Add collaborators to project",
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
        "name": "allure_deleteProjectGroups",
        "description": "Delete groups from project",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                },
                "groupId": {
                    "type": "array",
                    "description": "groupId",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "projectId",
                "groupId"
            ]
        }
    },
    {
        "name": "allure_getProjectAccessGroups",
        "description": "Get project access groups",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                },
                "query": {
                    "type": "string",
                    "description": "query"
                },
                "permissionsSetId": {
                    "type": "array",
                    "description": "permissionsSetId",
                    "items": {
                        "type": "string"
                    }
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
        "name": "allure_addProjectGroups",
        "description": "Add groups to project",
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

async def handle_project_access_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle project_access controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for project_access not yet implemented")
