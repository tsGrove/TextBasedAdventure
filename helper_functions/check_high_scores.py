# This just reads the json file and returns the data if the user so wishes to see it
def check_high_scores():
    check_scores = input('Would you like to see your top 10 high scores?\n' '(Y)es or (N)o.\n').lower()
    if check_scores == "yes" or check_scores == 'y':
        high_scores = []
        with open("json_scores.json", 'r') as f:
            data = json.load(f)
            for adventurers in data['High Scores']:
                adventurer_info = list(adventurers.values())
                high_scores.append(adventurer_info)
            print(tabulate(high_scores, headers=['Name', 'Level Reached', 'Monsters Slain', 'Gold Earned'], tablefmt="pretty"))
    else:
        print('Gotcha, Hope you\'re brave enough to try again!')