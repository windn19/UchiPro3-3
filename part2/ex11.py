with open('text_num.txt', encoding='utf8') as file_input, \
        open('output_num.txt', mode='wb', encoding='utf8') as file_output:
    for line in file_input:
        if line.rstrip('\n').isdigit():
            # file_output.write(line)
            print(line, file=file_output, end='')
