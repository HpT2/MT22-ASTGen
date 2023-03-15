import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

	"""test variable declaration"""
	def test1(self):
		input = """ a,b,c : string; """
		expect = """Program([
	VarDecl(a, StringType)
	VarDecl(b, StringType)
	VarDecl(c, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 301))

	def test2(self):
		input = """ a,b,c : string = "a","b","c"; """
		expect = """Program([
	VarDecl(a, StringType, StringLit(a))
	VarDecl(b, StringType, StringLit(b))
	VarDecl(c, StringType, StringLit(c))
])"""
		self.assertTrue(TestAST.test(input, expect, 302))

	def test3(self):
		input = """a,b,c : string = "a","b",1; """
		expect = """Program([
	VarDecl(a, StringType, StringLit(a))
	VarDecl(b, StringType, StringLit(b))
	VarDecl(c, StringType, IntegerLit(1))
])"""
		self.assertTrue(TestAST.test(input, expect, 303))

	def test4(self):
		input = """a : string = a; """
		expect = """Program([
	VarDecl(a, StringType, Id(a))
])"""
		self.assertTrue(TestAST.test(input, expect, 304))

	def test5(self):
		input = """a: array [1] of integer = {}; """
		expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 305))

	def test6(self):
		input = """a: array [1] of integer = {1,2,3}; """
		expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 306))

	def test7(self):
		input = """a: array [1] of integer = {a,b,c}; """
		expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([Id(a), Id(b), Id(c)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 307))

	def test8(self):
		input = """a: array [1] of integer = {true, 3, {}}; """
		expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([BooleanLit(True), IntegerLit(3), ArrayLit([])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 308))

	def test9(self):
		input = """
            fact: function integer(){
                
            }
        """
		expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 309))

	def test10(self):
		input = """
            main: function void () {
                x = foo(-{1,2,3});
            }
        """
		expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), FuncCall(foo, [UnExpr(-, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 310))


	def test11(self):
		input = """
        main: function void (){
            if (i) return 1;
        }
        """
		expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(i), ReturnStmt(IntegerLit(1)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 311))

	def test12(self):
		input = """main: function void (){
                x: integer = 1;
                x= -foo(b,c,d,e);
            }
        """
		expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), AssignStmt(Id(x), UnExpr(-, FuncCall(foo, [Id(b), Id(c), Id(d), Id(e)])))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 312))

	def test13(self):
		input = """
        main: function void (inherit out x: string){
            if(true){
                id = (------------id == 21) > 4;
            }
            else {
                if(false){}else{}
            }
        }
        """
		expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(x, StringType)], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(id), BinExpr(>, BinExpr(==, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, Id(id))))))))))))), IntegerLit(21)), IntegerLit(4)))]), BlockStmt([IfStmt(BooleanLit(False), BlockStmt([]), BlockStmt([]))]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 313))

	def test14(self):
		input = """
            main:function void (){
                if (x) 
                    if(y) return 1; 
                    else return 2;
            }
        """
		expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(x), IfStmt(Id(y), ReturnStmt(IntegerLit(1)), ReturnStmt(IntegerLit(2))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 314))

	def test15(self):
		input = """
        inc: function void(out n: integer, delta: integer) inherit abc {
            if(--a[foo(8,{1,3,4}),a[a[a[5]]]]) return;
            else 
                if (_1) return a==2+d; 
                else return true;
        }      
        """
		expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], abc, BlockStmt([IfStmt(UnExpr(-, UnExpr(-, ArrayCell(a, [FuncCall(foo, [IntegerLit(8), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4)])]), ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(5)])])])]))), ReturnStmt(), IfStmt(Id(_1), ReturnStmt(BinExpr(==, Id(a), BinExpr(+, IntegerLit(2), Id(d)))), ReturnStmt(BooleanLit(True))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 315))

	def test16(self):
		input = """
            fibo: function integer (n: integer){
                if (n==1) return 1;
                if (n==0) return 0;
                return n + fibo(n-1);
            }  
        """
		expect = """Program([
	FuncDecl(fibo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(0))), ReturnStmt(BinExpr(+, Id(n), FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(1))])))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 316))

	def test17(self):
		input = """
        main: function void (){
            while(true)
                do{
                    a[-"a"]=b>d;
                }while(1);
        } 
        """
		expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), DoWhileStmt(IntegerLit(1), BlockStmt([AssignStmt(ArrayCell(a, [UnExpr(-, StringLit(a))]), BinExpr(>, Id(b), Id(d)))])))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 317))

	def test18(self):
		input = """
            a:integer = a[1];
            b: string = {-foo(),123,"string"};
            sum: function integer(a:integer, b:integer){
                return (a+b);
            } 
        """
		expect = """Program([
	VarDecl(a, IntegerType, ArrayCell(a, [IntegerLit(1)]))
	VarDecl(b, StringType, ArrayLit([UnExpr(-, FuncCall(foo, [])), IntegerLit(123), StringLit(string)]))
	FuncDecl(sum, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 318))

	def test19(self):
		input = """
            max:function integer (x:integer, y:integer){
                if (x > y)
                    return x;
                else
                    return y;
            }  
            main:function void(){
                m:integer = max(9,!-1);
                print(m);
            }
        """
		expect = """Program([
	FuncDecl(max, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(x), Id(y)), ReturnStmt(Id(x)), ReturnStmt(Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(m, IntegerType, FuncCall(max, [IntegerLit(9), UnExpr(!, UnExpr(-, IntegerLit(1)))])), CallStmt(print, Id(m))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 319))

	def test20(self):
		input = """
            True:function boolean(x:integer){
                return !true;
            }  
        """
		expect = """Program([
	FuncDecl(True, BooleanType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(UnExpr(!, BooleanLit(True)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 320))



	

