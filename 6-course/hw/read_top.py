def read_top():
    with open('testtop.txt') as f:
        total_games = 0
        max_score = 0
        top_user = ''
        for line in f:
            total_games += 1
            user, score = line.split(':')
            int_score = int(score)
            if int_score > max_score:
                max_score = int_score
                top_user = user
    return f'Лучший результат у игрока {top_user} со счетом {max_score}\n' \
           f'Всего игр - {total_games}'


print(read_top())
