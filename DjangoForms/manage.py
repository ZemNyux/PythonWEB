# python -m venv env
# env\Scripts\activate
# pip install django

# правки зроблено у файлах:
# urls.py
# app / views.py
# app / forms.py
# app / templates / contact.html + є варіант contact+css.html

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'Forms.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)