import pyautogui
import pyperclip
import time
import requests

pyautogui.FAILSAFE = False

pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
time.sleep(2)

pyautogui.click(686, 203)
time.sleep(0.5)

pyautogui.moveTo(686, 203, duration=0.3)

pyautogui.dragTo(
    1843,
    933,
    duration=2.5,
    button="left"
)

time.sleep(1)

pyperclip.copy("")
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

chat = pyperclip.paste()

if chat == "":
    print("Nothing copied")
    quit()

print("Chat copied")

lines = chat.strip().split("\n")

message = lines[-1].strip()
print("Last message:", message)

pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
time.sleep(1)

print("Sending to Ollama...")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3:latest",
        "prompt": f"""
Reply naturally to this WhatsApp message.

Message:
{message}

Rules:
- Reply ONLY to this message
- Understand exact meaning
- Ignore previous chat
- Sound like a real friend from India
- Use casual English/Hinglish
- Keep reply short under 12 words
- Never explain
- Never summarize
- Never mention AI

Output only reply text.
""",
        "stream": False
    }
)

reply = response.json()["response"].strip()
print("AI Reply:", reply)

pyperclip.copy(reply)

pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
time.sleep(2)

pyautogui.click(1200, 980)
time.sleep(0.3)

pyautogui.hotkey("ctrl", "v")
time.sleep(0.2)

pyautogui.press("enter")

print("Message sent.")