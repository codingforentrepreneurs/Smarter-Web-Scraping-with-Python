from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

from .env import config

BRIGHT_DATA_USERNAME=config("BRIGHT_DATA_USERNAME", default=None)
BRIGHT_DATA_PASSWORD=config("BRIGHT_DATA_PASSWORD", default=None)
BRIGHT_DATA_HOST=config("BRIGHT_DATA_HOST", default=None)
BRIGHT_DATA_DEFAULT_PORT= 9222
BRIGHT_DATA_SELENIUM_PORT = 9515

def get_proxy_url(use_selenium=False):
    port = BRIGHT_DATA_DEFAULT_PORT
    if use_selenium:
        port = BRIGHT_DATA_SELENIUM_PORT
    auth_str = f"{BRIGHT_DATA_USERNAME}:{BRIGHT_DATA_PASSWORD}"
    return f"https://{auth_str}@{BRIGHT_DATA_HOST}:{port}"


def get_sbr_connection():
    proxy_url = get_proxy_url(use_selenium=True)
    return ChromiumRemoteConnection(proxy_url, 'goog', 'chrome')