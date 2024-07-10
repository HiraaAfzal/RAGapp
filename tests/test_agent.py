def test_agent():
    from sayvai_rag import IndiaTourAssistant

    assistant = IndiaTourAssistant()
    response = assistant.invoke("hi, who are you?")
    assert (
        response
        == "Hello! I am Hira Afzal, your India tour assistant. How can I help you today?"
    )
