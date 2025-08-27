import os

CONFIG = {
    "MONGO_URI": os.getenv("MONGO_URI", "mongodb://localhost:27017/prueba"),
    "DEBUG": os.getenv("DEBUG", "False") == "True"
}