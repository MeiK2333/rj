import logging
import logging.handlers
import sys

from pathlib import Path

Path("logs").mkdir(parents=True, exist_ok=True)


def module_logger(module: str, level=logging.INFO):
    log = logging.getLogger(module)
    log.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s [%(process)s] [%(filename)s:%(lineno)d] [%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.handlers.TimedRotatingFileHandler(
        module_log_file(module), when="midnight", interval=1, backupCount=14
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(stdout_handler)
    return log


def module_log_file(module: str):
    return f"logs/{module}.log"
