# CleanDesk - CRM for Cleaning Services

CleanDesk is a web-based CRM (Customer Relationship Management) system built with Flask, designed to manage clients, services, and internal users for a cleaning company.

This project demonstrates backend architecture, authentication systems, role-based access control, and relational database design.

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
- Remove services from clients dynamically

### 📊 Dashboard
- Display total clients, services, and users
- Show recent client activity

---

## 🛠 Tech Stack

- Backend: Python 3.12, Flask
- Database: SQLite, SQLAlchemy ORM
- Migrations: Flask-Migrate (Alembic)
- Authentication: Flask-Login, Bcrypt
- Forms: Flask-WTF, WTForms
- Frontend: HTML5, Jinja2
- Version Control: Git & GitHub

---

## 📦 Installation

1. Clone repository

git clone https://github.com/fevasquez444/cleandesk.git  
cd cleandesk  

2. Create virtual environment

python3 -m venv venv  
source venv/bin/activate  

3. Install dependencies

pip install -r requirements.txt  

4. Setup database

flask db upgrade  

5. Run application

python app.py  

---

## 🧪 Usage

- Access: http://127.0.0.1:5000
- Register a new user
- Login as admin
- Create clients and services
- Assign services to clients
- Manage users (admin only)

---

## 📁 Project Structure (Current)

cleandesk/
├── app.py
├── forms.py
├── services_forms.py
├── templates/
├── migrations/
├── instance/
├── requirements.txt

---

## 🔮 Future Improvements

- Modular architecture (Blueprints)
- API version (REST)
- Search & filtering
- Pagination
- UI improvements (Bootstrap / Tailwind)
- Deployment (Docker + Cloud)

---

## 👨‍💻 Author

Fernando Vasquez  
GitHub: https://github.com/fevasquez444

---

## 📌 Notes

This project is part of my journey to become a full stack developer, focusing on building real-world backend systems with scalable architecture.
