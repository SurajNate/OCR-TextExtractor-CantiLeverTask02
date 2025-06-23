import os
from flask import Flask, render_template, request
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Change path below if needed:
POPPLER_PATH = r'C:\poppler\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None

    if request.method == 'POST':
        if 'document' not in request.files:
            return render_template('index.html', extracted_text="No file uploaded.")

        file = request.files['document']

        if file.filename == '':
            return render_template('index.html', extracted_text="No selected file.")
        
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            try:
                if file.filename.lower().endswith('.pdf'):
                    images = convert_from_path(filepath, poppler_path=POPPLER_PATH)
                    extracted_text = ""
                    for i, img in enumerate(images):
                        extracted_text += f"\n--- Page {i+1} ---\n"
                        extracted_text += pytesseract.image_to_string(img)
                else:
                    image = Image.open(filepath)
                    extracted_text = pytesseract.image_to_string(image)
            except Exception as e:
                extracted_text = f"Error: {e}"
        else:
            extracted_text = "Invalid file type."

    return render_template('index.html', extracted_text=extracted_text)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
