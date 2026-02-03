import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def reason_answer(question, session_id):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        # QUAN TRỌNG: không cho app crash
        return f"ERROR from reason_answer: {str(e)}"
