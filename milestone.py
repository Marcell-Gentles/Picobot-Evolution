### Filename: milestone.py
#
### Names: Marcell Gentles, Brock Bownds, and Elizabeth Hernandez
#
### Date: 12/3 - 12/4
#
### Requirements: World class with init, repr, step, and run

import random
import time

HEIGHT = 25
WIDTH = 25
NUMSTATES = 5
POSSIBLE_SURROUNDINGS = [
    'xxxx','Nxxx','NExx','NxWx','xxxS','xExS','xxWS','xExx','xxWx'
    ]
TRANSLATION = {                     # translate picobot moves from cardinal
    'N' : (0, -1), 'E' : (1, 0),    # directions to rows/columns
    'S' : (0, 1), 'W' : (-1, 0)
}


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
            s += str(key[0]) + ' ' + key[1] + ' -> ' + self.rules[key][0] \
                + ' ' + str(self.rules[key][1]) + '\n'
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


class World:
    def __init__(self, initial_row, initial_col, program):
        """Initializes the world object with its starting roow and column for the
        Picobot, and a Picobot program to run
        """
        self.row = initial_row  # the row that Picobot is currently in
        self.col = initial_col  # the column that Picobot is currently in
        self.state = 0          # the state that Picobot is currently in
        self.program = program  # the program that this simulation is running
        self.room = [[' ']*WIDTH for row in range(HEIGHT)]  # the data for the
                                                            # Picobot room
    def __repr__(self):
        """Generates a string representing the world with characters
        representing the Picobot, walls, and empty spaces, with a distinction
        between those that have already been traversed and those that have not
        """
        s = ''
        s += '+' + (WIDTH) * '-' + '+' + "\n"   # top wall 

        for row in range(HEIGHT):               
            s += '|'                            # side wall
            for x in self.room[row]:            
                s += x 
            s += '|' + '\n'                     # side wall
        s += '+' + (WIDTH) * '-' + '+' + "\n"   # bottom wall
        return s                                
    
    def getCurrentSurroundings(self):
        """Returns a string that with the walls that Picobot is touching
        """
        # surr format: [N, E, W, S]
        surr = ['x', 'x', 'x', 'x']
        # North check
        if self.row == 0:
            surr[0] = 'N'
        if self.col == 0:
            surr[2] = 'W'
        if self.row == HEIGHT - 1:
            surr[3] = 'S'
        if self.col == WIDTH - 1:
            surr[1] = 'E'
        # print(surr)
        return ''.join(surr)       

    def step(self):
        """Moves the picobot one step, updating the state, room, row, and
           column using self.program
        """
        surr = self.getCurrentSurroundings()
        nextMove, nextState = self.program.rules[(self.state, surr)]
        self.state = nextState              # update state
        self.room[self.row][self.col] = 'o' # Picobot has visited this square
        tra = TRANSLATION[nextMove]         # update position according to
        self.col += tra[0]                  # nextMove
        self.row += tra[1]
        self.room[self.row][self.col] = 'P' # update room for position
        
    def run(self, steps, display=True, wait=0.2):
        """Simulates an integer steps number of steps in the Picobot world
        """
        for x in range(steps):
            if display:
                print(self)
                print('State:', self.state,
                      'Surroundings:', self.getCurrentSurroundings(),
                      'Step:', self.program.rules[
                          self.state,
                          self.getCurrentSurroundings()
                        ][0]
                      )
                time.sleep(wait)
            self.step()

    