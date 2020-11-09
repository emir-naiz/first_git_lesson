file1 = open('players.txt', 'w')
for i in range(6):
    player = input("Введите имя нового игрока за столом: ")
    file1.write(player + '\n')
file1.close()
file2 = open('players.txt')
players_list = file2.readlines()
cards = []
for i in range(6):
    cost = int(input(f'Введите сумму карт игрока {players_list[i]}: '))
    cards.append(cost)
print(cards)
i = 0
while i < len(cards):
    if cards[i] > 21:
        cards[i] = 0
    i = i + 1
max_cost = max(cards)
max_index = cards.index(max_cost)
winner = players_list[max_index]
print(f'Встречайте победителя! {winner}')

