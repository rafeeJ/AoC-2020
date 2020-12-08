# Going to comment this one because I actually really enjoyed todays challenge.

# Open the file, and create the 'program' which is just an array of commands. 
f = open('input.txt', 'r')
program = [i.strip() for i in f]

def read_line(line):
    """
    Function to process a command

    Returns: Tuple containing (command, associated int)

    Eg: ('acc', 29) or ('jmp', -10)
    """
    line_list = line.split(' ')
    command = line_list[0]
    num = line_list[1]
    return command, int(num)

def run_program(prog):
    """
    Function to run a given program (Array of commands)
    
    This function tracks the accumulator (acc) value, as well as
    program counter (pc) and commands executed (visited). 
    It also spits out whether the program terminated
    properly of just went into a loop (finished).

    Returns: Tuple containing (finished boolean, final acc value)

    Eg: (True, 733)
    """
    # Initialise all the variables
    acc = 0
    pc = 0
    visited = []
    finished = False
    # Loop indefininetly
    while True:
        #print('Now running command on line {}'.format(pc))
        # Check if this command has been visited (pc lookup)
        if pc in visited:
            break
        # Check if this command is within scope, if not we have finished.
        if pc >= len(prog):
            finished = True
            break
        # Otherwise, we are at a new command, log it. 
        else: visited.append(pc)
        
        # Read the line and get the command and associated int.
        cmd, num = read_line(prog[pc])
        # If acc command, increment accumulator. 
        if cmd == 'acc': 
            acc += num
            pc += 1
        # If jmp command, increment program counter.
        if cmd == 'jmp': pc += num
        # Else, just go to next command
        if cmd == 'nop': pc += 1
    return finished, acc

print('Part one solution: {}'.format(run_program(program)))

def get_indexes(prog):
    """
    Helper function that returns all of the jmp and nop commands, with indexes.

    Returns: dict containing {index: command} for all occurrences in prog.
    """
    # 'Nice' one-liner that iterates through prog, reads each line and stores if it's jmp or nop command.
    return {idx:val for idx,val in enumerate(prog) if read_line(val)[0] in ['jmp','nop']}

def swap(cmd):
    """
    Helper function that swaps the commands

    Returns: inverse of cmd
    """
    # Probably could have done this in one line, but hey-ho. 
    if cmd[0] == 'nop': return 'jmp {}'.format(cmd[1])
    if cmd[0] == 'jmp': return 'nop {}'.format(cmd[1])

def brute_force_baybee(prog, indexes):
    """
    Function that returns dict of swapped command and program output tuple.

    Returns: Dict containing {command_index: (finished boolean, final acc value)}
    """
    l = {}
    # For all of the jmp and nop commands in prog...
    for k,v in indexes.items():
        # Create a clean copy of prog...
        prog_copy = list(prog)
        # Change the command at the correct index...
        prog_copy[k] = swap(read_line(v))
        # Create an entry in l with program output...
        l[k] = run_program(prog_copy)
    # Return dict containing all completed programs!
    return {k:v for k,v in l.items() if v[0]==True}
        
print('Part two solution: {}'.format(brute_force_baybee(program, get_indexes(program))))