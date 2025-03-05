from collections import defaultdict

def epsilon(state, tranzitii):
    stack = [state]
    closure = set(stack)
    
    while stack:
        current = stack.pop()
        if (current, "ε") in tranzitii:
            for next_state in tranzitii[(current, "ε")]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
    
    return closure

def nfa(start, final, tranzitii, word):
    current_states = epsilon(start, tranzitii)
    
    for symbol in word:
        next = set()
        for state in current_states:
            if (state, symbol) in tranzitii:
                for next_i in tranzitii[(state, symbol)]:
                    next.update(epsilon(next_i, tranzitii))
        current_states = next
    
    return any(state in final for state in current_states)
 
tranzitii = defaultdict(list, {
    ("q0", "a"): ["q1"],
    ("q1", "a"): ["q1"],
    ("q1", "ε"): ["q2"],
    ("q2", "b"): ["q3"],
    ("q2", "a"): ["q3"],
    ("q3", "ε"): ["q4"],
    ("q4", "b"): ["q4"]
})

start = "q0"
final = {"q4"}

while True:
    word = input("Introduceti un cuvant (sau 'exit' pentru a iesi): ")
    if word.lower() == 'exit':
        break
    result = nfa(start, final, tranzitii, word)
    if result:
        print(f'Cuvantul "{word}" este ACCEPTAT.')
    else:
        print(f'Cuvantul "{word}" NU este acceptat.')
