# Creating a Kubernetes Cluster

## Introduction
- A Kubernetes cluster is a set of physical or virtual machines that run Kubernetes.
- It manages containerized applications, provides scalability and fault tolerance, and automates many tasks.
- In this section, we will learn about different Kubernetes components and deploy our Flask and React apps in a cluster using images from a container registry.

## Kubernetes Components and Their Functions
1. **Pod**
- The smallest deployable unit in Kubernetes.
- A Pod can host one or more containers.
- Provides a shared network namespace and storage volumes.

2. **Service**
- Manages network access to a set of Pods.
- Types of Services
    - `ClusterIP` (default): Exposes a service on an internal IP within the cluster.
    - `NodePort`: Exposes a service on a static port on each node's IP.
    - `LoadBalancer`: Exposes a service using a cloud load balancer.
    - `ExternalName`: Maps the service to an external name.

3. **Ingress**
- Manages external access to services.
- Acts as a reverse proxy to route traffic to different services based on rules.
- Supports SSL termination and host-based routing.

4. **ConfigMap**
- Stores configuration data as key-value pairs.
- Can be injected into Pods as environment variables or mounted as files.
- Useful for separating configuration from application code.

5. **Secret**
- Similar to ConfigMap but used for sensitive data like passwords and API keys.
- Stored securely and can be used as environment variables or mounted as files in Pods.

6. **Volume**
- Provides storage for Pods.
- Supports various types, including `emptyDir`, `hostPath`, and cloud-based volumes.
- Useful for sharing data between containers in the same Pod.

7. **Deployment**
- A declarative way to manage Pods and ReplicaSets.
- Ensures a specified number of replicas are running and handles updates.
- Useful for stateless applications that can scale horizontally.

8. **StatefulSet**
- Manages Pods with unique identities and persistent network identities.
- Useful for stateful applications that require stable network identities.

## YAML Files in Kubernetes
- **YAML** (YAML Ain't Markup Language) is a human-readable data serialization format used in Kubernetes to define and configure resources.
- In Kubernetes, YAML files are used to declare various resources, such as Pods, Services, Deployments, ConfigMaps, and more.
- Each resource is defined in a separate YAML file.
- YAML files consist of key-value pairs and lists, structured hierarchically using indentation.
- Kubernetes resources are defined by their specifications, including metadata, containers, volumes, and other attributes.
- YAML files make it easy to version and manage configurations for different environments (e.g., development, staging, production) by adjusting the files as needed.
See example [Deployment yaml file](./k8s/flask-deployment.yml)

## `kubectl` - The Kubernetes Command-Line Tool
- `kubectl` is the command-line interface (CLI) tool for interacting with a Kubernetes cluster.
- It allows you to perform various actions, such as deploying resources, inspecting the cluster, and managing applications.
- Common kubectl commands include:
    - `kubectl apply -f <filename>`: Deploy resources defined in a YAML file.
    - `kubectl get <resource>`: Retrieve information about resources (Pods, Services, Deployments, etc.).
    - `kubectl describe <resource> <resource-name>`: Get detailed information about a resource.
    - `kubectl logs <pod-name>`: Retrieve container logs from a Pod.
    - `kubectl exec -it <pod-name> -- <command>:` Execute a command in a running container.
    - `kubectl delete <resource> <resource-name>`: Delete resources.

- kubectl uses a configuration file (kubeconfig) to connect to a Kubernetes cluster. This file contains cluster details, authentication information, and context settings.
- You can switch between different contexts (e.g., multiple clusters or namespaces) using `kubectl config use-context <context-name>`.
- kubectl is an essential tool for managing and maintaining Kubernetes clusters, deploying applications, and troubleshooting issues.

## Let's Deploy Our Apps in a Kubernetes Cluster 🚀
- Reference the [k8s](./k8s) folder for the yaml files
- Use `kubectl apply -f <filename>` to deploy the yaml files

```shell
kubectl apply -f k8s/flask-deployment.yml
kubectl apply -f k8s/flask-service.yml
kubectl apply -f k8s/react-deployment.yml
kubectl apply -f k8s/react-service.yml
```

- Run `kubectl get service` to get an overview of the services running in the cluster

- You can now test the flask-app from your computer browser at `http://localhost:30200` and the react-app at `http://localhost:30100`.