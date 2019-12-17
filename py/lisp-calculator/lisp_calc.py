from typing import List

left_paren = "("
right_paren = ")"

functions = {
	"+": lambda x, y : x + y,
	"-": lambda x, y : x - y,
	"*": lambda x, y : x * y, 
}

def check_if_balanced(parenthesis: List[str]) -> bool:
	parenthesis_count = 0
	for paren in parenthesis:
		if paren == right_paren:
			if parenthesis_count == 0:
				return False
			else:
				parenthesis_count -= 1
		elif paren == left_paren:
			parenthesis_count += 1
	if parenthesis_count != 0:
		return False
	return True

def is_well_formed(exp: str):
	tokens = exp.replace("(", " ( ").replace(")", " ) ").split(" ")
	parenthesis = [token for token in tokens if token == "(" or token == ")"]
	return check_if_balanced(parenthesis)

def eval(exp: str) -> int:
	stack = []
	left_paren, right_paren = "(", ")"
	tokens = exp.replace("(", " ( ").replace(")", " ) ").split(" ")
	tokens = [token for token in tokens if token != ""]
	for token in tokens:
		if token != right_paren:
			stack.append(token)
		else:
			token_popped = stack.pop()
			operands = []
			while token_popped != left_paren:
				operands.append(token_popped)
				token_popped = stack.pop()
			if len(operands) > 3:
				print("ERROR")
				break
			else:
				num_two, num_one, func = operands
				ret = functions[func](int(num_one), int(num_two))
				stack.append(ret)
	return stack[0]




def repl(p=">>> "):
	quit = False
	while not quit:
		exp = input(p)
		try: 
			assert is_well_formed(exp)
			print(eval(exp))
		except Exception as e:
			print("Expression is not well formed!")
			continue

def main():
	repl()

if __name__ == '__main__':
	main()



