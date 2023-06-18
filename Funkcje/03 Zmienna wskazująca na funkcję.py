

def BuyMe(what):
    print('Give me ', what)


BuyMe('a new car')


StealForMe = BuyMe
print(type(StealForMe))
StealForMe('a new car')


def GoLeft(*args):
    print('PLACEHOLDER - turning left with', *args)

def GoRight(*args):
    print('PLACEHOLDER - turning right with', *args)

def GoForward(*args):
    print('PLACEHOLDER - going forward with', *args)

def GoBack(*args):
    print('PLACEHOLDER - going back with', *args)

def Start(*args):
    print('PLACEHOLDER - starting with', *args)

def Stop(*args):
    print('PLACEHOLDER - stopping with', *args)

instruction = [Start, GoForward, GoForward, GoLeft, GoForward, GoRight, Stop]

dish = 'pizza'
for instr in instruction:
    instr(dish)
