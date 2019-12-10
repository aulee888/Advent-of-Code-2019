from itertools import permutations

# Test Case 1
setting1 = [4,3,2,1,0]
code1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

# Test Case 2
setting2 = [0,1,2,3,4]
code2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]

# Test Case 3
setting3 = [1,0,4,3,2]
code3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

# Test Case 4
setting4 = [9,8,7,6,5]
code4 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

# Actual Data
code = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99]

def parameterize(opcode, code, i):
    instruction = opcode[:-2]

    # If necessary, add 0's to omitted 0's in opcode
    # i.e 102 -> 00102
    if len(instruction) < 3:
        for j in range(3 - len(instruction)):
            instruction = '0' + instruction

    #print(instruction)

    # Reading the parameter modes from right to left
    # Determines if parameter 1 is postion/immediate mode
    if instruction[-1] == '0':
        value1 = code[code[i+1]]
        #print('P1: Position -> {}'.format(value1))
    elif instruction[-1] == '1':
        value1 = code[i+1]
        #print('P1: Immediate -> {}'.format(value1))

    # Determnines mode of parameter 2
    if instruction[-2] == '0':
        if opcode[-1] == '4':  # Bypass a non-existent second parameter for opcode 4.
            value2 = 0
        else:
            value2 = code[code[i+2]]
            #print('P2: Position -> {}'.format(value2))
    elif instruction[-2] == '1':
        if opcode[-1] == '4':  # Bypass a non-existent second parameter for opcode 4.
            value2 = 0
        else:
            value2 = code[i+2]
            #print('P2: Immediate -> {}'.format(value2))

    # Parameter 3 should always be 0... will never write in immediate

    return value1, value2

def intcode(code, phase, input):
    i = 0
    input_counter = 0

    while True:
        operation = str(code[i])

        if operation[-2:] in ['01', '1']:  # Include both 01 and 1 to encompass both 1001 and 1 as opcodes
            #print('{} | {}, {}, {}, {}'.format(i, code[i], code[i+1], code[i+2], code[i+3]))
            temp = code[code[i+3]]
            m, n = parameterize(operation, code, i)
            added_value = m + n
            code[code[i+3]] = added_value
            #print('Target Index: {}, {} -> {}'.format(code[i+3], temp, code[code[i+3]]))
            i += 4

        elif operation[-2:] in ['02', '2']:  # Same as above
            #print('{} | {}, {}, {}, {}'.format(i, code[i], code[i+1], code[i+2], code[i+3]))
            temp = code[code[i+3]]
            m, n = parameterize(operation, code, i)
            mult_value = m * n
            code[code[i+3]] = mult_value
            #print('Target Index: {}, {} -> {}'.format(code[i+3], temp, code[code[i+3]]))
            i += 4

        # Only change to to this func is input_counter to account for when to use phase or input
        elif operation == '3':  
            #print('{} | {}, {}'.format(i, code[i], code[i+1]))
            temp = code[code[i+1]]
            if input_counter == 0:
                code[code[i+1]] = phase
                input_counter += 1
            else:
                code[code[i+1]] = input
                input_counter -= 1
            #print('Target Index: {}, {} -> {}'.format(code[i+1], temp, code[code[i+1]]))
            i += 2

        elif operation[-2:] in ['04', '4']:
            #print('{} | {}, {}'.format(i, code[i], code[i+1]))
            m = parameterize(operation, code, i)[0]
            dg = m
            #print('Output: {}'.format(m))
            i += 2 
            return m
        
        # 5 & 6 increase the instruction pointer (i) by 3 because only has three values in instruction i.e. (5, 1 ,2)
        elif operation[-2:] in ['05', '5']:
            #print('{} | {}, {}, {}'.format(i, code[i], code[i+1], code[i+2]))
            m, n = parameterize(operation, code, i)
            if m != 0:
                i = n
                #print('i : {}'.format(n))
            else:
                i += 3
            
        elif operation[-2:] in ['06', '6']:
            #print('{} | {}, {}, {}'.format(i, code[i], code[i+1], code[i+2]))
            m, n = parameterize(operation, code, i)
            if m == 0:
                i = n
                #print('i : {}'.format(n))
            else:
                i += 3
        
        elif operation[-2:] in ['07', '7']:
            #print('{} | {}, {}, {}, {}'.format(i, code[i], code[i+1], code[i+2], code[i+3]))
            temp = code[code[i+3]]
            m, n = parameterize(operation, code, i)
            if m < n:
                code[code[i+3]] = 1
            else:
                code[code[i+3]] = 0
                
            #print('Target Index: {}, {} -> {}'.format(code[i+3], temp, code[code[i+3]]))    
            i += 4
            
        elif operation[-2:] in ['08', '8']:
            #print('{} | {}, {}, {}, {}'.format(i, code[i], code[i+1], code[i+2], code[i+3]))
            temp = code[code[i+3]]
            m, n = parameterize(operation, code, i)
            if m == n:
                code[code[i+3]] = 1
            else:
                code[code[i+3]] = 0
                
            #print('Target Index: {}, {} -> {}'.format(code[i+3], temp, code[code[i+3]]))
            i += 4
        
        elif operation == '99':
            break

        #print('')

def signal(code):
    max_thrust = 0

    for phases in permutations(range(5), 5):
        output = 0

        for phase in phases:
            #print('Iteration: {}'.format(phase))
            #print('-'*15)
            copy_code = code[:]
            output = intcode(copy_code, phase, output)

            #print('')

        if output > max_thrust:
            max_thrust = output

    return max_thrust

def signal_fb(code, test=None):
    max_thrust = 0
    output = 0

    if test == None:

        for phases in permutations(range(5,10), 5):
            
            for phase in phases:
                #print('Iteration: {}'.format(phase))
                #print('-'*15)
                output = intcode(code, phase, output)

                #print('')

            if output > max_thrust:
                max_thrust = output

    else:
        for phase in phases:
            output = intcode(code, phase, output)

        if output > max_thrust:
            max_thrust = output

    return max_thrust

# Answer to Part 1
print(signal(code))
