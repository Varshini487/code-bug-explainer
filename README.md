# 💻 Code Bug Explainer

An **AI-powered debugging assistant** that analyzes buggy code and generates clear, plain-English explanations of what's wrong.

## 🎯 What It Does
Upload or paste buggy Python/JavaScript/Java code → AI analyzes it → outputs explanation of the bug with suggested fixes.

## 🧠 How It Works
1. User pastes code with a bug
2. LLM (GPT-4) parses the syntax tree
3. AI identifies: bug type, line number, root cause
4. Generates explanation: "This is a logic error. Loop never increments i, creating an infinite loop."
5. Provides fix with explanation

## 🛠️ Tech Stack
- **OpenAI GPT-4** – bug analysis and explanation
- **Python AST module** – syntax parsing (optional)
- **Streamlit** – web UI
- **FastAPI** – backend API

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/code-bug-explainer
cd code-bug-explainer
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Use Cases
- Learning tool for students
- Code review assistant
- Debugging help for junior developers
- Educational platform feature
