






# def fix_power_sign(equation):
#     return equation.replace("^", "**")
#
# def eval_polynomial(equation, x_value):
#     fixed_equation = fix_power_sign(equation.strip())
#     parts = fixed_equation.split("+")
#     x_str_value = str(x_value)
#     parts_with_values = (part.replace("x", x_str_value) for part in parts )
#     partial_values = (eval(part) for part in parts_with_values)
#     return sum(partial_values)


def f1(lst,exp):
    #x=lst[0]
    s=eval(exp,{'x':int(lst[0])})
    return s==int(lst[1])
#     xs = [ x.strip().replace('^','**') for x in exp.split('+') ]
#     return sum( [eval(n.replace('x', lst[0])) for n in xs] )==int(lst[1])

lst=input().split(' ')
exp = input()

print(f1(lst,exp))
'''
1 4
x**3+x**2+x+1
'''

