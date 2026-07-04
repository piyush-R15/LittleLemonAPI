# 🍋 Little Lemon API

A RESTful web application developed using **Django** and **Django REST Framework** for the Little Lemon restaurant. This project was created as part of the **Meta Back-End Developer Capstone** on Coursera.

## 📌 Project Overview

The Little Lemon API allows users to manage restaurant menu items and table bookings through RESTful endpoints. It demonstrates the use of Django models, serializers, views, URL routing, CRUD operations, static HTML rendering, and unit testing.

---

## 🚀 Features

- REST API using Django REST Framework
- Menu Management API
- Booking Management API
- CRUD Operations (Create, Read, Update, Delete)
- Django Admin Panel
- Static HTML Home Page
- SQLite Database
- Unit Testing
- Git Version Control
- GitHub Repository

---

## 🛠️ Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite
- Git
- GitHub
- VS Code
- Insomnia (API Testing)

---

## 📂 Project Structure

```
LittleLemonAPI/
│
├── littlelemon/
├── restaurant/
├── templates/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/piyush-R15/LittleLemonAPI.git
```

### Navigate into the project

```bash
cd LittleLemonAPI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run database migrations

```bash
python manage.py migrate
```

### Start the development server

```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

### Home Page

```
GET /
```

### Menu API

```
GET /menu/
POST /menu/
GET /menu/<id>/
PUT /menu/<id>/
DELETE /menu/<id>/
```

### Booking API

```
GET /booking/
POST /booking/
GET /booking/<id>/
PUT /booking/<id>/
DELETE /booking/<id>/
```

---

## 🧪 Running Tests

Run the following command:

```bash
python manage.py test
```

---

## 📸 API Testing

The APIs were tested using **Insomnia**.

---

## 👨‍💻 Author

**Piyush Rajora**

GitHub: https://github.com/piyush-R15

---

## 📜 License

This project was developed for educational purposes as part of the **Meta Back-End Developer Capstone** on Coursera.