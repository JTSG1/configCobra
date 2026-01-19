# ConfigCobra v0.1.6

ConfigCobra is a lightweight configuration-driven tool for deploying structured data changes to remote PostgreSQL databases via CI/CD pipelines.

Database operations are defined declaratively in YAML, allowing repeatable, controlled updates to configuration tables without manual SQL execution. The focus is deterministic data deployment across environments, making it well suited to containerised and automated workflows.

This is an early release with a deliberately small but practical feature set.

---

## Features (v0.1.6)

- PostgreSQL data deployments  
- Standard CRUD support (insert, update, delete, upsert)  
- Basic field validation against declared column lists  
- Flexible primary key naming  
- Pipeline-friendly execution using environment-driven DB configuration  

---

## Database Configuration

Connection details are supplied via environment variables (designed for container use):

```bash
CONFIG_COBRA_DB_NAME=load-test
CONFIG_COBRA_DB_USER=user-name
CONFIG_COBRA_DB_PASSWORD=strong-password
CONFIG_COBRA_DB_HOST=localhost
CONFIG_COBRA_DB_PORT=54321
