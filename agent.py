import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams

# Path to your MCP Toolbox binary and tools.yaml config
MCP_TOOLBOX_PATH = os.path.abspath("D:\\DularishMyPersonal\\FirstADKProj\\toolbox.exe")
TOOLS_YAML_PATH = os.path.abspath("D:\\DularishMyPersonal\\FirstADKProj\\tools.yaml")

# Define the agent
# sql_agent = LlmAgent(
#     model='gemini-2.5-flash',
#     name='sql_query_agent',
#     instruction='You are a database assistant. Use the tools to query SQL Server.',
#     tools=[
#         MCPToolset(
#             connection_params=StdioServerParameters(
#                 command=MCP_TOOLBOX_PATH,
#                 args=[
#                     "--tools-file",
#                     TOOLS_YAML_PATH
#                 ]
#             )
#         )
#     ]
# )

sql_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='sql_query_agent',
    instruction='You are a database assistant. Use the tools to query SQL Server.',
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                command=MCP_TOOLBOX_PATH,
                args=["--tools-file", TOOLS_YAML_PATH]
            )
        )
    ]
)
