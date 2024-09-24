FROM python:3.12-slim-bookworm

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the application into the container.
COPY . /app/backend

# Install the application dependencies.
WORKDIR /app/backend
RUN uv sync --no-cache