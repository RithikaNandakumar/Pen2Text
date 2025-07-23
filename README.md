# Pen2Text
AI-based handwritten notes digitization web app using TrOCR 
# ✍️ Pen2Text - Handwritten Notes to Digital Text

Pen2Text is a smart web application that helps you **convert handwritten notes into editable digital text** using AI. Whether it's lecture notes, rough ideas, or to-do lists, just upload an image and let Pen2Text do the magic!

---

## 💡 What It Does

- 📸 Upload a handwritten note as an image
- 🤖 Uses Microsoft's **TrOCR** model to recognize the text
- 🔍 Cleans up the image with preprocessing (grayscale, noise removal, thresholding)
- ✅ Autocorrects mistakes like "7waSoxpt" to "JavaScript"
- 📄 Lets you download the extracted text as a file
- 🎨 Clean, modern dark-themed interface (HTML, CSS, JS)

---

## 🛠️ Tech Stack

| Area          | Tools Used                                      |
|---------------|-------------------------------------------------|
| Backend       | Python, Flask                                   |
| AI/OCR Model  | TrOCR (`microsoft/trocr-base-handwritten`)      |
| Preprocessing | OpenCV                                          |
| Autocorrect   | Python’s `difflib`                              |
| Frontend      | HTML, CSS, JavaScript (Neon-themed UI)          |

---

## 📁 Project Structure

Pen2Text/
├── app.py # Flask backend
├── templates/ # HTML files
│ └── index.html
├── static/ # CSS, JS, images
│ ├── style.css
│ └── script.js
├── model/ (if any) # Optional - for custom models
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

#Set Up the Environment
 Create and activate a virtual environment (optional but recommended):
 python -m venv venv
 source venv/bin/activate       # On Linux/macOS
 venv\Scripts\activate          # On Windows
 
📦 Install dependencies:

   pip install -r requirements.txt

▶️ Run the Flask app:

   python app.py
   
🌐 Open your browser and go to:

   http://127.0.0.1:5000/
   
📸 Screenshots

<img width="1311" height="590" alt="image" src="https://github.com/user-attachments/assets/0a180338-1864-42bd-9705-9956cbbf5cdf" />
<img width="709" height="531" alt="image" src="https://github.com/user-attachments/assets/c680e03b-0940-49f3-89bd-428921f797d9" />
<img width="1052" height="475" alt="image" src="https://github.com/user-attachments/assets/07e3cfb1-63e2-4c8f-94c5-0617d1d43264" />
<img width="1144" height="622" alt="image" src="https://github.com/user-attachments/assets/08f766e7-b6c9-4b86-a128-44f5a05896c9" />

✨ Features at a Glance
#Supports long sentences and paragraphs

#Works on various handwriting styles

#Instant download of extracted text

#Animated “Processing...” indicator

#Mobile-responsive, futuristic UI

🙋‍♀️ About Me
I'm Rithika, a final-year B.Tech IT student passionate about AI and web development.
This project was built as a part of my academic and personal learning journey.
Feel free to fork it, use it, or suggest improvements!

🙏 Acknowledgements

Microsoft TrOCR Model
Hugging Face Transformers
Flask Framework
OpenCV, Python, and the open-source community 💛






