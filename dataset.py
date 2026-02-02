import json
import os

DATASET_PATH = os.path.join("data", "qa_dataset.json")

def load_dataset():
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def find_answer(question):
    dataset = load_dataset()
    question = question.lower()

    for item in dataset:
        if item["question"].lower() in question:
            return item["answer"]

    return None
