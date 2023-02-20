text1 = 'Явное лучше, чем неявное.\n'
text2 = 'Простое лучше, чем сложное.\n'
text3 = 'Сложное лучше, чем запутанное.\n'


with open('output.txt', mode='a', encoding='utf8') as f:
    # f.write(text1)
    # f.write(text2)
    # f.write(text3)
    f.writelines([text1, text2, text3])
