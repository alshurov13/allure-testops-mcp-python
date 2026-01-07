"""
Business Metric Controller - MCP Tools
Generated from Swagger specification
"""

import json
from typing import Any
from allure_client import AllureClient

# Tools definitions
business_metric_controller_tools = [
    {
        "name": "allure_business_metric_findAll",
        "description": "Find all business metrics",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
]

async def handle_business_metric_controller_tool(
    client: AllureClient,
    tool_name: str,
    args: dict[str, Any],
    default_project_id: str
) -> str:
    """Handle business_metric controller tool calls"""
    # TODO: Implement handler based on TypeScript version
    raise NotImplementedError(f"Handler for business_metric not yet implemented")
