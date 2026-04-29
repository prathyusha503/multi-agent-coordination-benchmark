import os
from dotenv import load_dotenv

load_dotenv()

def ask_model(prompt, provider="mock"):

    provider = provider.lower()

    try:
        if provider == "openai":
            from openai import OpenAI
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            r = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role":"user","content":prompt}]
            )
            return r.choices[0].message.content

        elif provider == "gemini":
            import google.generativeai as genai

            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-1.5-pro")
            r = model.generate_content(prompt)
            return r.text

        elif provider == "mistral":
            from mistralai.client import MistralClient
            from mistralai.models.chat_completion import ChatMessage

            client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))

            r = client.chat(
                model="mistral-small-latest",
                messages=[ChatMessage(role="user", content=prompt)]
            )

            return r.choices[0].message.content

    except Exception:
        pass

    return mock_response(prompt)


def mock_response(prompt):
    p = prompt.lower()

    if "planner" in p:
        return "Break task into clues and verify evidence."

    if "research" in p:
        return "Likely answer inferred from clues."

    if "critic" in p:
        return "Need stronger validation."

    if "final" in p:
        return "Most probable final answer based on clues."

    return "Generic output."