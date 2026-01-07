"""
Custom Field Value Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
custom_field_value_controller_tools = [
    {
        "name": "allure_custom_field_value_findAll",
        "description": "Find all custom field values",
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
                "global": {
                    "type": "boolean",
                    "description": "global"
                },
                "query": {
                    "type": "string",
                    "description": "query"
                },
                "strict": {
                    "type": "boolean",
                    "description": "strict"
                },
                "testCaseSearch": {
                    "type": "string",
                    "description": "testCaseSearch"
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
        "name": "allure_custom_field_value_create",
        "description": "Deprecated. Use POST /api/project/{projectId}/cfv instead",
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
        "name": "allure_mergeProjectFieldsToNewGlobalValue",
        "description": "Merge project custom field values into new global",
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
        "name": "allure_mergeProjectFieldsToExistingGlobalValue",
        "description": "Merge project custom field values into existing global",
        "inputSchema": {
            "type": "object",
            "properties": {
                "toCfvId": {
                    "type": "number",
                    "description": "Path parameter: toCfvId"
                },
                "body": {
                    "type": "object",
                    "description": "Request body"
                }
            },
            "required": [
                "toCfvId",
                "body"
            ]
        }
    },
    {
        "name": "allure_custom_field_value_suggest",
        "description": "Suggest custom field values",
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
        "name": "allure_custom_field_value_suggestV",
        "description": "Suggest custom field values",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                },
                "customFieldId": {
                    "type": "number",
                    "description": "customFieldId"
                },
                "query": {
                    "type": "string",
                    "description": "query"
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
    },
    {
        "name": "allure_custom_field_value_delete",
        "description": "Delete custom field value by id",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                }
            },
            "required": [
                "id"
            ]
        }
    },
    {
        "name": "allure_custom_field_value_findOne",
        "description": "Find custom field value by id",
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
        "name": "allure_custom_field_value_patch",
        "description": "Patch custom field value",
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
        "name": "allure_renameCustomFieldValue",
        "description": "Deprecated. Use PUT /api/project/{projectId}/cfv/{cvfId}/name instead",
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
    }
]

async def handle_custom_field_value_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle custom_field_value controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for custom_field_value not yet implemented")
