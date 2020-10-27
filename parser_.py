
# Este archivo se llama parser_.py porque python ya tiene un parser.py pre-construido
# Para evitar cualquier conflicto
# El parser va a transformar los tokens en nodos (nodes.py)

from tokens import TokenType    # Para chequear los tipos de los tokens
from nodes import *

class Parser:
    
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
    
    
    def raise_error(self):
        raise Exception("Sintaxis Invalida")

    
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None    # Ya no hay mas tokens.
    
    
    def parse(self):                     # Es el punto de entrada al parser.
        if self.current_token == None:
            return None

        result = self.expr()

        if self.current_token != None:
            self.raise_error()

        return result
    

    def expr(self):
        result = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())

            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubstractNode(result, self.term())
        
        return result

    def term(self):
        result = self.factor()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())
        
        return result

    def factor(self):
        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            
            self.advance()
            return result

        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        
        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())

        
        self.raise_error()

    
            
        






