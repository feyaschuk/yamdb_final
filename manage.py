import os
import sys
import dotenv


def main():
    dotenv.load_dotenv(
        os.path.join(os.path.dirname(__file__), '.env')
    )
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_yamdb.settings')
    if os.getenv('DJANGO_SETTINGS_MODULE'):
        os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
  