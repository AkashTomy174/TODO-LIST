# TODO: Implement Todo CRUD Operations in Separate 'todos' App

- [x] Create new Django app 'todos' using 'python manage.py startapp todos'
- [x] Add 'todos' to INSTALLED_APPS in sample/settings.py
- [x] Define Todo model in todos/models.py with fields: title, description, status, created_at
- [x] Create TodoForm in todos/forms.py for title, description, status
- [x] Implement views in todos/views.py: todo_list, create_todo, edit_todo, progress_todo, complete_todo
- [x] Create todos/urls.py with paths for todo operations
- [x] Create templates in todos/templates/todos/: todo_list.html, create_todo.html, edit_todo.html
- [x] Update sample/urls.py to include todos.urls
- [x] Update akash/templates/nav.html to add link to todo list
- [x] Run python manage.py makemigrations todos and migrate
- [x] Add progress button functionality to change todo status and color
- [x] Test the todo page functionality (server running at http://127.0.0.1:8000/todos/)
- [x] Update this TODO file with completion status
