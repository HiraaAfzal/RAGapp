import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))


def test_import():
    from sayvai_rag import __version__, search_index

    assert __version__ == "0.0.1"
