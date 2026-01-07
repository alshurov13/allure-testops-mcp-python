# Testing Allure TestOps MCP Server

## Quick Test

### 1. Set Environment Variables

```bash
export ALLURE_TESTOPS_URL='https://your-allure-instance.com'
export ALLURE_TOKEN='your-api-token'
export PROJECT_ID='1'
```

### 2. Run Simple Test

```bash
poetry run python test_simple.py
```

This will check:
- Environment variables are set
- Modules can be imported
- Server structure is correct

### 3. Run Full Test Suite

```bash
poetry run python test_mcp.py
```

This will test:
- AllureClient connection to API
- Controller tools registration
- Tool handler execution
- MCP server structure

## Manual Testing

### Test 1: Check Server Starts

```bash
poetry run python index.py
```

The server should start and wait for input on stdin. You should see:
```
Allure TestOps MCP Server running on stdio
Connected to: https://your-instance.com
Project ID: 1
Registered X tools
```

### Test 2: Test via MCP Client

If you have an MCP client configured, you can test by:

1. Add to your `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "allure-testops-python": {
      "command": "python3",
      "args": [
        "/Users/alexander.shurov/allure_testops/mcp/python/index.py"
      ],
      "env": {
        "ALLURE_TESTOPS_URL": "https://your-instance.com",
        "ALLURE_TOKEN": "your-token",
        "PROJECT_ID": "1"
      }
    }
  }
}
```

2. Restart Cursor/IDE
3. Try using MCP tools in chat

### Test 3: Test Individual Controller

```python
import asyncio
import os
from allure_client import create_allure_client
from controllers.test_case_controller import handle_test_case_controller_tool

async def test():
    client = create_allure_client(
        os.environ['ALLURE_TESTOPS_URL'],
        os.environ['ALLURE_TOKEN']
    )
    
    result = await handle_test_case_controller_tool(
        client,
        'allure_findAll_12',
        {'projectId': 1, 'page': 0, 'size': 10},
        '1'
    )
    print(result)

asyncio.run(test())
```

## Troubleshooting

### Server Won't Start

- Check environment variables are set
- Check Python version (requires 3.10+)
- Check dependencies: `poetry install` (ensures `pyproject.toml` dependencies are installed)

### Connection Errors

- Verify `ALLURE_TESTOPS_URL` is correct
- Verify `ALLURE_TOKEN` is valid
- Check network connectivity

### Import Errors

- Make sure you're in the project directory
- Check that all files are present
- Verify Python path includes project directory

### Tool Handler Errors

- Check API endpoint URLs
- Verify request parameters
- Check API response format




