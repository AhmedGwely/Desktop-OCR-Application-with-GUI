# Desktop OCR Application with GUI

A desktop application that extracts text from images using **EasyOCR** and **OpenCV**, featuring a **user-friendly GUI** developed with **Tkinter**.

---

## 🚀 Features

- Extracts text from images of various formats (JPG, PNG, AVIF, etc.).
- Supports **live OCR** from webcam input.
- Highlights detected text regions using **bounding boxes**.
- Saves extracted text to **Excel** or **text files**.
- Simple and intuitive **Tkinter GUI** for ease of use.

---

## 🖥️ Screenshots

![App Screenshot](IvV2y.png)  
![OCR Result](cod1.png)  

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Desktop-OCR-Application-with-GUI.git
cd Desktop-OCR-Application-with-GUI
```

## Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

## Install the required packages:

```bash
pip install -r requirements.txt

```
or 

```bash
pip install opencv-python easyocr tkinter pandas pillow

```


# 📁 Example Files

- License_plate_Egypt_private.jpg – Example image for testing license plate OCR.

- captured_image.jpg, x.jpg, x2.jpg – Sample images for OCR testing.

- extracted_text.xlsx – Sample output of recognized text.

- bounding_boxes.xlsx – Contains coordinates of detected text regions.

---
# ⚙️ Project Structure

Desktop-OCR-Application-with-GUI/

 - ├─ App.py                 # Main GUI application
 - ├─ ocr.py                 # OCR logic with EasyOCR
 - ├─ live ocr.py            # Live webcam OCR functionality
 - ├─ main.py                # Helper functions / scripts
 - ├─ test.py / test.ipynb   # Testing scripts
 - ├─ captured_image.jpg     # Sample image
 - ├─ extracted_text.xlsx    # Sample output
 - └─ requirements.txt       # Required Python packages

## 💻 Technology Stack

- Python 3.8+

- EasyOCR – Optical Character Recognition

- OpenCV – Image processing

- Tkinter – Desktop GUI

- Pandas – Excel/text file output

- Pillow (PIL) – Image handling

---


# 👨‍💻 Author

- **Ahmed Gwely**  
- Passionate about Computer Vision, Embedded Systems, and AI-driven IoT.  
- 🌐 [LinkedIn Profile](https://www.linkedin.com/in/ahmed-gwely-2589611b0/)  


