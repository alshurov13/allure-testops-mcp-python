# Quick Testing of MCP Server

## Step 1: Install Dependencies

```bash
cd /Users/alexander.shurov/allure_testops/mcp/python
pip install -r requirements.txt
```

## Step 2: Configure Environment Variables

```bash
export ALLURE_TESTOPS_URL='https://your-allure-instance.com'
export ALLURE_TOKEN='your-api-token'
export PROJECT_ID='1'
```

## Step 3: Simple Test

```bash
python test_simple.py
```

Should output:
```
✓ ALLURE_TESTOPS_URL: https://...
✓ ALLURE_TOKEN: ...
✓ PROJECT_ID: 1
✓ allure_client imported
✓ index imported
✓ Server initialized with X tools
```

## Step 4: Full Test

```bash
python test_mcp.py
```

This will check:
- Connection to Allure TestOps API
- Tool registration
- Handler execution
- MCP server structure

## Step 5: Run Server

```bash
python index.py
```

Server should start and wait for input on stdin. You will see:
```
Allure TestOps MCP Server running on stdio
Connected to: https://...
Project ID: 1
Registered X tools
```

## Testing via Cursor

1. Add to `~/.cursor/mcp.json`:
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

2. Restart Cursor
3. Try using the tools in chat

## Troubleshooting

### Import Error
```bash
# Make sure you're in the correct directory
cd /Users/alexander.shurov/allure_testops/mcp/python

# Check that all files are in place
ls -la controllers/
```

### API Connection Error
- Check the URL is correct
- Check the token
- Check network availability

### "Unknown tool" Error
- Make sure all controllers are imported in index.py
- Check that handlers are implemented




