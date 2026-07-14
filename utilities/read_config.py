import configparser
import os


class ReadConfig:

    config = configparser.ConfigParser()

    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "config",
        "config.ini"
    )

    config.read(config_path)

    @staticmethod
    def get_base_url():
        return ReadConfig.config.get("common", "baseURL")

    @staticmethod
    def get_browser():
        return ReadConfig.config.get("common", "browser")

    @staticmethod
    def get_implicit_wait():
        return ReadConfig.config.getint("common", "implicit_wait")

    @staticmethod
    def get_username():
        return ReadConfig.config.get("login", "username")

    @staticmethod
    def get_password():
        return ReadConfig.config.get("login", "password")