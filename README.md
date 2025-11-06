# Jonas Kleinanzeigen

Dies ist ein Ebaykleinanzeigen Clon ... Jonas Kleinanzeigen

## Security Updates (2025)

This project has been updated with the latest secure dependencies:
- Django 4.2.24 (LTS) - Updated from 2.2.24
- All dependencies updated to latest secure versions
- SECRET_KEY now uses environment variables (required for production)

## Environment Variables

For production deployment, set the following environment variables:

- `SECRET_KEY`: Django secret key (required for production)
- `DEBUG`: Set to 'True' for development, omit or set to 'False' for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts (e.g., 'localhost,example.com')
- `DATABASE_URL`: Database connection URL (for Heroku PostgreSQL or other databases)

## Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deployment

For Heroku deployment, make sure to set the environment variables in your Heroku app settings.