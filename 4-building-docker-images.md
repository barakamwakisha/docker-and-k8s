# Building Docker Images

## Introduction
- Building Docker images is a crucial step in containerization.
- We have a Flask app in the `flask-app` folder and a React app in the `web-app` folder, each with its own Dockerfile.
- Let's explore how to build images for these apps.

## Docker Build Command Basics
- The `docker build` command is used to create Docker images.
- Syntax: `docker build [OPTIONS] PATH`
- `PATH` is the build context, the directory containing the Dockerfile and application files.

---

- `--build-arg`: Set build-time variables. These variables can be used in the Dockerfile with the `ARG` instruction.
  - Example:
    ```shell
    docker build --build-arg APP_PORT=5000 -t flask-app .
    ```

---

- `-t`, `--tag`: Assign a name and optionally a tag to the image.
  - Example:
    ```shell
    docker build -t flask-app:1.0 .
    ```

---

- `--file`, `-f`: Specify a different Dockerfile (default is 'Dockerfile').
  - Example:
    ```shell
    docker build -f Dockerfile.dev -t flask-app .
    ```

---

- `--no-cache`: Build the image without using cache. Useful for forcing a full rebuild.
  - Example:
    ```shell
    docker build --no-cache -t flask-app .
    ```

---

- `--rm`: Remove intermediate containers after a successful build to reduce clutter.
  - Example:
    ```shell
    docker build --rm -t flask-app .
    ```

---

- `--quiet`, `-q`: Suppress the build output and only show the final image ID.
  - Example:
    ```shell
    docker build -q -t flask-app .
    ```

---

- `--force-rm`: Always remove intermediate containers, even if the build fails.
  - Example:
    ```shell
    docker build --force-rm -t flask-app .
    ```

## Building the Flask App Image
- Navigate to the `flask-app` directory.

```shell
cd flask-app
```

- Use the `docker build` command to build the image.

```shell
docker build -t flask-app .
```

- The `.` specifies the build context.


## Building the React App Image
- Navigate to the `web-app` directory.
- Use the `docker build` command with build arguments.

```shell
docker build -t react-app .
```

## Listing & Inspecting Images
- Use the `docker images` or `docker image ls` command to list all built images.

```shell
docker images
```

- Use the `docker inspect` command to inspect an image.

```shell
docker inspect flask-app
```