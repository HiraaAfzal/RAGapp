import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))


def test_agent():
    from sayvai_rag import IndiaTourAssistant

    assistant = IndiaTourAssistant()
    response = assistant.invoke("hi, who are you?")
    assert (
        response
        == "Hello! I am Hira Afzal, your India tour assistant. How can I help you today?"
    )
