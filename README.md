# Allure TestOps MCP Server (Python)

Model Context Protocol server for Allure TestOps API, written in Python.

## Overview

This MCP server provides a Python implementation for interacting with Allure TestOps API through the Model Context Protocol. It supports full CRUD operations for test cases, launches, and test plans, along with 56+ controller endpoints for comprehensive Allure TestOps integration.

## Installation

### Prerequisites

- Python 3.10 or higher
- Poetry package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd allure_testops/mcp/python
```

2. Install dependencies:
```bash
poetry install
```

3. Set up environment variables (see Configuration section below)

## Configuration

Set the following environment variables:

- `ALLURE_TESTOPS_URL`: Base URL of your Allure TestOps instance (e.g., `https://your-allure-instance.com`)
- `ALLURE_TOKEN`: API token for authentication (generate in Allure TestOps user settings)
- `PROJECT_ID`: Default project ID (numeric string, e.g., `"1"`)

### Using Environment Variables

```bash
export ALLURE_TESTOPS_URL='https://your-allure-instance.com'
export ALLURE_TOKEN='your-api-token'
export PROJECT_ID='1'
```

### Using .env File (Recommended)

Create a `.env` file in the project root:

```env
ALLURE_TESTOPS_URL=https://your-allure-instance.com
ALLURE_TOKEN=your-api-token
PROJECT_ID=1
```

**Note:** Never commit `.env` files to version control. Use `.env.example` as a template.

## Usage

### Running the MCP Server

Run the server directly:

```bash
poetry run python index.py
```

The server will run on stdio and communicate via the Model Context Protocol.

### Standalone Scripts

The repository includes utility scripts:

- `get_open_launches.py` - Fetch all open launches from Allure TestOps

```bash
poetry run python get_open_launches.py
```

## MCP Configuration

Add to your `mcp.json` (typically located in `~/.cursor/mcp.json` or similar):

```json
{
  "mcpServers": {
    "allure-testops-python": {
      "command": "python3",
      "args": [
        "/absolute/path/to/index.py"
      ],
      "env": {
        "ALLURE_TESTOPS_URL": "https://your-allure-instance.com",
        "ALLURE_TOKEN": "your-api-token",
        "PROJECT_ID": "1"
      }
    }
  }
}
```

## Available Tools

### Test Cases
- `list_test_cases` - List all test cases in the project
- `get_test_case` - Get a specific test case by ID
- `create_test_case` - Create a new test case
- `update_test_case` - Update an existing test case
- `delete_test_case` - Delete a test case
- `bulk_create_test_cases_from_csv` - Bulk create test cases from CSV

### Launches
- `list_launches` - List all launches in the project
- `get_launch` - Get a specific launch by ID
- `create_launch` - Create a new launch
- `update_launch` - Update an existing launch
- `delete_launch` - Delete a launch
- `close_launch` - Close a launch

### Test Plans
- `list_test_plans` - List all test plans in the project
- `get_test_plan` - Get a specific test plan by ID
- `create_test_plan` - Create a new test plan
- `update_test_plan` - Update an existing test plan
- `delete_test_plan` - Delete a test plan

## Features

- ✅ Full Allure TestOps API integration
- ✅ 56+ controller endpoints
- ✅ Async/await support for high performance
- ✅ Type-safe tool definitions
- ✅ Comprehensive error handling
- ✅ CSV import support for bulk operations

## Project Structure

```
.
├── index.py                 # Main MCP server entry point
├── allure_client.py         # HTTP client for Allure TestOps API
├── csv_parser.py           # CSV parsing utilities
├── controllers/            # API controller modules
├── get_open_launches.py   # Utility script for fetching open launches
├── pyproject.toml         # Poetry configuration
├── poetry.lock          # Lock file for dependencies
└── README.md              # This file
```

## Development

### Testing

Run the test scripts:

```bash
poetry run python test_simple.py
poetry run python test_mcp.py
```

See `TESTING.md` and `QUICK_TEST.md` for more details.

## Security Notes

- **Never commit API tokens or credentials** to version control
- Use environment variables or secure secret management
- The `.gitignore` file excludes sensitive files by default
- Rotate API tokens regularly

## Contributing

Contributions are welcome! Please ensure:

1. Code follows Python best practices
2. All tests pass
3. No sensitive data is included in commits
4. README is updated for new features

## License

See LICENSE file for details.

## Support

For issues and questions:
- Check the documentation in `TESTING.md` and `QUICK_TEST.md`
- Review Allure TestOps API documentation
- Open an issue in the repository

