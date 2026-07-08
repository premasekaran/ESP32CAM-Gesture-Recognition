 ESP32-CAM Gesture Recognition
 
 OVERVIEW
 --------
This project implements a real-time hand gesture recognition system using an ESP32-CAM, Python, and OpenCV.

The ESP32-CAM streams live video over Wi-Fi to a Python application running on a computer. The application detects hand gestures and sends the recognized gesture wirelessly to an ESP32, which displays the result on an I2C LCD.

---

> FEATURES
----------

- Real-time camera streaming
- Gesture recognition using OpenCV
- Wireless communication
- LCD output
- Modular architecture

Recognized Gestures
---

The system currently supports:

1. Fist → "FIST"
2. Finger → "ONE"
3. Fingers → "TWO"
4. Fingers → "THREE"
5. Fingers → "FOUR"
6. Fingers → "FIVE"

> HARDWARE
------------

1. ESP32-CAM (AI Thinker)
2. ESP32 DevKit
3. 16x2 I2C LCD Display
4. Wi-Fi Router
5. Jumper wires and power supply

> SOFTWARE
-----------

1. Python
2. OpenCV
3. cvzone
4. Arduino IDE


---
> SYSTEM ARCHITECTURE

![Architecture](images/architecture.png)


---
> WORKFLOW
-----------

1. ESP32-CAM initializes camera and starts streaming.
2. Python script connects to the stream URL.
3. Hand detection is performed frame-by-frame.
4. Gesture label is generated in real time.
5. Label is transmitted to ESP32.
6. LCD updates with the detected gesture.

---
> FOLDER STRUCTURE

```text
project/
│── esp32cam/ # Code for ESP32-CAM streaming
│── python/ # Python gesture detection scripts
│── esp32/ # ESP32 LCD display + communication code
│── images/ # Sample outputs or documentation images
```
---
RUN LOCALLY
---
1. Setup ESP32-CAM
Open Arduino IDE
Select board: AI Thinker ESP32-CAM
Upload the camera streaming code
Connect to Wi-Fi and note the stream URL (e.g., http://192.168.x.x)
2. Setup Python Environment

Install required libraries:

pip install opencv-python cvzone numpy requests
3. Run Gesture Detection
Update the stream URL in your Python script:
url = "http://192.168.x.x"
Run the script:
python main.py
4. Setup ESP32 with LCD
Connect I2C LCD to ESP32
Upload the display + receiver code
Ensure ESP32 is connected to the same Wi-Fi network
5. Test the System
Show hand gestures in front of ESP32-CAM
Check detected gesture in Python window
Verify output on LCD display

----
> FUTURE IMPROVEMENTS
----------------------

- Support more gestures
- Train a custom deep learning model
- Add speech output
- Control home automation devices



## Author
Prema
