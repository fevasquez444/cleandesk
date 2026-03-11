# CleanDesk - Cleaning Company Management System

A CRM built with Flask for cleaning companies. Manage your clients efficiently with a clean and simple interface.

## Features

- ✅ **Client Registration** - Add new clients with name, email, phone, and address
- ✅ **Client Listing** - View all clients in a organized table
- ✅ **Edit Clients** - Update client information
- ✅ **Delete Clients** - Remove clients with confirmation
- ✅ **Database Storage** - SQLite database for data persistence
- ✅ **Form Validation** - Email format validation and required fields

## Tech Stack

- **Backend:** Python 3.12, Flask 3.1
- **Database:** SQLite, SQLAlchemy ORM, Flask-Migrate
- **Forms:** Flask-WTF, WTForms
- **Frontend:** HTML5, Jinja2 templating
- **Version Control:** Git, GitHub

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/fevasquez444/cleandesk.git
   cd cleandesk

2. **Create and activate virtual environment**
 
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# or venv\Scripts\activate  # On Windows

3. **Install dependencies**

pip install flask flask-sqlalchemy flask-migrate flask-wtf email-validator

4. **Set up the database**

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. Run the application

python app.py

6. **Usage**   

 Open your browser and go to http://127.0.0.1:5000



    Home page - Start from the welcome screen

    Register a client - Click "Registrar nuevo cliente" and fill the form

    View all clients - Click "Ver lista de clientes" to see the table

    Edit a client - Click the ✏️ Edit button next to any client

    Delete a client - Click the 🗑️ Delete button (confirmation required)


7 **Project Structure**

cleandesk/
├── app.py              # Main application file
├── forms.py            # WTForms definitions
├── models.py           # Database models
├── requirements.txt    # Dependencies
├── static/             # CSS, images, etc.
├── templates/          # HTML templates
│   ├── index.html
│   ├── cliente_form.html
│   └── clientes_lista.html
├── migrations/         # Database migrations
└── instance/           # SQLite database file

8 **Future Improvements**

    Add authentication system (login/logout)

    Implement services catalog

    Add search and filter functionality

    Improve UI with Bootstrap

    Deploy to production

Author

Fernando Vasquez
GitHub: @fevasquez444
License
This project is for educational purposes as part of my Full Stack Web Development learning journey.


Early stage of developement Snapshots

<img width="1862" height="1122" alt="Screenshot from 2026-03-11 15-50-27" src="https://github.com/user-attachments/assets/3d49da2a-98b4-4e60-b35d-a7d5171b1571" />
<img width="1862" height="1122" alt="Screenshot from 2026-03-11 15-50-22" src="https://github.com/user-attachments/assets/761566cb-1e94-4aa1-98da-cc73865d0f52" />
<img width="1862" height="1122" alt="Screenshot from 2026-03-11 15-50-15" src="https://github.com/user-attachments/assets/c1543b1f-8b1b-4283-aaad-0df9cc34a09e" />

Second stage of developement Snapshots


<img width="1862" height="1122" alt="Screenshot from 2026-03-11 17-11-44" src="https://github.com/user-attachments/assets/f0b8b85a-9ec4-4c7d-a968-7708fe24a7d5" />
<img width="1862" height="1122" alt="Screenshot from 2026-03-11 17-11-39" src="https://github.com/user-attachments/assets/5a4bd754-958c-4ed4-9970-0ceec3c52a8e" />
<img width="1862" height="1122" alt="Screenshot from 2026-03-11 17-11-31" src="https://github.com/user-attachments/assets/010f3606-8c4f-4416-a415-68679430972a" />


