from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Assuming `IndiaTourAssistant` is imported correctly
from sayvai_rag.agent import IndiaTourAssistant

app = FastAPI()
assistant = IndiaTourAssistant()

class QueryModel(BaseModel):
    input_text: str


@app.post("/chat/")
def invoke_agent(query: QueryModel):
    try:
        
        response = assistant.invoke(query.input_text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
