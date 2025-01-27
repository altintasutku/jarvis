# Copyright (c) 2024 Utku Altıntaş
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import speech_recognition as sr
import pyttsx3
from ollama import Client
from gtts import gTTS
import os
import playsound

class AIVoiceAssistant:
    def __init__(self):
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        
        # Ses ayarlarını yapılandır
        voices = self.engine.getProperty('voices')
        # Mevcut sesleri kontrol et ve kadın sesini seç (genellikle daha doğal)
        for voice in voices:
            if "female" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        
        # Konuşma hızını ayarla (default: 200)
        self.engine.setProperty('rate', 175)
        
        # Ses tonunu ayarla (default: 100)
        self.engine.setProperty('volume', 0.9)
        
        # Initialize Ollama client
        self.client = Client(host='http://localhost:11434')
        
        # Define model names
        self.evaluation_model = 'llama3.2:1b'
        self.simple_model = 'llama3.2:1b'
        self.complex_model = 'deepseek-r1:8b'
        
        #self.language = 'tr'  # Türkçe için
        self.language = 'en'  
        
    def listen(self):
        """Capture voice input from the user"""
        with sr.Microphone() as source:
            print("Listening...")
            self.speak("I'm listening")
            audio = self.recognizer.listen(source)
            
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
                return None
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
                return None

    def evaluate_complexity(self, text):
        """Evaluate if the task is simple or complex using the smaller model"""
        prompt = f"""Evaluate if the following request is simple or complex. 
        Reply with only one word - either 'simple' or 'complex'.
        Request: {text}"""
        
        response = self.client.chat(model=self.evaluation_model, messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ])
        
        result = response.message.content.strip().lower()
        return result == 'complex'

    def get_ai_response(self, text, is_complex):
        """Get response from appropriate AI model based on complexity"""
        model = self.complex_model if is_complex else self.simple_model
        
        response = self.client.chat(model=model, messages=[
            {
                'role': 'user',
                'content': text
            }
        ])
        
        return response.message.content

    def speak(self, text):
        """Convert text to speech using Google TTS"""
        print(f"Assistant: {text}")
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save("response.mp3")
        playsound.playsound("response.mp3")
        os.remove("response.mp3")

    def run(self):
        """Main loop of the assistant"""
        self.speak("Hello! I'm your AI assistant. How can I help you?")
        
        while True:
            # Get voice input
            user_input = self.listen()
            
            if user_input:
                # Evaluate complexity
                is_complex = self.evaluate_complexity(user_input)
                print(f"Task evaluated as: {'complex' if is_complex else 'simple'}")
                
                # Get AI response
                response = self.get_ai_response(user_input, is_complex)
                
                # Speak the response
                self.speak(response)

if __name__ == "__main__":
    assistant = AIVoiceAssistant()
    try:
        assistant.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
