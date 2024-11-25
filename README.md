# Advent of Code 2021
To practice for 2024 and to try out Colab

I will put the test input in-line and my input in a file which is wiped after the session ends and so complies with the request not to post your individual input

After day for, I want a real debugger and will start posting .py files

## [Day 5: Hydrothermal Venture](day05.py)
Used a brute force approach, but it still finished right away

## [Day 6: Lanternfish](day06.py)
Part one can be finished by tracking individual fish, but part two needs a different approach to compute and seems to be the first part two to need this for 2021

## [Day 7: The Treachery of Whales](day07.py)
Temped to time a run with a more brute-force part 2 to see how long it would take, but this is just a warm up for 2024 at the moment

## [Day 8: Seven Segment Search](day08.py)
Took a bit of code, but pretty straight forward

## [Day 9: Smoke Basin](day09.py)
Had to reread to see it is only the product of the top three in part 2, but otherwise not bad

## [Day 10: Syntax Scoring](day10.py)
The hardest part here was correctly reading the scoring protocol of part 2

## [Day 11: Dumbo Octopus](day11.py)
A matrix manipulation puzzle. Both parts are straight forward with part 1 taking some code, but part 2 is a quick extension

## [Day 12: Passage Pathing](day12.py)
First puzzle with three test inputs and the first network/graph puzzle and the first where part two runs for more than a second. Used NetworkX, but just for an easy way to get neighbors in the graph

## [Day 13: Transparent Origami](day13.py)
I decided to move to using NumPy after a brief start and had to relearn its slicing. Then I assumed folding in perfect halves, which is true for the example, but not the input. Then np.pad() is a little hard to use and VS Code had a bug (feature?) to always wrap the output at 74 chars, so needed to clean up the output. Took a bit of time for part 2 (mostly modifications to the fold function), but not super difficult

## [Day 14: Extended Polymerization](day14.py)
Part one can be done in a brute force, tracking way. Part two needed a change to tracking just the counts of pairs until the number of iterations are done and then changing that back into the number of letters. It took me a good bit of time to figure this out and I left in most of my tries to get there in the final code (with some parts that were annoying to wait through commented out)

## [Day 15: Chiton](day15.py)
Got some practice with both NetworkX and NumPy
