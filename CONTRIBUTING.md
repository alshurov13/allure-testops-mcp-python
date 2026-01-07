# Contributing to Allure TestOps MCP Server

Thank you for your interest in contributing!

## Before You Commit

### 1. Check for Sensitive Data

Before committing, ensure you haven't included:
- API tokens or authentication credentials
- Real server URLs (use placeholders like `https://your-instance.com`)
- Personal or project-specific data
- Environment files (`.env`, `.env.local`, etc.)

### 2. Verify .gitignore

Make sure `.gitignore` is working correctly:

```bash
# Check what files would be committed
git status

# Verify sensitive files are ignored
git check-ignore -v .env open_launches_summary.json venv/
```

### 3. Code Quality

- Follow Python PEP 8 style guidelines
- Ensure all imports are used
- Add docstrings to new functions/classes
- Test your changes locally

### 4. Testing

Run the test suite before committing:

```bash
poetry run python test_simple.py
poetry run python test_mcp.py
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Code Style

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use type hints where appropriate
- Follow async/await patterns for async functions

## Questions?

Feel free to open an issue for questions or discussions.

