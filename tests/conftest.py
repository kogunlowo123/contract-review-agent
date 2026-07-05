"""Test configuration for Contract Review Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "contract-review-agent", "category": "Legal"}
