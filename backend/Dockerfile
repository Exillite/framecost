FROM python:3.8.2-alpine
COPY . .
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r ../requirements.txt
EXPOSE 8000