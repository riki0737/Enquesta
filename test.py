import sys
import networkx as nx
import matplotlib.pyplot as plt 
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from EnquestesVisitor import EnquestesVisitor

if len(sys.argv) > 1:
	input_stream = FileStream(sys.argv[1],encoding='utf-8')
else:
    input_stream = InputStream(input('? '))
                               
lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = EnquestesParser(token_stream)
tree = parser.chatboot()
print(tree.toStringTree(recog=parser))

visitor = EnquestesVisitor()
arbol = visitor.visit(tree)

nx.write_gpickle(arbol, "arbol.pickle")
pos = nx.circular_layout(arbol)
colors = [arbol[u][v]['color'] for u,v in arbol.edges()]
nx.draw(arbol,pos,with_labels=True, edge_color = colors)
plt.show()