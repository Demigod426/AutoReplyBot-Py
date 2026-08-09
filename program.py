import pyautogui
import pyperclip
import time
import re
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client=Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

def last_message_is_from_me(chat_history):

    messages = re.findall(
        r'\[\d{1,2}:\d{2}\s?(?:am|pm),\s?\d{1,2}/\d{1,2}/\d{4}\]\s*([^:\n]+):',
        chat_history,
        flags=re.IGNORECASE
    )

    if not messages:
        print("Could not detect any sender.")
        return False

    last_sender = messages[-1].strip()

    print("LAST SENDER:", repr(last_sender))

    return last_sender.lower() == "dev"

pyautogui.click(1180,1044)
time.sleep(1)

while True:
    
    pyautogui.moveTo(925,263,duration=0.2)
    pyautogui.dragTo(1750,891, duration=1,button="left")


    time.sleep(0.5)

    pyautogui.hotkey("ctrl","c")
    pyautogui.click(900,842)

    time.sleep(0.5)

    chat_history=pyperclip.paste()

    print("Copied text:")
    print(chat_history)

    if last_message_is_from_me(chat_history):
       print("Last message was sent by Dev. Waiting...")
       time.sleep(5)
       continue

    print("Last message was NOT sent by Dev.")

    completion=client.chat.completions.create(
        messages=[
            {
            "role":"system",
            "content": """
                        You are a person, an Indian coder who naturally speaks both English and Hindi.
            
                        You are replying to a WhatsApp conversation.
            
                        Analyze the WhatsApp conversation and write ONLY the reply that the person would naturally send.
            
                        Important rules:
                        - Do NOT include timestamps.
                        - Do NOT include sender's name like.
                        - Do NOT explain your reasoning.
                        - Do NOT say things like "Here's a response" or "You can reply with".
                        - Keep the response natural and conversational.
                        - Use Hinglish when appropriate.
                        - Don't sound like an AI assistant.
                        - Match the casual tone of the conversation.
                        - Keep replies reasonably short unless the conversation requires detail.
                                """ 
            },
            {
                "role":"user",
                "content":chat_history
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    response=completion.choices[0].message.content

    response=re.sub(r'^\s*\[\d{1,2}:\d{2}\s?(?:am|pm),\s?\d{1,2}/\d{1,2}/\d{4}\]\s*[^:]+:\s*','',response, flags=re.I)
    response=re.sub(r'\s*\([^)]*\)\s*$','',response).strip()

    pyperclip.copy(response)

    pyautogui.click(1340,942)
    time.sleep(0.5)

    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)

    pyautogui.press("enter")
