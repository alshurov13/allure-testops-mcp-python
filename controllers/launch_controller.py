"""
Launch Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
launch_controller_tools = [
    {
        "name": "allure_launch_findAll",
        "description": "Find all launches preview",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "search": {
                    "type": "string",
                    "description": "search"
                },
                "filterId": {
                    "type": "number",
                    "description": "filterId"
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
        "name": "allure_launch_create",
        "description": "Create a new launch",
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
        "name": "allure_merge",
        "description": "Merge launches",
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
        "name": "allure_launch_createViaEvent",
        "description": "Create a new launch via event",
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
        "name": "allure_launch_suggest",
        "description": "Suggest for launches",
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
        "name": "allure_launch_delete",
        "description": "Delete launch by id",
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
        "name": "allure_launch_findOne",
        "description": "Find launch by id",
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
        "name": "allure_launch_patch",
        "description": "Patch launch",
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
        "name": "allure_getAssignees",
        "description": "Get launch assignees",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "query": {
                    "type": "string",
                    "description": "query"
                }
            },
            "required": [
                "id"
            ]
        }
    },
    {
        "name": "allure_close",
        "description": "Close launch",
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
        "name": "allure_copyLaunch",
        "description": "Copy launch",
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
        "name": "allure_launch_getDefects",
        "description": "Get launch defects",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
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
        "name": "allure_applyDefectMatchers",
        "description": "Apply defect matchers to launch",
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
        "name": "allure_getDuration",
        "description": "Get launch duration",
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
        "name": "allure_getEnvironment",
        "description": "Get launch environment",
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
        "name": "allure_launch_getJobs",
        "description": "Get launch jobs",
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
        "name": "allure_suggestJobs",
        "description": "Suggest launch jobs",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "array",
                    "description": "id",
                    "items": {
                        "type": "string"
                    }
                },
                "query": {
                    "type": "string",
                    "description": "query"
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
            },
            "required": [
                "id"
            ]
        }
    },
    {
        "name": "allure_getMemberStats",
        "description": "Get member stats widget data",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
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
        "name": "allure_getMutedTestResults",
        "description": "Get muted test results",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
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
        "name": "allure_getProgress",
        "description": "Get progress widget data",
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
        "name": "allure_reopen",
        "description": "Reopen launch",
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
        "name": "allure_getRetries",
        "description": "Get retries widget data",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
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
        "name": "allure_getStatistic",
        "description": "Get launch statistic",
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
        "name": "allure_addTestCases",
        "description": "Add test cases to launch",
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
        "name": "allure_getTesters",
        "description": "Get launch testers",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "query": {
                    "type": "string",
                    "description": "query"
                }
            },
            "required": [
                "id"
            ]
        }
    },
    {
        "name": "allure_addTestPlan",
        "description": "Add test plan to launch",
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
        "name": "allure_getUnresolvedTestResults",
        "description": "Get unresolved test results",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
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
        "name": "allure_getVariables",
        "description": "Get variables widget data",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
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
        "name": "allure_getWidgetTree",
        "description": "Get suites for tree data",
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
                "id",
                "treeId"
            ]
        }
    }
]

async def handle_launch_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle launch controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for launch not yet implemented")
