# CS5-Picobot-Evolution

#### Thanks to my collaborators Brock Bownds and Elizabeth Hernandez

---

This was our final project for [CS5](https://catalog.hmc.edu/preview_course_nopop.php?catoid=22&coid=7197) at Harvey Mudd college in the fall 2023 semester. It is a genetic algorithm for evolving [Picobot](https://www.cs.hmc.edu/picobot/), a virtual 'robot' created by the Mudd CS department. Picobot traverses a room of cells, which are either walls or empty space. Its goal is to cover every empty cell in the room. At any moment, Picobot is aware of its state, represented by an integer, and its surroundings, i.e. whether the cells to its immediate north, east, west, and south are walls or empty space. A picobot program consists of a list of rules that instruct it to take a step north, east, west, or south, and then enter a new (or the same) state, based on its current state and surroundings.

Our class was first introduced to Picobot during the first week, when we were required to write Picobot programs that would successfully fully traverse certain rooms. For this project, we returned to Picobot with the task of creating a process for an intially random population of Picobot programs to evolve over several generations to become as successful as possible at covering a 23 X 23 square room. With some experimentation with biological variables, we were able to engineer a process that created a 100% successful process. A summary of our findings can be found within `final.txt`. `final.py` contains our complete project. The rest of the files contain progress that we submitted along the way.
