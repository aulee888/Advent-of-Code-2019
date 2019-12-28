# Each amp gets their own copy of the program
# But the program doesn't restart when the amp runs again
# Therefore use a class
class Amp:
    def __init__(self, prog):
        self.prog = prog[:]
        self.ip = 0
        self.ip_counter = 1  # Changed to '1' to avoid using phases
        self.output = []
        self.position = [0, 0]
        self.direction = 0
        self.r_base = 0
        self.halt = False

def split(opcode: int) -> str:
    opcode = str(opcode)
    
    if len(opcode) < 5:
        for i in range(5 - len(opcode)):
            opcode = '0' + opcode
    return opcode[-2:], opcode[:-2]


def get_values(ip: int, r_base: int, prog: list, op: str, modes: str) -> list:
    values = []
    
    #print('R_Base : {}, R_Base + Address: {}'.format(r_base, r_base + prog[ip + 1]))

    if op in ['01', '02', '03' ,'04', '05', '06', '07', '08', '09']:
        if modes[-1] == '0':
            values.append(prog[prog[ip + 1]])
        elif modes[-1] == '1':
            values.append(prog[ip + 1])
        else:
            values.append(prog[r_base + prog[ip + 1]])

        if op in ['01', '02', '05', '06', '07', '08']:
            if modes[-2] == '0':
                values.append(prog[prog[ip + 2]])
            elif modes[-2] == '1':
                values.append(prog[ip + 2])
            else:
                values.append(prog[r_base + prog[ip + 2]])

        # Destination Value
        if op in ['01', '02', '03', '07', '08']:
            if modes[-3] == '0':
                values.append(prog[ip + 3])
            else:
                values.append(r_base + prog[ip + 3])
        
    return values

def run_comp(amp: Amp, phase: int, input: int) -> int:
    while amp.prog[amp.ip] != 99:

        #print('{} | {}, {}, {}, {}'.format(amp.ip, amp.prog[amp.ip], amp.prog[amp.ip + 1], amp.prog[amp.ip + 2], amp.prog[amp.ip + 3]))

        op, modes = split(amp.prog[amp.ip])
        values = get_values(amp.ip, amp.r_base, amp.prog, op, modes)
        
        # Increases the size of the program by appending zeros
        # The plus 1 at the end of the third line of this block is due to counting from 0
        # Address 1000 does not exist on a program of length 999, hence the plus 1
        # Values don't get writen in op = 4, 5, 6... but r_base accounted for in get_values func
        # Therfore there values[2] doesn't get used in them
        if op in ['01', '02', '03', '07', '08']:

            if values[-1] >= len(amp.prog):
                amp.prog = amp.prog + [0 for i in range(values[-1] - len(amp.prog) + 1)]
            
        if op == '01':  # Add
            amp.prog[values[2]] = values[0] + values[1]
            amp.ip += 4

        elif op == '02':  # Multiply
            amp.prog[values[2]] = values[0] * values[1]
            amp.ip += 4

        # Use values[1] instead of values[2] as dest b/c get_values func doesn't give op = 3 three values
        elif op == '03':  # Change to Input
            
            if amp.ip_counter == 0:
                amp.prog[values[1]] = phase
                amp.ip_counter += 1
            else:
                amp.prog[values[1]] = input

            amp.ip += 2

        elif op == '04':  # Output
            if len(amp.output) > 1:  # Reset after every two values appended
                amp.output = []

            amp.output.append(values[0])
            amp.ip += 2
            
            if len(amp.output) == 2:
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
                amp.prog[values[2]] = 1
            else:
                amp.prog[values[2]] = 0
            amp.ip += 4

        elif op == '08':  # Equals
            if values[0] == values[1]:
                amp.prog[values[2]] = 1
            else:
                amp.prog[values[2]] = 0
            amp.ip += 4
        
        elif op == '09':  # Adjust Relative Base
            amp.r_base += values[0]
            amp.ip += 2

    amp.halt = True
    #return amp.output


paint = Amp(prog1)
white_panels = {}
panels_painted = 0

while paint.halt is False:

    # Robot Processing
    if paint.position not in white_panels:
        run_comp(paint, 1, 0)
    else:
        run_comp(paint, 1, 1)

    try:
        # Painting
        if paint.output[0] == 1:
            white_panels[paint.position] = '#'

        # Turning
        if paint.output[1] == 0:
            paint.direction = (paint.direction - 90) % 360
        else:
            paint.direction = (paint.direction + 90) % 360

        # Move forward
        if paint.direction == 0:
            paint.position[1] += 1

        elif paint.direction == 90:
            paint.position[0] += 1

        elif paint.direction == 180:
            paint.position[1] -= 1

        elif paint.direction == 270:
            paint.position[0] -= 1

        panels_painted += 1

    except IndexError:  # For when robot halts, there is no output


    
