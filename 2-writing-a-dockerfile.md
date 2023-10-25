# Writing a Dockerfile - Crafting Your Application's Container Blueprint

## Dockerfile Basics
- A Dockerfile is a text document that contains a set of instructions to build a Docker image.
- It defines the base image, sets up the environment, copies application files, and configures the container.
- Docker commands are executed in sequence to create the image.

## Sample Dockerfile
[View Dockerfile](./flask-app/Dockerfile)

## Understanding the Sample Dockerfile
- `FROM`: Specifies the base image (Python 3.8) for the new image.
- `WORKDIR`: Sets the working directory to `/app` within the container.
- `COPY`: Copies the local directory into the container at `/app`.
- `RUN`: Installs Python packages listed in `requirements.txt`.
- `EXPOSE`: Exposes port 80 for incoming connections.
- `ENV`: Sets an environment variable `NAME`.
- `CMD`: Defines the command to run when the container starts.
