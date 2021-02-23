# Lead Manager

## Quick Start

It is a simple web application TodoList, written on Django and React.js. The code is written the way, so it can be easily deployed on Heroku. Below you can see all the required commands to run in the terminal to run the app locally.

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
