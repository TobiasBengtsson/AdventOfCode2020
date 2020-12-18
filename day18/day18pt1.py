import sys

ans = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    nest_sums = [0]
    operator = ['']
    for c in line:
        if c == ' ':
            pass
        elif c == '(':
            nest_sums.append(0)
            operator.append('')
        elif c == ')':
            par_sum = nest_sums.pop()
            operator.pop()
            op = operator[len(nest_sums) - 1]
            if op == '':
                nest_sums[-1] = int(par_sum)
            if op == '+':
                nest_sums[-1] += int(par_sum)
            elif op == '*':
                nest_sums[-1] *= int(par_sum)
        elif c in ('+', '*'):
            operator[-1] = c
        else:
            op = operator[len(nest_sums) - 1]
            if op == '':
                nest_sums[-1] = int(c)
            if op == '+':
                nest_sums[-1] += int(c)
            elif op == '*':
                nest_sums[-1] *= int(c)
    print(nest_sums[0])
    ans += nest_sums[0]

print(ans)
