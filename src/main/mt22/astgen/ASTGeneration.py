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
        exprlst.append(ctx.expr().getText())
        return list(map(lambda x,y: VarDecl(x,type_,y),varlst,exprlst))
        
        
    def visitType_(self,ctx: MT22Parser.Type_Context):
        child = ctx.getChild(0)
        if(isinstance(child,MT22Parser.Atomic_typeContext)):
            return self.visit(child)
        elif (isinstance(child,MT22Parser.AUTO)):
            return AutoType()
        return ['self.visitArray_type(child)']
    
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
        return [ctx.ID()] + self.visitRecur(ctx.recur()) + [ctx.expr().getText()]
        
        
    def visitExpr(self,ctx: MT22Parser.ExprContext):
        return "expr"
        
