# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module sitecustomize_hello."""
import contextlib
import os


@contextlib.contextmanager
def change_working_directory(directory):
    current_directory = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(current_directory)


def test_sitecustomize_hello() -> None:
    assert os.getcwd() == os.getenv("PWD_DIR")


def test_sitecustomize_hello(tmpdir) -> None:
    assert os.getcwd() == os.getenv("PWD_DIR")

    with change_working_directory(tmpdir):
        assert str(tmpdir) != os.getenv("PWD_DIR")

    assert os.getcwd() == os.getenv("PWD_DIR")
