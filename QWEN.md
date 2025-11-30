# pyconid2025-django-htmx

## Project Overview
This is a Django 5.2.4 project that demonstrates the integration of HTMX for building dynamic, interactive web applications without requiring custom JavaScript. The project features a Todo application with both traditional Django views and HTMX-enhanced views to showcase the differences between standard server-side rendering and progressive enhancement with HTMX.

The project was created for PyCon ID 2025 and serves as a practical example of using HTMX with Django to create responsive user interfaces with minimal JavaScript.

### Architecture
- **Backend**: Django 5.2.4
- **Frontend**: Django templates with HTMX for dynamic interactions
- **Database**: SQLite3 (default)
- **Frontend Library**: HTMX (included as htmx.min.js in static files)

### Key Components
- **Todo App**: The main application module implementing CRUD operations for todos
- **HTMX Integration**: Separate views and templates for HTMX-enhanced interactions
- **Static Files**: Includes htmx.min.js for HTMX functionality

## Building and Running

### Prerequisites
- Python 3.11 or higher
- uv package manager (or pip)

### Setup
1. Clone the repository
2. Install dependencies using uv:
   ```bash
   uv sync
   ```
   Or if using pip:
   ```bash
   pip install -r requirements.txt  # if there was a requirements.txt, but using pyproject.toml instead
   ```
3. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Running the Application
After starting the server, navigate to:
- Traditional Todo interface: `http://127.0.0.1:8000/todos/all/`
- HTMX-enhanced Todo interface: `http://127.0.0.1:8000/todos/all_htmx/`

## Development Conventions

### Code Style
- Follows standard Django conventions
- Uses type hints for view function parameters
- Uses snake_case for function and variable names
- Uses standard Python formatting (PEP 8)

### HTMX Implementation
The project demonstrates several HTMX patterns:
- Progressive enhancement of traditional forms
- Dynamic content updates without page refreshes
- Targeted element updates using `hx-target`
- Client-side confirmations using `hx-confirm`
- Dynamic form loading using `hx-get`

### Project Structure
- `a_core/` - Main Django project settings
- `todo/` - Django app handling todo functionality
  - `models.py` - Todo model definition
  - `views.py` - Contains both traditional and HTMX-enhanced views
  - `urls.py` - URL routing for todo operations
  - `forms.py` - Todo form definition
- `templates/todo/` - Templates for both traditional and HTMX views
- `static/js/` - Contains htmx.min.js library

### Views Organization
The todo app includes both traditional views and HTMX-enhanced alternatives:
- Traditional views (e.g., `get_all_todos`) for full-page rendering
- HTMX views (e.g., `get_all_todos_htmx`) optimized for partial page updates
- Component-based templates that can be reused in HTMX requests

## Key Features
- Full CRUD operations for todos
- HTMX-enhanced user interactions
- Dynamic content updates without page reloads
- Separate interfaces demonstrating traditional vs HTMX approaches
- Message framework integration for user feedback