#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pyngrok import ngrok

from coupon.views import load_csv


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

        # Start the Django development server
    # django_port = 8000  # Replace with your Django development server's port
    # public_url = ngrok.connect(django_port)
    # print("Public URL:", public_url)

    # try:
    load_csv()
    execute_from_command_line(sys.argv)
    # finally:
    #     # Disconnect and terminate the tunnel when done
    #     ngrok.disconnect(public_url)
    #     ngrok.terminate()



if __name__ == '__main__':
    main()
