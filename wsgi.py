import sys
import os

# Add the web_service directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'web_service'))

from web_service.app import app

if __name__ == "__main__":
    app.run()
