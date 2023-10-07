"""sitecustomize_hello.__init__."""
__version__ = "1.0"
__copyright__ = "Copyright 2023 Libranet."
__license__ = "MIT License"


def entrypoint() -> None:
    """Print hello to standard output."""
    print("Hello!")

