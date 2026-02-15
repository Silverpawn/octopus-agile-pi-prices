import py_compile
try:
    py_compile.compile('octoprice_main_inky_with_lametric.py', cfile='__pycache__/check_syntax.pyc', doraise=True)
    print("Syntax OK")
except py_compile.PyCompileError as e:
    print(f"Syntax Error: {e}")
except Exception as e:
    print(f"Error: {e}")
