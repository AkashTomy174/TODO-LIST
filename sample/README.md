# Django Sample Project: Contact Message App

## Overview
This is a beginner-friendly Django project demonstrating a simple web application for managing contact messages. It includes features like submitting messages with optional image uploads, viewing all messages in a table, editing, and deleting messages. This project is perfect for students learning Django, as it covers core concepts like models, views, forms, templates, URLs, and database migrations.

The app is named `akash` and is part of the `sample` Django project. It uses SQLite for the database (easy for development) and includes basic styling for a clean UI.

## Features
- **Index Page**: A simple welcome page.
- **Home Page**: Displays user information with conditional rendering (e.g., age check).
- **Contact Form**: Submit name, email, message, and optional image.
- **Messages List**: View all submitted messages in a table with edit/delete options.
- **Edit Message**: Update existing messages.
- **Delete Message**: Confirm and delete messages.
- **Image Uploads**: Store and display uploaded images in the `media/` folder.
- **Django Admin**: Access the admin panel to manage data (login required).

## Prerequisites
Before starting, ensure you have:
- Python 3.8 or higher installed.
- Basic knowledge of Python and web development (HTML, CSS).
- A code editor like VS Code.

## Installation and Setup
Follow these steps to get the project running on your local machine.

### 1. Clone or Download the Project
- Download the `sample/` folder to your computer.
- Open a terminal and navigate to the `sample/` directory:
  ```
  cd path/to/sample
  ```

### 2. Set Up a Virtual Environment (Recommended)
Virtual environments keep dependencies isolated.
- Create a virtual environment:
  ```
  python -m venv virtual
  ```
- Activate it:
  - On Windows: `virtual\Scripts\activate`
  - On macOS/Linux: `source virtual/bin/activate`
- Install Django:
  ```
  pip install django
  ```
- (Optional) Install Pillow for image handling: `pip install pillow` (though it's included in Django's default setup).

### 3. Apply Database Migrations
Django uses migrations to create/update the database.
- Run migrations:
  ```
  python manage.py migrate
  ```
- This creates the SQLite database (`db.sqlite3`) and tables for the app.

### 4. Create a Superuser (for Admin Access)
- Create an admin user:
  ```
  python manage.py createsuperuser
  ```
- Follow prompts to set username, email, and password.

### 5. Run the Development Server
- Start the server:
  ```
  python manage.py runserver
  ```
- Open your browser and go to `http://127.0.0.1:8000/` (or `http://localhost:8000/`).
- Access admin at `http://127.0.0.1:8000/admin/` (login with superuser credentials).

## Usage
- **Navigate the App**:
  - `/`: Index page.
  - `/home/`: Home page (shows name and age logic).
  - `/form/`: Submit a contact message.
  - `/messages/`: View all messages.
  - Click "Edit" or "Delete" on messages to modify them.
- **Uploading Images**: In the form, select an image file. It saves to `media/contact_images/`.
- **Testing**: Submit a few messages, edit one, and delete another. Check the admin panel for data.

## Project Structure
Here's a breakdown of the key files and folders:
```
sample/
├── manage.py                 # Django's command-line tool
├── db.sqlite3                # SQLite database file
├── sample/                   # Project settings folder
│   ├── settings.py           # Main configuration (apps, database, etc.)
│   ├── urls.py               # Root URL patterns
│   ├── wsgi.py               # For production deployment
│   └── asgi.py               # For async deployment
├── akash/                    # Main Django app
│   ├── models.py             # Database models (e.g., contactMessage)
│   ├── views.py              # View functions (handle requests)
│   ├── forms.py              # Django forms (for user input)
│   ├── urls.py               # App URL patterns
│   ├── admin.py              # Registers models for admin
│   ├── apps.py               # App configuration
│   ├── migrations/           # Database migration files
│   └── templates/            # HTML templates
│       ├── index.html        # Welcome page
│       ├── home.html         # Home page with conditionals
│       ├── form.html         # Contact form
│       ├── messages.html     # Messages table
│       ├── edit_message.html # Edit form
│       ├── delete_message.html # Delete confirmation
│       └── nav.html          # Navigation bar (included in others)
├── media/                    # User-uploaded files (images)
└── virtual/                  # Virtual environment (not part of Django)
```

## Key Concepts Explained
As a student, focus on these Django fundamentals:

### 1. **Models (models.py)**
- Define data structures (e.g., `contactMessage` with fields like name, email).
- Use Django's ORM to interact with the database without writing SQL.
- Example: `message = contactMessage.objects.all()` fetches all messages.

### 2. **Views (views.py)**
- Functions that process requests and return responses.
- Handle logic like form submission, data fetching, and rendering templates.
- Example: `render(request, 'form.html', {'form': form})` sends data to the template.

### 3. **Forms (forms.py)**
- Simplify user input validation and rendering.
- Tied to models for easy saving.
- Example: `form.is_valid()` checks if input is correct.

### 4. **URLs (urls.py)**
- Map URLs to views (e.g., `/form/` calls `form_view`).
- Use names for easy linking in templates (e.g., `{% url 'messages' %}`).

### 5. **Templates (templates/)**
- HTML files with Django Template Language (DTL).
- Use `{{ }}` for variables, `{% %}` for logic (if/for).
- Include reusable parts like `nav.html`.

### 6. **Settings (settings.py)**
- Configure the project: apps, database, static files, etc.
- `DEBUG = True` for development; turn off for production.

### 7. **Migrations**
- Track database changes.
- Run `makemigrations` after model changes, then `migrate`.

### 8. **Admin**
- Built-in interface for managing data.
- Register models in `admin.py`.

## Common Issues and Tips
- **Images not showing**: Ensure `MEDIA_URL` and `MEDIA_ROOT` are set in `settings.py`. In development, add to `urls.py`: `from django.conf.urls.static import static; urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`.
- **Form not saving**: Check for CSRF token in templates and `enctype="multipart/form-data"` for file uploads.
- **Database errors**: Delete `db.sqlite3` and re-run `migrate` if issues arise.
- **Styling**: Templates use inline CSS; for better design, link external CSS files.
- **Learning Resources**: Read Django's official docs (docs.djangoproject.com). Practice by adding features like user authentication or pagination.

## Next Steps for Learning
- Add user registration/login using Django's auth system.
- Implement pagination for the messages list.
- Convert to a REST API with Django REST Framework.
- Deploy to Heroku or another platform.

If you run into issues or want to modify the app, feel free to ask! This project is a great starting point for building more complex Django applications.
