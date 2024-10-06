import json
from difflib import get_close_matches
from time import sleep
from gtts import gTTS
import os
import speech_recognition as sr
import time
import sys

recognizer = sr.Recognizer()


def load_knowledge_base(file_path: str) -> dict:
    """Load the knowledge base from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data: dict = json.load(file)
        return data
    except FileNotFoundError:
        print(f'Error: File {file_path} not found.')
        return {"questions": []}


def save_knowledge_base(file_path: str, data: dict):
    """Save the knowledge base to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    """Find the closest match to the user's question."""
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def text_to_speech(text: str, filename: str):
    """Convert text to speech and play the audio."""
    tts = gTTS(text, lang="en")
    tts.save(filename)
    os.system(f"start {filename}")

def typing_effect(text: str, delay: float = 0.6):
    """Simulate typing out text word by word with a delay."""
    words = text.split()  # Split the text into words
    for word in words:
        print(word, end=' ', flush=True)  # Print word followed by space
        sys.stdout.flush()  # Ensure the output is displayed immediately
        time.sleep(delay)  # Delay between each word in milliseconds

    print()

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    """Find and return the answer for a given question from the knowledge base."""
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            text_to_speech(q["answer"], "answer.mp3")
            
            return q["answer"]
    return None


def chat_bot():
    """Main chatbot function."""
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        try:
            with sr.Microphone() as source:
                sleep(1)
                print("Bot is listening to your speech...")
                recognizer.adjust_for_ambient_noise(source, duration=2)
                audio = recognizer.listen(source)

                try:
                    user_input: str = recognizer.recognize_google(audio).lower()
                    print(f'You: {user_input}')
                except sr.UnknownValueError:
                    text_to_speech('Sorry, I could not understand what you said.', "answer.mp3")
                    sleep(4)
                    print("Sorry, I could not understand what you said.")
                    continue

                if user_input == 'i quit' or user_input == 'quit' or user_input == 'exit':
                    text_to_speech('Thanks for your time and goodbye!', "answer.mp3")
                    print("Goodbye!")
                    break

                best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

                if best_match:
                    answer: str = get_answer_for_question(best_match, knowledge_base)
                    typing_effect(f'Bot: {answer}')
                else:
                    text_to_speech('I don\'t know the answer. Can you teach me?', "answer.mp3")
                    print('Bot: I don\'t know the answer. Can you teach me?')
                    sleep(4)
                    text_to_speech('Type the new answer or "skip" to skip:', "answer.mp3")
                    new_answer: str = input('Type the new answer or type "skip" to skip: ')

                    if new_answer.lower() != 'skip':
                        knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                        save_knowledge_base('knowledge_base.json', knowledge_base)
                        text_to_speech('Thank you! I learned a new response!', "answer.mp3")
                        print('Bot: Thank you! I learned a new response!')

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    chat_bot()