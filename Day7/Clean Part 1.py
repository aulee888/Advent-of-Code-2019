from itertools import permutations

prog1 = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99]

prog2 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

prog3 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]

prog4 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

prog5 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

def split(opcode: int) -> str:
    opcode = str(opcode)
    
    if len(opcode) < 5:
        for i in range(5 - len(opcode)):
            opcode = '0' + opcode
    return opcode[-2:], opcode[:-2]


def get_values(ip: int, prog: list, op: str, modes: str) -> list:
    values = []
    
    if op in ['01', '02', '03' ,'04', '05', '06', '07', '08']:
        if modes[-1] == '0':
            values.append(prog[prog[ip + 1]])
        else:
            values.append(prog[ip + 1])

        if op in ['01', '02', '05', '06', '07', '08']:
            if modes[-2] == '0':
                values.append(prog[prog[ip + 2]])
            else:
                values.append(prog[ip + 2])

    return values

def run_comp(prog: list, phase: int, input: int) -> int:
    ip = 0
    ip_counter = 0

    while prog[ip] != 99:
        #print(ip)
        op, modes = split(prog[ip])
        values = get_values(ip, prog, op, modes)

        if op == '01':  # Add
            prog[prog[ip + 3]] = values[0] + values[1]
            ip += 4

        elif op == '02':  # Multiply
            prog[prog[ip + 3]] = values[0] * values[1]
            ip += 4

        elif op == '03':  # Change to Input
            if ip_counter == 0:
                prog[prog[ip + 1]] = phase
                ip_counter += 1
            else:
                prog[prog[ip + 1]] = input
            ip += 2

        elif op == '04':  # Output
            output = values[0]
            ip += 2
            
            #print(output)
        
        elif op == '05':  # Jump if True
            if values[0] != 0:
                ip = values[1]
            else:
                ip += 3

        elif op == '06':  # Jump if False
            if values[0] == 0:
                ip = values[1]
            else:
                ip += 3

        elif op == '07':  # Less than
            if values[0] < values[1]:
                prog[prog[ip + 3]] = 1
            else:
                prog[prog[ip + 3]] = 0
            ip += 4

        elif op == '08':  # Equals
            if values[0] == values[1]:
                prog[prog[ip + 3]] = 1
            else:
                prog[prog[ip + 3]] = 0
            ip += 4


    return output


# Answer to Part 1
max_signal = 0
for phases in permutations(range(5), 5):
    output = 0

    for phase in phases:
        output = run_comp(prog1, phase, output)

    if output > max_signal:
        max_signal = output

print(max_signal)

