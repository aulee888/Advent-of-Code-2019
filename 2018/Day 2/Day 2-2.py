data = open('input.txt').read().split('\n')


def scanner(input):
    n = len(input)
    word_len = len(input[0])

    for i in range(n):
        comparisons = 0
        early_breaks = 0

        for j in range(i, n):
            differences = 0
            matching = ''
            comparisons += 1

            for k in range(word_len):
                if input[i][k] != input[j][k]:
                    differences += 1
                else:
                    matching = matching + input[i][k]

                if differences > 1:
                    early_breaks += 1
                    break

            if differences == 1:
                print(f'Comparisons: {comparisons}')
                print(f'Early Breaks: {early_breaks}')
                # return [input[i], input[j]]
                return matching

    return 'No Answer'


print(scanner(data[:-1]))
