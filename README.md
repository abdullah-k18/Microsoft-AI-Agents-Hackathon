# 🧠 DEV Community Blog Creator — AI Agents Hackathon Submission

Welcome to **DEV Community Blog Creator**, a Streamlit application powered by multi-agent collaboration via [CrewAI](https://docs.crewai.com/). This project is my submission for the **Microsoft AI Agents Hackathon** and demonstrates how LLM agents can collaborate to research, write, and polish a professional-quality blog post based on any given topic.

## 🚀 Project Overview

This app simulates a real-world content creation pipeline using three AI agents:

- **Content Planner**: Researches the topic and creates an outline.
- **Content Writer**: Writes the full blog post based on the planner's output.
- **Editor**: Polishes and proofreads the blog post to ensure it meets editorial standards.

The result is a well-structured blog post ready for publication.

---

## ✨ Features

- ✅ Multi-agent collaboration using [CrewAI](https://github.com/joaomdmoura/crewAI)
- ✅ Fully automated research, writing, and editing
- ✅ Real-time blog generation in Streamlit
- ✅ Uses environment variables for secure API key management
- ✅ Outputs final blog post in Markdown format

---

## 🛠️ Tech Stack

- Python
- Streamlit
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- Groq Cloud API
- Dotenv for managing secrets

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/dev-community-blog-creator.git
cd dev-community-blog-creator
```

2. **Create a .env file**
```python
OPENAI_API_BASE=https://api.openai.com/v1
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL_NAME=gpt-4  # or your preferred model
```

3. **Install dependencies**
```bash
pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29 streamlit 
```

5. Run the app
```bash
streamlit run main.py
```

---

### 🖼️ App Interface
![1](https://github.com/user-attachments/assets/cb066e90-e6ab-4c4d-936b-de3e4668d77a)
*User enters blog topic*

![2](https://github.com/user-attachments/assets/897ee678-aa3b-4c0a-afcb-0a4cda3c8bce)
*Final blog post generated by agents*

---

## 🧠 How It Works

| Agent           | Role Description                                                                 |
|------------------|----------------------------------------------------------------------------------|
| **Content Planner** | Gathers insights, defines the audience, and outlines the blog structure         |
| **Content Writer**  | Writes a structured post using the planner's outline and SEO recommendations     |
| **Editor**          | Refines tone, grammar, and flow for final publishing                            |

All tasks are managed and executed using the **CrewAI** framework, which enables LLM agents to work collaboratively.

---

## 🧪 Example Topics

- "AI Agents in Software Development"  
- "How LLMs are Transforming Technical Writing"  
- "Top 10 AI Tools for Content Creation"

