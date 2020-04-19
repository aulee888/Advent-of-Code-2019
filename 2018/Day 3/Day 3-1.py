data = open('input.txt').read().split('\n')


def parser(input):
    fabric = {}

    for claim in input:
        at_reached = False
        colon_reached = False
        comma_reached = False
        x_reached = False
        x_coor = ''
        y_coor = ''
        length = ''
        width = ''
        claim_number = ''

        for number in claim:
            if number in '1234567890' and not at_reached and not colon_reached:
                claim_number = claim_number + number

            elif number in '1234567890' and at_reached and not colon_reached:
                if not comma_reached:
                    x_coor = x_coor + number
                if comma_reached:
                    y_coor = y_coor + number

            elif number in '1234567890' and at_reached and colon_reached:
                if not x_reached:
                    length = length + number
                if x_reached:
                    width = width + number

            if number == '@':
                at_reached = True

            if number == ',':
                comma_reached = True

            if number == ':':
                colon_reached = True

            if number == 'x':
                x_reached = True

        claim_number = int(claim_number)
        x_coor = int(x_coor)
        y_coor = int(y_coor)
        length = int(length)
        width = int(width)

        for j in range(1, width + 1):
            for i in range(1, length + 1):

                if (x_coor + i, y_coor + j) not in fabric:
                    fabric[(x_coor + i, y_coor + j)] = [claim_number]
                else:
                    fabric[(x_coor + i, y_coor + j)].append(claim_number)

    return fabric


def overlap(fabric):
    count = 0
    for sq_in in fabric:
        if len(fabric[sq_in]) > 1:
            count += 1
    return count


fabric = parser(data[:-1])
print(overlap(fabric))


