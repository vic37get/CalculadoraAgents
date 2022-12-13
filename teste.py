ex = "(2*3)+5-(4/2)-12^2+(5/5))"
def find_parens(s):
    toret = []
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret.append((pstack.pop(),i+1))

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret

print(find_parens(ex))