import os
import pyautogui
import sounddevice as sd
import numpy as np
import pygame
import datetime

current_dir = os.path.dirname(os.path.realpath(__file__))
screenshot_folder = os.path.join(current_dir, 'screenshots')
os.makedirs(screenshot_folder, exist_ok=True)

def select_audio_device():
    devices = sd.query_devices()
    print("Audio devices:")
    for idx, device in enumerate(devices):
        print(f"{idx}: {device['name']}")
    selected_device = int(input("Select audio device number: "))
    return devices[selected_device]['name']

audio_device = select_audio_device()

def take_screenshot():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(screenshot_folder, f'screenshot_{timestamp}.png')
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    
    pygame.mixer.init(devicename=audio_device)
    pygame.mixer.music.load(os.path.join(current_dir, 'camera_click.mp3'))
    pygame.mixer.music.play()

def audio_callback(indata, frames, time, status):
    avg_volume = np.mean(np.abs(indata)) * 100 
    if avg_volume > 0.7:
        take_screenshot()


with sd.InputStream(callback=audio_callback):
    while True:
        pass