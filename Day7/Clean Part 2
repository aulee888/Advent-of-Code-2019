from itertools import permutations

prog1 = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99]

prog2 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

prog3 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]

prog4 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

prog5 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

prog6 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

# Each amp gets their own copy of the program
# But the program doesn't restart when the amp runs again
# Therefore use a class
class Amp:
    def __init__(self, prog):
        self.prog = prog[:]
        self.ip = 0
        self.ip_counter = 0
        self.output = 0
        self.halt = False

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

def run_comp(amp: Amp, phase: int, input: int) -> int:
    while amp.prog[amp.ip] != 99:

        op, modes = split(amp.prog[amp.ip])
        values = get_values(amp.ip, amp.prog, op, modes)

        if op == '01':  # Add
            amp.prog[amp.prog[amp.ip + 3]] = values[0] + values[1]
            amp.ip += 4

        elif op == '02':  # Multiply
            amp.prog[amp.prog[amp.ip + 3]] = values[0] * values[1]
            amp.ip += 4

        elif op == '03':  # Change to Input
            if amp.ip_counter == 0:
                amp.prog[amp.prog[amp.ip + 1]] = phase
                amp.ip_counter += 1
            else:
                amp.prog[amp.prog[amp.ip + 1]] = input
            amp.ip += 2

        elif op == '04':  # Output
            amp.output = values[0]
            amp.ip += 2
            
            return amp.output
        
        elif op == '05':  # Jump if True
            if values[0] != 0:
                amp.ip = values[1]
            else:
                amp.ip += 3

        elif op == '06':  # Jump if False
            if values[0] == 0:
                amp.ip = values[1]
            else:
                amp.ip += 3

        elif op == '07':  # Less than
            if values[0] < values[1]:
                amp.prog[amp.prog[amp.ip + 3]] = 1
            else:
                amp.prog[amp.prog[amp.ip + 3]] = 0
            amp.ip += 4

        elif op == '08':  # Equals
            if values[0] == values[1]:
                amp.prog[amp.prog[amp.ip + 3]] = 1
            else:
                amp.prog[amp.prog[amp.ip + 3]] = 0
            amp.ip += 4

    amp.halt = True
    return amp.output

# Testing Part 1 using a class
'''
# Answer to Part 1 
max_signal = 0
test = Amp(prog1)

for phases in permutations(range(5), 5):
    test.output = 0

    for phase in phases:
        test.ip = 0
        test.ip_counter = 0
        test.prog = prog1[:]

        test.output = run_comp(test, phase, test.output)
        #print(test.output)
        #print(max_signal)

    if test.output > max_signal:
        max_signal = test.output

print(max_signal)
'''

max_signal = 0
for phases in permutations(range(5, 10), 5):
    amp_list = [Amp(prog1) for i in range(5)]
    curr = 0

    while amp_list[-1].halt is False:
        amp_list[curr].output = run_comp(amp_list[curr], phases[curr], amp_list[curr - 1].output)
        curr = (curr + 1) % 5

    if amp_list[-1].output > max_signal:
        max_signal = amp_list[-1].output

print(max_signal)
