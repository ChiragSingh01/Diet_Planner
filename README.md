# 🥗✨ AI Diet Plan Generator

Welcome to **AI Diet Plan Generator** — your personal AI-powered nutrition assistant!  
Built with **Python Flask**, **Together AI / Hugging Face**, and **Bootstrap 5**, this web app generates custom meal plans and a weekly diet planner with **PDF export** — all in one sleek package.

---

## 🚀 Features

✅ **AI-Powered Meal Plans**  
Generate personalized 1-day or weekly meal plans using powerful open-source AI models via Together AI or Hugging Face.

✅ **Beautiful Responsive UI**  
Clean, modern Bootstrap styling with your own branding — mobile-friendly and fast.

✅ **PDF Export & Print**  
Export your generated plan as a PDF or print it directly from your browser.

✅ **Weekly Planner**  
Create and manage your own weekly diet checklist and export that too.

✅ **Secure**  
Secrets and API keys are managed using `.env` — never push secrets to your repository!

---

## 📸 Preview

![Preview](static/preview/p1 (1).png)

## 🛠️ Tech Stack

- **Python 3**
- **Flask** — web framework
- **Together AI / Hugging Face** — text generation
- **Bootstrap 5** — front-end styling
- **wkhtmltopdf** — server-side PDF export

---

## ⚙️ Getting Started

### 1️⃣ Clone this repository

```bash
git clone https://github.com/ChiragSingh01/Diet_Planner
cd ai-diet-generator

2️⃣ Create a virtual environment & install dependencies
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### 3️⃣ Add your secrets
- Create a .env file in the project root with your API key:

- env
- Copy
- Edit
- TOGETHER_API_KEY=YOUR_TOGETHER_AI_API_KEY

### 4️⃣ Install wkhtmltopdf
For PDF export, you’ll need wkhtmltopdf:

Download it from wkhtmltopdf.org

Install it and add its bin folder to your system PATH

Or configure it in app.py like this:
```
py
Copy
Edit
PDFKIT_CONFIG = pdfkit.configuration(
    wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
)
```

### 5️⃣ Run the Flask server
```bash
  # On your terminal:
    flask run
```

### 📄 How it Works
1. The user fills out age, gender, dietary preference, and goal.
2. Flask calls the AI model using Together AI or Hugging Face Inference API.
3. The AI generates a natural language meal plan.
4. The plan is parsed and displayed as a neat checklist.
5. Users can check items, print, export as PDF, or plan a whole week.

### 🙏 Credits
Made with ❤️ by Chirag.
Powered by Together AI / Hugging Face.
Styled with Bootstrap.

### 📬 License
MIT — free to use, share, and modify.
Please do not publish your .env or secret keys!

### ⭐️ Show Your Support
If you like this project, star it 🌟, fork it, and share your feedback.
Let’s build more awesome AI tools together! 🚀✨
