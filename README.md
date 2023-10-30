## screen_pyspy

### Overview

screen_pyspy is a Python script that captures screenshots when a certain noise level is detected, and it also plays a sound as a notification. This can be useful for various purposes, such as monitoring your workspace.

### Requirements

To use screen_pyspy, you will need the following:

- Python
- sounddevice library (`pip install sounddevice`)
- pyautogui library (`pip install pyautogui`)
- pygame library (`pip install pygame`)
- A virtual audio cable (e.g., VB-Audio Virtual Cable) for correct audio routing.

### Usage

1. Make sure you have installed the required Python libraries.
2. Install a virtual audio cable (e.g., VB-Audio Virtual Cable) on your system.
3. Place the `screen_pyspy.py` script in your desired directory.
4. Run the script with Python by executing `python screen_pyspy.py`.
5. The script will ask you to select an audio device for playback. Choose the appropriate device number and press Enter.
6. The script will start monitoring the audio input.
7. When the audio input surpasses a certain noise threshold (specified in the script), it will capture a screenshot of your desktop and play a notification sound.

### Customization

You can customize the following parameters in the `screen_pyspy.py` script:

- The folder where screenshots are saved.
- The noise threshold level for capturing screenshots.
- The sound to be played when a screenshot is captured.

### Notes

- Make sure to install the required libraries and a virtual audio cable for correct functionality.
- The script continuously runs and captures screenshots whenever the noise threshold is exceeded.

### License

This project is licensed under the MIT License. You can find the license details in the `LICENSE` file.

### Author

Mistkeithy

### Contributing

If you'd like to contribute to this project, please follow the guidelines in the [CONTRIBUTING](CONTRIBUTING.md) file.