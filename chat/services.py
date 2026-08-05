import os

from dotenv import load_dotenv
from google import genai

from .prompts import SYSTEM_PROMPT
from .agent import execute_tool

# -----------------------------------
# Load Environment
# -----------------------------------

load_dotenv()


# -----------------------------------
# Build Prompt
# -----------------------------------

def build_prompt(history, user_message):

    tool_result = execute_tool(user_message)

    if tool_result:

        product_data = ""

        for product in tool_result:

            product_data += f"""
Product Name : {product['name']}
Price        : ₹{product['price']}
Description  : {product['description']}

----------------------------------
"""

    else:

        product_data = "No product search required."

    prompt = f"""
{SYSTEM_PROMPT}

==================================
AVAILABLE PRODUCTS
==================================

{product_data}

==================================
CHAT HISTORY
==================================
"""

    for item in history:

        role = "Customer" if item["role"] == "user" else "Assistant"

        prompt += f"\n{role}: {item['message']}"

    prompt += f"\nCustomer: {user_message}"

    return prompt


# -----------------------------------
# Ask Gemini
# -----------------------------------

def ask_ai(history, user_message):

    # Create Gemini client only when needed
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    history.append({
        "role": "user",
        "message": user_message
    })

    prompt = build_prompt(history, user_message)

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        answer = response.text

    except Exception as e:

        print("Gemini Error:", e)

        answer = (
            "😔 Sorry, I'm temporarily unavailable because the AI service "
            "is currently unavailable. Please try again in a few minutes."
        )

    history.append({
        "role": "assistant",
        "message": answer
    })

    return answer, history
