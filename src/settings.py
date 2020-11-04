import os


# Host on which to run application
HOST = os.environ.get('HOST', '0.0.0.0')

# Port on which to run application
PORT = os.environ.get('PORT', '8080')

# Boolean value. True if debugging (development) mode is enabled.
DEBUG = bool(int(os.environ.get('DEBUG', 0)))
