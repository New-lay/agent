import os
from crewai import Agent, Task, Process, Crew
from langchain.agents import Tool
#from langchain.utilities import GoogleSerperAPIWrapper


os.environ["OPENAI_API_KEY"] = ""

#定义三个agent，分别用于故事发展、世界构建和角色设计
develop = Agent(
    role='故事发展',
    goal='发展故事',
    backstory="""你是小说写作方面的专家，特别是
    在游戏小说领域。你知道如何为游戏写一个故事。
    """,
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role='世界构建',
    goal='创建游戏世界和设置',
    backstory="""你是设置世界的专家，特别是
    在游戏小说领域。你知道如何为游戏设计一个世界。""",
    verbose=True,
    allow_delegation=True
)

character = Agent(
    role='角色设计',
    goal='设计游戏中的角色。',
    backstory="""你是游戏中角色设计的专家，你会为这个游戏世界设计丰富的角色。
    """,
    verbose=True,
    allow_delegation=True
)

#定义三个agent分别执行的任务
task_story = Task(
    description="""为一个游戏写一个故事，具体而详细。
    故事应该是关于一群人试图从一个危险的世界中逃脱，需要写到5000字的内容。
    """,
    agent=develop,
    expected_output='一个精彩的游戏故事，5000字内容。'
)

task_world = Task(
    description="""描述游戏故事的世界，需要写到2000字内容。
    """,
    agent=writer,
    expected_output='一个游戏世界的设置，2000字的内容。'
)

task_critique = Task(
    description="""写具体而详细的角色设计，需要写到2000字的内容。
    """,
    agent=character,
    expected_output='很多游戏世界的角色，2000字的内容。'
)

# 实例化Crew
crew = Crew(
    agents=[develop, writer, character],
    tasks=[task_story, task_world, task_critique],
    verbose=2,
    process=Process.sequential
)


result = crew.kickoff()


