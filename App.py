import cv2
import pytesseract
#import pandas as pd
import os
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Set Tesseract command path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize panel as None
panel = None


# Function to select an image and perform text recognition
def open_image():
    global img, panel

    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename(title="Select an Image",
                                           filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if len(file_path) > 0:
        # Read the image using OpenCV
        image = cv2.imread(file_path)

        # Convert image to grayscale
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Extract text using Tesseract
        text = pytesseract.image_to_string(gray_img)

        # Draw bounding boxes around the detected text
        boxes = pytesseract.image_to_boxes(gray_img)
        for itm in boxes.splitlines():
            b = itm.split()
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(image, (x, image.shape[0] - y), (w, image.shape[0] - h), (0, 255, 0), 2)
            cv2.putText(image, b[0], (x, image.shape[0] - y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Convert the image to a format Tkinter can display
        img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        img = ImageTk.PhotoImage(img)

        # If there's already an image panel, update it
        if panel is None:
            panel = Label(image=img, bg="white")
            panel.image = img
            panel.pack(side="left", padx=10, pady=10)
        else:
            panel.configure(image=img)
            panel.image = img

        # Update the text output
        text_output.delete(1.0, END)
        text_output.insert(END, text)

"""       # Save the extracted text to an Excel file
        df = pd.DataFrame(text.split(" "))
        df.to_excel('extracted_text.xlsx', index=False)"""


# Function to copy text to clipboard with custom message
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(text_output.get(1.0, END))
    messagebox.showinfo("Copied", "Text copied to clipboard best \n Wishes Eng Ahmed Gwely!")


# Create the main window
root = Tk()
root.title("Text Recognition App")
root.geometry("1000x600")
root.configure(bg="white")  # Set background color to white

# Create a stylish frame for controls
control_frame = Frame(root, bg="white")
control_frame.pack(side="top", fill="x", padx=20, pady=20)

# Create a stylish button to open an image
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6, background="#f0f0f0", foreground="#000000")

btn = ttk.Button(control_frame, text="Open Image", command=open_image, style="TButton")
btn.pack(side="left", padx=10, pady=10)

# Create a button to copy the text
copy_btn = ttk.Button(control_frame, text="Copy Text", command=copy_text, style="TButton")
copy_btn.pack(side="left", padx=10, pady=10)

# Create a text box to display the extracted text
text_frame = Frame(root, bg="white")
text_frame.pack(side="right", fill="y", padx=20, pady=20)

text_output = Text(text_frame, wrap="word", width=40, height=25, font=("Helvetica", 14), bg="#f0f0f0", fg="#000000",
                   insertbackground="black")
text_output.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Add a scroll bar to the text box
scrollbar = Scrollbar(text_frame, command=text_output.yview, bg="white")
text_output.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

copyright_label = Label(root, text="© 2024 Ahmed Fathy Gwely. All rights reserved.", bg="white", fg="gray", font=("Arial", 10))
copyright_label.pack(side="bottom", pady=10, anchor="center")

# Start the GUI event loop
root.mainloop()
