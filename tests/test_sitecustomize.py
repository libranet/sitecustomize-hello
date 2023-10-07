# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module sitecustomize."""


def test_import_sitecustomize() -> None:
    try:
        import sitecustomize  # noqa: F401
    except ImportError:
        # package sitecustomize-entrypoints is not installed
        assert False


def test_entrypoint_registration() -> None:
    from sitecustomize._vendor.importlib_metadata import entry_points

    assert "sitecustomize_hello" in entry_points(group="sitecustomize").names
