import streamlit as st
from llama_cpp import Llama
from huggingface_hub import hf_hub_download
import os

st.set_page_config(page_title="ML-Bangla Simplifier (Offline)", page_icon="🇧🇩")

st.title("🤖 ML-Bangla Concept Simplifier")
st.write("Running 100% locally and offline. No API keys needed!")

# Download and cache the local model
@st.cache_resource
def load_model():
    with st.spinner("Loading local Gemma model (downloading ~1.6GB on first run)..."):
        # Downloads a quantized Gemma-2 2B model
        model_path = hf_hub_download(
            repo_id="bartowski/gemma-2-2b-it-GGUF",
            filename="gemma-2-2b-it-Q4_K_M.gguf"
        )
        return Llama(
            model_path=model_path,
            n_ctx=2048,  # Context window limit
            verbose=False
        )

llm = load_model()

concept = st.text_input("What ML concept do you want to learn? (e.g., Overfitting, Gradient Descent)")

if st.button("Explain it to me!") and concept:
    with st.spinner("Thinking in Banglish (Local Brain)..."):
        try:
            # Read your Open Standard Agent Skill
            with open("skills/ml-bangla-simplifier/SKILL.md", "r", encoding="utf-8") as file:
                skill_instructions = file.read()
            
            # Format the prompt using Gemma's native chat structure
            prompt = f"<start_of_turn>user\nSystem Instructions:\n{skill_instructions}\n\nTask:\n{concept}<end_of_turn>\n<start_of_turn>model\n"
            
            # Generate the response completely offline
            response = llm(
                prompt,
                max_tokens=800,
                stop=["<end_of_turn>"],
                echo=False
            )

            st.success("Here is your explanation:")
                
            # Grab the raw text
            raw_text = response["choices"][0]["text"].strip()
            
            # 1. Strip out the triple backticks if the model wrapped its response
            clean_text = raw_text.replace("```markdown", "").replace("```md", "").replace("```", "")
            
            # 2. Strip leading spaces from every single line (just to be safe)
            clean_text = "\n".join([line.lstrip() for line in clean_text.split("\n")])
            
            # Render the clean, wrapping text
            st.markdown(clean_text)
            
        except Exception as e:
            st.error(f"Something went wrong: {e}")