users = []
with open('users.txt', encoding='utf-8') as file:
    for line in file:
        users.append(line.strip('\n'))

with open('sorted_users.txt', 'w', encoding='utf-8') as file:
    file.writelines([user + '\n' for user in sorted(users)])
