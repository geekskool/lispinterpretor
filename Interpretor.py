import math
import operator as op
from Parser import parser

env = {'+':op.add, '-':op.sub, '*':op.mul, '/':op.floordiv, '%':op.mod,
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '==':op.eq, 
        'abs':   abs,
        'append':  op.add,  
        #'apply':   apply,
        'begin':   lambda *x: x[-1],
        'car':   lambda x: x[0],
        'cdr':   lambda x: x[1:], 
        'cons':  lambda x,y: [x] + y,
        'eq?':   op.is_, 
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: list(x), 
        'list?':   lambda *x: type(x) == list, 
        'map':   map,
        'max':   max,
        'min':   min,
        'not':   op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: type(x)== int,   
        'round':   round,
        #'symbol?': lambda x: isinstance(x, Symbol),
    }

env.update(vars(math))

def interpretor(x,env):
    if(type(x) == str):
        return(env[x])
    elif(type(x) == int):
        return(x)
    elif(x[0] == '#'):              
        pass
    elif(x[0]=='if'):               
        return(if_interpretor(x,env))
    elif(x[0] == 'print'):          
        print_interpretor(x,env)
    elif(x[0] == 'update'):
        _,variable,value = x
        env[variable] = interpretor(value, env)
    elif(x[0] == 'define'):
        _, variable, value = x
        env[variable]=interpretor(value,env)
    else:
        operation = env[x[0]]
        operands = [interpretor(y,env) for y in x[1:]]  
        return(operation(*operands))

def if_interpretor(x,env):
    _,test,correct,incorrect = x
    if(interpretor(test,env)):
        return(interpretor(correct,env))
    else:
        return(interpretor(incorrect,env))

def print_interpretor(x,env):
    if(type(x[1]) == list):
        print(' '. join(x[1]))
    else:
        for y in x[1:]:
            print(env[y], end = ' ')
        print()

parsed_output,_=parser("""(begin (if (number? *) (print (YES))(print (NO))))""")
#print(parsed_output)
interpretor(parsed_output,env)

#(if (> (val x) 0) (fn (+ (aref A i) 1) (quote (one two))))