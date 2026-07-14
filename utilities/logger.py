import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        log_path = os.path.join("logs", "automation.log")

        logging.basicConfig(
            filename=log_path,
            format="%(asctime)s : %(levelname)s : %(message)s",
            level=logging.INFO,
            force=True
        )

        return logging.getLogger()