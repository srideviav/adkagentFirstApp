from google.adk.agents import BaseAgent, InvocationContext, Agent
from google.genai import types as genai_types
from google.adk.events import Event
from .URLContentExtractorAgent import URLContentExtractorAgent

url_extractor_agent = Agent(
    model='gemini-2.0-flash-001',
    name='url_extractor_agent',
    description='Extracts URL from the input',
    instruction='From the input, extract URL and put to output_key if present, otherwise, display the string "ERROR"',
    output_key="url"
)

url_content_extractor = URLContentExtractorAgent(name="url_content_extractor")

class MyOrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="MyOrchestratorAgent", sub_agents=[url_extractor_agent, url_content_extractor])

    async def _run_async_impl(self, ctx: InvocationContext):
        async for event in self.impl(ctx):
            yield event

    async def _run_live_impl(self, ctx):
        async for event in self.impl(ctx):
            yield event

    async def impl(self, ctx):
        url_extractor_agent_local = self.find_sub_agent("url_extractor_agent")
        async for event in url_extractor_agent_local.run_async(ctx):
            yield event
        url = ctx.session.state['url']
        url = None if "error" in str(url).lower() else url
        if not url:
            yield Event(
                author=self.name,
                invocation_id=ctx.invocation_id,
                content=genai_types.Content(parts=[genai_types.Part(text="No URL found in the input.")]),
                turn_complete=True,
            )
            return
        url_content_extractor_local = self.find_sub_agent("url_content_extractor")
        async for event in url_content_extractor_local.run_async(ctx):
            yield event

root_agent = MyOrchestratorAgent()

if __name__ == "__main__":
    root_agent.run()