import random

win_stats = [0,0,0]

for round in range(100):

    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    random.shuffle(xartia)

    # Play rigged turn for player 1
    player1 = []
    sum1 = 0
    while True:
        idx1 = int(random.random() * len(xartia))
        test1 = xartia[idx1]
        if (test1[0] in figures) or (int(test1[0]) == 10):
            xartia.remove(test1)
            player1.append(test1)
            break
        else:
            continue

    while sum1 < 16:
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1 = sum1 + 10
            else:
                sum1 = sum1 + card[0]

    if sum1 > 21:
        win_stats[1] += 1

    else:
        player2 = []
        sum2 = 0
        # Play rigged turn for player 2
        while True:
            idx2 = int(random.random() * len(xartia))
            test2 = xartia[idx2]
            if (test2 in figures) or (test2 == "10"):
                continue
            else:
                xartia.remove(test2)
                player2.append(test2)
                break

        while sum2 < 16:
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2 = sum2 + 10
                else:
                    sum2 = sum2 + card[0]

        if sum2 > 21:
            sum2 = 0

        if sum1 > sum2:
            win_stats[0] += 1
        elif sum2 > sum1:
            win_stats[1] += 1
        else:
            win_stats[2] += 1

print(win_stats)
