# tests/integration/test_databricks_deploy.py
import os
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.workspace.api import WorkspaceApi

def test_databricks_connection():
    host = os.getenv('DATABRICKS_HOST')
    token = os.getenv('DATABRICKS_TOKEN')
    
    # Verify environment variables are set
    assert host is not None, "DATABRICKS_HOST environment variable not set"
    assert token is not None, "DATABRICKS_TOKEN environment variable not set"
    
    api_client = ApiClient(
        host=host,
        token=token
    )
    workspace_api = WorkspaceApi(api_client)
    assert workspace_api is not None
    
    # Verify client configuration
    assert api_client.url == host
