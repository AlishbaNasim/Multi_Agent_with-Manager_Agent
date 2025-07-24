from dotenv import load_dotenv
import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Gemini client and model setup
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# WEB DEVELOPER  Agents
web_developer = Agent(
    name="Web_developer",
    instructions="Expert in frontend and backend web development.\nHelps with coding, debugging, and deploying modern websites."
)

# MOBILE APP DEVELOPER  Agents

mobile_app_developer = Agent(
    name="Mobile_App_developer",
    instructions="Skilled in cross-platform and native mobile app development.\nAssists with UI, APIs, bugs, and publishing apps."
)

# MARKETING Agents

marketing_agent = Agent(
    name="Marketing_Agent",
    instructions="Specialist in digital marketing, SEO, and content strategy.\nGuides on campaigns, branding, and social media growth."
)

# MANAGER  Agents

manager_agent = Agent(
    name="Manager_Agent",
    instructions="Manage all agents by assigning tasks to the right expert.\nIf a task doesn’t match any agent, inform the user it's unsupported and manage everything smoothly.",
    handoffs=[web_developer, mobile_app_developer, marketing_agent]
)

# RESPONSE PRINT..
response = Runner.run_sync(
    manager_agent,
    input = "write code for my web development.",
    run_config=config
    )


print(response)