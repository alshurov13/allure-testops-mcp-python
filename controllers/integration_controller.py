"""
Integration Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
integration_controller_tools = [
    {
        "name": "allure_getIntegrations",
        "description": "GET /api/integration",
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
        "name": "allure_integration_create",
        "description": "POST /api/integration",
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
        "name": "allure_getAvailableIntegrations",
        "description": "GET /api/integration/available",
        "inputSchema": {
            "type": "object",
            "properties": {
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
            }
        }
    },
    {
        "name": "allure_getGlobalFields",
        "description": "GET /api/integration/globalfields",
        "inputSchema": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "type"
                },
                "integrationId": {
                    "type": "number",
                    "description": "integrationId"
                }
            },
            "required": [
                "type",
                "integrationId"
            ]
        }
    },
    {
        "name": "allure_createProjectIntegration",
        "description": "POST /api/integration/project",
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
        "name": "allure_integration_validateProject",
        "description": "POST /api/integration/project/validate",
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
        "name": "allure_getProjectIntegrations",
        "description": "GET /api/integration/project/{projectId}",
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
        "name": "allure_getProjectAvailableIntegrations",
        "description": "GET /api/integration/project/{projectId}/available",
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
        "name": "allure_getProjectIntegrationFields",
        "description": "GET /api/integration/projectfields",
        "inputSchema": {
            "type": "object",
            "properties": {
                "integrationId": {
                    "type": "number",
                    "description": "integrationId"
                },
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                }
            },
            "required": [
                "integrationId",
                "projectId"
            ]
        }
    },
    {
        "name": "allure_integration_suggest",
        "description": "Suggest integrations",
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
                "operation": {
                    "type": "array",
                    "description": "operation",
                    "items": {
                        "type": "string"
                    }
                },
                "integrationType": {
                    "type": "array",
                    "description": "integrationType",
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
        "name": "allure_integration_validate",
        "description": "POST /api/integration/validate",
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
        "name": "allure_integration_deleteById",
        "description": "DELETE /api/integration/{id}",
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
        "name": "allure_findOneById",
        "description": "GET /api/integration/{id}",
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
        "name": "allure_integration_patch",
        "description": "PATCH /api/integration/{id}",
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
        "name": "allure_getIntegrationProjects",
        "description": "GET /api/integration/{id}/project",
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
                },
                "my": {
                    "type": "boolean",
                    "description": "my"
                },
                "favorite": {
                    "type": "boolean",
                    "description": "favorite"
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
        "name": "allure_deleteProjectIntegration",
        "description": "DELETE /api/integration/{integrationId}/project/{projectId}",
        "inputSchema": {
            "type": "object",
            "properties": {
                "integrationId": {
                    "type": "number",
                    "description": "Path parameter: integrationId"
                },
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                }
            },
            "required": [
                "integrationId",
                "projectId"
            ]
        }
    },
    {
        "name": "allure_findProjectIntegrationById",
        "description": "GET /api/integration/{integrationId}/project/{projectId}",
        "inputSchema": {
            "type": "object",
            "properties": {
                "integrationId": {
                    "type": "number",
                    "description": "Path parameter: integrationId"
                },
                "projectId": {
                    "type": "number",
                    "description": "Path parameter: projectId"
                }
            },
            "required": [
                "integrationId",
                "projectId"
            ]
        }
    },
    {
        "name": "allure_patchProjectIntegration",
        "description": "PATCH /api/integration/{integrationId}/project/{projectId}",
        "inputSchema": {
            "type": "object",
            "properties": {
                "integrationId": {
                    "type": "number",
                    "description": "Path parameter: integrationId"
                },
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
                "integrationId",
                "projectId",
                "body"
            ]
        }
    }
]

async def handle_integration_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle integration controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for integration not yet implemented")
