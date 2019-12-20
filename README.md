# Lead Manager

## Quick Start

```bash
# Install dependencies
npm install

# Set virtual environment
pipenv shell

# Install necessary django packages
pipenv install django djangorestframework django-rest-knox

# Apply migrations
python3 leadmanager/manage.py migrate

# Serve API on localhost:8000
python3 leadmanager/manage.py runserver

# Run webpack (from root)
npm run dev

# Build for production
npm run build
```
