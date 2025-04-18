# .devcontainer/Dockerfile

# Base image with Python and Node
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install Node.js (v20+)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
  && apt-get install -y nodejs

# Angular CLI
RUN npm install -g @angular/cli

# Install Python packages globally (optional)
COPY backend/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

# Set workdir for VS Code
WORKDIR /workspace
