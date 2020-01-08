# Generated from Enquestes.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\6\2\30\n\2\r\2\16\2\31")
        buf.write("\3\3\3\3\3\3\3\3\6\3 \n\3\r\3\16\3!\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\6\5.\n\5\r\5\16\5/\3\5\6\5\63\n")
        buf.write("\5\r\5\16\5\64\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\7\7F\n\7\f\7\16\7I\13\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\6\tW\n\t\r\t\16")
        buf.write("\tX\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2^\2\27\3")
        buf.write("\2\2\2\4\33\3\2\2\2\6%\3\2\2\2\b\62\3\2\2\2\n\66\3\2\2")
        buf.write("\2\f=\3\2\2\2\16L\3\2\2\2\20R\3\2\2\2\22\30\5\4\3\2\23")
        buf.write("\30\5\6\4\2\24\30\5\n\6\2\25\30\5\f\7\2\26\30\5\20\t\2")
        buf.write("\27\22\3\2\2\2\27\23\3\2\2\2\27\24\3\2\2\2\27\25\3\2\2")
        buf.write("\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2")
        buf.write("\2\2\32\3\3\2\2\2\33\34\7\22\2\2\34\35\7\5\2\2\35\37\7")
        buf.write("\24\2\2\36 \7\27\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2")
        buf.write("\2!\"\3\2\2\2\"#\3\2\2\2#$\7\23\2\2$\5\3\2\2\2%&\7\20")
        buf.write("\2\2&\'\7\5\2\2\'(\7\21\2\2()\5\b\5\2)\7\3\2\2\2*+\7\13")
        buf.write("\2\2+-\7\5\2\2,.\7\27\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2")
        buf.write("\2/\60\3\2\2\2\60\61\3\2\2\2\61\63\7\4\2\2\62*\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\t\3\2\2")
        buf.write("\2\66\67\7\25\2\2\678\7\5\2\289\7\26\2\29:\7\22\2\2:;")
        buf.write("\7\3\2\2;<\7\20\2\2<\13\3\2\2\2=>\7\r\2\2>?\7\5\2\2?@")
        buf.write("\7\16\2\2@A\7\25\2\2AB\7\b\2\2BG\5\16\b\2CD\7\n\2\2DF")
        buf.write("\5\16\b\2EC\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3")
        buf.write("\2\2\2IG\3\2\2\2JK\7\t\2\2K\r\3\2\2\2LM\7\6\2\2MN\7\13")
        buf.write("\2\2NO\7\n\2\2OP\7\25\2\2PQ\7\7\2\2Q\17\3\2\2\2RS\7\27")
        buf.write("\2\2ST\7\5\2\2TV\7\17\2\2UW\7\25\2\2VU\3\2\2\2WX\3\2\2")
        buf.write("\2XV\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\7\f\2\2[\21\3\2\2\2")
        buf.write("\t\27\31!/\64GX")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "';'", "':'", "'('", "')'", "'['", 
                     "']'", "','", "<INVALID>", "'END'", "<INVALID>", "'ALTERNATIVA'", 
                     "'ENQUESTA'", "<INVALID>", "'RESPOSTA'", "<INVALID>", 
                     "'?'", "'PREGUNTA'", "<INVALID>", "'ITEM'" ]

    symbolicNames = [ "<INVALID>", "EDGE", "PC", "TP", "AP", "CP", "AC", 
                      "CC", "COMA", "NUM", "END", "IDALTER", "ALTERNATIVA", 
                      "ENQUESTA", "IDRESPUESTA", "RESPOSTA", "IDPREGUNTA", 
                      "INTERROGANTE", "PREGUNTA", "IDITEM", "ITEM", "PARAULA", 
                      "WS" ]

    RULE_chatboot = 0
    RULE_preguntas = 1
    RULE_respuesta = 2
    RULE_respuestas = 3
    RULE_item = 4
    RULE_alternative = 5
    RULE_alter = 6
    RULE_enque = 7

    ruleNames =  [ "chatboot", "preguntas", "respuesta", "respuestas", "item", 
                   "alternative", "alter", "enque" ]

    EOF = Token.EOF
    EDGE=1
    PC=2
    TP=3
    AP=4
    CP=5
    AC=6
    CC=7
    COMA=8
    NUM=9
    END=10
    IDALTER=11
    ALTERNATIVA=12
    ENQUESTA=13
    IDRESPUESTA=14
    RESPOSTA=15
    IDPREGUNTA=16
    INTERROGANTE=17
    PREGUNTA=18
    IDITEM=19
    ITEM=20
    PARAULA=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ChatbootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preguntas(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.PreguntasContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.PreguntasContext,i)


        def respuesta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.RespuestaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.RespuestaContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ItemContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ItemContext,i)


        def alternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AlternativeContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AlternativeContext,i)


        def enque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.EnqueContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.EnqueContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_chatboot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChatboot" ):
                return visitor.visitChatboot(self)
            else:
                return visitor.visitChildren(self)




    def chatboot(self):

        localctx = EnquestesParser.ChatbootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chatboot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [EnquestesParser.IDPREGUNTA]:
                    self.state = 16
                    self.preguntas()
                    pass
                elif token in [EnquestesParser.IDRESPUESTA]:
                    self.state = 17
                    self.respuesta()
                    pass
                elif token in [EnquestesParser.IDITEM]:
                    self.state = 18
                    self.item()
                    pass
                elif token in [EnquestesParser.IDALTER]:
                    self.state = 19
                    self.alternative()
                    pass
                elif token in [EnquestesParser.PARAULA]:
                    self.state = 20
                    self.enque()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EnquestesParser.IDALTER) | (1 << EnquestesParser.IDRESPUESTA) | (1 << EnquestesParser.IDPREGUNTA) | (1 << EnquestesParser.IDITEM) | (1 << EnquestesParser.PARAULA))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PreguntasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDPREGUNTA(self):
            return self.getToken(EnquestesParser.IDPREGUNTA, 0)

        def TP(self):
            return self.getToken(EnquestesParser.TP, 0)

        def PREGUNTA(self):
            return self.getToken(EnquestesParser.PREGUNTA, 0)

        def INTERROGANTE(self):
            return self.getToken(EnquestesParser.INTERROGANTE, 0)

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_preguntas

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreguntas" ):
                return visitor.visitPreguntas(self)
            else:
                return visitor.visitChildren(self)




    def preguntas(self):

        localctx = EnquestesParser.PreguntasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_preguntas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(EnquestesParser.IDPREGUNTA)
            self.state = 26
            self.match(EnquestesParser.TP)
            self.state = 27
            self.match(EnquestesParser.PREGUNTA)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.match(EnquestesParser.PARAULA)
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.PARAULA):
                    break

            self.state = 33
            self.match(EnquestesParser.INTERROGANTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespuestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDRESPUESTA(self):
            return self.getToken(EnquestesParser.IDRESPUESTA, 0)

        def TP(self):
            return self.getToken(EnquestesParser.TP, 0)

        def RESPOSTA(self):
            return self.getToken(EnquestesParser.RESPOSTA, 0)

        def respuestas(self):
            return self.getTypedRuleContext(EnquestesParser.RespuestasContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_respuesta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRespuesta" ):
                return visitor.visitRespuesta(self)
            else:
                return visitor.visitChildren(self)




    def respuesta(self):

        localctx = EnquestesParser.RespuestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_respuesta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(EnquestesParser.IDRESPUESTA)
            self.state = 36
            self.match(EnquestesParser.TP)
            self.state = 37
            self.match(EnquestesParser.RESPOSTA)
            self.state = 38
            self.respuestas()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespuestasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.NUM)
            else:
                return self.getToken(EnquestesParser.NUM, i)

        def TP(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.TP)
            else:
                return self.getToken(EnquestesParser.TP, i)

        def PC(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PC)
            else:
                return self.getToken(EnquestesParser.PC, i)

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_respuestas

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRespuestas" ):
                return visitor.visitRespuestas(self)
            else:
                return visitor.visitChildren(self)




    def respuestas(self):

        localctx = EnquestesParser.RespuestasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_respuestas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.match(EnquestesParser.NUM)
                self.state = 41
                self.match(EnquestesParser.TP)
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 42
                    self.match(EnquestesParser.PARAULA)
                    self.state = 45 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==EnquestesParser.PARAULA):
                        break

                self.state = 47
                self.match(EnquestesParser.PC)
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDITEM(self):
            return self.getToken(EnquestesParser.IDITEM, 0)

        def TP(self):
            return self.getToken(EnquestesParser.TP, 0)

        def ITEM(self):
            return self.getToken(EnquestesParser.ITEM, 0)

        def IDPREGUNTA(self):
            return self.getToken(EnquestesParser.IDPREGUNTA, 0)

        def EDGE(self):
            return self.getToken(EnquestesParser.EDGE, 0)

        def IDRESPUESTA(self):
            return self.getToken(EnquestesParser.IDRESPUESTA, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(EnquestesParser.IDITEM)
            self.state = 53
            self.match(EnquestesParser.TP)
            self.state = 54
            self.match(EnquestesParser.ITEM)
            self.state = 55
            self.match(EnquestesParser.IDPREGUNTA)
            self.state = 56
            self.match(EnquestesParser.EDGE)
            self.state = 57
            self.match(EnquestesParser.IDRESPUESTA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDALTER(self):
            return self.getToken(EnquestesParser.IDALTER, 0)

        def TP(self):
            return self.getToken(EnquestesParser.TP, 0)

        def ALTERNATIVA(self):
            return self.getToken(EnquestesParser.ALTERNATIVA, 0)

        def IDITEM(self):
            return self.getToken(EnquestesParser.IDITEM, 0)

        def AC(self):
            return self.getToken(EnquestesParser.AC, 0)

        def alter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AlterContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AlterContext,i)


        def CC(self):
            return self.getToken(EnquestesParser.CC, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.COMA)
            else:
                return self.getToken(EnquestesParser.COMA, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_alternative

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternative" ):
                return visitor.visitAlternative(self)
            else:
                return visitor.visitChildren(self)




    def alternative(self):

        localctx = EnquestesParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(EnquestesParser.IDALTER)
            self.state = 60
            self.match(EnquestesParser.TP)
            self.state = 61
            self.match(EnquestesParser.ALTERNATIVA)
            self.state = 62
            self.match(EnquestesParser.IDITEM)
            self.state = 63
            self.match(EnquestesParser.AC)
            self.state = 64
            self.alter()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.COMA:
                self.state = 65
                self.match(EnquestesParser.COMA)
                self.state = 66
                self.alter()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(EnquestesParser.CC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(EnquestesParser.AP, 0)

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def COMA(self):
            return self.getToken(EnquestesParser.COMA, 0)

        def IDITEM(self):
            return self.getToken(EnquestesParser.IDITEM, 0)

        def CP(self):
            return self.getToken(EnquestesParser.CP, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_alter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlter" ):
                return visitor.visitAlter(self)
            else:
                return visitor.visitChildren(self)




    def alter(self):

        localctx = EnquestesParser.AlterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_alter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EnquestesParser.AP)
            self.state = 75
            self.match(EnquestesParser.NUM)
            self.state = 76
            self.match(EnquestesParser.COMA)
            self.state = 77
            self.match(EnquestesParser.IDITEM)
            self.state = 78
            self.match(EnquestesParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnqueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self):
            return self.getToken(EnquestesParser.PARAULA, 0)

        def TP(self):
            return self.getToken(EnquestesParser.TP, 0)

        def ENQUESTA(self):
            return self.getToken(EnquestesParser.ENQUESTA, 0)

        def END(self):
            return self.getToken(EnquestesParser.END, 0)

        def IDITEM(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.IDITEM)
            else:
                return self.getToken(EnquestesParser.IDITEM, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_enque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnque" ):
                return visitor.visitEnque(self)
            else:
                return visitor.visitChildren(self)




    def enque(self):

        localctx = EnquestesParser.EnqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_enque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(EnquestesParser.PARAULA)
            self.state = 81
            self.match(EnquestesParser.TP)
            self.state = 82
            self.match(EnquestesParser.ENQUESTA)
            self.state = 84 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83
                self.match(EnquestesParser.IDITEM)
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.IDITEM):
                    break

            self.state = 88
            self.match(EnquestesParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





