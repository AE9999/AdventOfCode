import sys, re

class Execution():
    def __init__(self, lines):
        self.before = [int(d) for d in re.findall(r'-?\d+', lines[0])]
        self.instruction = [int(d) for d in re.findall(r'-?\d+', lines[1])]
        self.after = [int(d) for d in re.findall(r'-?\d+', lines[2])]
    pass

    def __str__(self):
        return ("(Execution before:%s, instruction:%s after:%s)" % (str(self.before), str(self.instruction), str(self.after)))
    pass
pass

def addr(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]] + registers[instructions[2]]
    return n
pass

def addi(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]] + instructions[2]
    return n
pass

def mulr(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]] * registers[instructions[2]]
    return n
pass

def muli(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]] * instructions[2]
    return n
pass

def banr(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]] & registers[instructions[2]]
    return n
pass

def bani(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]] & instructions[2]
    return n
pass

def borr(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]] | registers[instructions[2]]
    return n
pass

def bori(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]] | instructions[2]
    return n
pass

def setr(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = registers[instructions[1]]
    return n
pass

def seti(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = instructions[1]
    return n
pass

def gtir(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = 1 if instructions[1] > registers[instructions[2]] else 0
    return n
pass

def gtri(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = 1 if registers[instructions[1]] > instructions[2] else 0
    return n
pass

def gtrr(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = 1 if registers[instructions[1]] > registers[instructions[2]] else 0
    return n
pass

def eqir(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = 1 if instructions[1] == registers[instructions[2]] else 0
    return n
pass

def eqri(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = 1 if registers[instructions[1]] == instructions[2] else 0
    return n
pass

def eqrr(registers, instructions):
    n = [r for r in registers]
    n[instructions[3]] = 1 if registers[instructions[1]] == registers[instructions[2]] else 0
    return n
pass

myInput = open('input.dat')
lines = list(map(lambda x: x.rstrip(), myInput.readlines()))
executions = [ Execution(lines[i:i+4])  for i in range(0, len(lines), 4)]
instructions = [ addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr ]

print(len(list(filter(lambda execution:
            sum([ 1 if i(execution.before, execution.instruction) == execution.after else 0 for i in instructions ]) >= 3,
      executions)))) #  Sollution 1

opcodes2possibilities = dict([(i, set(instructions)) for i in range(16)])
opcodes2instructions = dict()
instructions2opcodes = dict()

for execution in executions:
    candidates = opcodes2possibilities[execution.instruction[0]]
    candidates = candidates - set(filter(lambda i: i(execution.before, execution.instruction) != execution.after,
                                         instructions))
    opcodes2possibilities[execution.instruction[0]] = candidates
pass

while len(opcodes2possibilities.keys()) > 0:
    opcodes = list(filter(lambda x: len(opcodes2possibilities[x]) == 1, opcodes2possibilities))
    instructions = []
    for opcode in opcodes:
        instruction = list(opcodes2possibilities[opcode])[0]
        if instruction in instructions2opcodes.keys(): raise Exception('double instruction')
        if opcode in opcodes2instructions.keys(): raise Exception('double opcode')
        opcodes2instructions[opcode] = instruction
        instructions2opcodes[instruction] = opcode
        instructions.append(instruction)
        del opcodes2possibilities[opcode]
    pass

    for key in opcodes2possibilities.keys():
        candidates = opcodes2possibilities[key]
        opcodes2possibilities[key] = candidates - set(instructions)
    pass
pass

registers = [0,0,0,0]  # As claimed by program
commands =  list(map(lambda x: x.split(' '),
                     map(lambda x: x.rstrip(), open('input-program.dat').readlines() )))
for command in commands:
    command = list(map(int, command))
    registers = opcodes2instructions[command[0]](registers, command)
pass
print ("Final state %s .." % str(registers))
