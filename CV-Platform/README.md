# FastAPI Dockerized Application

## Overview

This project is a simple FastAPI application running inside Docker, with PostgreSQL as the database. It provides two endpoints:

- `GET /`: Returns a hello message.
- `GET /db-check`: Attempts to connect to the PostgreSQL database and returns connection status.

## Project Structure

```
fastapi-docker-app/
│   .dockerignore
│   .env
│   .gitignore
│   Commands.pdf
│   docker-compose.yml
│   Dockerfile
│   requirements.txt
│   
└───app
    │   main.py
    │   __init__.py
    │   
    └───__pycache__
```

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

## Running the Application

1. **Build and start the services:**

   ```bash
   docker-compose up --build
   ```

2. **Access the application:**

   - Open your browser and go to `http://localhost:8000` to see the root endpoint response.
   - Check the database connection endpoint at `http://localhost:8000/db-check`.

3. **Stop the services:**

   In the terminal where Docker Compose is running, press `CTRL+C`. Then remove the containers (optional):

   ```bash
   docker-compose down -v
   ```

## Environment Variables

The `.env` file contains the database configuration:

```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
POSTGRES_PORT

DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASS
```

## Useful Commands

- **Rebuild without cache:**

  ```bash
  docker-compose build --no-cache
  ```

- **View logs:**

  ```bash
  docker-compose logs -f
  ```

- **Remove all stopped containers, networks, and volumes:**

  ```bash
  docker system prune -af --volumes
  ```

## License

This project is for educational and demonstration purposes.

