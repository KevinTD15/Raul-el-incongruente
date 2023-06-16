import sympy

class logic:
    def __init__(self, var : str, val : int) -> None:
        self.var = var
        self.val = val
    
def encode(logic_formula, primes):
    mark = []
    encoded = {}
    index = 0
    for i in logic_formula:
        for j in i:
            if(j.var not in mark):
                encoded[j.var] = primes[index]
                index += 1
                mark.append(j.var)
    return encoded

def solve(encoded, logic_formula, mul):
    solutions = simultaneous_congruences(encoded, logic_formula)
    inc = []
    for i in solutions:
        inc.append((i, mul))
    return simultaneous_incongruences(inc)

def simultaneous_congruences(encoded, logic_formula):
    solutions = []
    for i in logic_formula:
        b = []
        n = []
        for j in i:
            b.append(j.val)
            n.append(encoded[j.var])
        solutions.append(chinese_reminder_theorem(b, n))
    return solutions

def chinese_reminder_theorem(a, m):
    M = 1
    for mi in m:
        M *= mi
    
    Mi = [M // mi for mi in m]
    
    mult_inverse = [pow(Mi[i], -1, m[i]) for i in range(len(m))]
    
    x = sum(a[i] * Mi[i] * mult_inverse[i] for i in range(len(m))) % M
    
    return x

def simultaneous_incongruences(inc):
    flag = True
    for i in range(10000000000):
        for j in inc:
            if((i - j[0]) % j[1] == 0):
                flag = True
                break
            else:
                flag = False
        if(not flag):
            return i
    return 'No hay valor'

def main():
    x = logic('x', 0)
    nx = logic('x', 1)
    y = logic('y', 0)
    ny = logic('y', 1)
    z = logic('z', 0)
    nz = logic('z', 1)
    logic_formula = [[nx, ny, nz], [nx, y, z], [x, y, nz]]

    primes = list(sympy.primerange(0, 1000))
    
    enc = encode(logic_formula, primes)
    n = 1
    for i in enc:
        n *= enc[i]
    
    res = solve(enc, logic_formula, n)
    print(res)
    if(type(res) == int):
        print(True)
    else:
        print(False)
    
main()