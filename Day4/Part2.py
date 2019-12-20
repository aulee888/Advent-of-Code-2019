input = '359282-820401'
input_range = input.split('-')
lower_bound = int(input_range[0])
upper_bound = int(input_range[1])

valid_combos = []

for i in range(lower_bound, upper_bound+1):
    digits = [int(digit) for digit in str(i)]
    if sorted(digits) == digits:

        # For each combo, count the number of times a digit is in the combo.
        # According to rules, the two occurences must be adjacent and always increase L -> R.
        # Therefore a number such as 123898 is not possible and number of occurrences should be
        # 2.
        # Doubles list for avoiding adding the adjacent digit into doubles list.
        # That way if there's only one set of adjacent digits can it be a valid combo.
        doubles = []
        for digit in digits:
            occurrences = digits.count(digit)
            if occurrences == 2 and digit not in doubles:  # Changed from >= to == from Part 1 to Part 2
                doubles.append(digit)
        
        if doubles != []:
            valid_combos.append(i)

# Answer to Part 2
print(len(valid_combos))
