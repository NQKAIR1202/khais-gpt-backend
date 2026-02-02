# memory.py

# Lưu hội thoại theo session_id
conversation_memory = {}

def get_memory(session_id):
    return conversation_memory.get(session_id, [])

def save_memory(session_id, role, content):
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    conversation_memory[session_id].append({
        "role": role,
        "content": content
    })
