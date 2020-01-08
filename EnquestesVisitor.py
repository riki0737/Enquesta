# Generated from Enquestes.g by ANTLR 4.7.2
from antlr4 import *
import networkx as nx
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitor(ParseTreeVisitor):
    def __init__(self):
        self.AST = nx.DiGraph()
        self.items = {}

    # Visit a parse tree produced by EnquestesParser#chatboot.
    def visitChatboot(self, ctx:EnquestesParser.ChatbootContext):
        self.visitChildren(ctx)
        return self.AST


    # Visit a parse tree produced by EnquestesParser#preguntas.
    def visitPreguntas(self, ctx:EnquestesParser.PreguntasContext):
        g = ctx.getChildren()
        n = ctx.getChildCount();
        l = [next(g) for i in range(n)]
        pregunta = ''
        for j in range(3,n):
            pregunta += l[j].getText()
        self.AST.add_node(l[0].getText(),pregunta=pregunta)

    # Visit a parse tree produced by EnquestesParser#respuesta.
    def visitRespuesta(self, ctx:EnquestesParser.RespuestaContext):
        g = ctx.getChildren()
        n = ctx.getChildCount();
        l = [next(g) for i in range(n)]
        respuestas = self.visit(l[n-1])
        a = {}
        a[l[0].getText()] = respuestas
        self.AST.add_node(l[0].getText(),respuestas=a)


    # Visit a parse tree produced by EnquestesParser#respuestas.
    def visitRespuestas(self, ctx:EnquestesParser.RespuestasContext):
        g = ctx.getChildren()
        n = ctx.getChildCount();
        l = [next(g) for i in range(n)]
        respuestas = ''
        for j in range(1,n-1):
            if l[j].getText() == ':':
                respuestas += l[j].getText() + ' '
            else:
                respuestas += l[j].getText()
        return respuestas


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        g = ctx.getChildren()
        n = ctx.getChildCount()
        l = [next(g) for i in range(n)]
        self.AST.add_edge(l[3].getText(),l[5].getText(), item=l[0].getText(), color = 'blue', textItem=l[0].getText())
        self.items[l[0].getText()] = l[3].getText();


    def visitAlternative(self, ctx:EnquestesParser.AlternativeContext):
        g = ctx.getChildren()
        n = ctx.getChildCount()
        l = [next(g) for i in range(n)]
        fixid = self.items[l[3].getText()]
        print("Estamos en alternative")
        print(fixid)
        for j in range(5,n-1):
            if l[j].getText() != ',':
                addid = self.items[self.visit(l[j])]
                print(addid)
                self.AST.add_edge(fixid,addid,color='green')


    # Visit a parse tree produced by EnquestesParser#alter.
    def visitAlter(self, ctx:EnquestesParser.AlterContext):
        g = ctx.getChildren()
        n = ctx.getChildCount()
        l = [next(g) for i in range(n)]
        return l[3].getText()


    # Visit a parse tree produced by EnquestesParser#enque.
    def visitEnque(self, ctx:EnquestesParser.EnqueContext):
        g = ctx.getChildren()
        n = ctx.getChildCount()
        l = [next(g) for i in range(n)]
        primer = l[0].getText();
        for j in range(3,n-1):
            self.AST.add_edge(primer,self.items[l[j].getText()],color='black')
            primer = self.items[l[j].getText()]
        self.AST.add_edge(primer,"END",color='black')



del EnquestesParser