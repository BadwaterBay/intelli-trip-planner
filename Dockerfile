# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.4-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN mkdir /app/

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY src /app/src/

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# ENTRYPOINT [ "python" ]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "localhost:5000", "src.app:app"]
