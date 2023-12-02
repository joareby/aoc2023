with open('i2.txt') as f:
    maxes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    possible_games = []
    for line in map(str.strip, f):
        game, cube_samples = line.split(':')
        game = int(game.split(' ')[1])
        cube_samples = list(map(
            lambda x: list(map(
                lambda y: (
                    int(y.strip().split(' ')[0]),
                    y.strip().split(' ')[1]
                ),
                x.split(',')
            )),
            cube_samples.split(';')
        ))
        game_maxes = {}
        for cube_sample in cube_samples:
            for i, color in cube_sample:
                game_maxes[color] = max(game_maxes.get(color, 0), i)
        possible_game = True
        for color, i in game_maxes.items():
            if i > maxes[color]:
                possible_game = False
                break
        if possible_game:
            possible_games.append(game)
    print(sum(possible_games))
