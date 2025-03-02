import argparse
import logging

from typing import Optional

from hephaestus.io import configure_root_logger
from hephaestus.common import PathLike


def add_common_script_args(parser: argparse.ArgumentParser):
    """Adds common script arguments to argument parser.

    Args:
        parser: a script's argument parser.

    Note:
        Adds `disable-color`, `verbose`, and `version` arguments.
    """

    parser.add_argument(
        "--disable-color",
        help="Disable colored output to standard out",
        required=False,
        dest="disable_color",
        action="store_true",
    )

    parser.add_argument(
        "-vv",
        "--verbose",
        help="output debug messages",
        required=False,
        dest="verbose",
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--version",
        help="print the version of the script",
        required=False,
        dest="version",
        action="store_true",
    )


def set_script_logger(
    script_args: argparse.Namespace, script_log_file: Optional[PathLike] = None
):
    """Configures script logger using passed arguments.

    Args:
        script_args: the parsed arguments passed to the script.
        script_log_file: the script's designated log file path. Defaults to None.
    """

    configure_root_logger(
        min_level=logging.DEBUG if script_args.verbose else logging.INFO,
        log_file=script_log_file,
        enable_color=(not script_args.disable_color),
    )


def check_version_arg(script_args: argparse.Namespace, script_version: str):
    """Checks whether user wants script version.

    Args:
        script_args: the parsed arguments passed to the script.
        script_version: the script's version to output if desired.

    Note:
        Will exit script if `version` arg is set.
    """

    if script_args.version:
        print(script_version)
        exit(0)
