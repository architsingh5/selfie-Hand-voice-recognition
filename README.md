# Selfie with Hand Recognition

Python script to add functionality to cameras to recognize open palm/detect specific voice command for capturing photos after 3 seconds.

## Project Description

By this users can click their photos without actually touching the capture button and they have to only show their palms to click pics. They also can give voice command like "take photo", "photo", "picture", "smile" to capture photograph. This helps users when they are taking selfies and are holding the mobile in such a way that their fingers are not able to touch the capture button. This feature is already integrated with the cameras of the latest devices.
 
The project is dependent on the pre-made Cascade for Palm Detection. The Recognition for open palm is not exactly accurate but it serves the purpose.

The captured images are stored in the images folder as img1.png, img2.png. The countdown on the camera tells the user to be ready in 3 seconds to take the pic. At the time of capturing the photo, the camera-shutter sound creates the effect of capturing pic for User. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules.

```bash
pip install opencv-python playsound SpeechRecognition
```

## Usage
Run the given command in your terminal to run the program
```bash
python handvoice.py
python handonly.py
```
## Contributors

Archit Singh and Abhishek Jajoo