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
