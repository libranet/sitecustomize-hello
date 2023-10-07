"""sitecustomize_hello.__init__."""
__version__ = "1.0"
__copyright__ = "Copyright 2023 Libranet."
__license__ = "MIT License"
import os


def strtobool(val: str) -> bool:
    """Convert a string representation of truth to true (1) or false (0).

    True values are case insensitive 'y', 'yes', 't', 'true', 'on', and '1'.
    false values are case insensitive 'n', 'no', 'f', 'false', 'off', and '0'.
    Raises ValueError if 'val' is anything else.

    Copied from distutils.util.strtobool, which is deprecated

    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif val in ("n", "no", "f", "false", "off", "0"):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))


def entrypoint() -> None:
    """Print hello to standard output.

    commands known to break:
      > poetry lock
        Expecting value: line 1 column 1 (char 0)


    """
    try:
        enabled = strtobool(os.getenv("SITECUSTOMIZE_HELLO_ENABLE", "1"))
    except ValueError:
        enabled = False

    if enabled:
        print("Hello!")
