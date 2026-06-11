import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="💻 Code Bug Explainer", layout="wide")
st.title("💻 Code Bug Explainer")
st.markdown("Paste buggy code → AI explains the bug in plain English")

openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
language = st.sidebar.selectbox("Code Language:", ["Python", "JavaScript", "Java", "C++", "C#"])

st.markdown("### 📝 Paste Your Buggy Code")
code_input = st.text_area("Enter code with bug:", height=200, placeholder="def fibonacci(n):\n    for i in range(n):\n        print(i)")

if st.button("🔍 Analyze Bug") and openai_key and code_input:
    client = OpenAI(api_key=openai_key)
    
    prompt = f"""You are an expert {language} programmer and debugging teacher. 
A student has written buggy code. Your job:
1. Identify the bug(s)
2. Explain WHAT is wrong in simple terms (like you're teaching)
3. Explain WHY it's wrong (root cause)
4. Provide the FIXED code
5. Explain how the fix works

Code to debug:
{code_input}

Format your response as:
🐛 BUG FOUND: [bug description]
📍 LINE: [approximate line number]
❌ THE PROBLEM: [why this breaks]
✅ THE FIX: [corrected code]
💡 HOW IT WORKS NOW: [explanation of fix]
"""
    
    with st.spinner("Analyzing code..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        explanation = response.choices[0].message.content
    
    st.markdown("### 🤖 AI Analysis")
    st.markdown(explanation)
    
    # Show side-by-side comparison
    if "✅ THE FIX:" in explanation:
        parts = explanation.split("✅ THE FIX:")
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**❌ Original (Buggy)**")
            st.code(code_input, language=language.lower())
        with col2:
            st.markdown("**✅ Fixed Code**")
            if len(parts) > 1:
                fixed = parts[1].split("💡")[0].strip()
                st.code(fixed, language=language.lower())
