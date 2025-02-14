# Required installations
#!pip install streamlit
!#pip install transformers
#!pip install tensorflow
#!pip install nltk
#!pip install tf-keras

# Importing necessary libraries
import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Downloading NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')

# Setting up the chatbot pipeline
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult a doctor."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant:", response)
            print(reponse)
        else:
            st.write("Please enter a message to get a response or enter a query.")

if __name__ == "__main__":
    main()
