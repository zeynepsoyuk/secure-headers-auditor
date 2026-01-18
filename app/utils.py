import logging
import os
from dotenv import load_dotenv

# ortam değişkenleri
load_dotenv()

def setup_logger():
    """Logging."""
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    logging.basicConfig(
        filename='logs/audit_app.log',
        level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')),
        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
        filemode='a'
    )
    # Konsola da log basmak için
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console)

def get_config(key, default=None):
    """Reading env. var.."""
    return os.getenv(key, default)