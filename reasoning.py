# reasoning.py

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def reason_answer(question, memory):
    """
    question: câu hỏi hiện tại của user
    memory: list hội thoại trước đó (role/content)
    """

    messages = []

    # add memory vào context
    for m in memory:
        messages.append({
            "role": m["role"],
            "content": m["content"]
        })

    # add câu hỏi hiện tại
    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content
