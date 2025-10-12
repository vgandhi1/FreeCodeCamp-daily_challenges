"""
Battle of Words
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
"""

def battle(our_team, opponent):
    n_our_team = len(our_team.split())
    n_opponent = len(opponent.split())

    length_condition = n_our_team == n_opponent
    space_char_condition = (" " in our_team) & (" " in opponent) & (our_team.replace(" ", "a").isalpha()) & (opponent.replace(" ", "a").isalpha())


    battle_point = 0
    our_team_score = []
    opponent_score = []

    if space_char_condition & length_condition:
        for words in our_team.split():
            word_score = 0
            for char in words:
                if char.isupper():
                    value = ord(char) - ord("A") + 2
                elif char.islower():
                    value = ord(char) - ord("a") + 1
                else:
                    print("invalid character")
                word_score += value
            
            our_team_score.append(word_score)   

        for words in opponent.split():
            word_score = 0
            for char in words:
                if char.isupper():
                    value = ord(char) - ord("A") + 2
                elif char.islower():
                    value = ord(char) - ord("a") + 1
                else:
                    print("invalid character")
                word_score += value
            
            opponent_score.append(word_score)  

        for score_x, score_y in zip(our_team_score, opponent_score):
            
            if score_x >  score_y:
                battle_point += 1
            elif score_x <  score_y:
                battle_point -= 1
            elif score_x == score_y:
                battle_point += 0

        #return our_team_score, opponent_score

        if battle_point > 0:
            return "We win"
        if battle_point < 0:
            return "We lose"
        if battle_point == 0:
            return "Draw"
#battle("Cheeseburger with fries", "Cheeseburger with Fries")
#battle("Hello world", "hello world")


"""
tests
Passed: 1. battle("hello world", "hello word") should return "We win".
Passed: 2. battle("Hello world", "hello world") should return "We win".
Passed: 3. battle("lorem ipsum", "kitty ipsum") should return "We lose".
Passed: 4. battle("hello world", "world hello") should return "Draw".
Passed: 5. battle("git checkout", "git switch") should return "We win".
Passed: 6. battle("Cheeseburger with fries", "Cheeseburger with Fries") should return "We lose".
Passed: 7. battle("We must never surrender", "Our team must win") should return "Draw".
"""



