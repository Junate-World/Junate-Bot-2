Voice-Activated Chatbot with Learning Ability
This is a Python-based voice-activated chatbot that can recognize your speech, match your question to a knowledge base, and provide an appropriate response using text-to-speech (TTS). If the chatbot doesn't know the answer, you can teach it new responses that are saved to the knowledge base for future conversations.

Features
Speech Recognition: The chatbot listens to your questions and converts your speech into text.
Natural Language Processing: It finds the closest matching question in the knowledge base using fuzzy matching.
Text-to-Speech (TTS): Provides vocal responses to your questions using Google Text-to-Speech.
Learning Ability: If the chatbot doesn't know an answer, you can teach it and the response is saved for future use.
Persistent Knowledge Base: The knowledge base is stored in a JSON file, allowing the chatbot to remember answers across sessions.
Typing_effect: Simulates typing out text word by word with a delay.

Requirements
Before you begin, ensure you have met the following requirements:

Python 3.x
The following Python libraries:
gTTS (Google Text-to-Speech)
speech_recognition
json
difflib
os
time (optional for delays)
pyaudio (optional for speech recognition)

You can install these packages using the following command:

bash

pip install gTTS SpeechRecognition pyaudio

Usage
Clone this repository or download the code.

Prepare the Knowledge Base: Create a JSON file named knowledge_base.json. The format should look like this:
{
  "questions": [
    {"question": "what is python", "answer": "Python is a programming language."},
    {"question": "how are you", "answer": "I am doing well, thank you!"}
  ]
}

Run the Chatbot: Execute the "yourchatbotname.py" script to start the chatbot.
bash
python chat_bot.py

Interacting:

Speak your question when prompted.
If the chatbot knows the answer, it will respond using TTS and print the answer to the console.
If the chatbot does not know the answer, you will be asked to provide a response. This new response will be saved to the knowledge base.

To Quit: Say "quit" to exit the chatbot.

Example Interaction
vbnet

Bot is listening to your speech...
You: what is python
Bot: Python is a programming language.

If the bot doesn't know the answer:

vbnet

Bot: I don't know the answer. Can you teach me?
You: Type the new answer or "skip" to skip: "Python is a programming language for developers."
Bot: Thank you! I learned a new response!
#   J u n a t e - B o t - 2 
 
 