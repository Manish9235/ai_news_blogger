from crewai import Agent
import os
from dotenv import load_dotenv
load_dotenv()
from tools import tool


from langchain_google_genai import ChatGoogleGenerativeAI
## Call the gemini model
llm= ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                            verbose=True,
                            temperature=0.5,
                            google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
  role="Senior Researcher",
  goal="Uncover ground breaking technologies in {topic}",
  verbose=True,
  memory=True,
  backstory=(
    "Driven by curiocity, you are at the forefront of"
    "innovation, eager to explore and share knowledgethat could change"
    "the world"
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=True
)


## Creating a writer agent with custom tools responsible for writing news blogs
news_writer=Agent(
  role="Writer",
  goal="Narrate compelling tech stories about {topic}",
  verbose=True,
  memory=True,
  backstory=(
    "with a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)