from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")
tools = toolbox.load_toolset('sahayak_toolset')

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for user questions regarding rollnumbers',
    instruction='Answer user questions to the best of your knowledge regarding rollNumber and corresponding names in the database.',
    tools = tools,
)