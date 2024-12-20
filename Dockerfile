FROM python:3.14-rc-slim
RUN python3 -m pip install selenium schedule
COPY . /app
WORKDIR /app