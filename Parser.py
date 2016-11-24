import re

keywords = ['begin','define', 'print', 'if']
mathematic_operators = ['+','-','*','/','%','>']
comparison_operators = ['==','!=','<>','<','>','>=','<=']

def num_parser(data):
	match = re.match(r'\d+',data)       # matches for numbers and returns a match object 
	if(match):
		return(int(data[:match.end()]), data[match.end():])

def space_parser(data):
	match=re.match(r'\s+',data)         # matches for white spaces and returns a match object 
	if(match):
		return([],data[match.end():])

def word_parser(data):
	match=re.match(r'[a-zA-Z_]+',data)   # matches for string and returns a match object 
	if(match):
		return(data[:match.end()], data[match.end():])

def keyword_parser(data):				# matches for keywords 
	for keyword in keywords:
		if(data.startswith(keyword)):
			return(data[:len(keyword)],data[len(keyword):])

def mathematic_parser(data):
	for operator in mathematic_operators:
		if(data.startswith(operator)):
			return(data[:len(operator)],data[len(operator):])

def comparison_parser(data):
	for operator in comparison_operators:
		if(data.startswith(operator)):
			return(data[:len(operator)],data[len(operator):])

def parser(data):
	if(data[0]=='('):
		L=[]
		data=data[1:]	
		while(data[0]!=')'):
			output, data = parser(data)
			if(not output):
				continue
			else:
				L.append(output)
		return(L,data[1:])
	else:
		return(space_parser(data) or num_parser(data) or keyword_parser(data) or mathematic_parser(data) or comparison_parser(data) or word_parser(data))

data="(begin (define circle_area (lambda r (* pi (* r r)))))"
A,_ = parser(data)
print(A)