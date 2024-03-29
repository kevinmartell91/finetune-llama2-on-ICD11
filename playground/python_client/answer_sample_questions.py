import lamini
import jsonlines
from tqdm import tqdm
import os

lamini.api_key = os.getenv("LAMINI_API_KEY")

def main():
    """
    Main function to load questions, answer them, and save the answers.
    """
    questions = load_questions()

    answers = answer_questions(questions)

    save_answers(answers)

def load_questions():
    """
    Load questions from a JSON file.
    """
    with jsonlines.open("sample_questions.jsonl") as reader:
        questions = [q for q in reader]

    return questions

def answer_questions(questions):
    """
    Answer the given questions using the MistralRunner from lamini.
    """
    answers = []

    for question in tqdm(questions):
        llm = lamini.MistralRunner()

        answer = llm(question["question"])

        answers.append({
            "question": question["question"],
            "answer": answer
        })

    return answers

def save_answers(answers):
    """
    Save the answers to a JSON file.
    """
    with jsonlines.open("data/sample_answers.jsonl", mode="w") as writer:
        writer.write_all(answers)

if __name__ == "__main__":
    main()