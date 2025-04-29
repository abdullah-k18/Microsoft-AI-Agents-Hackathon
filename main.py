import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()

api_base = os.getenv("OPENAI_API_BASE")
model_name = os.getenv("OPENAI_MODEL_NAME")
api_key = os.getenv("OPENAI_API_KEY")

st.title("DEV Community Blog Creator")
topic = st.text_input("Enter a blog topic", value="")

if st.button("Generate Blog Post"):
    with st.spinner("Running your agents..."):

        # Define agents
        planner = Agent(
            role="Content Planner",
            goal=f"Plan engaging and factually accurate content on {topic}",
            backstory=(
                f"You're planning a blog article about {topic}. "
                "You collect insightful information that helps readers learn and make decisions."
            ),
            allow_delegation=False,
            verbose=True,
        )

        writer = Agent(
            role="Content Writer",
            goal=f"Write insightful and factually accurate opinion piece on {topic}",
            backstory=(
                f"You're writing a new opinion piece on {topic}, based on the planner's outline."
                " Acknowledge opinions versus facts clearly."
            ),
            allow_delegation=False,
            verbose=True
        )

        editor = Agent(
            role="Editor",
            goal="Edit the blog post to match brand tone and journalistic standards.",
            backstory=(
                "You're an editor. Your goal is to ensure the final blog post is polished, unbiased, "
                "and avoids controversy when possible."
            ),
            allow_delegation=False,
            verbose=True
        )

        # Define tasks
        plan = Task(
            description=(
                "1. Research latest trends and news on {topic}.\n"
                "2. Identify the target audience.\n"
                "3. Create a detailed outline.\n"
                "4. Suggest SEO keywords and sources."
            ),
            expected_output="Content plan with outline, keywords, and audience analysis.",
            agent=planner,
        )

        write = Task(
            description=(
                "Write a compelling blog post on {topic}, using the planner's outline.\n"
                "Include an intro, body, and conclusion. Use SEO keywords and ensure clear formatting."
            ),
            expected_output="Markdown blog post with sections, 2-3 paragraphs each.",
            agent=writer,
        )

        edit = Task(
            description="Proofread and polish the blog post for grammar and tone.",
            expected_output="Final markdown blog post, ready to publish.",
            agent=editor,
        )

        # Run the crew
        crew = Crew(
            agents=[planner, writer, editor],
            tasks=[plan, write, edit],
            verbose=2
        )

        result = crew.kickoff(inputs={"topic": topic})
        st.success("Blog post created successfully!")
        st.markdown(result)
