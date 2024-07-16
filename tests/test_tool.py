import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))


def test_tool():
    from sayvai_rag import search_index

    assert (
        search_index("tell me something about kochi chinese net")
        == "Chinese fishing nets - Cheenavala in Malayalam - is believed to have been introduced in Kochi by Chinese explorer Zheng He, from the court of the Kubla Khan. The fishing net established itself on the Kochi shores between 1350 and 1450 AD."
    )
