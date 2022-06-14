
from operator import eq, mod

def javaScript(n: int) -> str:
    return 'javaScript' if eq(mod(n, 3), 0) else n

def javaScript_python(n: int) -> str:
    return 'javaScript e python' if eq(mod(n, 3), 0) and eq(mod(n, 5), 0 ) else n

def jscript_python(val: int):
    if javaScript_python(val) == 'javaScript e python':
        return 'javaScript e python'

    if javaScript(val) == 'javaScript':
        return 'javaScript'
        
    if val == 5:
        return 'python'
    return 'javaScript e python'
        
        