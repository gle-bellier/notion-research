import pytest
from notion_research.main import is_article


def test_is_article():
    assert is_article("articles/Autoregressive.pdf")
