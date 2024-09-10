# Chess project for Education of M&M

![image](https://github.com/user-attachments/assets/3138483d-3501-4d73-b628-a639a68b48c3)

- Meant to run in cli, purely, without depending on external visual representations
- Technical details:
  - The CLI game should be based in python 3.11
  - Code should be primarily object-oriented (class and object representation of board states +...)
  - See "Gameplay Requirements" below for all required .
  - Should run without issues on any computer with python3.11 who runs:

```bash
pip install -r requirements.txt
python3.11 main.py
```

## Branch Rules:
All branches should fall under one of the following:
1) main - protected and requires pull request to update (+ review by maintainer [Ben])
2) test/[v+VERSION NUMBER] - e.g. test/v0.1 - unprotected, code should be mostly stable, lower priority branches should be merged to this branch.
3) dev/[FEATURE NAME] - e.g. dev/en-passant - unprotected, should be worked on by a single individual directly on a specific feature.
4) bugfix/[BUG DESCRIPTOR] - e.g. bugfix/stalemate-not-identified - unprotected, should be worked on by a single individual on a specific bug that has been identified.
5) refactor/[FILE OR FUNCTION NAME] - e.g. refactor/piece - unprotected, should be worked on by a single individual on a specific file or function that will be cleaned or optimized without affecting overall functionality.

## Gameplay Requirements
- The game should be interfaced exclusively in the CLI directly, without other visualization.
- The game should allow for initializing a new game with the standard starting board. See [Startup](https://en.wikipedia.org/wiki/Chess#Setup)
- All pieces should only be able to make legal moves, including captures; other moves should be rejected. See [Movement](https://en.wikipedia.org/wiki/Chess#Movement)
- The game should appropriately identify when a player is in check, and only allow legal moves from check. See [Check and Checkmate](https://en.wikipedia.org/wiki/Chess#Check_and_checkmate)
- The game should end when a player is either stalemated or checkmated. For checkmate, see Check and Checkmate above. For stalemate, see [Draw](https://en.wikipedia.org/wiki/Chess#Draw)
- Players should be able to dictate their move with algebraic notation - e.g. 'bxc6' implies that the pawn that was in the 'b' column has taken the pawn that was on the square 'c6' - see [Algebraic Notation (Chess)](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) for more details.
- At startup, the players should be able to define the amount of time they should each recieve for the game - e.g. 10 minutes implies that EACH PLAYER has 10 minutes total to make moves - or have the game untimed. If a player runs out of time, they should automatically be assigned a loss, and the option to continue the game untimed should be presented.
- When a pawn reaches the end of the board - e.g. white pawn reaching row 8 - the pawn should transform into a queen.
- The player should be allowed to castle when the rules allow. See [Castling](https://en.wikipedia.org/wiki/Chess#Castling).
- The complete game notation should be printed to the CLI when the game is over.

## How game will be tested:
1) A famous game will be taken from a known database - e.g. [Nakamura vs Niemann 2024](https://www.chessgames.com/perl/chessgame?gid=2767828).
2) The games moveset will be fed into the CLI in strict algebraic notation.
3) The board state after each move will be compared to the appropriate board state in the game.

Example notation for moveset from above game (White move __space__ Black move):
1. Nf3 d5
2. g3 Nf6
3. Bg2 e6
4. c4 Be7
5. O-O O-O
6. b3 b6
7. e3 Bb7
8. Qe2 Nbd7
9. Nc3 Ne4
10. Bb2 Nxc3
11. Bxc3 Nf6
12. d4 Ne4
13. Bb2 c5
14. dxc5 Bxc5
15. Rfd1 Qe7
16. cxd5 Bxd5
17. Ne5 Qb7
18. b4 Bxb4
19. Bxe4 Bxe4
20. Rd7 Qc8
21. Rd4 **1-0**
