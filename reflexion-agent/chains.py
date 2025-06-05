import datetime

from dotenv import load_dotenv

load_dotenv()

from langchain_core.output_parsers.openai_tools import (
    JsonOutputToolsParser,
    PydanticToolsParser,
)

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

actor_prompt_template = ChatPromptTemplate([
    (
        "system",
    """
        You are an exper researcher.
    Current time: {time}
    
1. {first_instruction}
2. Reflect and critique your answer. Be severe to maximize improvement.
3. Recomend search queries to research information and improve your answers.
""",
    ),
    MessagesPlaceholder(variable_name="messages"),
    ("system", "Answer the user's question above using the required format.")
    ]).partial(
        time=lambda: datetime.datetime.now().isoformat(),
    )
