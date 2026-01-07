#!/usr/bin/env python3
"""
Allure TestOps MCP Server
Model Context Protocol server for Allure TestOps API
"""

import asyncio
import json
import os
import sys
from typing import Any
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from allure_client import AllureClient, create_allure_client
from csv_parser import parse_test_cases_from_csv

# Environment variables
ALLURE_TESTOPS_URL = os.environ.get('ALLURE_TESTOPS_URL')
ALLURE_TOKEN = os.environ.get('ALLURE_TOKEN')
PROJECT_ID = os.environ.get('PROJECT_ID')

# Validate required environment variables
if not ALLURE_TOKEN:
    print('Error: ALLURE_TOKEN environment variable is required', file=sys.stderr)
    sys.exit(1)

if not ALLURE_TESTOPS_URL:
    print('Error: ALLURE_TESTOPS_URL environment variable is required', file=sys.stderr)
    sys.exit(1)

if not PROJECT_ID:
    print('Error: PROJECT_ID environment variable is required', file=sys.stderr)
    sys.exit(1)

# Initialize Allure client
allure_client = create_allure_client(ALLURE_TESTOPS_URL, ALLURE_TOKEN)

# Define tools matching Node.js version
all_tools: list[Tool] = [
    Tool(
        name='list_test_cases',
        description='List all test cases in the project',
        inputSchema={
            'type': 'object',
            'properties': {
                'page': {'type': 'number', 'description': 'Page number (optional)'},
                'size': {'type': 'number', 'description': 'Page size (optional)'},
            },
        },
    ),
    Tool(
        name='get_test_case',
        description='Get a specific test case by ID',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Test case ID'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='create_test_case',
        description='Create a new test case',
        inputSchema={
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'description': 'Test case name'},
                'description': {'type': 'string', 'description': 'Test case description'},
                'status': {'type': 'string', 'description': 'Test case status'},
                'automated': {'type': 'boolean', 'description': 'Is automated'},
            },
            'required': ['name'],
        },
    ),
    Tool(
        name='update_test_case',
        description='Update an existing test case',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Test case ID'},
                'name': {'type': 'string', 'description': 'Test case name'},
                'description': {'type': 'string', 'description': 'Test case description'},
                'status': {'type': 'string', 'description': 'Test case status'},
                'automated': {'type': 'boolean', 'description': 'Is automated'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='delete_test_case',
        description='Delete a test case',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Test case ID'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='bulk_create_test_cases_from_csv',
        description='Bulk create test cases from CSV content. CSV should have columns: name, description, status, automated',
        inputSchema={
            'type': 'object',
            'properties': {
                'csv_content': {'type': 'string', 'description': 'CSV file content'},
            },
            'required': ['csv_content'],
        },
    ),
    Tool(
        name='list_launches',
        description='List all launches in the project',
        inputSchema={
            'type': 'object',
            'properties': {
                'page': {'type': 'number', 'description': 'Page number (optional)'},
                'size': {'type': 'number', 'description': 'Page size (optional)'},
            },
        },
    ),
    Tool(
        name='get_launch',
        description='Get a specific launch by ID',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Launch ID'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='create_launch',
        description='Create a new launch',
        inputSchema={
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'description': 'Launch name'},
                'closed': {'type': 'boolean', 'description': 'Is closed'},
            },
            'required': ['name'],
        },
    ),
    Tool(
        name='update_launch',
        description='Update an existing launch',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Launch ID'},
                'name': {'type': 'string', 'description': 'Launch name'},
                'closed': {'type': 'boolean', 'description': 'Is closed'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='delete_launch',
        description='Delete a launch',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Launch ID'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='close_launch',
        description='Close a launch',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Launch ID'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='list_test_plans',
        description='List all test plans in the project',
        inputSchema={
            'type': 'object',
            'properties': {
                'page': {'type': 'number', 'description': 'Page number (optional)'},
                'size': {'type': 'number', 'description': 'Page size (optional)'},
            },
        },
    ),
    Tool(
        name='get_test_plan',
        description='Get a specific test plan by ID',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Test plan ID'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='create_test_plan',
        description='Create a new test plan',
        inputSchema={
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'description': 'Test plan name'},
                'description': {'type': 'string', 'description': 'Test plan description'},
            },
            'required': ['name'],
        },
    ),
    Tool(
        name='update_test_plan',
        description='Update an existing test plan',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Test plan ID'},
                'name': {'type': 'string', 'description': 'Test plan name'},
                'description': {'type': 'string', 'description': 'Test plan description'},
            },
            'required': ['id'],
        },
    ),
    Tool(
        name='delete_test_plan',
        description='Delete a test plan',
        inputSchema={
            'type': 'object',
            'properties': {
                'id': {'type': 'number', 'description': 'Test plan ID'},
            },
            'required': ['id'],
        },
    ),
]

# Create MCP server
server = Server("allure-testops-mcp")

@server.list_tools()
async def list_tools() -> list[Tool]:
    """Return list of available tools"""
    return all_tools

@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls"""
    try:
        match name:
            case 'list_test_cases':
                params = arguments or {}
                result = await allure_client.get_test_cases(PROJECT_ID, params)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'get_test_case':
                test_case_id = arguments.get('id')
                result = await allure_client.get_test_case(test_case_id)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'create_test_case':
                test_case = {k: v for k, v in arguments.items()}
                result = await allure_client.create_test_case(PROJECT_ID, test_case)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'update_test_case':
                test_case_id = arguments.get('id')
                update_data = {k: v for k, v in arguments.items() if k != 'id'}
                result = await allure_client.update_test_case(test_case_id, update_data)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'delete_test_case':
                test_case_id = arguments.get('id')
                await allure_client.delete_test_case(test_case_id)
                return [TextContent(type="text", text=f"Test case {test_case_id} deleted successfully")]

            case 'bulk_create_test_cases_from_csv':
                csv_content = arguments.get('csv_content')
                test_cases = parse_test_cases_from_csv(csv_content)
                results = await allure_client.bulk_create_test_cases(PROJECT_ID, test_cases)
                return [TextContent(type="text", text=json.dumps(results, indent=2))]

            case 'list_launches':
                params = arguments or {}
                result = await allure_client.get_launches(PROJECT_ID, params)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'get_launch':
                launch_id = arguments.get('id')
                result = await allure_client.get_launch(launch_id)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'create_launch':
                launch = {k: v for k, v in arguments.items()}
                result = await allure_client.create_launch(PROJECT_ID, launch)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'update_launch':
                launch_id = arguments.get('id')
                update_data = {k: v for k, v in arguments.items() if k != 'id'}
                result = await allure_client.update_launch(launch_id, update_data)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'delete_launch':
                launch_id = arguments.get('id')
                await allure_client.delete_launch(launch_id)
                return [TextContent(type="text", text=f"Launch {launch_id} deleted successfully")]

            case 'close_launch':
                launch_id = arguments.get('id')
                result = await allure_client.close_launch(launch_id)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'list_test_plans':
                params = arguments or {}
                result = await allure_client.get_test_plans(PROJECT_ID, params)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'get_test_plan':
                test_plan_id = arguments.get('id')
                result = await allure_client.get_test_plan(test_plan_id)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'create_test_plan':
                test_plan = {k: v for k, v in arguments.items()}
                result = await allure_client.create_test_plan(PROJECT_ID, test_plan)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'update_test_plan':
                test_plan_id = arguments.get('id')
                update_data = {k: v for k, v in arguments.items() if k != 'id'}
                result = await allure_client.update_test_plan(test_plan_id, update_data)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

            case 'delete_test_plan':
                test_plan_id = arguments.get('id')
                await allure_client.delete_test_plan(test_plan_id)
                return [TextContent(type="text", text=f"Test plan {test_plan_id} deleted successfully")]

            case _:
                return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as error:
        error_message = str(error)
        # Try to extract more details from httpx errors
        if hasattr(error, 'response') and hasattr(error.response, 'text'):
            error_message += f"\n{error.response.text}"
        return [TextContent(type="text", text=f"Error: {error_message}")]

async def main():
    """Main function to run the server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    print("Allure TestOps MCP Server running on stdio", file=sys.stderr)
    print(f"Connected to: {ALLURE_TESTOPS_URL}", file=sys.stderr)
    print(f"Project ID: {PROJECT_ID}", file=sys.stderr)
    print(f"Registered {len(all_tools)} tools", file=sys.stderr)
    asyncio.run(main())
