# Kubernetes

Kubernetes is an open source orchestration system for Docker containers. It is used to manage the state of the containers (start/stop them automatically).

The main focus is to create a set of stateless apps that can be horizontally scaled. A stateless app:

- Does not write local files or to local sessions
- Session management must occur outside the container
- No Memecahce or Redis
- Files must be stored in Amazon S3 or something similar

You can scale pod up or down by running

    kubectl scale --replicas=0 <pod-name>
    kubectl scale --replicas=3 <pod-name>

## Tools

- [kubernetes](https://github.com/kubernetes/kubernetes)
- [minikube](https://github.com/kubernetes/minikube) implements a local Kubernetes cluster on macOS, Linux, and Windows.

## Definitions

Term                | Definition
--------------------|--------------------------
**Pod**             | <li>Describes an application running on Kubernetes</li><li>Contains one or more tightly coupled containers</li><li>Apps communicate using local port numbers</li>
**Node**            | A group of pods on a single machine
**Cluster**         | A group of nodes overseen by a matter node
**Cluster IP**      | A virtual IP that is only visible within the cluster
**NodePort**        | A port that is the same on each node and is visible outside the cluster
**livelinessProbe** | Checks if the container is running and restarts it if needed
**readinessProbe**  | Checks if the container is ready to serve requests and removes the **Pod**'s IP from the service if it fails

## Deployments

A deployment declaration allows you to do deployments and updates on your app.

- You define the state of the app and Kubernetes ensures that the clusters match the desired state
- This allows create/update actions
- You can also do rolling updates (0 downtime deployments)
- Finally, you can rollback to a previous version of your application

## Pods

Pods are meant to be ephemeral (short-lived). They should never accessed directly. Instead, they should be accessed through a service

## Known Issues

- [Mac minikube setup issue](https://github.com/kubernetes/minikube/issues/2266#issuecomment-453617810)