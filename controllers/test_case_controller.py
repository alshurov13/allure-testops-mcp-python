"""
TestCase Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
test_case_controller_tools = [
    {
        "name": "allure_test_case_findAll",
        "description": "Find all test cases for specified project",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
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
        "name": "allure_test_case_create",
        "description": "Create a new test case",
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
        "name": "allure_findAllDeleted",
        "description": "Find all deleted test cases for given project",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
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
        "name": "allure_test_case_findHistoryByParams",
        "description": "Find run history for test case",
        "inputSchema": {
            "type": "object",
            "properties": {
                "testCaseId": {
                    "type": "number",
                    "description": "testCaseId"
                },
                "projectId": {
                    "type": "number",
                    "description": "projectId"
                },
                "launchId": {
                    "type": "number",
                    "description": "launchId"
                },
                "testResultId": {
                    "type": "number",
                    "description": "testResultId"
                },
                "search": {
                    "type": "string",
                    "description": "search"
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
                "testCaseId"
            ]
        }
    },
    {
        "name": "allure_findAllMuted",
        "description": "Find all muted test cases for given project",
        "inputSchema": {
            "type": "object",
            "properties": {
                "projectId": {
                    "type": "number",
                    "description": "projectId"
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
        "name": "allure_test_case_suggest",
        "description": "Find suggest for test case",
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
        "name": "allure_test_case_delete",
        "description": "Delete test case by id",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "force": {
                    "type": "boolean",
                    "description": "force"
                }
            },
            "required": [
                "id"
            ]
        }
    },
    {
        "name": "allure_test_case_findOne",
        "description": "Find test case by id",
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
        "name": "allure_test_case_patch",
        "description": "PATCH /api/testcase/{id}",
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
        "name": "allure_detachAutomation",
        "description": "Detach automation from test case",
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
        "name": "allure_test_case_findHistoryById",
        "description": "Find run history for test case",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Path parameter: id"
                },
                "search": {
                    "type": "string",
                    "description": "search"
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
        "name": "allure_restore",
        "description": "Restore test case by id",
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
        "name": "allure_findWorkflow",
        "description": "Find workflow for test case",
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

async def handle_test_case_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle test case controller tool calls"""
    try:
        match tool_name:
            case 'allure_test_case_findAll':
                project_id = args.get('projectId')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'projectId': project_id, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get('/api/testcase', query_params)
                return json.dumps(result, indent=2)

            case 'allure_test_case_create':
                body = args.get('body')
                result = await client.post('/api/testcase', body)
                return json.dumps(result, indent=2)

            case 'allure_findAllDeleted':
                project_id = args.get('projectId')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'projectId': project_id, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get('/api/testcase/deleted', query_params)
                return json.dumps(result, indent=2)

            case 'allure_test_case_findHistoryByParams':
                test_case_id = args.get('testCaseId')
                project_id = args.get('projectId')
                launch_id = args.get('launchId')
                test_result_id = args.get('testResultId')
                search = args.get('search')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'testCaseId': test_case_id, 'projectId': project_id, 'launchId': launch_id, 'testResultId': test_result_id, 'search': search, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get('/api/testcase/history', query_params)
                return json.dumps(result, indent=2)

            case 'allure_findAllMuted':
                project_id = args.get('projectId')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'projectId': project_id, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get('/api/testcase/muted', query_params)
                return json.dumps(result, indent=2)

            case 'allure_test_case_suggest':
                query = args.get('query')
                project_id = args.get('projectId')
                id_list = args.get('id')
                ignore_id = args.get('ignoreId')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'query': query, 'projectId': project_id, 'id': id_list, 'ignoreId': ignore_id, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get('/api/testcase/suggest', query_params)
                return json.dumps(result, indent=2)

            case 'allure_test_case_delete':
                id_val = args.get('id')
                force = args.get('force')
                query_params = {k: v for k, v in {'force': force}.items() if v is not None}
                await client.delete(f'/api/testcase/{id_val}', query_params)
                return 'Successfully deleted'

            case 'allure_test_case_findOne':
                id_val = args.get('id')
                result = await client.get(f'/api/testcase/{id_val}')
                return json.dumps(result, indent=2)

            case 'allure_test_case_patch':
                id_val = args.get('id')
                body = args.get('body')
                result = await client.patch(f'/api/testcase/{id_val}', body)
                return json.dumps(result, indent=2)

            case 'allure_detachAutomation':
                id_val = args.get('id')
                body = args.get('body')
                result = await client.post(f'/api/testcase/{id_val}/detachautomation', body)
                return json.dumps(result, indent=2)

            case 'allure_test_case_findHistoryById':
                id_val = args.get('id')
                search = args.get('search')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'search': search, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get(f'/api/testcase/{id_val}/history', query_params)
                return json.dumps(result, indent=2)

            case 'allure_restore':
                id_val = args.get('id')
                result = await client.post(f'/api/testcase/{id_val}/restore', {})
                return json.dumps(result, indent=2)

            case 'allure_findWorkflow':
                id_val = args.get('id')
                result = await client.get(f'/api/testcase/{id_val}/workflow')
                return json.dumps(result, indent=2)

            case _:
                raise ValueError(f"Unknown tool: {tool_name}")
    except Exception as error:
        raise Exception(f"TestCaseController operation failed: {str(error)}")


