with open('users.txt', encoding='utf8') as f, open('sorted_users.txt', mode='w', encoding='utf8') as out:
    lines = sorted(f.readlines())
    out.writelines(lines)
