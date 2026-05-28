# AI-Powered Healthcare Assistant Chatbot

## 📌 Project Overview
This project is an AI-driven healthcare chatbot designed to improve patient engagement and streamline basic healthcare inquiries. Developed in collaboration with industry-aligned training partners including **Microsoft, TechSaksham, and SAP**, this application demonstrates the practical application of Artificial Intelligence and Natural Language Processing (NLP) in a real-world scenario.

The chatbot provides instant responses to common healthcare-related keywords (like appointments and medication) and leverages a pre-trained language model to handle more conversational queries, offering a seamless user experience.

## ✨ Features
* **Keyword Intent Recognition:** Instantly identifies specific triggers (e.g., "symptom", "appointment", "medication") to provide safe, predefined guidance.
* **AI Text Generation:** Uses Hugging Face's `distilgpt2` model to generate dynamic, conversational responses for general queries.
* **Interactive Web Interface:** Provides a clean, user-friendly chat interface built with Streamlit.
* **Real-Time Processing:** Delivers immediate feedback to user inputs with built-in loading indicators for a smooth experience.

## 🛠️ Technologies & Libraries Used
* **Python 3.x:** The core programming language.
* **Streamlit:** For rapid development of the web-based graphical user interface.
* **Hugging Face Transformers:** For implementing the `distilgpt2` text-generation pipeline.
* **TensorFlow:** Serves as the deep learning backend for the transformer models.
* **NLTK (Natural Language Toolkit):** Integrated for foundational text processing and tokenization capabilities.

## 🚀 How to Run

### Prerequisites
Ensure you have Python installed on your system. You will need to install the required dependencies before running the application.
```bash
pip install streamlit transformers tensorflow nltk tf-keras
