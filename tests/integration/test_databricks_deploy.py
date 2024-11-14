# tests/integration/test_databricks_deploy.py
import os
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.workspace.api import WorkspaceApi

def test_databricks_connection():
   host = os.getenv('DATABRICKS_HOST')
   token = os.getenv('DATABRICKS_TOKEN')
   
   api_client = ApiClient(
       host=host,
       token=token
   )
   workspace_api = WorkspaceApi(api_client)
   workspaces = workspace_api.list_objects("/")
   assert workspaces is not None
