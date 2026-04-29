# CallHub — Institutional Phone Directory System

A centralized contact management system built for institutions to securely store, search, and manage member contact information with role-based access control.

## Features

- JWT-based authentication with login/logout session tracking
- Role-Based Access Control (RBAC) — admin vs regular user permissions
- Add, edit, delete, and search member contacts
- Department and category classification
- Horizontal database sharding across 3 MySQL instances
- Audit logging for unauthorized access attempts
- IP address and timestamp tracking for all login sessions

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL (with horizontal sharding)
- **Auth:** JWT (JSON Web Tokens)
- **Frontend:** HTML, CSS, JavaScript

## Project Structure
app/
├── app.py          # Main Flask app, route registration
├── auth.py         # JWT auth, login/logout endpoints
├── db.py           # Database connections and sharding logic
├── rbac.py         # Role-based access control decorators
└── routes/
├── members.py      # Member CRUD operations
├── departments.py  # Department management
├── analytics.py    # Analytics endpoints
└── requests.py     # Request handling
## Database Sharding

Members are distributed across 3 MySQL shards using:

shard_id = member_id % 3

Each shard runs on a separate port (3307, 3308, 3309). Fan-out queries search all 3 shards and merge results.

## Setup

1. Clone the repo
```bash
git clone https://github.com/gellajayaramakrishna/callhub.git
cd callhub
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure your database credentials in `app/db.py`

4. Run the app
```bash
python app/app.py
```

## API Endpoints

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| POST | `/login` | Login and get JWT token | Public |
| GET | `/isAuth` | Verify token validity | Public |
| POST | `/logout` | Logout and record session end | Auth |
| GET | `/members` | List all members | Auth |
| POST | `/members` | Add new member | Admin |
| PUT | `/members/<id>` | Update member | Admin |
| DELETE | `/members/<id>` | Delete member | Admin |
| GET | `/departments` | List departments | Auth |

## Security

- Passwords are not stored in plaintext
- All admin-only route violations are logged to `logs/audit.log`
- JWT tokens expire after 2 hours
- Input validation on all endpoints
