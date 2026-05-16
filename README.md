# KB Workflow App

A Flask-based troubleshooting workflow application deployed to Microsoft Azure App Service.

## Overview

This project was built to practice real-world cloud infrastructure, deployment workflows, and application hosting in Azure.

The application allows users to navigate troubleshooting workflows through a lightweight Flask web interface.

## Features

- Flask backend application
- HTML/CSS frontend
- Workflow-based troubleshooting system
- Azure App Service deployment
- GitHub version control integration
- Azure CLI deployment workflow
- Azure budgeting and cost monitoring

## Technologies Used

- Python
- Flask
- HTML
- CSS
- GitHub
- Microsoft Azure
- Azure App Service
- Azure CLI

## Cloud Infrastructure

Azure resources used in this deployment:

- Azure Resource Group
- Azure App Service Plan
- Azure Web App
- Azure Cost Management Budget Alerts

## Deployment Process

The application was deployed using Azure CLI commands directly from VS Code.

Core workflow included:

```bash
az login
az group create
az appservice plan create
az webapp create
az webapp up
