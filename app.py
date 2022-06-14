
from functools import partial, wraps
from operator import eq, mod
from typing import Callable, Any

# criando uma composição de funções
def compose(*funcs):
    def inner(arg): # função interna - que recebe um argumento 
        state = arg # estado inicial recebe argumento 
        for func in reversed(funcs):
            state = func(state) # state recebe o resultado da função aplicada ao state anterior 
        return state
    return inner # retorna a função inner()

# criar decorator para checar se os valores são inteiro ou não 
def is_int(func: Callable ) -> Callable: 
    @wraps(func)
    def inner( val: Any) -> Any:
        return func(val) if isinstance(val, int) else val
    
    return inner


@is_int
def javaScript(n: int) -> str:
    return 'javaScript' if eq(mod(n, 3), 0) else n


@is_int
def javaScript_python(n: int) -> str:
    return 'javaScript e python' if eq(mod(n, 3), 0) and eq(mod(n, 5), 0 ) else n


@is_int
def python(n: int) -> str:
    return 'python' if eq(mod(n, 5), 0) else n

# def jscript_python(val: int):
#     if javaScript_python(val) == 'javaScript e python':
#         return 'javaScript e python'

#     if javaScript(val) == 'javaScript':
#         return 'javaScript'

#     if python(val) == 'python':
#         return 'python'

jscript_python = compose(javaScript, python, javaScript_python)
allStaks = compose(list, partial(map, jscript_python))

   
        
        