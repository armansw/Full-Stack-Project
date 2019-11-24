# Arman's Manager


## Quick Start

```bash
# Install dependencies
npm install

# Set up virtual environment
pipenv shell

#Install all neccessary packages for django
pipenv install django djangorestframework django-rest-knox

#Apply all migrations
python3 leadmanager/manage.py migrate

# Serve API on localhost:8000
python leadmanager/manage.py runserver

# Run webpack
npm run dev

# Build for production
npm run build
```
