import random


def main():
    with open('in.txt', 'r') as f:
        input_text = [list(s.split()) for s in f.readlines()]

    output_text = [[] for _ in range(len(input_text))]
    working_with_input = input_text

    # step 1: lines (cool example text -> example text cool)
    for i in range(len(working_with_input)):
        while len(working_with_input[i]) > 0:
            index = random.randint(0, len(working_with_input[i]) - 1)
            output_text[i].append(working_with_input[i][index])
            del working_with_input[i][index]

    # step 2: words (word -> wdor)
    working_with_input = output_text
    output_text = [[] for _ in range(len(working_with_input))]

    for i in range(len(working_with_input)):
        count = 0
        for j in range(len(working_with_input[i])):
            output_text[i].append('')
            count += 1
            helper = list(working_with_input[i][j])
            while len(helper) > 0:
                index = random.randint(0, len(helper) - 1)
                output_text[i][j] += helper[index]
                del helper[index]

    for el in output_text:
        el.append('\n')

    with open('out.txt', 'w') as f:
        string = ''
        for line in output_text:
            for word in line:
                string += f'{word} ' if word != '\n' else f'{word}'

        f.write(string)


if __name__ == '__main__':
    main()
