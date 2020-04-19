data = open('input.txt').read().split('\n')


def frequency(input):
    result = 0

    for reading in input:
        if reading[0] == '+':
            result += int(reading[1:])
        elif reading[0] == '-':
            result -= int(reading[1:])
        elif reading == '0':
            print(f'A zero was encountered')
        else:
            print(f'Anomaly occured: {reading}')

    return result


# Last item in input.txt is a blank b/c split on \n.
print(frequency(data[:-1]))
