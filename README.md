# 🍬 Sweet Shop Management System

A full-stack inventory management system for a sweet shop, built with Django (backend), React (frontend), SQLite3 (database), and JWT authentication. Includes TDD with Python for reliability.

---

## 🚀 Features

- ✅ User registration and login (JWT)
- 🧁 Add, update, delete sweets (admin only)
- 🛒 Purchase sweets (user)
- 📦 Restock sweets (admin)
- 🔍 Search sweets by name or category
- 🧪 Unit tests with Django's test framework

---

## 🛠️ Tech Stack

| Layer       | Technology               |
|------------|--------------------------|
| Backend     | Django, Django REST Framework |
| Frontend    | React, Axios             |
| Database    | SQLite3                  |
| Auth        | JWT (SimpleJWT)          |
| Testing     | Django TestCase          |

---

## 📦 Installation

### 🔙 Backend Setup

```bash
git clone https://github.com/qureshisohel/Sweet-Shop-Management.git
cd sweetshop/backend
pip install -r requirements.txt
pip install djangorestframework
pip install djangorestframework-jwt
python manage.py migrate
python manage.py runserver

