### Filename: final.py
#
### Names: Marcell Gentles, Brock Bownds, and Elizabeth Hernandez
#
### Date: December 8, 2023
import builtins
import random
import time
from operator import itemgetter

HEIGHT = 23
WIDTH = 23
NUMSTATES = 5
POSSIBLE_SURROUNDINGS = [
    'xxxx','Nxxx','NExx','NxWx','xxxS','xExS','xxWS','xExx','xxWx'
    ]
TRANSLATION = {                     # translate picobot moves from cardinal
    'N' : (0, -1), 'E' : (1, 0),    # directions to rows/columns
    'S' : (0, 1), 'W' : (-1, 0)
}
# GA values
TRIALS = 50
STEPS = 1000
FRAC_TO_KEEP = 0.088
MUT_PROB = 0.10


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
                while move in surr:     # pick a move not into a wall
                    move = random.choice(['N', 'S', 'E', 'W'])
                new_state = random.choice(range(NUMSTATES))
                self.rules[(state, surr)] = (move, new_state)
    
    def mutate(self, display=False):
        """Chooses a single rule from self.rules and should change the value
           (the move and new state) for it
        """
        # pick state/surroundings pair to mutate a response toward
        mrule = random.choice(list(self.rules))
        new_state = random.choice(range(NUMSTATES))
        move = random.choice(['N', 'S', 'E', 'W'])
        while move in mrule[1]:     # don't let it move into a wall!
            move = random.choice(['N', 'S', 'E', 'W'])
        # assign the new response to the selected environment
        self.rules[mrule] = (move, new_state)

    def crossover(self, other):
        """Returns a new "offspring" Program that contains some of the rules
           from self and the rest from the Program other. 
        """
        rules = {}                      # empty set of rules for the offspring
        cr_st = random.choice(range(4)) # crossover state
        # identify which parent passes down their response to each environment 
        self_envs = [env for env in self.rules if env[0] <= cr_st]
        other_envs = [env for env in self.rules if env[0] > cr_st]
        # populate the rules with parents' rules
        for env in self_envs:
            rules[env] = self.rules[env]
        for env in other_envs:
            rules[env] = other.rules[env]
        # create a new Program whose rules are given by this method instead of
        # randomization
        new = Program()
        new.rules = rules
        return new


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
        # start by assuming no neighboring walls
        surr = ['x', 'x', 'x', 'x']
        # check if there are neighboring walls; if so, populate the
        # appropriate position in the future string
        if self.row == 0:
            surr[0] = 'N'
        if self.col == 0:
            surr[2] = 'W'
        if self.row == HEIGHT - 1:
            surr[3] = 'S'
        if self.col == WIDTH - 1:
            surr[1] = 'E'
        # turn the list into a string of format 'NEWS'
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
        
    def run(self, steps, display=False, wait=0.2):
        """Simulates an integer steps number of steps in the Picobot world,
           with the option to display them in the terminal with wait number of
           seconds between each step
        """
        for x in range(steps):
            if display:
                # display the world, state, surroundings, and step
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

    def fractionVisitedCells(self):
        """Returns the float fraction of cells in self.room that have been
           marked as visited (including Picobot's current location)
        """
        total = 0
        for row in self.room:
            total += row.count('o')
        total += 1      # account for the cell Picobot is occupying
        return total / (HEIGHT*WIDTH)
    
    def clear(self):
        for row_in in range(len(self.room)):
            for col_in in range(len(self.room[row_in])):
                self.room[row_in][col_in] = ' '
    

def genPop(size):
    """Returns a population (list) of size number of random Picobot Programs
    """
    L = []
    for x in range(size):
        p = Program()
        p.randomize()
        L += [p]
    return L

def evaluateFitness(program, trials, steps):
    """Uses the World method fractionVisitedCells to return the average
       'fitness' (number of cells visited by Picobot) of a Program over trials
       number of simulations of steps steps starting at a random cell
    """
    sum = 0
    for x in range(trials):
        # for each trial, instantiate a new world     
        w = World(random.choice(range(HEIGHT)),
                  random.choice(range(WIDTH)),
                  program)
        # then run it for the specified number of steps
        w.run(steps)
        # add fractionVistedCells for that trial into the running sum
        sum += w.fractionVisitedCells()
    return sum/trials  # find the average of all trials

def GA(popsize, numgens, FRAC_TO_KEEP=FRAC_TO_KEEP, MUT_PROB=MUT_PROB, display=True):
    """Creates popsize random Picobot Programs and uses their crossover method
       numgens times along with occasional mutation to 'breed' the most fit
       population and return the single most fit Program after the evolution
    """
    # generate a population of popsize Programs
    pop = genPop(popsize)
    for gen in range(numgens):
        # create lists of tuples of the fitness of Programs with the Programs
        L = [(evaluateFitness(program, TRIALS, STEPS), program)
             for program in pop]
        L = sorted(L)           # then sort it from least to most fit
        if display:
            LC = [e[0] for e in L]
            print("Generation :", gen,
                  "\n    Average fitness :",
                  sum(LC) / len(LC),
                  "\n    Highest fitness :",
                  max(LC))
        # calculate how many programs will reproduce
        num_keep = int(len(L) * FRAC_TO_KEEP)
        # then keep that many from the fit end of the list
        L = L[-num_keep:]
        # make a copy of the list to manipulate during the mating process
        temp = [x for x in L]
        # create an emtpy list of offspring programs
        pop = []
        # make more unitl there are enough
        while len(pop) < popsize:
            # if we run out of parents, refresh them; they effectively mate
            # more than once
            if len(temp) < 3:
                temp = [x for x in L]
            # assign two parents from the manipulated list and then remove
            # them from the list
            parent1 = temp.pop(random.choice(range(len(temp))))[1]
            parent2 = temp.pop(random.choice(range(len(temp))))[1]
            # fill the new population with offspring
            pop.append(parent1.crossover(parent2))
            # then do it over again
        # give each offspring a chance to mutate
        for p in pop:
            if random.random() <= MUT_PROB:
                p.mutate()
    # return the final generation's most fit program
    return L[-1][1]

def saveToFile(filename, p):
        """Saves the data from Program p to a file named filename"""
        f = open(filename, "w")
        print(p, file = f)        # prints Picobot program from __repr__
        f.close()

def sorted(L):
    """Keys element 0 for sorting the (fitness, Program) tuples"""
    return builtins.sorted(L, key=itemgetter(0))

def bestVariables(popsize, numgens, combos):
    """Picks random biological variables to determine which are the most
       advantageous toward fitness
    """
    # create a zero minimum to compare against
    default = Program()
    default.randomize()
    best = ((0,0), 0, default)
    # create combinations of mating and muatation probabilities
    for i in range(int(combos**0.5)):
        keep = random.uniform(0.05, 0.5)
        for j in range(int(combos**0.5)):
            print('Combo #', i, '.', j)
            mut = random.uniform(0.01, 0.10)
            # find the highest performance under those conditions
            winner = GA(popsize, numgens, keep, mut, False)
            fitness = evaluateFitness(winner, TRIALS, STEPS)
            # keep it if it's the highest yet
            if fitness > best[1]:
                best = ((keep, mut), fitness, winner)
    return best


