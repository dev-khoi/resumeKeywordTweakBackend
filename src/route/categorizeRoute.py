from google.adk.agents.llm_agent import Agent
from models.jobCategory import AiJobCategory
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from dotenv import load_dotenv
import os

from ai.prompt import systemInstruction
from config.logger import logger

# Load environment variables from .env file
load_dotenv()

APP_NAME = "weather_sentiment_agent"
USER_ID = "user1234"
SESSION_ID = "1234"
MODEL_ID = "gemini-2.0-flash"

root_agent = Agent(
    model="gemini-3-flash-preview",
    name="root_agent",
    description="Give exactly the result of the instruction/systemInstruction",
    instruction=systemInstruction,
    output_schema=AiJobCategory,
    
)


async def get_ai_response(job_description: str) -> AiJobCategory:
    """Generate AI categorization response for a job description."""
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    runner = Runner(
        agent=root_agent, app_name=APP_NAME, session_service=session_service
    )
    
    # Convert string to Content object
    message = types.Content(role='user', parts=[types.Part(text=job_description)])
    
    events = runner.run(
        user_id=USER_ID, session_id=SESSION_ID, new_message=message
    )
    logger.info(events)
    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response:", final_response)
