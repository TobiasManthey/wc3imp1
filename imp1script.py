import pyautogui
import time
import os
import sys

def resource_path(relative_path):
    # Get the absolute path for images when running as exe
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Example usage:
image_path = resource_path("assets/images")

# Map images to messages
image_messages = {
    resource_path("assets/images/botleft1close.png"): "Bot left!",
    resource_path("assets/images/botleft2close.png"): "Bot left!",
    resource_path("assets/images/topleft1close.png"): "Top left!",
    resource_path("assets/images/topleft2close.png"): "Top left!",
    resource_path("assets/images/botright1close.png"): "Bot right!",
    resource_path("assets/images/botright2close.png"): "Bot right!",
    resource_path("assets/images/topright1close.png"): "Top right!",
    resource_path("assets/images/topright2close.png"): "Top right!"
}

# Detection region: (left, top, width, height)
region = (320, 540, 980, 135)

# Delay before starting
time.sleep(2)
print("Starting detection...")

# Keep track of which images are currently on screen
images_on_screen = set()

while True:
    current_detected = set()

    for image, message in image_messages.items():
        try:
            # Limit search to the specified region
            location = pyautogui.locateOnScreen(image, region=region, confidence=0.6)
            if location:
                current_detected.add(image)

                # Only trigger for new appearances
                if image not in images_on_screen:
                    print(f"Detected {image} at {location}")
                    pyautogui.press('enter')
                    pyautogui.write(message)
                    pyautogui.press('enter')
        except Exception:
            pass

    # Update the images_on_screen set
    images_on_screen = current_detected

    time.sleep(0.1)
