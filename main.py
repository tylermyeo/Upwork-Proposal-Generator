#UPWORK PROPOSAL GENERATOR

import os
import streamlit as st
import openai

api_key = st.secrets['API_KEY']
openai.api_key = api_key

org_key = st.secrets['OPEN-AI-ORGANISATION']
openai.organization = org_key

# RETRIEVE OPENAI MODEL
openai.Model.list()
openai.Model.retrieve("text-davinci-003")

# PROMPT FUNCTION
def prompt(input):
  with st.spinner('Writing...'):
    set_prompt = input
    set_max_tokens = 1024
    set_creativity = 0.2 #between 0 and 2
    set_variations = 1
    set_variety_range = 1 #between -2 and 2
    set_uniqueness = 1 #between -2 and 2
  
    output = openai.Completion.create(
    model="text-davinci-003",
    prompt=set_prompt,
    max_tokens=set_max_tokens,
    top_p=1,
    temperature=set_creativity,
    n=set_variations,
    presence_penalty = set_variety_range,
    frequency_penalty = set_uniqueness
  )

  output_list = output.choices

  for item in range(len(output_list)):
    output_dict = output_list[item]
    output_text = output_dict['text']
    tokens_used = output_dict['usage']['total_tokens']
    return output_text
    return tokens_used


# SIDEBAR
with st.sidebar:
  st.title("Upwork Proposal Generator")
  st.write("An AI-powered proposal generator. Trained on Upwork's recommendations for effective proposals.")
  tone = st.multiselect('Select the tone of the proposal.', ['Conversational', 'Informative', 'Professional', 'Friendly', 'Confident'])
  experience = st.text_area("Relevant Experience", placeholder='Enter relevant experience...')
  notes = st.text_area("Notes", placeholder='Enter any extra info to be included in the proposal...')
  job_description = st.text_area("Job Description", placeholder="Paste the job description here.")
  prompt_input = f"""
  Write an Upwork job proposal for the following job description: \n
  {job_description} \n 
  \n
  The proposal tone should be {tone}. \n
  Write the proposal in the first-person. \n
  The proposal should be 3 paragraphs. \n
  Address all of the requirements mentioned in the job description. \n
  Include an estimate of how long you expect the project to take. \n
  
  Mention the following in the proposal:\n
  {experience} \n
  {notes} \n
  """


  if(st.sidebar.button("✨ Write for me", key=1)):
    st.write(prompt(prompt_input))