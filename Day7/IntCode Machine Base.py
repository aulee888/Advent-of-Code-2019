prog1 = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99]

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

def run_comp(prog: list, input: int) -> int:
    ip = 0

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
            prog[prog[ip + 1]] = input
            ip += 2

        elif op == '04':  # Output
            output = values[0]
            ip += 2
            
            print(output)
        
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

print(run_comp(prog1, 5))
