"""Prevent dotenv reads; sitecustomize supplies network isolation."""

import json
from pathlib import Path
from unittest.mock import patch


patches = []


def pytest_configure(config):
    scope = json.loads(Path(__file__).with_name("quality_scope.json").read_text())
    if "offline_guard" not in scope["plugins"]:
        try:
            p = patch("dotenv.load_dotenv", return_value=False)
            p.start()
            patches.append(p)
        except ImportError:
            pass


def pytest_unconfigure(config):
    for p in reversed(patches):
        p.stop()
