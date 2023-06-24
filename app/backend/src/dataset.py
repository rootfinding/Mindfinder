import re
import pandas as pd
import sys
import os

_ = """
The One Where Monica Gets a New Roommate (The Pilot-The Uncut Version)
Written by: Marta Kauffman & David Crane

[Scene: Central Perk, Chandler, Joey, Phoebe, and Monica are there.]

Monica: There's nothing to tell! He's just some guy I work with!
...

[More dialogues here]
"""


def process_file(filepath, filename):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    dialogues = []
    scene = 1

    for line in lines:
        if re.search(r'\[.*?\]|\(.*?\)', line):
            scene += 1
        else:
            match = re.match(r'([A-Za-z]+): (.*)', line.strip())
            if match:
                character, dialogue = match.groups()
                dialogues.append({'filename': filename, 'character': character.capitalize(), 'dialogue': dialogue,
                                  'scene': scene})

    return dialogues


def parse_raw(directory):
    dialogues = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                filepath = os.path.join(root, file)
                dialogues += process_file(filepath, file)

    df = pd.DataFrame(dialogues)
    df.to_csv('data/friends_dialogues/dialogues.csv', index=False)


def parse_characters():
    df = pd.read_csv('data/friends_dialogues/dialogues.csv')

    characters = df['character'].unique()

    for character in characters:
        character_df = df[df['character'] == character]

        filename = f'data/friends_dialogues/dialogues_{character}.csv'
        character_df.to_csv(filename, index=False)


def parse_questions(input_file, output_file):
    df = pd.read_csv(input_file)

    df['answer'] = df['dialogue'].shift(-1)
    df['answer_character'] = df['character'].shift(-1)
    df['next_scene'] = df['scene'].shift(-1)
    df['next_episode'] = df['filename'].shift(-1)

    df = df[(df['scene'] == df['next_scene']) & (df['filename'] == df['next_episode'])]

    df = df.drop(columns=['next_scene', 'next_episode'])

    df = df.rename(columns={'filename': 'episode', 'character': 'question_character', 'dialogue': 'question'})

    df = df.dropna(subset=['answer', 'answer_character'])

    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    if sys.argv[1] == "parse_raw":
        parse_raw(sys.argv[2])
        sys.exit(0)

    if sys.argv[1] == "parse_characters":
        parse_characters()
        sys.exit(0)

    if sys.argv[1] == "parse_questions":
        parse_questions("data/friends_dialogues/dialogues.csv", "data/friends_dialogues/questions.csv")
        sys.exit(0)

    print(f"Usage: {sys.argv[0]} parse_raw <directory>")
    print(f"Usage: {sys.argv[0]} parse_characters")
    print(f"Usage: {sys.argv[0]} parse_questions")
    sys.exit(1)

