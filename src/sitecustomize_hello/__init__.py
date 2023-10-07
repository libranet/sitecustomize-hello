"""sitecustomize_hello.__init__."""
__version__ = "1.0"
__copyright__ = "Copyright 2023 Libranet."
__license__ = "MIT License"
import os


def entrypoint() -> None:
    """Print hello to standard output.

    commands known to break:
      > poetry lock
        Expecting value: line 1 column 1 (char 0)


    """
    try:
        enabled = int(os.getenv("SITECUSTOMIZE_HELLO_ENABLE", 1))
    except ValueError:
        enabled = 0

    # print(f"ena: {enabled}")

    if bool(enabled):
        print("Hello!")
