import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):
    
    def test_empty(self):
        tokens = []                               # No hay tokens
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 20.9)]  # El token es un numero
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(20.9))

    def test_individual_operations(self):
        tokens = [                        # Add Node
             Token(TokenType.NUMBER, 18),
             Token(TokenType.PLUS),
             Token(TokenType.NUMBER, 12),
         ]                               
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(18), NumberNode(12)))

        tokens = [                        # Substract Node
             Token(TokenType.NUMBER, 18),
             Token(TokenType.MINUS),
             Token(TokenType.NUMBER, 12),
         ]                               
        node = Parser(tokens).parse()
        self.assertEqual(node, SubstractNode(NumberNode(18), NumberNode(12)))

        tokens = [                        # Multiply Node
             Token(TokenType.NUMBER, 18),
             Token(TokenType.MULTIPLY),
             Token(TokenType.NUMBER, 12),
         ]                               
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(18), NumberNode(12)))

        tokens = [                        # Divide Node
             Token(TokenType.NUMBER, 18),
             Token(TokenType.DIVIDE),
             Token(TokenType.NUMBER, 12),
         ]                               
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(18), NumberNode(12)))
    

    def test_full_expression(self):
       
        tokens =[
             Token(TokenType.NUMBER, 27),
             Token(TokenType.PLUS),
             Token(TokenType.LPAREN),
             Token(TokenType.NUMBER, 43),
             Token(TokenType.DIVIDE),
             Token(TokenType.NUMBER, 36),
             Token(TokenType.MINUS),
             Token(TokenType.NUMBER, 48),
             Token(TokenType.RPAREN),
             Token(TokenType.MULTIPLY),
             Token(TokenType.NUMBER, 51),
         ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(
            NumberNode(27), 
            MultiplyNode(
              SubstractNode(
                  DivideNode(
                      NumberNode(43),
                      NumberNode(36)
                  ),
                  NumberNode(48),
              ),
              NumberNode(51), 
            )   
          ))


# python -m unittest parser_test.py
