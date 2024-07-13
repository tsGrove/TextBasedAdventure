def game_over(player):

    addition_to_high_score = {
        "name": str(player.name),
        "level reached" : int(player.level),
        "monsters slain" : int(player.monsters_slain),
        "gold earned" : int(player.gold)
                 }

    if player.monsters_slain <= 1:
        print('Cmon you can definitely do better than ONE or ZERO monsters...right?\n'
              f'The mighty {player.name} slayed a whopping {player.monsters_slain} monsters, wow! \n'
              f'Better luck next time!')

    else:
        print(f'It was a good run {player.name}, but eventually you fell. \n'
              f'You slayed {player.monsters_slain} monsters, had {player.gold} gold, and reached level {player.level}!\n')

    with open("./functionality/json_scores.json", "r+") as file:
        file_data = json.load(file)
        file_data["High Scores"].append(addition_to_high_score)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    check_high_scores()
    input()