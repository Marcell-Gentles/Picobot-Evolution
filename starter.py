### starter.py
#
### Marcell Gentles and Brock Bownds
#
### Nov 28, 2023

import random

HEIGHT = 25
WIDTH = 25
NUMSTATES = 5
POSSIBLE_SURROUNDINGS = [
    'xxxx','Nxxx','NExx','NxWx','xxxS','xExS','xxWS','xExx','xxWx'
    ]



class Program:
    def __init__(self):
        """Creates an empty dictionary that will store the set of rules that
           makes up the Picobot program
        """
        self.rules = {}

    def __repr__(self):
        """Translates the Picobot program from a Python dictionary to the
           Picobot syntax of [STATE] [SURROUNDINGS]] -> [STEP] [STATE]
        """
        s = ''
        for key in self.rules:
            s += str(key[0]) + ' ' + key[1] + ' ' + '->' + ' '
            + self.rules[key][0] + ' ' + str(self.rules[key][1]) + '\n'
        return s
    
    def randomize(self):
        """Creates a random move and new state corresponding to each possible
           combination of surroundings and states
        """
        for state in range(NUMSTATES):
            for surr in POSSIBLE_SURROUNDINGS:
                move = random.choice(['N', 'S', 'E', 'W'])
                while move in surr:
                    move = random.choice(['N', 'S', 'E', 'W'])
                new_state = random.choice(range(NUMSTATES))
                self.rules[(state, surr)] = (move, new_state)