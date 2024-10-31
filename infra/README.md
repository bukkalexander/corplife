
# Infrastructure as Code (IaC) - Root Folder

This repository contains the infrastructure configuration for deploying resources using **OpenTofu** (formerly Terraform). The infrastructure is modularized, separating different components by function for easier management and scalability.

## Table of Contents
- [Infra Folder Structure](#infra-folder-structure)
- [Overview](#overview)
- [Usage](#usage)
  - [Initial Setup](#initial-setup)
  - [Main Deployment](#main-deployment)
- [Modules](#modules)

---

## Infra Folder Structure

Below is the structure of this IaC folder, with a brief description of each directory and file.

```
Root IaC Folder
├── main/
│   ├── backend.tf        # Backend configuration (e.g., S3 for state storage)
│   ├── main.tf           # Main entry point that orchestrates the modules
│   └── variables.tf      # Input variables for configuring the infrastructure
├── modules/
│   ├── providers/        # Module for setting up cloud providers (e.g., AWS)
│   └── ...               # Additional modules for other infrastructure components
```

### Folder Descriptions:
- **`main/`**: The main folder where all the infrastructure modules are integrated. This is the configuration you apply to deploy the resources using OpenTofu.
- **`modules/`**: A collection of reusable modules that define specific infrastructure components (e.g., backend storage, cloud providers). Modules help to modularize and encapsulate logic for reuse and separation of concerns.
---

## Overview

This repository is designed to manage cloud infrastructure using OpenTofu. The configurations are divided into modular components to ensure reusability and maintainability. By utilizing this approach, you can easily scale and manage your infrastructure with minimal effort.

- **State Management**: We are using an S3 bucket (with optional DynamoDB for state locking) to manage the OpenTofu state across environments.
- **Provider Configuration**: The provider setup (e.g., AWS) is modularized to simplify management of credentials, regions, and environments.

---

## Usage

### Main Deployment

Once the backend is configured, the main infrastructure can be deployed from the `main` folder. This integrates all the required modules to deploy your resources.

#### Steps:
1. Navigate to the `main` folder:
   ```bash
   cd main/
   ```
2. Initialize the configuration:
   ```bash
   opentofu init
   ```
3. Review the plan:
   ```bash
   opentofu plan
   ```
4. Apply the configuration:
   ```bash
   opentofu apply
   ```

This will deploy the infrastructure as defined by the various modules (e.g., VPC, networking, compute instances, etc.).

---

## Modules

The infrastructure is divided into several reusable modules located in the `modules/` directory. Here are some key modules:

- **`providers/`**: Configures the cloud providers (e.g., AWS) and their regions for the infrastructure.
- **Other Modules**: Additional modules can be added here to encapsulate various aspects of the infrastructure such as networking, security, and compute resources.

You can easily extend the infrastructure by creating new modules in the `modules/` directory and referencing them in the `main.tf` file.
