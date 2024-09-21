import configparser
import json
import logging
import os
from random import choice, randint
from time import sleep


def load_config(config_file="config.ini"):
    """
    Loads configuration from the specified .ini file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        configparser.ConfigParser: The configuration parser object.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def setup_logging(log_folder, log_file, log_level):
    """
    Sets up the logging configuration.

    Args:
        log_folder (str): Directory for the log file.
        log_file (str): Name of the log file.
        log_level (str): Logging level (e.g., 'NOTSET').
    """
    os.makedirs(log_folder, exist_ok=True)
    log_path = os.path.join(log_folder, log_file)
    logging.basicConfig(
        level=getattr(logging, log_level, logging.NOTSET),
        format="%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler(),
        ],
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def load_data(data_folder, json_file):
    """
    Loads sentence components from the JSON data file into lists.

    Args:
        data_folder (str): Directory where the JSON file is located.
        json_file (str): Name of the JSON file.

    Returns:
        tuple: (subjects, verbs, objects, adverbs) - Lists of sentence components.
    """
    json_path = os.path.join(data_folder, json_file)
    try:
        with open(json_path) as f:
            data = json.load(f)
            return (
                data.get("subjects", []),
                data.get("verbs", []),
                data.get("objects", []),
                data.get("adverbs", []),
            )
    except FileNotFoundError:
        logging.error(f"File {json_path} not found.")
        return [], [], [], []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file {json_path}.")
        return [], [], [], []


class RandomSentenceLogger:
    """
    Generates and logs random sentences at various levels.
    """

    LOG_LEVELS = [
        logging.info,
        logging.warning,
        logging.debug,
        logging.error,
        logging.critical,
    ]

    def __init__(self, subjects, verbs, objects, adverbs):
        self.subjects = subjects
        self.verbs = verbs
        self.objects = objects
        self.adverbs = adverbs

    def generate_random_sentence(self, random_number):
        """
        Generates a random sentence with the given random number.

        Args:
            random_number (int): The random number to include in the sentence.

        Returns:
            str: The generated random sentence.
        """
        if not (self.subjects and self.verbs and self.objects and self.adverbs):
            raise ValueError("Data is missing to generate a sentence.")

        subject = choice(self.subjects)
        verb = choice(self.verbs)
        obj = choice(self.objects)
        adverb = choice(self.adverbs)

        return f"{subject} {verb} {obj} {adverb}. ({random_number})"

    def log_random_message(self):
        """
        Logs a randomly generated sentence to all log levels with different random numbers.
        """
        for log_function in self.LOG_LEVELS:
            random_number = randint(1, 1_000_000)
            message = self.generate_random_sentence(random_number)
            log_function(message)

    def start_logging(self, interval):
        """
        Continuously generates and logs random sentences at the specified interval.

        Args:
            interval (float): Time interval (in seconds) between logging messages.
        """
        while True:
            self.log_random_message()
            sleep(interval)


def main():
    """
    Main entry point for the script. Loads configuration, data, creates a RandomSentenceLogger instance,
    and starts logging.
    """
    config = load_config()

    # Configuration
    log_folder = r"C:\Users\snake\Desktop\Courses\Big data training\Task 2\Random-Logs-Generator-main\logs"
    log_file = "generated_logs.log"
    log_level = config.get("logging", "log_level", fallback='INFO').upper()
    data_folder = r"C:\Users\snake\Desktop\Courses\Big data training\Task 2\Random-Logs-Generator-main\data"
    json_file = "words.json"
    interval = float(config.get("settings", "interval", fallback=1.0))

    # Setup logging
    setup_logging(log_folder, log_file, log_level)

    # Load data
    subjects, verbs, objects, adverbs = load_data(data_folder, json_file)

    # Start logging
    logger = RandomSentenceLogger(subjects, verbs, objects, adverbs)
    logger.start_logging(interval)


if __name__ == "__main__":
    main()
