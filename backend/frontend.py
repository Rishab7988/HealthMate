import numpy as np
import tensorflow as tf
import streamlit as st
import requests
from backend import df_description,df_precautions
# from langchain_helper import get_qa_chain, create_vector_db


st.set_page_config(layout="wide")
st.title("HealthMate 🏥💉👨‍⚕️")


# text="Some text in a box!"
# st.write("HELLO")


# mydict={"Diabetes":[""]}

symptoms=st.text_input("Enter your symptoms in detail... (give 4-5 symptoms)")
# st.write(symptoms)

if symptoms!=None:

    prediction=requests.get(f"http://127.0.0.1:8000/disease_prediction/{symptoms}")
    if prediction.status_code==200:
        response = prediction.json()  # Assuming the response is in JSON format
        st.write("Diagnosis: "+ response)

        st.write()
        st.write(f"Description about the disease {response}: ")
        data1=df_description[df_description['Disease']==response]['Description']
        st.write(data1)
        data1=df_precautions[df_precautions['Disease']=='Tuberculosis']
    mylist=[]
    for i in range(1,5):
        # if df_precautions[df_precautions['Disease']=='Tuberculosis'][f"Precaution_{i}"] !='NaN':
        mylist.append(df_precautions[df_precautions['Disease']=='Tuberculosis'][f"Precaution_{i}"])

    for i in mylist:
        st.write(i)







# st.title("Healthbot Your personal assistant")
# btn = st.button("Create Knowledgebase")
# if btn:
#     create_vector_db()

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# #Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# # Take user input
# question = st.chat_input("Question: ")

# if question:
#     # displaying user message in chat-bot container
#     with  st.chat_message("user"):
#         st.markdown(question)

#     # Add user message to chat history
#     st.session_state.messages.append({"role":"user","content":question})

#     chain = get_qa_chain()
#     response = chain.run(question)

#     # display bot response in chat container
#     with st.chat_message("assistant"):
#         st.markdown(response)
    
#     # Add bot response to chat history
#     st.session_state.messages.append({"role":"bot","content":response})

# st.write("HELLO")






    
    
    