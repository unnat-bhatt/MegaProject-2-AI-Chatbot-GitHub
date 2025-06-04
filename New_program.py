import pyautogui
import pyperclip
import time
from openai import OpenAI
import re

#coordinates can vary system to system so use cusor.py to find coordinates for click
#hope this adds value to your project 
#Don't forget to enter your friend name and your OpenAiapikey



def clean_message(text):
    # Removes all occurrences of [time, date] name:
    pattern = r'\[\d{1,2}:\d{2}\s[ap]m,\s\d{1,2}/\d{1,2}/\d{4}\]\s[^:]+:'
    cleaned = re.sub(pattern, '', text)
    return cleaned.strip()

client = OpenAI(
    api_key = "Your_OpenAiapikey"
)


def is_last_message_from_sender(chat_text, sender_name="Your_Friend"):
    lines = chat_text.strip().split('\n')
    last_sender = None

    for line in lines:
        if line.startswith('[') and '] ' in line:
            try:
                timestamp_and_rest = line.split('] ', 1)
                if len(timestamp_and_rest) != 2:
                    continue
                rest = timestamp_and_rest[1]
                if ': ' in rest:
                    sender, _ = rest.split(': ', 1)
                    last_sender = sender.strip()
            except Exception:
                continue

    return last_sender == sender_name


# Wait a bit to let the user focus the correct window
print("Script will start in 1.5 seconds...")
time.sleep(1.5)

# Step 1: Click the Edge icon
pyautogui.moveTo(423, 751, duration=0.5)
pyautogui.click()
time.sleep(1)

while True:
    # Step 2: Drag to select the text
    
    pyautogui.moveTo(488, 159, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(1319, 645, duration=1.5)
    pyautogui.mouseUp()

    # Step 3: Copy selected text to clipboard
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5) 
    pyautogui.click(1320,630)


    # Step 4: Get the text from the clipboard
    time.sleep(0.5)  # Give clipboard time to update
    chat_history = pyperclip.paste()

    print("Copied text:")
    print(chat_history)

    # Clean the chat history to remove [time, date] sender: from beginning
    cleaned_chat_history = clean_message(chat_history)

    print("Cleaned text:")
    print(cleaned_chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
    
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
        
        {"role": "system", "content":"You are a person named kaka who speaks hindi as well as english. you are form India and you are a coder. You analyze chat history and respond like kaka in typing language of english. Output should be the next chat response as kaka"},
        {"role": "user", "content": cleaned_chat_history}
            ]
            )

        response = completion.choices[0].message.content

        pyperclip.copy(response)

        # Give user time to focus the correct window
        print("Starting in 2 seconds...")
        time.sleep(1)

        # Step 1: Click at (978, 684)
        pyautogui.click(978, 684)
        time.sleep(0.5)

        # Step 2: Paste the clipboard content (Ctrl+V)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)

        # Step 3: Press Enter
        pyautogui.press('enter')

