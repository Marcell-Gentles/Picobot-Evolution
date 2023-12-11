# Picobot-Evolution

#### Thanks to my collaborators Brock Bownds and Elizabeth Hernandez

---

This was our final project for [CS5](https://catalog.hmc.edu/preview_course_nopop.php?catoid=22&coid=7197) at Harvey Mudd college in the fall 2023 semester. It is a genetic algorithm for evolving [Picobot](https://www.cs.hmc.edu/picobot/), a virtual 'robot' created by the Mudd CS department. Picobot traverses a room of cells, which are either walls or empty space. Its goal is to cover every empty cell in the room. At any moment, Picobot is aware of its state, represented by an integer, and its surroundings, i.e. whether the cells to its immediate north, east, west, and south are walls or empty space. A Picobot program consists of a list of rules that instruct it to take a step north, east, west, or south, and then enter a new (or the same) state, based on its current state and surroundings.

Our class was first introduced to Picobot during the first week, when we were required to write Picobot programs that would successfully fully traverse certain rooms. For this project, we returned to Picobot with the task of creating a process for an initially random population of Picobot programs to evolve over several generations to become as successful as possible at covering a 23 X 23 square room. With some experimentation with biological variables, we were able to engineer a process that created a 100% successful process. A summary of our findings can be found within `final.md`. `final.py` contains our complete project. The rest of the files contain progress that we submitted along the way.

You can see the best program that we evolved in action by going to the [Picobot](https://www.cs.hmc.edu/picobot/) website and pasting this program into the 'Rules' field:

```
  0 xxxx -> W 0
  0 Nxxx -> S 2
  0 NExx -> S 0
  0 NxWx -> E 1
  0 xxxS -> E 1
  0 xExS -> W 2
  0 xxWS -> E 2
  0 xExx -> S 2
  0 xxWx -> S 2
  1 xxxx -> S 0
  1 Nxxx -> E 3
  1 NExx -> W 0
  1 NxWx -> E 2
  1 xxxS -> W 4
  1 xExS -> W 4
  1 xxWS -> E 4
  1 xExx -> S 3
  1 xxWx -> E 4
  2 xxxx -> N 3
  2 Nxxx -> W 0
  2 NExx -> W 4
  2 NxWx -> E 2
  2 xxxS -> N 2
  2 xExS -> N 2
  2 xxWS -> N 1
  2 xExx -> W 0
  2 xxWx -> E 4
  3 xxxx -> E 3
  3 Nxxx -> W 3
  3 NExx -> W 2
  3 NxWx -> S 3
  3 xxxS -> W 0
  3 xExS -> N 3
  3 xxWS -> N 4
  3 xExx -> N 3
  3 xxWx -> E 4
  4 xxxx -> E 4
  4 Nxxx -> E 1
  4 NExx -> W 1
  4 NxWx -> E 3
  4 xxxS -> W 0
  4 xExS -> N 2
  4 xxWS -> E 1
  4 xExx -> W 1
  4 xxWx -> S 2
```
