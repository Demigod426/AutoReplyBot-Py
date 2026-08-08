import pyautogui
import pyperclip
import time

# 1. Click the icon
pyautogui.click(1180, 1044)

# Give the UI time to respond
time.sleep(1)

# 2. Drag to select the text
pyautogui.moveTo(865, 222, duration=0.2)
pyautogui.dragTo(1899, 894, duration=1, button="left")

# Give selection time to complete
time.sleep(0.5)

# 3. Copy selected text
pyautogui.hotkey("ctrl", "c")

# Wait for clipboard to update
time.sleep(0.5)

# 4. Store clipboard contents in a variable
text = pyperclip.paste()

# 5. Use the variable
print("Copied text:")
print(text)