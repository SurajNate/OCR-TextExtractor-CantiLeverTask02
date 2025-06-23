# 🧠 OCR Flask App (Image & PDF Text Extraction)

This is a simple OCR (Optical Character Recognition) web app built with **Flask** that allows users to upload **images** or **PDF documents**, extract text using **Tesseract OCR**, and display the output on a web page.

---

## 🚀 Features

- ✅ Upload image files (`.png`, `.jpg`, `.jpeg`)
- ✅ Upload PDF files (multi-page supported)
- ✅ Text extracted using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- ✅ Web interface using Flask
- ✅ Cross-platform (Windows/Linux/Mac)

---

## 📥 Install Tesseract OCR
Download installer:
- https://github.com/UB-Mannheim/tesseract/wiki
- Install to: C:\Program Files\Tesseract-OCR
- Add path to system environment variables
- OR set manually in code : pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

## 📥 Install Poppler for PDF Support
Download Poppler:
- https://github.com/oschwartz10612/poppler-windows/releases
- Extract and move it to: C:\poppler
- Use in code: POPPLER_PATH = r'C:\poppler\Library\bin'

![image](https://github.com/user-attachments/assets/db24e597-6262-43ff-ad7c-f87b17cd5a2f)
  
