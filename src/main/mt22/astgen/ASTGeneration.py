from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decls = self.visit(ctx.getChild(0));
        return Program(decls)
    
    def visitProg(self, ctx: MT22Parser.ProgContext):
        if(ctx.getChildCount()==1):
            return self.visit(ctx.declaration())
        return self.visit(ctx.declaration()) + self.visit(ctx.prog())

    def visitDeclaration(self, ctx: MT22Parser.DeclarationContext):
        child = ctx.getChild(0)
        if(isinstance(child,MT22Parser.Var_declareContext)):
            return self.visit(child)
        return ['func declare']
    
    def visitVar_declare(self, ctx: MT22Parser.Var_declareContext):
        child0 = ctx.getChild(0)
        vardecl_list = []
        varlist = child0.getText().split(',')
        if(isinstance(child0,MT22Parser.Id_listContext)):
            type_ = self.visit(ctx.getChild(2))
            for var in varlist:
                vardecl_list.append(VarDecl(var,type_))
            return vardecl_list
        varlst = [ctx.ID().getText()]
        exprlst = []
        recur = self.visit(ctx.recur())
        tail = len(recur)
        pos = tail - 1
        for i in range(tail):
            if i == pos :
                type_ = recur[i]
                break
            varlst.append(recur[i].getText())
            exprlst.append(recur[pos])
            pos = pos - 1
        exprlst.reverse()
        exprlst.append(self.visit(ctx.expr()))
        return list(map(lambda x,y: VarDecl(x,type_,y),varlst,exprlst))
        
        
    def visitType_(self,ctx: MT22Parser.Type_Context):
        child = ctx.getChild(0)
        if(isinstance(child,MT22Parser.Atomic_typeContext)):
            return self.visit(child)
        elif(isinstance(child,MT22Parser.Array_typeContext)):
            return self.visitArray_type(child)
        return AutoType()
    
    def visitAtomic_type(self,ctx: MT22Parser.Atomic_typeContext):
        child = ctx.getChild(0)
        if(child.getText() == 'integer'):
            return IntegerType()
        elif(child.getText() == 'float'):
            return FloatType()
        elif(child.getText() == 'string' ):
            return StringType()
        return BooleanType()
    
    def visitRecur(self,ctx: MT22Parser.RecurContext):
        if(ctx.getChildCount()==3):
            return [self.visit(ctx.type_())]
        return [ctx.ID()] + self.visitRecur(ctx.recur()) + [self.visit(ctx.expr())]
        
        
    def visitExpr(self,ctx: MT22Parser.ExprContext):
        if (ctx.getChildCount()==1):
            return self.visitExpr1(ctx.expr1(0))
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        op = ctx.getChild(1).getText()
        return BinExpr(op,left,right)
    
    def visitExpr1(self,ctx: MT22Parser.Expr1Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.expr2(0))
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        op = ctx.getChild(1).getText()
        return BinExpr(op,left,right)
    
    def visitExpr2(self,ctx: MT22Parser.Expr2Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.expr3())
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        return BinExpr(op,left,right)
    
    def visitExpr3(self,ctx: MT22Parser.Expr3Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.expr4())
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        return BinExpr(op,left,right)
    
    def visitExpr4(self,ctx: MT22Parser.Expr4Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.expr5())
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        return BinExpr(op,left,right)
    
    def visitExpr5(self,ctx:MT22Parser.Expr5Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.expr6())
        op = ctx.getChild(0).getText()
        val = self.visit(ctx.expr5())
        return UnExpr(op,val)
    
    def visitExpr6(self,ctx:MT22Parser.Expr6Context):
        if (ctx.getChildCount()==1):
            return self.visit(ctx.expr7())
        op = '-'
        val = self.visit(ctx.expr6())
        return UnExpr(op,val)
    
    def visitExpr7(self,ctx:MT22Parser.Expr7Context):
        return self.visit(ctx.getChild(0))
    
    def visitExprval(self,ctx: MT22Parser.ExprvalContext):
        if(ctx.getChildCount()==3):
            return self.visit(ctx.expr())
        child = ctx.getChild(0)
        if(not(isinstance(child,MT22Parser.Call_stmtContext)) and not(isinstance(child,MT22Parser.Indexed_arrayContext))):
           type_ =  child.getSymbol().type
           if (type_ == MT22Parser.INT_TYPE):
               return IntegerLit(child.getText())
           if (type_ == MT22Parser.FLOAT_TYPE):
               return FloatLit(child.getText())
           if (type_ == MT22Parser.STRING_TYPE):
               return StringLit(child.getText())
           if (type_ == MT22Parser.ID):
               return Id(child.getText())
           return BooleanLit(child.getText())
        return self.visit(child)
    
    def visitIndexop(self,ctx: MT22Parser.IndexopContext):
        ID = ctx.ID().getText()
        exprlist = self.visit(ctx.exprlist())
        return ArrayCell(ID,exprlist)
    
    def visitExprlist(self,ctx: MT22Parser.ExprlistContext):
        print(ctx.getText())
        if(ctx.getChildCount()==1):
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())
    
    def visitCall_stmt(self,ctx: MT22Parser.ExprlistContext):
        ID = ctx.ID().getText()
        args = self.visit(ctx.argument())
        return CallStmt(ID,args)

    def visitArgument(self,ctx: MT22Parser.ArgumentContext):
        if(ctx.getChildCount()==0):
            return []
        expr = self.visit(ctx.expr())
        print(ctx.getChildCount())
        if(ctx.getChildCount()==1):
            return [expr]
        return [expr] + self.visit(ctx.argument())
    
    def visitIndexed_array(self,ctx: MT22Parser.Indexed_arrayContext):
        if(ctx.getChildCount()==3):
            exprlist = self.visit(ctx.exprlist())
            return ArrayLit(exprlist)
        return ArrayLit([])

    def visitArray_type(self,ctx: MT22Parser.Array_typeContext):
        type_ = self.visit(ctx.atomic_type())
        dimension = self.visit(ctx.dimension())
        return ArrayType(dimension,type_)
    
    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        return self.visit(ctx.intlist())
    
    def visitIntlist(self, ctx: MT22Parser.IntlistContext):
        if(ctx.getChildCount()==1):
            return [IntegerLit(ctx.INT_TYPE().getText())]
        return [IntegerLit(ctx.INT_TYPE().getText())] + self.visit(ctx.intlist())