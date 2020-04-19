data = open('input.txt').read().split('\n')


def scanner(input):
    twos = []
    threes = []
    barcodes = {}

    for barcode in input:
        barcodes[barcode] = {}
        letters_seen = barcodes[barcode]

        for letter in barcode:
            if letter not in letters_seen:
                letters_seen[letter] = 1
            else:
                letters_seen[letter] += 1

        for letter in letters_seen:
            # If a letter appears two times, count it in twos.
            # Only adds one time if there are two or more letters
            # that appears 2 times.
            if letters_seen[letter] == 2:
                if barcode not in twos:
                    twos.append(barcode)

            # If a letter appears three times, count it in threes.
            # Only adds one time if there are two or more letters
            # that appears 3 times.
            if letters_seen[letter] == 3:
                if barcode not in threes:
                    threes.append(barcode)

    return len(twos) * len(threes)


print(scanner(data[:-1]))
