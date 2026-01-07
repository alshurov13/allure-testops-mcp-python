"""
Test Case Tree Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
test_case_tree_controller_tools = [
    {
        "name": "allure_test_case_tree_countLeaves",
        "description": "Count all tree leaves for given path and filter",
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
                "treeId": {
                    "type": "number",
                    "description": "treeId"
                },
                "filterId": {
                    "type": "number",
                    "description": "filterId"
                },
                "deleted": {
                    "type": "boolean",
                    "description": "deleted"
                },
                "path": {
                    "type": "array",
                    "description": "path",
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
        "name": "allure_getGroups",
        "description": "Find tree groups for node (AQL)",
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
                "treeId": {
                    "type": "number",
                    "description": "treeId"
                },
                "filterId": {
                    "type": "number",
                    "description": "filterId"
                },
                "path": {
                    "type": "array",
                    "description": "path",
                    "items": {
                        "type": "string"
                    }
                },
                "withEmptyCategories": {
                    "type": "boolean",
                    "description": "withEmptyCategories"
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
                },
                "baseRql": {
                    "type": "string",
                    "description": "baseRql"
                }
            },
            "required": [
                "projectId"
            ]
        }
    },
    {
        "name": "allure_test_case_tree_addGroup",
        "description": "Add a new group (AQL)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "filterId": {
                    "type": "number",
                    "description": "filterId"
                },
                "search": {
                    "type": "string",
                    "description": "search"
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
                "baseRql": {
                    "type": "string",
                    "description": "baseRql"
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
        "name": "allure_test_case_tree_renameGroup",
        "description": "Rename tree group (AQL)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "filterId": {
                    "type": "number",
                    "description": "filterId"
                },
                "search": {
                    "type": "string",
                    "description": "search"
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
                "baseRql": {
                    "type": "string",
                    "description": "baseRql"
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
        "name": "allure_getJobsInfo",
        "description": "Get information about jobs that will be used to run selected test cases",
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
        "name": "allure_getLeaves",
        "description": "Find tree leaves for node (AQL)",
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
                "treeId": {
                    "type": "number",
                    "description": "treeId"
                },
                "filterId": {
                    "type": "number",
                    "description": "filterId"
                },
                "path": {
                    "type": "array",
                    "description": "path",
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
                },
                "baseRql": {
                    "type": "string",
                    "description": "baseRql"
                }
            },
            "required": [
                "projectId"
            ]
        }
    },
    {
        "name": "allure_test_case_tree_addLeaf",
        "description": "Add a new group",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
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
        "name": "allure_test_case_tree_renameLeaf",
        "description": "Rename tree leaf",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "leafId": {
                    "type": "number",
                    "description": "leafId"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "projectId",
                "leafId",
                "body"
            ]
        }
    },
    {
        "name": "allure_paths",
        "description": "Find all paths to test case in tree",
        "inputSchema": {
            "type": "object",
            "properties": {
                "treeId": {
                    "type": "number",
                    "description": "treeId"
                },
                "testCaseId": {
                    "type": "number",
                    "description": "testCaseId"
                }
            },
            "required": [
                "treeId",
                "testCaseId"
            ]
        }
    },
    {
        "name": "allure_test_case_tree_getRunStats",
        "description": "Get run information",
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
        "name": "allure_test_case_tree_suggest",
        "description": "Tree groups suggest",
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
            },
            "required": [
                "projectId"
            ]
        }
    }
]

async def handle_test_case_tree_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle test_case_tree controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for test_case_tree not yet implemented")
