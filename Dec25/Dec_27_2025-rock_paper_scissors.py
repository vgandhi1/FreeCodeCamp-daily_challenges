"""
Rock, Paper, Scissors
Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

The input strings will always be "Rock", "Paper", or "Scissors".
"Rock" beats "Scissors".
"Paper" beats "Rock".
"Scissors" beats "Paper".
Return:

"Player 1 wins" if Player 1 wins.
"Player 2 wins" if Player 2 wins.
"Tie" if both players choose the same option.
"""
def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return "Tie"
    if player2 == "Scissors" and player1 == "Paper":
        return "Player 2 wins"
    if player2 == "Rock" and player1 == "Scissors":
        return "Player 2 wins"
    if player2 == "Paper" and player1 == "Rock":
        return "Player 2 wins"

    
    return "Player 1 wins"

print(rock_paper_scissors("Rock", "Rock"))

"""
Tests

Passed: 1. rock_paper_scissors("Rock", "Rock") should return "Tie".
Passed: 2. rock_paper_scissors("Rock", "Paper") should return "Player 2 wins".
Passed: 3. rock_paper_scissors("Scissors", "Paper") should return "Player 1 wins".
Passed: 4. rock_paper_scissors("Rock", "Scissors") should return "Player 1 wins".
Passed: 5. rock_paper_scissors("Scissors", "Scissors") should return "Tie".
Passed: 6. rock_paper_scissors("Scissors", "Rock") should return "Player 2 wins".
"""
