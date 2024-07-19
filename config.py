import os

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID")
IS_PRIVATE = os.environ.get("IS_PRIVATE", False)  # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')

# Split AUTH_USERS by commas and convert to integers
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(",")) if os.environ.get("AUTH_USERS") else []

# Ensure OWNER_ID is in AUTH_USERS
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
