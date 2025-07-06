import cv2
import pytesseract
import re
import pandas as pd
import os
import serial

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Excel setup
excel_file = "numbers.xlsx"
if not os.path.exists(excel_file):
    pd.DataFrame(columns=["Detected Numbers"]).to_excel(excel_file, index=False)

# Serial setup
ser = serial.Serial('COM3', 9600)  # Use your correct COM port

def capture_and_extract_numbers():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
        text = pytesseract.image_to_string(gray, config=config)
        numbers_only = re.findall(r'\d+', text)
        print("Extracted Numbers:", numbers_only)

        # Save to Excel
        if numbers_only:
            df_existing = pd.read_excel(excel_file)
            for num in numbers_only:
                df_existing = pd.concat([df_existing, pd.DataFrame([[num]], columns=["Detected Numbers"])], ignore_index=True)
            df_existing.to_excel(excel_file, index=False)
            print("Numbers saved to Excel.")

        cv2.imshow("Captured Frame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to capture image.")
    cap.release()

# Main loop – WAIT for signal
print("Waiting for ESP8266 signal (send 'start')...")
while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        print("Received from ESP:", line)
        if line.lower() == 'start':
            capture_and_extract_numbers()
