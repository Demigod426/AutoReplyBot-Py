import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client=Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)
command='''
[3:55 pm, 3/8/2026] Person: Hii
[3:55 pm, 3/8/2026] Person: Mujhe AI ki assignment bhejna pls
[3:55 pm, 3/8/2026] Person: 2nd Question se
[11:13 pm, 3/8/2026] Rohan: Mule ke pas hai mene use bola hai ki wo tuze bhej de
[11:13 pm, 3/8/2026] Rohan: Bheja ya nhi usane
[11:14 pm, 3/8/2026] Person: Nahi bheja, kal le luga
[11:14 pm, 3/8/2026] Rohan: Okk
'''
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
            "content":command
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(completion.choices[0].message.content)