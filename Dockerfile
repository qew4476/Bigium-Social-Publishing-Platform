# 使用轻量级的 Python 镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安裝 Poetry
RUN pip install poetry

# 設定環境變數，避免 Poetry 建立虛擬環境
ENV POETRY_VIRTUALENVS_CREATE=false

# 複製依賴文件（假設 pyproject.toml 和 poetry.lock 是你的依賴文件）
COPY pyproject.toml /app/

# 安裝依賴
RUN poetry install --no-root

# 複製其餘項目文件
COPY . /app/

# 暴露端口
EXPOSE 8000

# 設定默認啟動命令
CMD ["poetry", "run", "manage.py", "runserver", "0.0.0.0:8000"]
