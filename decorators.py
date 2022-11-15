

def adding_hypens(func):
	def wrapper_adding_hypens(*args, **kwarg):
		kwarg_ = {}
		for key, value in kwarg.items():
			if len(value):
				value = "\'" + value + "\'"
			kwarg_[key] = value
		return func(*args, **kwarg_)
	return wrapper_adding_hypens

def converting_none_to_null(func):
	def wrapper_converting_none_to_null(*args, **kwarg):
		kwarg_ = {}
		for key, value in kwarg.items():
			if not len(value):
				value = 'NULL'
			kwarg_[key] = value
		return func(*args, **kwarg_)
	return wrapper_converting_none_to_null
