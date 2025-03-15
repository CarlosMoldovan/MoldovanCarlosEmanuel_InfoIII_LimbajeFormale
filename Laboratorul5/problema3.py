import re

def gen_limbaj(er, lung):
    rez = set()
    for i in range(2 ** lung):
        sir = format(i, f'0{lung}b')
        if re.fullmatch(er, sir):
            rez.add(sir)
    return rez

er1 = r'(1|00*1)|(1|00*1)(0|10*1)*(0|10*1)'
er2 = r'0*1(0|10*1)*'
lung = 6
l1 = gen_limbaj(er1, lung)
l2 = gen_limbaj(er2, lung)
print(l1 == l2)
