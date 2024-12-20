FROM python:3.14-rc-slim
RUN python3 -m pip install selenium schedule python-dotenv requests
COPY . /app
WORKDIR /app