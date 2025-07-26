from google.adk.agents import BaseAgent, InvocationContext
from google.genai import types as genai_types
from google.adk.events import Event
import requests

class URLContentExtractorAgent(BaseAgent):
    async def _run_async_impl(self, ctx:InvocationContext):
        async for event in self.impl(ctx):
            yield event

    async def _run_live_impl(self, ctx):
        async for event in self.impl(ctx):
            yield event

    async def impl(self, ctx):
        url = ctx.session.state['url']
        url = url.strip()
        response = requests.get(url, verify=False, timeout= 90 * 1000)
        yield Event(
            author=self.name,
            invocation_id=ctx.invocation_id,
            content=genai_types.Content(parts=[genai_types.Part(text=response.text)]),
            turn_complete=True,
        )