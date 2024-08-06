# Checkers Rules
Some of these rules are variation from the standard rules of checkers.

## Robot Movements
- A pawn piece only moves foward, diagonally.
- A pawn piece can only move to an empty square that is adjacent to its current position.
- A queen piece can move foward and backward, diagonally.
- A queen piece can move to any empty square that is diagonal to its current position.
- A queen cannot jump over another piece of the same color.

### Priorities
1 - Capture.

1.1 - If there are multiple captures, the player must choose the one that captures the most pieces.

1.2 - If there are multiple captures that capture the same amount of pieces, the player must choose the one that captures the most queens.

2 - Movement that promotes a pawn to a queen.

3 - Movement that can generate a multiple capture in the next turn.

4 - Movement that does not put the piece in capture risk.

## Board Representation:
 0  1  2  3  4  5  6  7

 8  9 10 11 12 13 14 15

16 17 18 19 20 21 22 23

24 25 26 27 28 29 30 31

32 33 34 35 36 37 38 39

40 41 42 43 44 45 46 47

48 49 50 51 52 53 54 55

56 57 58 59 60 61 62 63
