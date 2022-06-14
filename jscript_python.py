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
from app import allStaks



class TestJavaScriptAndPython(TestCase):
    # def test_exit_javascrip_and_python(self):
    #     jscript_python()

    def test_jsAndpy_deve_retornar_javascript_quando_input_for_multiplo_de_3(self):
        """ jscript_python(3)' javaScript' """
        valores_entrada = [3,6,9]
        valor_esperado = 'javaScript'
        for valor in valores_entrada:
            #create subTest
            with self.subTest(valor=valor):
                self.assertEqual(jscript_python(valor), valor_esperado)

    def test_jsAndpy_deve_retornar_python_quando_input_for_multiplo_de_5(self):
        """ jscript_python(5) 'python' """
        valores_entrada = [5,10,20]
        valor_esperado = 'python'
        for valor in valores_entrada:
            with self.subTest(valor=valor):
                self.assertEqual(jscript_python(valor), valor_esperado)

    def test_jsAndpy_deve_retornar_javascript_e_python_quando_for_multipo_de_15(self):
        """jscript_python(15) -> 'javaScript e python' """
        valor_entrada = 15
        valor_esperado = 'javaScript e python'
        self.assertEqual(jscript_python(valor_entrada), valor_esperado)

    def test_jsAnpy_deve_retornar_javascript_python_e_javaScript_python_quando_receber_uma_lista_com_todos_os_multiplos(self):
        """allStaks -> irá retornar todos os multiplos """
        valores_entrada = [3,5,15]
        valor_esperado = ['javaScript', 'python', 'javaScript e python']
        self.assertEqual(allStaks(valores_entrada), valor_esperado)


main()