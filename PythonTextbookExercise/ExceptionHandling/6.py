# Logging means recording what happens in your program — especially errors — so you can:

#     🛠 Debug problems later

#     📜 Keep a history of events

#     📣 Alert developers without showing raw errors to users

# Instead of using print(), you use Python’s built-in logging module.

import logging
logging.basicConfig(level=logging.INFO)

# This sets up the logging system. You can choose levels like:

#     DEBUG: detailed info for developers

#     INFO: general events (e.g., “User logged in”)

#     WARNING: something might be wrong

#     ERROR: something went wrong

#     CRITICAL: serious failure

try:
    age=int(56)
except ValueError as e:
    logging.error(f"Error converting age: {e}")

logging.info("user signed up successfully")
logging.basicConfig(filename="app.log", level=logging.INFO)
logging.info("App started")