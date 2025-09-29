# **Hand Gesture Volume Control with Python** ✋🔊

This project uses **OpenCV**, **Mediapipe (HandTrackingModule)**, and **PyCaw** to control the system volume with simple **hand gestures**. By detecting the distance between your thumb and index finger, you can increase or decrease the volume in real time.

---

## **✨ Features**

* 🎥 Real-time **hand tracking** using a webcam.
* ✋ Detects hand landmarks with a custom `HandTrackingModule`.
* 🔊 Adjusts **system volume** using **PyCaw** library.
* 🟢 Green indicator when the volume is being set.
* 📊 On-screen volume bar and percentage display.
* ⚡ Smooth gesture recognition with FPS counter.

---

## **📂 Project Structure**

```
HandGestureVolumeControl/
│── HandTrackingModule.py  
│── hand_volume_control.py  
│── README.md  
```

---

## **⚙️ Requirements**

Install the dependencies with:

```bash
pip install opencv-python
pip install numpy
pip install comtypes
pip install pycaw
```

You’ll also need the **HandTrackingModule**, which is usually built with **Mediapipe**. If you don’t have it yet, install:

```bash
pip install mediapipe
```

---

## **🚀 How to Run**

1. Connect a webcam to your system.

2. Run the script:

   ```bash
   python hand_volume_control.py
   ```

3. Show your hand to the camera:

   * Move your **thumb and index finger apart** → Increase volume.
   * Move them **closer** → Decrease volume.
   * Keep the **pinky finger down** to activate volume changes.

4. Press **Q** to quit the program.

---

## **📝 Notes**

* Works on **Windows** with PyCaw (system audio control).
* `HandTrackingModule.py` must be present in the project (based on Mediapipe hand tracking).
* The system volume bar will be displayed on screen in real time.

---
