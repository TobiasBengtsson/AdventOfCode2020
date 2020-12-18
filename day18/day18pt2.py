import sys

class Expression:
    def __init__(self, expression):
        self.sub_expressions = []
        par_level = 0
        par_expression = ''
        self.expression = ''
        for c in expression:
            if c == ' ':
                pass
            elif c == '(':
                par_level += 1
                if par_level == 1:
                    self.expression += 'X'
                else:
                    par_expression += c
            elif c == ')':
                par_level -= 1
                if par_level == 0:
                    self.sub_expressions.append(Expression(par_expression))
                    par_expression = ''
                else:
                    par_expression += c
            elif par_level > 0:
                par_expression += c
            else:
                self.expression += c

        mod_expr = ''
        sum_paran = False
        for i, c in enumerate(self.expression):
            if len(self.expression) > i + 1 and self.expression[i+1] == '+' and not sum_paran:
                mod_expr += '('
                mod_expr += c
                sum_paran = True
            elif len(self.expression) > i + 1 and self.expression[i+1] == '*' and sum_paran:
                mod_expr += c
                mod_expr += ')'
                sum_paran = False
            else:
                mod_expr += c
            
        if sum_paran:
            sum_paran = False
            mod_expr += ')'
        self.expression = mod_expr

    def eval(self):
        sub_expression_i = 0
        nest_sums = [0]
        operator = ['']
        for c in self.expression:
            if c == '(':
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
                if c == 'X':
                    c = self.sub_expressions[sub_expression_i].eval()
                    sub_expression_i += 1
                op = operator[len(nest_sums) - 1]
                if op == '':
                    nest_sums[-1] = int(c)
                if op == '+':
                    nest_sums[-1] += int(c)
                elif op == '*':
                    nest_sums[-1] *= int(c)
        return nest_sums[0]

    def print(self):
        p = ''
        sub_expression_i = 0
        for c in self.expression:
            if c == 'X':
                p += '('
                p += self.sub_expressions[sub_expression_i].print()
                p += ')'
                sub_expression_i += 1
            else:
                p += c
        return p
ans = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    exp = Expression(line)
    ans += exp.eval()

print(ans)
