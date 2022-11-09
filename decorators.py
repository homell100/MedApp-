

def adding_hypens_to_args(func):
	def wrapper_adding_hypens_to_args(*args):
		args_ = []
		for arg in args:
			print(arg, type(arg))
			if len(arg):
				arg = "\'" + arg + "\'"
			else:
				arg = 'NULL'
			print(arg, type(arg))
			args_.append(arg)
		func(*args_)
	return wrapper_adding_hypens_to_args