# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.
# (You could alternatively use another country and provinces,
# or countries of the world and capitals).

import random

states_to_capitals = {
    "Alabama": "montgomery",
    "Alaska": "juneau",
    "Arizona": "phoenix",
    "Arkansas": "little rock",
    "California": "sacramento",
    "Colorado": "denver",
    "Connecticut": "hartford",
    "Delaware": "dover",
    "Florida": "tallahassee",
    "Georgia": "atlanta",
    "Hawaii": "honolulu",
    "Idaho": "boise",
    "Illinois": "springfield",
    "Indiana": "indianapolis",
    "Iowa": "des moines",
    "Kansas": "topeka",
    "Kentucky": "frankfort",
    "Louisiana": "baton rouge",
    "Maine": "augusta",
    "Maryland": "annapolis",
    "Massachusetts": "boston",
    "Michigan": "lansing",
    "Minnesota": "saint paul",
    "Mississippi": "jackson",
    "Missouri": "jefferson city",
    "Montana": "helena",
    "Nebraska": "lincoln",
    "Nevada": "carson city",
    "New Hampshire": "concord",
    "New Jersey": "trenton",
    "New Mexico": "santa fe",
    "New York": "albany",
    "North Carolina": "raleigh",
    "North Dakota": "bismarck",
    "Ohio": "columbus",
    "Oklahoma": "oklahoma city",
    "Oregon": "salem",
    "Pennsylvania": "harrisburg",
    "Rhode Island": "providence",
    "South Carolina": "columbia",
    "South Dakota": "pierre",
    "Tennessee": "nashville",
    "Texas": "austin",
    "Utah": "salt lake city",
    "Vermont": "montpelier",
    "Virginia": "richmond",
    "Washington": "olympia",
    "West Virginia": "charleston",
    "Wisconsin": "madison",
    "Wyoming": "cheyenne",
}

def main():
    correct_count = 0
    incorrect_count = 0

    states = (list(states_to_capitals.keys()))
    random.shuffle(states)
    for state in states:
        answer = input(f'What is the capital of {state}? ').strip()
        for i in answer:
            i = i.lower()

        if answer.lower() == states_to_capitals[state].lower():
            print ('correct')
            correct_count += 1
        else:
            print ('incorrect')
            incorrect_count += 1
    print(f'you answered {correct_count} correct, and {incorrect_count} incorrect.')


main()



