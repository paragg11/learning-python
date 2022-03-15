#one.py


def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
	print("ONE.py is run directly!")
else:
	print("ONE.py is imported!")