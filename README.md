# Databricks CI/CD Template Project

Enterprise-grade CI/CD template for deploying Python code, notebooks, and libraries to Azure Databricks.

## Features
- Automated testing and deployment pipeline
- Multi-environment support (dev/prod)
- Package management with wheel files
- Code quality checks (black, pylint, mypy)
- Test coverage reporting

## Repository Setup

This project uses a two-repository approach:
1. **Template Repository**: [databricks-devops](https://github.com/narayan-shyam/databricks-devops)
   - Contains reusable CI/CD workflows
   - Must be public for non-Enterprise GitHub accounts
   - Contains core deployment logic

2. **Project Repository** (Current): databricks_demo
   - Contains project-specific code
   - Uses workflows from template repository
   - Configures environment-specific settings

### GitHub Enterprise vs Non-Enterprise Setup

#### For GitHub Enterprise Users:
- Template repository can remain private
- Configure repository access in organization settings
- Use organization-specific workflow references:
  ```yaml
  uses: your-org/databricks-devops/.github/workflows/databricks-enterprise.yml@main
  ```

#### For Non-Enterprise GitHub Users:
- Template repository must be public
- No special organization settings required
- Use public repository reference:
  ```yaml
  uses: narayan-shyam/databricks-devops/.github/workflows/databricks-enterprise.yml@main
  ```

## Project Structure
```
databricks_demo/
├── .github/workflows/      # CI/CD pipeline definitions
├── src/data_processor/     # Main package code
├── notebooks/             # Databricks notebooks
├── tests/                # Unit and integration tests
└── requirements.txt      # Dependencies
```

## Workflow Structure
```
databricks_demo/
└── .github/
    └── workflows/
        └── main.yml       # Calls template workflow from databricks-devops repo
```

This workflow calls the enterprise deployment template with project-specific configurations.

## Prerequisites Configuration

### 1. Azure Databricks Setup

#### Get DATABRICKS_HOST:
1. Login to Azure Portal
2. Navigate to your Databricks workspace
3. Click on "Launch Workspace"
4. Once in Databricks console, copy the URL from your browser
   - Example: https://adb-xxxxxxxxxxxxx.xx.azuredatabricks.net
   - This is your DATABRICKS_HOST

#### Get DATABRICKS_TOKEN:
1. In Databricks workspace, click on Settings (gear icon) in the left sidebar
2. Click on User Settings
3. Go to the "Access Tokens" tab
4. Click "Generate New Token"
   - Provide a description (e.g., "GitHub Actions Deploy")
   - Set an expiration period (90 days recommended)
5. Click "Generate"
6. **IMPORTANT**: Copy the token immediately - it won't be shown again
   - This is your DATABRICKS_TOKEN

#### Get DATABRICKS_CLUSTER_ID:
1. In Databricks workspace, click on "Compute" in the left sidebar
2. Find your target cluster
3. Click on the cluster name
4. In the cluster details page, look at the URL
   - It will look like: `.../clusters/xxxx-xxxxxx-xxxxxxxx`
   - The last part (xxxx-xxxxxx-xxxxxxxx) is your DATABRICKS_CLUSTER_ID
5. Copy this ID

### 2. GitHub Repository Setup

#### a. Template Repository Access
1. Ensure access to databricks-devops repository
2. For non-Enterprise GitHub:
   - Verify template repository is public
   - No additional access configuration needed
3. For Enterprise GitHub:
   - Configure organization-level access
   - Grant workflow permissions

#### b. Configure GitHub Secrets:
1. Go to your GitHub repository
2. Click on "Settings" tab
3. In the left sidebar, click "Secrets and variables" → "Actions"
4. Click "New repository secret"
5. Add each secret:

   a. DATABRICKS_HOST
   - Name: DATABRICKS_HOST
   - Value: Your Databricks workspace URL (from step 1)
   - Click "Add secret"

   b. DATABRICKS_TOKEN
   - Name: DATABRICKS_TOKEN
   - Value: Your generated access token (from step 2)
   - Click "Add secret"

   c. DATABRICKS_CLUSTER_ID
   - Name: DATABRICKS_CLUSTER_ID
   - Value: Your cluster ID (from step 3)
   - Click "Add secret"

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/databricks_demo.git
cd databricks_demo
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create .env file (don't commit this!)
echo "DATABRICKS_HOST=your-workspace-url" > .env
echo "DATABRICKS_TOKEN=your-token" >> .env
```

## Running Tests

### Unit Tests:
```bash
pytest tests/unit
```

### Integration Tests:
```bash
pytest tests/integration
```

## Deployment Process

### Manual Verification After Deployment:
1. Login to Databricks workspace
2. Navigate to "Workspace" → "Shared" in left sidebar
3. Look for your deployed code in the specified path
   - For prod: /Shared/data_processor/prod
   - For dev: /Shared/data_processor/dev
4. Verify files are present:
   - processor.py
   - utils.py
   - __init__.py
5. Click on files to verify content
6. Optional: Run a notebook to test functionality

### CLI Verification:
```bash
# List deployed files
databricks workspace ls /Shared/data_processor/prod

# Export a file to verify content
databricks workspace export /Shared/data_processor/prod/processor.py processor.py
```

## Branch Strategy
- `main`: Production code
- `develop`: Development code
- Feature branches: Create from `develop`

## Contributing
1. Create feature branch from develop
2. Make changes
3. Run tests
4. Submit PR to develop
5. After review, merge to develop
6. Merge develop to main for production release

## Troubleshooting

### Common Issues:

1. Deployment Failed:
   - Verify secrets are correctly set in GitHub
   - Check Databricks token hasn't expired
   - Ensure paths exist in Databricks workspace
   - Verify template repository accessibility (public/private settings)

2. Tests Failed:
   - Verify virtual environment is activated
   - Run `pip install -r requirements.txt`
   - Check Python version (3.8 or 3.9)

3. Permission Issues:
   - Verify Databricks token permissions
   - Check workspace access rights
   - Ensure cluster access permissions

4. Workflow Reference Issues:
   - For non-Enterprise: Verify template repo is public
   - For Enterprise: Check organization access settings
   - Verify workflow file paths in both repositories
