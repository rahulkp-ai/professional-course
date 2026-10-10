# Docker Engine Notes

## 1. Docker Architecture & Client-Server Model

Docker Engine operates on a standard **Client-Server Architecture**.

- **Docker CLI (Client):** The command-line interface utility where users execute Docker commands.
- **Docker Daemon (`dockerd` / Server):** The background service acting as the server. It receives inputs from the CLI, manages Docker objects, and runs operations.
- **REST API:** The communication bridge that allows the Docker Client and Docker Daemon to interact with each other.

---

## 2. Platform Support & Installation

Docker Engine can be deployed across major operating systems and environments:

- **Linux:** Supports almost all distributions (e.g., downloadable via **RPM** packages for CentOS/RHEL or **DEB** packages for Ubuntu/Debian).
- **Windows:** Installed via standard **EXE** or **MSI** installers.
- **macOS:** Supported via standard Docker Desktop installation packages.

---

## 3. Configuration & State Management

- **Desired State:** Administrators can define specific conditions and configurations for the Docker Engine via configuration files or configuration management tools.
- **Automated Management:** The Docker Engine automatically modifies settings to continuously maintain the defined state.

---

## 4. Docker Swarm

- **Clustering Concept:** A cluster is a group or collection of servers providing similar services.
- **Definition:** Docker Swarm is the built-in clustering and container orchestration system embedded directly within the Docker Engine.
- **Swarm Kit:** Serves as the underlying base framework for Swarm orchestration features.

---

## 5. Docker Plugins

Plugins extend the functional capabilities of the Docker Engine. They can be installed and managed (from setup to removal) via Docker Hub or public registries.

### Primary Plugin Types

- **Volume Plugins:** Allow data volumes to persist across multiple separate Docker hosts.
- **Network Plugins:** Provide custom network plumbing and topology setups for containers.
- **Authorization Plugins:** Handle granular access controls and permission checks.

### Extended & Custom Plugins

- **Cloud Integration:** Custom plugins for cloud providers (AWS, GCP, Azure) to extend functionality into cloud environments.
- **CI/CD Integration:** Plugins like the Jenkins Docker plugin extend Docker capabilities into automated build and deployment pipelines.
- **Custom Development:** Docker plugins are customizable, allowing teams to create bespoke drivers tailored to specific infrastructure requirements.

---

## 6. Data Volumes

Data volumes act as the dedicated storage mechanism (analogous to a hard drive or flash storage) for containers within the Docker Engine.

### Key Features

- **Persistence & Sharing:** Data volumes can be shared simultaneously across multiple containers.
- **Cross-Platform Compatibility:** The same volume mechanisms can be utilized on both Linux and Windows operating systems, enabling high portability.
- **Lifecycle Management:** Managed directly via the Docker CLI, making backups, migrations, and cleanups straightforward.
