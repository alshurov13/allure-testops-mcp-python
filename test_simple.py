#!/usr/bin/env python3
"""
Simple test to verify MCP server can start
"""

import os
import sys
import asyncio

# Check environment variables
print("Checking environment variables...")
required_vars = ['ALLURE_TESTOPS_URL', 'ALLURE_TOKEN', 'PROJECT_ID']
missing = []

for var in required_vars:
    value = os.environ.get(var)
    if value:
        # Mask sensitive values
        if 'TOKEN' in var:
            display_value = value[:10] + "..." if len(value) > 10 else "***"
        else:
            display_value = value
        print(f"  ✓ {var}: {display_value}")
    else:
        print(f"  ✗ {var}: NOT SET")
        missing.append(var)

if missing:
    print(f"\nERROR: Missing required environment variables: {', '.join(missing)}")
    print("\nSet them with:")
    print("  export ALLURE_TESTOPS_URL='https://your-instance.com'")
    print("  export ALLURE_TOKEN='your-token'")
    print("  export PROJECT_ID='1'")
    sys.exit(1)

# Try to import modules
print("\nChecking imports...")
try:
    from allure_client import AllureClient, create_allure_client
    print("  ✓ allure_client imported")
except ImportError as e:
    print(f"  ✗ Failed to import allure_client: {e}")
    sys.exit(1)

try:
    from index import server, all_tools
    print("  ✓ index imported")
    print(f"  ✓ Server initialized with {len(all_tools)} tools")
except ImportError as e:
    print(f"  ✗ Failed to import index: {e}")
    sys.exit(1)

print("\n✓ Basic checks passed! Server should be ready to run.")
print("\nTo test the server, run:")
print("  poetry run python index.py")




