with open('text_num.txt', encoding='utf8') as file_input:
    lines = file_input.readlines()


with open('output_num.txt', mode='w', encoding='utf8') as file_output:
    for line in lines:
        if line.rstrip('\n').isdigit():
            file_output.write(line)
