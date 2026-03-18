# CleanDesk - CRM for Cleaning Services

CleanDesk is a web-based CRM (Customer Relationship Management) system built with Flask, designed to manage clients, services, and internal users for a cleaning business.

This project is part of my journey learning full-stack development. I built it to practice backend development, CRUD operations, authentication, database management, and real-world application structure using Flask.

---

## 📌 Project Status

This is an educational project in active development.

I am continuously improving it while learning backend and full-stack concepts, focusing on building real and functional systems rather than just tutorials.

---

## 🚀 Features

### 🔐 Authentication & User Management
- User registration and login system
- Password hashing with Bcrypt
- Role-based access control (Admin / Employee)
- Protected routes using Flask-Login

### 👥 Client Management
- Create, edit, and delete clients
- Store contact information (email, phone, address)
- Track client registration dates

### 🧰 Service Management
- Create and manage cleaning services
- Define price and duration
- Maintain service catalog

### 🔗 Client-Service Assignment
- Assign multiple services to clients
- Many-to-many relationship implementation
- Prevent duplicate service assignments
- Remove services dynamically

### 📊 Dashboard
- Display total clients, services, and users
- Show recent client activity
- Basic reports and statistics section

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-Bcrypt
- Flask-WTF / WTForms
- SQLite
- HTML / Jinja2
- Git & GitHub

---

## 📚 Dependencies

This project uses the following main dependencies:

- `Flask`
- `Flask-SQLAlchemy`
- `Flask-Migrate`
- `Flask-Login`
- `Flask-Bcrypt`
- `Flask-WTF`
- `WTForms`
- `SQLAlchemy`
- `Jinja2`

All dependencies are listed in:

```text
requirements.txt
```

---

## 🧠 What I Practiced in This Project

This project helped me practice:

- Building routes and views with Flask
- Designing database models
- Creating and validating forms
- Implementing authentication and session handling
- Using role-based permissions
- Organizing a growing project structure
- Working with Git and GitHub while learning development workflows

---

## 🖼️ Screenshots

_Add screenshots here showing:_
- Dashboard
- Client list
- Services list
- Login screen
- Reports page

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/fevasquez444/cleandesk.git
cd cleandesk
```

### 2. Create virtual environment

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variable

#### Linux / Mac

```bash
export SECRET_KEY="your-secret-key"
```

#### Windows PowerShell

```powershell
$env:SECRET_KEY="your-secret-key"
```

### 5. Run migrations

```bash
flask db upgrade
```

### 6. Run the app

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## 🧪 Usage

- Access the application in the browser
- Register a new user
- Login with your account
- Create clients
- Create services
- Assign services to clients
- Manage users if logged in as admin
- Review dashboard and reports

---

## 📁 Project Structure

```text
cleandesk/
├── app.py
├── forms.py
├── services_forms.py
├── requirements.txt
├── templates/
├── migrations/
├── instance/
└── README.md
```

---

## 🔮 Future Improvements

- Search and filters
- Better dashboard metrics
- Improved UI styling
- Form error feedback improvements
- Deployment
- Better project modularization (Blueprints / separate models)

---

## 👨‍💻 Author

Fernando Vasquez

- GitHub: [@fevasquez444](https://github.com/fevasquez444)

---

## 📌 Note

This repository is part of my learning process as a future full-stack developer.

I focus on building real practice projects while improving my programming fundamentals.