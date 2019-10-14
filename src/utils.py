from typing import Iterable, Optional
import os
import logging
import datetime

from numpy import cos, ndarray, pi, sin, array, vstack, arccos
from numpy.linalg import norm

PROJECT_DIR = os.curdir
FIGURES_DIR = os.path.join(PROJECT_DIR, "figures")


def angle_iter_to_unit_circil_coor_array(angle_iter: Iterable[float]) -> ndarray:
    rad_angle_array = array(angle_iter) * pi / 180.0
    return vstack((cos(rad_angle_array), sin(rad_angle_array))).T


def outer_product_3d(array_1: ndarray, array_2: ndarray) -> ndarray:
    return array(
        (
            array_1[1] * array_2[2] - array_1[2] * array_2[1],
            array_1[2] * array_2[0] - array_1[0] * array_2[2],
            array_1[0] * array_2[1] - array_1[1] * array_2[0],
        ),
        float,
    )


def get_angle(x_array: ndarray, y_array: ndarray) -> float:
    return arccos(x_array.dot(y_array) / norm(x_array) / norm(y_array)) * 180.0 / pi


def get_now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")


def get_file_name_root(file_path: str) -> str:
    return os.path.splitext(os.path.split(file_path)[1])[0]


def make_log_dir(log_dir: Optional[str] = None) -> str:
    if log_dir is None:
        log_dir = os.path.join(os.curdir, "log")

    if os.path.exists(log_dir):
        if not os.path.isdir(log_dir):
            raise Exception(f"{log_dir} exists, but not a directory.")
    else:
        os.mkdir(log_dir)

    return log_dir


def set_logging_basic_config(
        main_python_file_name: str,
        level: int = logging.INFO,
        format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        log_dir: Optional[str] = None,
):
    """
    Sets basic logging configuration.
    """
    main_python_file_name_root = get_file_name_root(main_python_file_name)
    log_dir: str = make_log_dir(log_dir)
    log_file_full_path = os.path.join(log_dir, f"{main_python_file_name_root}_{get_now_str()}.log")

    logging.basicConfig(
        level=level,
        format=format,
        handlers=[
            logging.FileHandler(log_file_full_path),
            logging.StreamHandler(),
        ],
    )


def set_logger_config(
        logger: logging.Logger,
        main_python_file_name: str,
        level: int = logging.INFO,
        format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        log_dir: Optional[str] = None,
):
    """
    Sets basic logging configuration.
    """
    main_python_file_name_root = get_file_name_root(main_python_file_name)
    log_dir: str = make_log_dir(log_dir)
    log_file_full_path = os.path.join(log_dir, f"{main_python_file_name_root}_{get_now_str()}.log")

    logger.setLevel(level)

    file_handler: logging.FileHandler = logging.FileHandler(log_file_full_path)
    stream_handler: logging.StreamHandler = logging.StreamHandler()

    formatter: logging.Formatter = logging.Formatter(format)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
