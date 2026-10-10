## Core Components Workflow

### Core Architecture

Docker Engine consists of three primary components that work in unison as the **Docker Server**:

- **Docker CLI (Client):** The command-line utility where users issue commands and instructions.
- **REST API:** The intermediate communicator and protocol layer that accepts commands from the CLI, transfers them to the daemon, and returns execution results back to the user interface.
- **Docker Daemon (`dockerd` / Server):** A persistent background process that continuously listens for REST API requests, executes operations, manages container lifecycle, and returns output.

---

### End-to-End Workflow & Capabilities

When these core components interact, they enable automated workflows to **build, ship, and run** applications:

1. **Images & Registries:** Containers are instantiated from Docker images pulled from registries such as Docker Hub or private image repositories.
2. **Container Resources:** When launching a container, the Docker Engine provisions and attaches associated storage volumes and networking interfaces.
3. **Execution Loop:**
   $$\text{CLI (User Command)} \longrightarrow \text{REST API} \longrightarrow \text{Docker Daemon (Execution)} \longrightarrow \text{REST API} \longrightarrow \text{CLI Display}$$
