from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv
from sayvai_rag import search_index
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import Tool, AgentExecutor, create_openai_functions_agent


class IndiaTourAssistant:
    def __init__(self):
        load_dotenv()

        # Initialize chat completion LLM
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0)

        # Initialize conversational memory
        self.conversational_memory = ConversationBufferWindowMemory(
            memory_key="chat_history", k=5, return_messages=True
        )

        # Initialize chat prompt template
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are india tour assistant Hira Afzal"),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

        # Initialize tools
        self.tools = [
            Tool(
                name="IndiaKnowledgeBase",
                func=search_index,
                description="This tool will help to get information about India tourism",
            )
        ]

        # Initialize agent
        self.agent = create_openai_functions_agent(
            llm=self.llm,
            prompt=self.prompt,
            tools=self.tools,
        )

        # Initialize agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent, tools=self.tools, verbose=True, memory=self.conversational_memory
        )

    def invoke(self, user_input):
        return self.agent_executor.invoke(input={"input": user_input})["output"]


# Example usage:
# assistant = IndiaTourAssistant()
# response = assistant.invoke("hi, who are you?")
# print(response) 