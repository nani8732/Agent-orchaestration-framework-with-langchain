import streamlit as st
from app import run_agents

st.set_page_config(
    page_title="Agent Orchestration Framework",
    layout="wide",
)

st.title("🤖 Agent Orchestration Framework")

st.markdown(
    "Enter a query..."
)

task = st.text_area(
    "Enter your query",
    height=150,
    placeholder="Example: Analyze the impact of AI in healthcare and draft an email to my manager.",
)

extra_instructions = st.text_area(
    "Extra instructions (optional)",
    height=100,
    placeholder="Example: Focus on recent papers from 2022 onwards, neutral tone.",
)

generate_email = st.checkbox("Generate email", value=True)

if st.button("🚀 Run Orchestration"):
    if not task.strip():
        st.warning("Please enter a goal / topic.")
    else:
        with st.spinner("Agents are working..."):
            result = run_agents(
                user_goal=task,
                generate_email=generate_email,
                extra_instructions=extra_instructions or None,
            )

        st.subheader("🔍 Research Agent Output")
        st.write(result.get("research", ""))

        st.subheader("📝 Summary Agent Output")
        st.write(result.get("summary", ""))

        if generate_email:
            st.subheader("📧 Email Agent Output")
            st.write(result.get("email", "No email generated."))
