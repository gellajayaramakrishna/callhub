# CallHub — Institutional Phone Directory System

A centralized contact management system built for IIT Gandhinagar to securely store, search, and manage member contact information with role-based access control, SQL indexing optimization, and security audit logging.

## Tech Stack

- **Backend:** Python 3, Flask
- **Database:** MySQL
- **Auth:** JWT (JSON Web Tokens)
- **Frontend:** HTML, CSS, JavaScript

## Project Structure
## Project Structure
```
├── app/
│   ├── app.py              # Main Flask app + page routes
│   ├── auth.py             # JWT login/logout/session
│   ├── rbac.py             # Role-based access decorators
│   ├── db.py               # MySQL connection
│   ├── routes/
│   │   ├── members.py      # Member CRUD APIs
│   │   ├── departments.py  # Department CRUD APIs
│   │   └── analytics.py    # Search, interactions, analytics
│   ├── templates/          # HTML pages
│   └── static/             # CSS + JS
├── sql/
│   ├── schema.sql          # Database schema
│   ├── dump_file.sql       # Full DB dump with sample data
│   └── indexes.sql         # SQL indexes
├── scripts/
│   └── benchmark.py        # Benchmarking script
├── logs/
│   └── audit.log           # Audit log file
├── benchmark_results.txt   # Benchmark output
├── report.ipynb            # Jupyter notebook report
├── requirements.txt
└── README.md
```


## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/gellajayaramakrishna/callhub.git
cd callhub
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up MySQL database
- Open MySQL Workbench
- Run `sql/dump_file.sql` to create the database and load sample data

### 5. Update DB credentials
Edit `app/db.py`:
```python
LOCAL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password_here",
    "database": "CallHub"
}
```

### 6. Run the app
```bash
cd app
python app.py
```
Visit: `http://127.0.0.1:5000`

## Test Login Credentials

| Name | Email | Password | Role |
|------|-------|----------|------|
| Rohit Das | rohit@org.in | 9000000009 | Director (Admin) |
| Pooja Singh | pooja@org.in | 9000000008 | HOD (Admin) |
| Amit Sharma | amit@org.in | 9000000001 | Student (Regular) |

> Password = Primary phone number

## API Endpoints

| Endpoint | Method | Access | Description |
|----------|--------|--------|-------------|
| `/login` | POST | Public | Login and get JWT token |
| `/isAuth` | GET | Public | Verify session token |
| `/logout` | POST | Public | Logout |
| `/members` | GET | Login | Get all members |
| `/members/<id>` | GET | Login | Get single member |
| `/members` | POST | Admin | Add new member |
| `/members/<id>` | PUT | Admin | Update member |
| `/members/<id>` | DELETE | Admin | Soft-delete member |
| `/departments` | GET | Login | Get all departments |
| `/departments` | POST | Admin | Add department |
| `/departments/<id>` | PUT | Admin | Update department |
| `/departments/<id>` | DELETE | Admin | Delete department |
| `/search` | POST | Login | Search directory |
| `/analytics` | GET | Admin | Get analytics |
| `/login-history` | GET | Admin | Get login history |

## RBAC Roles

**Admin roles:** Director, HOD, Dean, Admin Staff, HR Manager
- Full CRUD on members and departments
- View analytics and audit logs

**Regular users:** Student, Professor, etc.
- Read-only access to directory
- Search and view profiles only

## Security

- JWT tokens expire after 2 hours
- All unauthorized access attempts logged to `logs/audit.log`
- Login history tracked with IP address and timestamps
- Input validation on all endpoints
