# Инструкция по публикации на GitHub

## Шаг 1: Инициализация Git репозитория

```bash
# Перейдите в директорию проекта
cd /Users/alexander.shurov/allure_testops/mcp/python

# Инициализируйте git репозиторий
git init

# Добавьте все файлы (кроме тех, что в .gitignore)
git add .

# Сделайте первый коммит
git commit -m "Initial commit: Allure TestOps MCP Server"
```

## Шаг 2: Создание репозитория на GitHub

1. Зайдите на [GitHub.com](https://github.com)
2. Нажмите "New repository" (или перейдите по прямой ссылке создания)
3. Заполните:
   - **Repository name**: `allure-testops-mcp-python` (или другое имя)
   - **Description**: "Model Context Protocol server for Allure TestOps API"
   - **Visibility**: Public или Private (на ваше усмотрение)
   - **НЕ** добавляйте README, .gitignore или LICENSE (они уже есть)
4. Нажмите "Create repository"

## Шаг 3: Подключение локального репозитория к GitHub

```bash
# Добавьте remote (замените YOUR_USERNAME и REPO_NAME на ваши значения)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Переименуйте ветку в main (если нужно)
git branch -M main

# Отправьте код на GitHub
git push -u origin main
```

## Шаг 4: Проверка перед публикацией

### ✅ Убедитесь, что:

1. **Нет конфиденциальных данных:**
   ```bash
   # Проверьте, что эти файлы не будут закоммичены
   git status
   # Должны быть в списке "Untracked files" или игнорироваться:
   # - .env
   # - open_launches_summary.json
   # - venv/
   # - __pycache__/
   ```

2. **Все необходимые файлы на месте:**
   - ✅ `.gitignore` - создан
   - ✅ `README.md` - обновлен
   - ✅ `LICENSE` - добавлен
   - ✅ `pyproject.toml` - присутствует
   - ✅ `CONTRIBUTING.md` - создан (опционально)

3. **Проверьте содержимое коммита:**
   ```bash
   # Посмотрите, что будет закоммичено
   git status
   git diff --cached  # для staged файлов
   ```

## Шаг 5: Дополнительные настройки на GitHub

После публикации:

1. **Добавьте описание репозитория** в настройках
2. **Добавьте теги/топики**: `mcp`, `allure-testops`, `python`, `api-client`
3. **Включите Issues** (если планируете принимать баги/запросы)
4. **Настройте GitHub Actions** (опционально, для CI/CD)

## Важные напоминания

⚠️ **НИКОГДА не коммитьте:**
- API токены (`ALLURE_TOKEN`)
- Реальные URL серверов
- Файлы `.env` с реальными данными
- Персональные данные
- Файлы `open_launches_summary.json` с реальными данными

✅ **Всегда используйте:**
- Переменные окружения для конфиденциальных данных
- `.env.example` как шаблон (если создадите)
- Placeholder значения в примерах кода

## Полезные команды Git

```bash
# Посмотреть статус
git status

# Посмотреть изменения
git diff

# Добавить конкретный файл
git add filename.py

# Отменить добавление файла
git reset filename.py

# Посмотреть историю коммитов
git log --oneline

# Обновить код с GitHub
git pull origin main
```

## Если что-то пошло не так

Если случайно закоммитили конфиденциальные данные:

1. **Немедленно** смените токены/пароли
2. Удалите файл из истории Git:
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch path/to/file" \
     --prune-empty --tag-name-filter cat -- --all
   ```
3. Или используйте `git-filter-repo` (более современный инструмент)
4. Принудительно отправьте изменения:
   ```bash
   git push origin --force --all
   ```

**Внимание:** Force push изменяет историю, используйте осторожно!

