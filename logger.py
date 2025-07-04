import logging

app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)
app_handler = logging.FileHandler("app.log")
app_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
app_logger.addHandler(app_handler)

validation_logger = logging.getLogger("validation_logger")
validation_logger.setLevel(logging.INFO)
validation_handler = logging.FileHandler("validation.log")
validation_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
validation_logger.addHandler(validation_handler)
