from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

''' El lexer opera a nivel de caracteres
    El parser opera a nivel de tokens 
    El lexer construye una lista de tokens y sus valores si los tiene
    En el parser se consideran las reglas de la gramatica
    Factor Termino Expresion
    El termino busca * y /
    La expresion busca + y -
    Los factores son los numeros:

      5         +    2      *      10
    ------        ------         ------
    factor        factor         factor
    -------       ---------------------
    Termino             termino
    ------------------------------------
           E x p r e s i o n

    5 es un factor y un termino
    2 y 10 son factores cada uno
    2 * 10 es un termino
    5 + 2 * 10 es una expresion.
    un termino puede tener cero o mas operadores.
    El parser construye un arbol.
    Y el interprete ejecuta el arbol.
    lexer      ----> Lista de tokens:valores      parser  -------> arbol de  nodos (reglas gramaticales) ------>   interprete        ------->  salida
    caracteres                                    tokens                                                           arbol nodos (rg)
    string                                        lista                                                            nodos                       float o error
'''

while True:
    try:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        #print(list(tokens))
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)
        if not tree: continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        print(e)
