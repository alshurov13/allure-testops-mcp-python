"""
Test Plan Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
test_plan_controller_tools = [
    {
        "name": "allure_findAllByProject",
        "description": "Find all test plans for given project",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "name": {
                    "type": "string",
                    "description": "name"
                },
                "treeId": {
                    "type": "number",
                    "description": "treeId"
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
        "name": "allure_test_plan_create",
        "description": "Create a new test plan",
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
        "name": "allure_test_plan_suggest",
        "description": "Suggest for test plans",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "query"
                },
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "id": {
                    "type": "array",
                    "description": "id",
                    "items": {
                        "type": "string"
                    }
                },
                "ignoreId": {
                    "type": "array",
                    "description": "ignoreId",
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
            }
        }
    },
    {
        "name": "allure_test_plan_delete",
        "description": "Delete test plan by given id",
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
    },
    {
        "name": "allure_test_plan_findOne",
        "description": "Find test plan by id",
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
    },
    {
        "name": "allure_test_plan_patch",
        "description": "Patch test plan",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "id",
                "body"
            ]
        }
    },
    {
        "name": "allure_test_plan_assign",
        "description": "Assign test plan test cases to user",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "id",
                "body"
            ]
        }
    },
    {
        "name": "allure_getDiff",
        "description": "Get test plan test cases changes",
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
    },
    {
        "name": "allure_getJobs",
        "description": "Get test plan jobs statistic",
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
    },
    {
        "name": "allure_setJobParameters",
        "description": "Configure test plan job parameters",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "id",
                "body"
            ]
        }
    },
    {
        "name": "allure_test_plan_getMembers",
        "description": "Get test plan members statistic",
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
    },
    {
        "name": "allure_resetJobs",
        "description": "Reset test plan",
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
    },
    {
        "name": "allure_test_plan_run",
        "description": "Run test plan by given id",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "id",
                "body"
            ]
        }
    },
    {
        "name": "allure_sync",
        "description": "Sync test plan",
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
    },
    {
        "name": "allure_test_plan_getGroups",
        "description": "Find tree groups for node",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "treeId": {
                    "type": "number",
                    "description": "treeId"
                },
                "path": {
                    "type": "array",
                    "description": "path",
                    "items": {
                        "type": "string"
                    }
                },
                "username": {
                    "type": "string",
                    "description": "username"
                },
                "jobId": {
                    "type": "number",
                    "description": "jobId"
                },
                "manual": {
                    "type": "boolean",
                    "description": "manual"
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
                "id"
            ]
        }
    },
    {
        "name": "allure_test_plan_getLeafs",
        "description": "Find tree leafs for node",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "treeId": {
                    "type": "number",
                    "description": "treeId"
                },
                "path": {
                    "type": "array",
                    "description": "path",
                    "items": {
                        "type": "string"
                    }
                },
                "username": {
                    "type": "string",
                    "description": "username"
                },
                "jobId": {
                    "type": "number",
                    "description": "jobId"
                },
                "manual": {
                    "type": "boolean",
                    "description": "manual"
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
                "id"
            ]
        }
    }
]

async def handle_test_plan_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle test_plan controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for test_plan not yet implemented")
