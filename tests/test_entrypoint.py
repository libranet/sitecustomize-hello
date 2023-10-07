# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module sitecustomize_hello."""


def test_entrypoint(capsys) -> None:
    import sitecustomize_hello

    # Call the entrypoint function
    sitecustomize_hello.entrypoint()

    # Capture the standard output
    captured = capsys.readouterr()

    # Check if the captured output matches the expected message
    assert captured.out.strip() == "Hello!"

