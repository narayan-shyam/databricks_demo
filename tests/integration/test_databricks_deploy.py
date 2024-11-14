# tests/integration/test_databricks_deploy.py
import pytest
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.workspace.api import WorkspaceApi

def test_databricks_connection(databricks_token, databricks_host):
    api_client = ApiClient(
        host=databricks_host,
        token=databricks_token
    )
    workspace_api = WorkspaceApi(api_client)
    workspaces = workspace_api.list("/")
    assert workspaces is not None