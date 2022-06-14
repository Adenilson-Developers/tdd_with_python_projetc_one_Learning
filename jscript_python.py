"""
Prolema...
Uma entrada de valores numéricos (Lista)

3X -> javaScript - quando for multiplo de 3 - responde quero aprender javaScript
5X -> Python - quando for multiplo de 5 - responde quero aprender python 
3X e 5X javaScript e Python - quando for multiplo de 3 e 5 - quero aprender javaScript e python 

 problem...

 an input of numeric values ( List )

 3X -> javaScript - When it is multiple of 3 - say i want to learn JavaScrit
 5X -> Python - When it is multiple of 5  say i want to learn Python 
 3X e 5X javaScript and Python - When it is multiple of 3 and 5  - say i want to learn JavaScript and python 

"""

from unittest import TestCase, main
from app import jscript_python



class TestJavaScriptAndPython(TestCase):
    # def test_exit_javascrip_and_python(self):
    #     jscript_python()

    def test_jsAndpy_deve_retornar_javascript_quando_input_for_multiplo_de_3(self):
        """ jscript_python(3)' javaScript' """
        valor_entrada = 3
        valor_esperado = 'javaScript'
        self.assertEqual(jscript_python(valor_entrada), valor_esperado)

    def test_jsAndpy_deve_retornar_python_quando_input_for_multiplo_de_5(self):
        """ jscript_python(5) 'python' """
        valor_entrada = 5
        valor_esperado = 'python'
        self.assertEqual(jscript_python(valor_entrada), valor_esperado)


main()