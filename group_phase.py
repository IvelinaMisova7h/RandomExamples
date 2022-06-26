team_name = input()
games = int(input())
score = 0

all_goals = 0
all_goals_recieved = 0

for game in range(1, games + 1):
    goals = int(input())
    goals_recieved = int(input())

    all_goals += goals
    all_goals_recieved += goals_recieved

    if goals > goals_recieved:
        score += 3
    elif goals == goals_recieved:
        score += 1

diff = all_goals - all_goals_recieved
if all_goals >= all_goals_recieved:
    print(f"{team_name} has finished the group phase with {score} points.")
    print(f"Goal difference: {diff}.")
else:
    print(f"{team_name} has been eliminated from the group phase.")
    print(f"Goal difference: {diff}.")
