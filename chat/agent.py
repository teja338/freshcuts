import json
import os

from dotenv import load_dotenv
from google import genai

from .tools import TOOLS

load_dotenv()

SYSTEM = """
You are FreshCuts AI Planner.

Your only job is deciding which tool to use.

Available tools

1. search_products
2. recipe_tool
3. offers_tool
4. delivery_tool
5. order_tool

Reply ONLY JSON.

Example

{
  "tool":"search_products",
  "query":"chicken"
}

If no tool required

{
  "tool":"none"
}
"""


def choose_tool(message):

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM}\n\nUser:\n{message}"
    )

    text = response.text.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)


def execute_tool(message):

    try:
        plan = choose_tool(message)
    except Exception as e:
        print("Tool selection error:", e)
        return None

    tool_name = plan.get("tool")

    if tool_name == "none":
        return None

    tool = TOOLS.get(tool_name)

    if tool is None:
        return None

    query = plan.get("query", message)

    return tool(query)
