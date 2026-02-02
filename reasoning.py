from dataset import find_answer

def reason(question, memory):
    # 1. Ưu tiên kiến thức đã train
    dataset_answer = find_answer(question)
    if dataset_answer:
        return dataset_answer

    # 2. Nếu có hội thoại trước → suy luận
    if memory:
        last_topic = memory[-1]
        return f"Dựa trên câu hỏi trước ('{last_topic}'), thì '{question}' có thể hiểu là liên quan đến chủ đề đó."

    # 3. Không biết → fallback
    return "Câu này tao chưa được dạy, mày có thể hỏi rõ hơn hoặc tao sẽ search giúp mày."
