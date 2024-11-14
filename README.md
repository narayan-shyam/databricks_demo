# Databricks CI/CD Template Project

Enterprise-grade CI/CD template for deploying Python code, notebooks, and libraries to Azure Databricks.

## Features
- Automated testing and deployment pipeline
- Security scanning with Snyk and OWASP
- Multi-environment support (dev/prod)
- Package management with wheel files
- Code quality checks (black, pylint, mypy)
- Test coverage reporting

## Project Structure
```
databricks_demo/
├── .github/workflows/      # CI/CD pipeline definitions
├── src/data_processor/     # Main package code
├── notebooks/             # Databricks notebooks
├── tests/                # Unit and integration tests
└── requirements.txt      # Dependencies
```

## Setup
1. Configure GitHub Secrets:
   - DATABRICKS_HOST
   - DATABRICKS_TOKEN
   - DATABRICKS_CLUSTER_ID

2. Install Dependencies:
```bash
pip install -r requirements.txt
```

3. Run Tests:
```bash
pytest tests/
```

## Deployment
- PRs trigger development deployment
- Merges to main trigger production deployment

## Environment Variables
Copy `.env.example` to `.env` and configure:
```
DATABRICKS_HOST=your-workspace-url
DATABRICKS_TOKEN=your-token
```