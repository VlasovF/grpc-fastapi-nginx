import os


class BaseConfig:
    base_path = os.environ.get("BASE_PATH", "storage/data.json")


settings = BaseConfig()
