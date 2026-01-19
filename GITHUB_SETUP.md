# GitHub Publishing Guide

## Step 1: Initialize Git Repository

```bash
# Navigate to the project directory
cd ..

# Initialize git repository
git init

# Add all files (except those in .gitignore)
git add .

# Make the first commit
git commit -m "Initial commit: Allure TestOps MCP Server"
```

## Step 2: Create Repository on GitHub

1. Go to [GitHub.com](https://github.com)
2. Click "New repository" (or go directly to the creation link)
3. Fill in:
   - **Repository name**: `allure-testops-mcp-python` (or another name)
   - **Description**: "Model Context Protocol server for Allure TestOps API"
   - **Visibility**: Public or Private (your choice)
   - **DO NOT** add README, .gitignore, or LICENSE (they already exist)
4. Click "Create repository"

## Step 3: Connect Local Repository to GitHub

```bash
# Add remote (replace YOUR_USERNAME and REPO_NAME with your values)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Rename branch to main (if needed)
git branch -M main

# Push code to GitHub
git push -u origin main
```

## Step 4: Pre-Publication Checklist

### ✅ Make sure that:

1. **No sensitive data:**
   ```bash
   # Check that these files will not be committed
   git status
   # Should be in "Untracked files" list or ignored:
   # - .env
   # - open_launches_summary.json
   # - venv/
   # - __pycache__/
   ```

2. **All necessary files are in place:**
   - ✅ `.gitignore` - created
   - ✅ `README.md` - updated
   - ✅ `LICENSE` - added
   - ✅ `pyproject.toml` - present
   - ✅ `CONTRIBUTING.md` - created (optional)

3. **Review commit contents:**
   ```bash
   # See what will be committed
   git status
   git diff --cached  # for staged files
   ```

## Step 5: Additional GitHub Settings

After publishing:

1. **Add repository description** in settings
2. **Add topics/tags**: `mcp`, `allure-testops`, `python`, `api-client`
3. **Enable Issues** (if you plan to accept bugs/requests)
4. **Set up GitHub Actions** (optional, for CI/CD)

## Important Reminders

⚠️ **NEVER commit:**
- API tokens (`ALLURE_TOKEN`)
- Real server URLs
- `.env` files with real data
- Personal data
- `open_launches_summary.json` files with real data

✅ **Always use:**
- Environment variables for sensitive data
- `.env.example` as a template (if you create one)
- Placeholder values in code examples

## Useful Git Commands

```bash
# Check status
git status

# View changes
git diff

# Add a specific file
git add filename.py

# Unstage a file
git reset filename.py

# View commit history
git log --oneline

# Update code from GitHub
git pull origin main
```

## If Something Goes Wrong

If you accidentally committed sensitive data:

1. **Immediately** change tokens/passwords
2. Remove file from Git history:
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch path/to/file" \
     --prune-empty --tag-name-filter cat -- --all
   ```
3. Or use `git-filter-repo` (more modern tool)
4. Force push changes:
   ```bash
   git push origin --force --all
   ```

**Warning:** Force push changes history, use with caution!
