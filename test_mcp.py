#!/usr/bin/env python3
"""
Test script for Allure TestOps MCP Server
"""

import os
import sys
import asyncio
import json
from typing import Any, Dict

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from allure_client import AllureClient, create_allure_client
from controllers.test_case_controller import (
    test_case_controller_tools,
    handle_test_case_controller_tool
)
from controllers.launch_controller import (
    launch_controller_tools,
    handle_launch_controller_tool
)
from controllers.project_controller import (
    project_controller_tools,
    handle_project_controller_tool
)

async def test_allure_client():
    """Test AllureClient connection"""
    print("Testing AllureClient...")
    
    allure_url = os.environ.get('ALLURE_TESTOPS_URL')
    allure_token = os.environ.get('ALLURE_TOKEN')
    
    if not allure_url or not allure_token:
        print("ERROR: ALLURE_TESTOPS_URL and ALLURE_TOKEN must be set")
        return False
    
    try:
        client = create_allure_client(allure_url, allure_token)
        
        # Test simple GET request
        print(f"  Connecting to: {allure_url}")
        print(f"  Token: {allure_token[:10]}...")
        
        # Try to get projects list
        try:
            result = await client.get('/api/project', {'page': 0, 'size': 1})
            print(f"  ✓ Successfully connected to Allure TestOps")
            print(f"  ✓ API is accessible")
            return True
        except Exception as e:
            print(f"  ✗ API request failed: {e}")
            return False
            
    except Exception as e:
        print(f"  ✗ Client creation failed: {e}")
        return False

async def test_controller_tools():
    """Test controller tools registration"""
    print("\nTesting controller tools...")
    
    controllers = [
        ("test_case", test_case_controller_tools),
        ("launch", launch_controller_tools),
        ("project", project_controller_tools),
    ]
    
    total_tools = 0
    for name, tools in controllers:
        count = len(tools) if tools else 0
        total_tools += count
        status = "✓" if count > 0 else "✗"
        print(f"  {status} {name}: {count} tools")
    
    print(f"  Total tools: {total_tools}")
    return total_tools > 0

async def test_tool_handler():
    """Test tool handler execution"""
    print("\nTesting tool handler...")
    
    allure_url = os.environ.get('ALLURE_TESTOPS_URL')
    allure_token = os.environ.get('ALLURE_TOKEN')
    project_id = os.environ.get('PROJECT_ID', '1')
    
    if not allure_url or not allure_token:
        print("  ✗ Environment variables not set")
        return False
    
    try:
        client = create_allure_client(allure_url, allure_token)
        
        # Test a simple tool call (list test cases)
        print("  Testing 'allure_test_case_findAll' (list test cases)...")
        args = {
            'projectId': project_id,
            'page': 0,
            'size': 1
        }
        
        result = await handle_test_case_controller_tool(
            client,
            'allure_test_case_findAll',
            args,
            project_id
        )
        
        print(f"  ✓ Tool handler executed successfully")
        print(f"  ✓ Result length: {len(result)} characters")
        
        # Try to parse JSON
        try:
            data = json.loads(result)
            print(f"  ✓ Result is valid JSON")
            return True
        except json.JSONDecodeError:
            print(f"  ✗ Result is not valid JSON")
            return False
            
    except Exception as e:
        print(f"  ✗ Tool handler failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_mcp_server_structure():
    """Test MCP server structure"""
    print("\nTesting MCP server structure...")
    
    try:
        # Try to import index
        from index import server, all_tools
        
        print(f"  ✓ Server created: {server}")
        print(f"  ✓ Total tools registered: {len(all_tools)}")
        
        # Check if tools have required structure
        if all_tools:
            sample_tool = all_tools[0]
            required_fields = ['name', 'description', 'inputSchema']
            # Tool is a Pydantic model, so check attributes using hasattr
            missing = [f for f in required_fields if not hasattr(sample_tool, f)]
            
            if missing:
                print(f"  ✗ Tools missing fields: {missing}")
                return False
            else:
                print(f"  ✓ Tools have required structure")
                # Verify they have values
                if sample_tool.name and sample_tool.description and sample_tool.inputSchema:
                    print(f"  ✓ Sample tool: {sample_tool.name}")
                else:
                    print(f"  ✗ Sample tool has empty required fields")
                    return False
        
        return True
        
    except ImportError as e:
        print(f"  ✗ Failed to import index: {e}")
        return False
    except Exception as e:
        print(f"  ✗ Structure test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Run all tests"""
    print("=" * 60)
    print("Allure TestOps MCP Server - Test Suite")
    print("=" * 60)
    
    results = []
    
    # Test 1: AllureClient
    results.append(await test_allure_client())
    
    # Test 2: Controller tools
    results.append(await test_controller_tools())
    
    # Test 3: Tool handler
    if results[0]:  # Only test if client works
        results.append(await test_tool_handler())
    else:
        print("\nSkipping tool handler test (client not working)")
        results.append(False)
    
    # Test 4: MCP server structure
    results.append(await test_mcp_server_structure())
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    test_names = [
        "AllureClient connection",
        "Controller tools registration",
        "Tool handler execution",
        "MCP server structure"
    ]
    
    for i, (name, result) in enumerate(zip(test_names, results)):
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        print(f"  {symbol} {name}: {status}")
    
    passed = sum(results)
    total = len(results)
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✓ All tests passed! MCP server is ready to use.")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)




