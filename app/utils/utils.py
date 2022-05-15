import sys
import typing as tp

from dotenv import dotenv_values
from .. import PATH_TO_APP


def get_port(place: str = "BACKEND") -> int:
    """
    This function returns port from config file or 5555
    :param place: BACKEND or FRONTEND
    :return: port
    """
    config: dict[str, tp.Optional[str]] = dotenv_values(PATH_TO_APP / ".env")
    port: int = 8888

    if place + "_PORT" in config:
        try:
            port = int(config[place + "_PORT"] or "8888")
        except ValueError:
            sys.stderr.write("Incorrect port in .env file!")
    return port
