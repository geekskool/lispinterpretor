import math
import operator as op
from Parser import parser

def standard_env():
	env = dict()
	env.update(vars(math)) # sin, cos, sqrt, pi, ...
	env.update({
		'+':op.add, '-':op.sub, '*':op.mul, '/':op.div, 
		'>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
		'abs':	 abs,
		'append':  op.add,  
		'apply':   apply,
		'begin':   lambda *x: x[-1],
		'car':	 lambda x: x[0],
		'cdr':	 lambda x: x[1:], 
		'cons':	lambda x,y: [x] + y,
		'eq?':	 op.is_, 
		'equal?':  op.eq, 
		'length':  len, 
		'list':	lambda *x: list(x), 
		'list?':   lambda x: isinstance(x,list), 
		'map':	 map,
		'max':	 max,
		'min':	 min,
		'not':	 op.not_,
		'null?':   lambda x: x == [], 
		'number?': lambda x: isinstance(x, Number),   
		'procedure?': callable,
		'round':   round,
		'symbol?': lambda x: isinstance(x, Symbol),
	})
	return env

global_env = standard_env()

def interpretor(x,env=global_env):
    if(isinstance(x,str)):
        return(env[x])
    elif(not isinstance(x,list)):
        return(x)
    elif(x[0]=='if'):
        _,test,correct,incorrect = x
        if(interpretor(test,env)):
            a=correct
        else:
            a=incorrect
        return(interpretor(a,env))
    elif(x[0] == 'define'):
        _, variable, value = x
        env[variable]=interpretor(value,env)
    else:
		operation = env[x[0]]
		operands = [interpretor(y,env) for y in x[1:]]
		print(operands)
		return(operation(*operands))

parsed_output,_=parser("(begin (define r 10) (* pi (* r r)))")
print(parsed_output)
print(interpretor(parsed_output,global_env))

#(if (> (val x) 0) (fn (+ (aref A i) 1) (quote (one two))))