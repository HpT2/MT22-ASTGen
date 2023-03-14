import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
 



    def test_simple_program(self):
        """Simple program"""
        input = """main: function string (out a:integer) inherit aa {

        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))


