# 🍽️ Recipe App
This repo is the version for local testing, so it uses SQLite instead of MySQL or PostgreSQL.

## 📌 Introduction
The **Recipe App** is a web-based platform built using **Django**, designed to help users create, manage, and search for recipes. The app allows users to add ingredients, specify cooking times, and automatically calculates the difficulty level based on predefined logic.

This project follows best practices in **web development with Django**, including **database management**, **user authentication**, and **data processing**. The platform enables users to contribute and explore recipes while ensuring a smooth and interactive experience.

🔗 **Live Demo:** [Recipe App](https://andersontsaitw.pythonanywhere.com/)

---

## 🚀 Features

### ✅ Core Functionalities
- **User Authentication**: Register, log in, and manage personal recipes.
- **Recipe Management**: Users can create, edit, and delete recipes.
- **Ingredient-Based Search**: Find recipes by searching for ingredients.
- **Automatic Difficulty Rating**: The app automatically determines the difficulty level based on cooking time and ingredient count.
- **Django Admin Panel**: Manage recipes, ingredients, and users via an admin dashboard.

### 🎨 UI & UX Features
- **Responsive Design**: Optimized for desktop and mobile devices.
- **Image Uploads**: Add images for recipes and ingredients.
- **User-Friendly Forms**: Simplified recipe entry with ingredient selection.

---

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS (Bootstrap)
- **Backend**: Django (Python)
- **Database**: MySQL (Hosted on PythonAnywhere)
- **Authentication**: Django’s built-in authentication system
- **Hosting**: PythonAnywhere

---

## 🏗️ Project Structure
recipeapp/
│── recipe_project/          # Main Django project settings
│   ├── settings.py          # Configuration settings
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI for deployment
│
├── recipes/                 # Recipe management app
│   ├── models.py            # Recipe models
│   ├── views.py             # Recipe logic
│   ├── urls.py              # Recipe routes
│   ├── templates/           # HTML templates
│
├── ingredients/             # Ingredient management app
│   ├── models.py            # Ingredient models
│   ├── views.py             # Ingredient logic
│   ├── urls.py              # Ingredient routes
│
├── static/                  # Static files (CSS, JS, images)
├── media/                   # Uploaded images
└── manage.py                # Django management script

### 🔧 Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **Django 4+**
- **MySQL** (or an alternative database)
- **A virtual environment** (recommended)

### 📥 Clone the Repository

```bash
git clone https://github.com/yourusername/recipe-app.git
cd recipe-app
```

## 🚀 Create & Activate Virtual Environment

```bash
python -m venv myvenv
source myvenv/bin/activate  # MacOS/Linux
myvenv\Scripts\activate     # Windows
```


## 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

## 🏃 Run It
```bash
python manage.py migrate  # Apply database migrations
python manage.py runserver  # Start the Django development server
```
PS. The second time, you need to run venv first
```bash
source myvenv/bin/activate  # MacOS/Linux
myvenv\Scripts\activate     # Windows
```

# 📌 Environment Variables (`SECRET_KEY`) will be generate automatically
