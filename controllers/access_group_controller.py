"""
Access Group Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions - will be populated from TypeScript
access_group_controller_tools = []

async def handle_access_group_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle access group controller tool calls"""
    try:
        match tool_name:
            case 'allure_findAll_48':
                query = args.get('query')
                project_id = args.get('projectId')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'query': query, 'projectId': project_id, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get('/api/accessgroup', query_params)
                return json.dumps(result, indent=2)
        
            case 'allure_create_56':
                body = args.get('body')
                result = await client.post('/api/accessgroup', body)
                return json.dumps(result, indent=2)
        
            case 'allure_suggest_26':
                query = args.get('query')
                id_list = args.get('id')
                ignore_id = args.get('ignoreId')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'query': query, 'id': id_list, 'ignoreId': ignore_id, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get('/api/accessgroup/suggest', query_params)
                return json.dumps(result, indent=2)
        
            case 'allure_deleteById_7':
                id_val = args.get('id')
                await client.delete(f'/api/accessgroup/{id_val}')
                return 'Successfully deleted'
        
            case 'allure_fetchById':
                id_val = args.get('id')
                result = await client.get(f'/api/accessgroup/{id_val}')
                return json.dumps(result, indent=2)
        
            case 'allure_patchById_4':
                id_val = args.get('id')
                body = args.get('body')
                result = await client.patch(f'/api/accessgroup/{id_val}', body)
                return json.dumps(result, indent=2)
        
            case 'allure_deleteProjects':
                id_val = args.get('id')
                project_id = args.get('projectId')
                query_params = {k: v for k, v in {'projectId': project_id}.items() if v is not None}
                await client.delete(f'/api/accessgroup/{id_val}/project', query_params)
                return 'Successfully deleted'
        
            case 'allure_getProjects':
                id_val = args.get('id')
                query = args.get('query')
                permissions_set_id = args.get('permissionsSetId')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'query': query, 'permissionsSetId': permissions_set_id, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get(f'/api/accessgroup/{id_val}/project', query_params)
                return json.dumps(result, indent=2)
        
            case 'allure_addProjects':
                id_val = args.get('id')
                body = args.get('body')
                result = await client.post(f'/api/accessgroup/{id_val}/project', body)
                return json.dumps(result, indent=2)
        
            case 'allure_deleteUsers_1':
                id_val = args.get('id')
                username = args.get('username')
                query_params = {k: v for k, v in {'username': username}.items() if v is not None}
                await client.delete(f'/api/accessgroup/{id_val}/user', query_params)
                return 'Successfully deleted'
        
            case 'allure_getUsers':
                id_val = args.get('id')
                query = args.get('query')
                page = args.get('page')
                size = args.get('size')
                sort = args.get('sort')
                query_params = {k: v for k, v in {'query': query, 'page': page, 'size': size, 'sort': sort}.items() if v is not None}
                result = await client.get(f'/api/accessgroup/{id_val}/user', query_params)
                return json.dumps(result, indent=2)
        
            case 'allure_addUsers':
                id_val = args.get('id')
                body = args.get('body')
                result = await client.post(f'/api/accessgroup/{id_val}/user', body)
                return json.dumps(result, indent=2)
        
            case _:
                raise ValueError(f"Unknown tool: {tool_name}")
    except Exception as error:
        raise Exception(f"AccessGroupController operation failed: {str(error)}")
