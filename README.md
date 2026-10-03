# 🇧🇩 ML-Bangla Concept Simplifier

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest-2026-orange.svg)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Offline AI](https://img.shields.io/badge/AI-100%25%20Offline-green.svg)

An offline, privacy-first AI application built for Bangladeshi students (particularly in the Dinajpur region) to understand complex Machine Learning concepts. It uses a custom **Agent Skill** to explain technical jargon in conversational "Banglish," utilizing relatable local analogies (like agriculture and local transport) and simplified math.

This project was created for **Hacktoberfest 2026** and specifically targets the **Best Open-Source AI Project** category.

---

## ✨ Features

- **100% Offline & Local:** Runs a quantized open-weights AI model (`gemma-2-2b-it-Q4_K_M.gguf`) entirely on your local machine using `llama-cpp-python`. Zero API keys or active internet connection required after initial model download.
- **Agent Skill Open Standard:** The persona and behavior are driven by a strictly compliant `SKILL.md` file, making the prompt logic portable to any standard AI agent platform (e.g., Cursor, Claude Code, DevRelay).
- **Banglish & Local Context:** Translates dry ML textbook definitions into relatable Bangladeshi contexts (such as Dinajpur lychee farming, Kataribhog rice, bazaar bargaining, and university exam prep).
- **Streamlit UI:** A clean, lightweight web interface for fast, interactive concept lookup.

---

## 📁 Repository Structure

```text
antigravity-agent/
├── skills/
│   └── ml-bangla-simplifier/
│       └── SKILL.md       # Open Standard Agent Skill defining AI persona & rules
├── app.py                 # Streamlit UI & local LLM runner
├── .gitignore             # Git ignore configuration
├── LICENSE                # MIT License
└── README.md              # Project documentation
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+** installed on your system.
- Build tools (C++ compiler) if installing `llama-cpp-python` from source, or pre-built wheels for your system architecture.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ZuhairHossain/ml-bangla-simplifier.git
   cd ml-bangla-simplifier
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install streamlit llama-cpp-python huggingface_hub
   ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

> **Note:** On the first launch, the app will automatically download the quantized Gemma 2B model (~1.6 GB) from HuggingFace. All subsequent runs execute completely offline.

---

## 💡 Response Format

Every explanation produced by the app strictly adheres to the 4-part structure defined in [`skills/ml-bangla-simplifier/SKILL.md`](file:///home/zuhairhossain/Personal/hacktoberfest/antigravity-agent/skills/ml-bangla-simplifier/SKILL.md):

1. **The Textbook Definition (Boi-er Bhashay):** High-level summary of the ML term.
2. **The Local Analogy (Deshi Golpo):** Relatable Bangladeshi scenario in warm, conversational Banglish.
3. **The Math / Mechanics (Esho Math Kori):** Intuitive breakdown of the formula or inner workings.
4. **Quick Summary (Sarboshesh Kotha):** A single-sentence takeaway.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)