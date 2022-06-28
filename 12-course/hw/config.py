import logging

# path config
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
LOGS_PATH = "logs/basic.log"

# ext conf
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# logs conf
# logging.basicConfig(filename=LOGS_PATH)
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOGS_PATH)
log_formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)
