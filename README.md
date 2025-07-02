# 🧠 Knowledge Base Platform

This is a full-stack Knowledge Base Platform built as part of the Frigga Cloud Labs Software Development Assignment.

## 🌐 Overview

This platform allows users to:
- Register and login with secure authentication (JWT).
- Access protected routes.
- Create and store knowledge base documents using a rich text editor (Quill).
- Store user and document data in MySQL.

## 🏗️ Tech Stack

- **Frontend**: React, React Router, Quill.js
- **Backend**: Flask, Flask-CORS, Flask-MySQLdb
- **Database**: MySQL
- **Authentication**: JWT (JSON Web Tokens)

---

## 🚀 How to Run the Project

### 📁 1. Clone the Repository

bash
git clone https://github.com/your-username/knowledge-base-platform.git
cd knowledge-base-platform

🔧 2. Backend Setup (/backend)
bash
Copy
Edit
cd backend
python -m venv venv
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

⚙️ Configuration
Create a file called config.py inside backend/ with the following content:

python
Copy
Edit
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "your_mysql_user",
    "password": "your_mysql_password",
    "database": "knowledge_base"
}

JWT_SECRET = "your_secret_key"
▶️ Run the Flask Server
bash
Copy
Edit
python app.py
Server will start on http://127.0.0.1:5050

💻 3. Frontend Setup (/frontend)
bash
Copy
Edit
cd ../frontend
npm install
npm start
React app will run on http://localhost:3000

🧱 Project Structure
mathematica
Copy
Edit
knowledge-base-platform/
├── backend/
│   ├── app.py
│   ├── config.py
│   └── routes/
│       └── auth_routes.py
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── Login.js
│   │   ├── Register.js
│   │   ├── Protected.js
│   │   └── CreateDocument.js
├── README.md

👤 Demo Credentials

Email: demo@example.com
Password: demo123

🧪 Features
✅ JWT-based login & protected routes

✅ Quill.js WYSIWYG editor for document creation

✅ Token saved in localStorage

✅ Flask–MySQL database operations for user and document management

📩 Submission Info
Name: Mohamed Rafik A
Email: mohameedrafik.a@gmail.com
Phone: 9790629375
Role: Associate Software Engineer (Internship)
