data = open('input.txt').read().split('\n')


def frequency2(input):
    results = {0: '*'}
    curr_freq = 0

    iteration = 0
    while True:
        # print(iteration)  # For debugging

        for reading in input:
            if reading[0] == '+':
                curr_freq += int(reading[1:])
            elif reading[0] == '-':
                curr_freq -= int(reading[1:])
            elif reading == '0':
                print(f'A zero was encountered')
            else:
                print(f'Anomaly occured: {reading}')

            if curr_freq in results:
                return curr_freq
            else:
                results[curr_freq] = '*'

        iteration += 1


# Last item in input.txt is a blank b/c split on \n.
print(frequency2(data[:-1]))