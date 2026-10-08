# Snake

A rattlesnake take on the classic Snake game, built with Python's `turtle` module.

Guide the snake around the board eating fruit. Every piece of fruit makes the snake one segment longer and adds a point to your score. Hit a wall or your own body and the round ends: the score resets and a new snake starts straight away.

## Features

- A rattlesnake with diamond-patterned scales, a flicking forked tongue and a rattle that shakes as it moves
- A random piece of fruit each time: apple, orange, banana, cherries, grapes, strawberry, lemon or watermelon
- A chomp sound effect each time the snake eats (Windows only)
- A high score that is saved between games

## Requirements

- Python 3 with Tkinter (included with the standard python.org installer)
- No third-party packages

## Running the game

From the project folder:

```
python main.py
```

## Controls

| Key | Action |
| --- | --- |
| ↑ ↓ ← → | Steer the snake |

Close the window to quit. If you beat the high score before closing, it is saved.

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Sets up the screen and runs the game loop, collision checks and controls |
| `snake.py` | The `Snake` class, plus the head, body and rattle shapes |
| `food.py` | The `Food` class and the fruit shapes |
| `scoreboard.py` | Displays the score and saves the high score |
| `sound.py` | Creates and plays the chomp sound |
| `chomp.wav` | The chomp sound (recreated by `sound.py` if deleted) |
| `high_score_log.txt` | The saved high score |

## Notes

- The sound uses `winsound`, which only exists on Windows. On macOS and Linux the game runs without sound.
- To reset the high score, set the contents of `high_score_log.txt` to `0`.
