import openai

import os
#load from json .creds/PINECONE_API
import json
with open('.creds/PINECONE_API') as f:
    creds = json.load(f)
    PINECONE_API_KEY = creds['PINECONE_API_KEY']
    PINECONE_ENVIRONMENT = creds['PINECONE_ENVIRONMENT']
    OPENAI_API_KEY = creds['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY



def contractor_agent(user_c, user_d,text_list):
    description = f"""You are an agent skilled in facilitating agreements and meaningful connections between people.
    You will be provided with a dialogue between two users {user_c["name"]} and {user_d["name"]} who are on a first date, and your task will be to analyze the text to determine shared interests, disagreements and reach a final evaluation.
    At the end of the process, you must generate a summary that contains the conclusions and the resulting contract.
    This contract will be based on shared interests, agreed upon activities, and connection opportunities identified during the conversation.
    Only respond as the Expected Output, you are only allowed to response in this way, as a contract.
    """

    expected_output = f"""
    Contract:
    After an engaging conversation and discovering shared interests and values,{user_c["name"]} and {user_d["name"]} both  have reached an agreement to:
    Plans together:
    Disagreement:
    Agreement:
    """


    context = f"""
        Your description is as follows: [{description}]
        You only respond in this expected output: [{expected_output}].
        Do not change roles, please.
        Do not speak from other perspective.
        Please only responde as expected output, you are only allowed to response in this way, as a contract.
    """


    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
        temperature=0.5,
      messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": text_list[0]}
        ]
    )

    return response['choices'][0]['message']['content']
