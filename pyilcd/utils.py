"""Utilities module for pyilcd."""

import importlib.metadata
from typing import Union


def get_version_tuple() -> tuple:
    """Returns version as (major, minor, micro)."""

    def as_integer(version_str: str) -> Union[int, str]:
        try:
            return int(version_str)
        except ValueError:  # pragma: no cover
            return version_str  # pragma: no cover

    return tuple(
        as_integer(v) for v in importlib.metadata.version("pyilcd").strip().split(".")
    )
