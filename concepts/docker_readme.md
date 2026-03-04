# Docker Commands Reference

Quick reference for Docker commands used with the concepts application.

## 1. Docker Build

Build a Docker image from the Dockerfile in the current directory.

```bash
docker build -t concepts-app .
```

- `-t concepts-app` — Tags the image with the name `concepts-app`
- `.` — Build context (current directory)

---

## 2. Docker Images

List all Docker images on your system.

```bash
docker images
```

To filter by repository name:

```bash
docker images concepts-app
```

---

## 3. Docker Run

Run a container from an image.

```bash
docker run -p 8000:8000 concepts-app
```

- `-p 8000:8000` — Maps host port 8000 to container port 8000
- Run in detached mode (background): add `-d`

```bash
docker run -d -p 8000:8000 concepts-app
```

---

## 4. Docker Run (Interactive Terminal)

Run a container with an interactive terminal (useful for debugging or shell access).

```bash
docker run -it concepts-app /bin/bash
```

- `-i` — Keep STDIN open (interactive)
- `-t` — Allocate a pseudo-TTY (terminal)
- `/bin/bash` — Command to run (opens a shell inside the container)

To run the app and get a shell:

```bash
docker run -it -p 8000:8000 concepts-app /bin/bash
# Then inside: uvicorn app.rest:app --host 0.0.0.0 --port 8000
```

---

## 5. Docker Compose Up (with Build)

Build and start services defined in `docker-compose.yml`.

```bash
docker compose up --build
```

- `--build` — Build images before starting containers
- Runs in foreground (logs visible). Add `-d` for detached mode:

```bash
docker compose up --build -d
```

---

## 6. Docker Compose Down

Stop and remove containers, networks, and volumes created by `docker compose up`.

```bash
docker compose down
```

To also remove volumes:

```bash
docker compose down -v
```

---

## Quick Start (Concepts App)

```bash
# Build the image
docker build -t concepts-app .

# Run the container
docker run -p 8000:8000 concepts-app
```

Then open http://localhost:8000 in your browser.
