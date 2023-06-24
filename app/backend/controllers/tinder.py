import os
import json
import pandas as pd

with open('.creds') as f:
    creds = json.load(f)
    PINECONE_API_KEY = creds['PINECONE_API_KEY']
    PINECONE_ENVIRONMENT = creds['PINECONE_ENVIRONMENT']
    OPENAI_API_KEY = creds['OPENAI_API_KEY']

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
)
from src.agent_type import DialogueAgent
from src.simulation_type import DialogueSimulator

def select_next_speaker(step, agents):
    idx = step % len(agents)
    return idx

word_limit = 50  # word limit for task brainstorming


def generate_user(identity_agent, possible_match):
    quest = "This is a date to find the defects and positive values of the other person in that date and do actions to know each other and evaluate"

    identity_system_message = SystemMessage(
        content=(
            f"""{quest}
    Always remember that engaging in discussions involves both finding common ground and acknowledging differences with the other person.
    You are {identity_agent['name']}, and your date is {possible_match['name']}.
    Your character description is as follows: {identity_agent['description']}.
    During the conversation, you will have the opportunity to share about yourself and ask questions to get to know your date, {identity_agent['name']}.
    You hate things and you love other things. Evaluate if the person in front of you is suitable for you.
    Speak in the first person from the perspective of {identity_agent['name']}.
    Do not change roles!
    Do not speak from the perspective of  {possible_match['name']}.
    Do not forget to finish speaking by saying, 'It is your turn, {possible_match['name']}.'
    Do not add anything else.
    If you don´t have anything else to say do not hallucinate and stay within the context.
    Remember you are {identity_agent['name']}.
    Stop speaking the moment you finish speaking from your perspective.
    """
        )
    )
    return identity_system_message


class TinderController:
    def account():
        return ["account"]

    def agent():
        return "agent"

    def match(user_a, user_b):
        userA_system_message = generate_user(user_a, user_b)
        AGENT_A = DialogueAgent(
            name=user_a['name'],
            system_message=userA_system_message,
            model=ChatOpenAI(temperature=0.2),
        )

        userB_system_message = generate_user(user_b, user_a)
        AGENT_B = DialogueAgent(
            name=user_b['name'],
            system_message=userB_system_message,
            model=ChatOpenAI(temperature=0.2),
        )

        simulator = DialogueSimulator(
            agents=[AGENT_B] + [AGENT_A], selection_function=select_next_speaker
        )
        simulator.reset()

        id_list = []
        text_list = []

        max_iters = 5
        n = 0
        while n < max_iters:
            name, message = simulator.step()
            print(f"({name}): {message}")
            print("\n")
            n += 1

            # Append to lists
            id_list.append(name)
            text_list.append(message)

        # Create DataFrame
        df = pd.DataFrame({
            'ID': id_list,
            'Text': text_list
        })

        # Separate the text from the candidate, interviewer, and all text
        user_A_text = df[df['ID'] == user_a['name']]['Text']
        user_B_text = df[df['ID'] == user_b['name']]['Text']

        all_text = df['Text']

        return {'user_a': user_A_text.to_list(), 'user_b': user_B_text.to_list(), 'all_text': all_text.to_list()}

    def feedback():
        return "feedback"
