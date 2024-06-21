# Generated from E:/uni file/compiler/createDsl/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,66,341,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,1,4,1,71,8,1,11,1,12,1,72,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        97,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,5,21,
        221,8,21,10,21,12,21,224,9,21,1,21,1,21,1,21,1,21,5,21,230,8,21,
        10,21,12,21,233,9,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,0,2,1,0,4,6,1,0,60,61,331,0,66,1,0,0,0,2,70,1,0,0,0,4,96,1,
        0,0,0,6,98,1,0,0,0,8,105,1,0,0,0,10,112,1,0,0,0,12,114,1,0,0,0,14,
        116,1,0,0,0,16,118,1,0,0,0,18,129,1,0,0,0,20,137,1,0,0,0,22,149,
        1,0,0,0,24,156,1,0,0,0,26,168,1,0,0,0,28,170,1,0,0,0,30,179,1,0,
        0,0,32,184,1,0,0,0,34,191,1,0,0,0,36,193,1,0,0,0,38,202,1,0,0,0,
        40,213,1,0,0,0,42,215,1,0,0,0,44,236,1,0,0,0,46,246,1,0,0,0,48,254,
        1,0,0,0,50,256,1,0,0,0,52,266,1,0,0,0,54,278,1,0,0,0,56,280,1,0,
        0,0,58,288,1,0,0,0,60,299,1,0,0,0,62,315,1,0,0,0,64,327,1,0,0,0,
        66,67,3,2,1,0,67,68,5,0,0,1,68,1,1,0,0,0,69,71,3,4,2,0,70,69,1,0,
        0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,3,1,0,0,0,74,97,
        3,8,4,0,75,97,3,6,3,0,76,97,3,16,8,0,77,97,3,18,9,0,78,97,3,20,10,
        0,79,97,3,22,11,0,80,97,3,24,12,0,81,97,3,28,14,0,82,97,3,30,15,
        0,83,97,3,32,16,0,84,97,3,36,18,0,85,97,3,38,19,0,86,97,3,42,21,
        0,87,97,3,44,22,0,88,97,3,46,23,0,89,97,3,50,25,0,90,97,3,52,26,
        0,91,97,3,56,28,0,92,97,3,58,29,0,93,97,3,60,30,0,94,97,3,62,31,
        0,95,97,3,64,32,0,96,74,1,0,0,0,96,75,1,0,0,0,96,76,1,0,0,0,96,77,
        1,0,0,0,96,78,1,0,0,0,96,79,1,0,0,0,96,80,1,0,0,0,96,81,1,0,0,0,
        96,82,1,0,0,0,96,83,1,0,0,0,96,84,1,0,0,0,96,85,1,0,0,0,96,86,1,
        0,0,0,96,87,1,0,0,0,96,88,1,0,0,0,96,89,1,0,0,0,96,90,1,0,0,0,96,
        91,1,0,0,0,96,92,1,0,0,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,
        0,97,5,1,0,0,0,98,99,5,30,0,0,99,100,5,31,0,0,100,101,5,32,0,0,101,
        102,5,10,0,0,102,103,3,10,5,0,103,104,5,1,0,0,104,7,1,0,0,0,105,
        106,5,30,0,0,106,107,5,31,0,0,107,108,5,32,0,0,108,109,5,9,0,0,109,
        110,3,10,5,0,110,111,5,1,0,0,111,9,1,0,0,0,112,113,5,61,0,0,113,
        11,1,0,0,0,114,115,5,61,0,0,115,13,1,0,0,0,116,117,5,61,0,0,117,
        15,1,0,0,0,118,119,5,13,0,0,119,120,5,31,0,0,120,121,3,10,5,0,121,
        122,5,45,0,0,122,123,3,10,5,0,123,124,5,46,0,0,124,125,5,12,0,0,
        125,126,5,44,0,0,126,127,3,10,5,0,127,128,5,1,0,0,128,17,1,0,0,0,
        129,130,5,14,0,0,130,131,5,33,0,0,131,132,5,48,0,0,132,133,3,10,
        5,0,133,134,5,44,0,0,134,135,3,10,5,0,135,136,5,1,0,0,136,19,1,0,
        0,0,137,138,5,15,0,0,138,139,5,36,0,0,139,140,3,12,6,0,140,141,5,
        46,0,0,141,142,3,12,6,0,142,143,5,46,0,0,143,144,5,54,0,0,144,145,
        5,43,0,0,145,146,5,44,0,0,146,147,3,14,7,0,147,148,5,1,0,0,148,21,
        1,0,0,0,149,150,5,16,0,0,150,151,5,35,0,0,151,152,3,12,6,0,152,153,
        5,44,0,0,153,154,3,12,6,0,154,155,5,1,0,0,155,23,1,0,0,0,156,157,
        5,17,0,0,157,158,5,34,0,0,158,159,5,37,0,0,159,160,5,51,0,0,160,
        161,5,35,0,0,161,162,5,2,0,0,162,163,3,12,6,0,163,164,5,3,0,0,164,
        165,5,44,0,0,165,166,3,26,13,0,166,167,5,1,0,0,167,25,1,0,0,0,168,
        169,5,37,0,0,169,27,1,0,0,0,170,171,5,18,0,0,171,172,5,34,0,0,172,
        173,5,47,0,0,173,174,5,35,0,0,174,175,5,2,0,0,175,176,3,12,6,0,176,
        177,5,3,0,0,177,178,5,1,0,0,178,29,1,0,0,0,179,180,5,19,0,0,180,
        181,5,35,0,0,181,182,3,12,6,0,182,183,5,1,0,0,183,31,1,0,0,0,184,
        185,5,16,0,0,185,186,5,10,0,0,186,187,5,31,0,0,187,188,5,44,0,0,
        188,189,3,34,17,0,189,190,5,1,0,0,190,33,1,0,0,0,191,192,5,61,0,
        0,192,35,1,0,0,0,193,194,5,20,0,0,194,195,5,40,0,0,195,196,5,50,
        0,0,196,197,5,38,0,0,197,198,5,60,0,0,198,199,5,44,0,0,199,200,5,
        60,0,0,200,201,5,1,0,0,201,37,1,0,0,0,202,203,5,21,0,0,203,204,5,
        11,0,0,204,205,5,52,0,0,205,206,5,35,0,0,206,207,5,2,0,0,207,208,
        3,12,6,0,208,209,5,3,0,0,209,210,5,47,0,0,210,211,3,40,20,0,211,
        212,5,1,0,0,212,39,1,0,0,0,213,214,7,0,0,0,214,41,1,0,0,0,215,216,
        5,22,0,0,216,217,5,36,0,0,217,222,5,61,0,0,218,219,5,7,0,0,219,221,
        5,61,0,0,220,218,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,
        1,0,0,0,223,225,1,0,0,0,224,222,1,0,0,0,225,226,5,44,0,0,226,231,
        5,61,0,0,227,228,5,7,0,0,228,230,5,61,0,0,229,227,1,0,0,0,230,233,
        1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,234,1,0,0,0,233,231,
        1,0,0,0,234,235,5,1,0,0,235,43,1,0,0,0,236,237,5,23,0,0,237,238,
        5,47,0,0,238,239,3,12,6,0,239,240,5,46,0,0,240,241,5,56,0,0,241,
        242,5,41,0,0,242,243,5,42,0,0,243,244,3,12,6,0,244,245,5,1,0,0,245,
        45,1,0,0,0,246,247,5,24,0,0,247,248,5,38,0,0,248,249,5,49,0,0,249,
        250,3,12,6,0,250,251,5,8,0,0,251,252,3,48,24,0,252,253,5,1,0,0,253,
        47,1,0,0,0,254,255,5,60,0,0,255,49,1,0,0,0,256,257,5,25,0,0,257,
        258,5,52,0,0,258,259,5,61,0,0,259,260,5,42,0,0,260,261,5,35,0,0,
        261,262,5,2,0,0,262,263,3,12,6,0,263,264,5,3,0,0,264,265,5,1,0,0,
        265,51,1,0,0,0,266,267,5,26,0,0,267,268,5,41,0,0,268,269,3,54,27,
        0,269,270,5,45,0,0,270,271,3,54,27,0,271,272,5,42,0,0,272,273,5,
        35,0,0,273,274,5,2,0,0,274,275,3,12,6,0,275,276,5,3,0,0,276,277,
        5,1,0,0,277,53,1,0,0,0,278,279,7,1,0,0,279,55,1,0,0,0,280,281,5,
        15,0,0,281,282,5,40,0,0,282,283,5,49,0,0,283,284,3,12,6,0,284,285,
        5,8,0,0,285,286,3,48,24,0,286,287,5,1,0,0,287,57,1,0,0,0,288,289,
        5,27,0,0,289,290,5,59,0,0,290,291,5,38,0,0,291,292,5,55,0,0,292,
        293,5,50,0,0,293,294,5,35,0,0,294,295,5,2,0,0,295,296,3,12,6,0,296,
        297,5,3,0,0,297,298,5,1,0,0,298,59,1,0,0,0,299,300,5,28,0,0,300,
        301,5,34,0,0,301,302,5,55,0,0,302,303,5,50,0,0,303,304,5,35,0,0,
        304,305,5,2,0,0,305,306,3,12,6,0,306,307,5,3,0,0,307,308,5,46,0,
        0,308,309,5,54,0,0,309,310,5,64,0,0,310,311,5,44,0,0,311,312,5,65,
        0,0,312,313,5,66,0,0,313,314,5,1,0,0,314,61,1,0,0,0,315,316,5,13,
        0,0,316,317,5,36,0,0,317,318,3,12,6,0,318,319,5,46,0,0,319,320,3,
        12,6,0,320,321,5,46,0,0,321,322,5,54,0,0,322,323,5,43,0,0,323,324,
        5,44,0,0,324,325,3,14,7,0,325,326,5,1,0,0,326,63,1,0,0,0,327,328,
        5,29,0,0,328,329,5,34,0,0,329,330,5,42,0,0,330,331,5,35,0,0,331,
        332,5,2,0,0,332,333,3,12,6,0,333,334,5,3,0,0,334,335,5,47,0,0,335,
        336,5,58,0,0,336,337,5,45,0,0,337,338,3,48,24,0,338,339,5,1,0,0,
        339,65,1,0,0,0,4,72,96,222,231
    ]

class ExampleDSLParser ( Parser ):

    grammarFileName = "ExampleDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'day'", "'month'", 
                     "'year'", "','", "'>'", "'input'", "'output'", "'report'", 
                     "'write'", "'Combine'", "'Convert'", "'Add'", "'Rename'", 
                     "'Change'", "'Sort'", "'Delete'", "'Apply'", "'Generate'", 
                     "'Reorder'", "'Group'", "'Filter'", "'Search'", "'Replace'", 
                     "'Remove'", "'Split'", "'Resize'", "'Set'", "'file'", 
                     "'path'", "'format'", "'data'", "'column'", "'columns'", 
                     "'type'", "'rows'", "'row'", "'condition'", "'values'", 
                     "'in'", "'result'", "'to'", "'with'", "'and'", "'by'", 
                     "'from'", "'where'", "'on'", "'of'", "'for'", "'as'", 
                     "'save'", "'based'", "'sum'", "'new'", "'multiplying'", 
                     "'duplicate'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INPUT", "OUTPUT", "REPORT", "WRITE", 
                      "COMBINE", "CONVERT", "ADD", "RENAME", "CHANGE", "SORT", 
                      "DELETE", "APPLY", "GENERATE", "REORDER", "GROUP", 
                      "FILTER", "SEARCH", "REPLACE", "REMOVE", "SPLIT", 
                      "RESIZE", "SET", "FILE", "PATH", "FORMAT", "DATA", 
                      "COLUMN", "COLUMNS", "TYPE", "ROWS", "ROW", "CONDITION", 
                      "VALUES", "IN", "RESULT", "TO", "WITH", "AND", "BY", 
                      "FROM", "WHERE", "ON", "OF", "FOR", "AS", "SAVE", 
                      "BASED", "SUM", "NEW", "MULTIPLYING", "DUPLICATE", 
                      "NUMBER", "STRING", "ID", "WS", "RESULTS", "SEPARATE", 
                      "FILES" ]

    RULE_start = 0
    RULE_program = 1
    RULE_statement = 2
    RULE_setFileOutputPathStatement = 3
    RULE_setFileInputPathStatement = 4
    RULE_path = 5
    RULE_column = 6
    RULE_result = 7
    RULE_combineStatement = 8
    RULE_convertStatement = 9
    RULE_addColumnsStatement = 10
    RULE_renameColumnStatement = 11
    RULE_changeDataTypeStatement = 12
    RULE_type = 13
    RULE_sortDataStatement = 14
    RULE_deleteColumnStatement = 15
    RULE_renameFileStatement = 16
    RULE_file_name = 17
    RULE_applyConditionStatement = 18
    RULE_generateReportStatement = 19
    RULE_period = 20
    RULE_reorderColumnsStatement = 21
    RULE_groupByStatement = 22
    RULE_filterRowsStatement = 23
    RULE_value = 24
    RULE_searchTextStatement = 25
    RULE_replaceValuesStatement = 26
    RULE_values = 27
    RULE_addConditionStatement = 28
    RULE_removeDuplicatesStatement = 29
    RULE_splitDataStatement = 30
    RULE_combineColumnsStatement = 31
    RULE_resizeDataStatement = 32

    ruleNames =  [ "start", "program", "statement", "setFileOutputPathStatement", 
                   "setFileInputPathStatement", "path", "column", "result", 
                   "combineStatement", "convertStatement", "addColumnsStatement", 
                   "renameColumnStatement", "changeDataTypeStatement", "type", 
                   "sortDataStatement", "deleteColumnStatement", "renameFileStatement", 
                   "file_name", "applyConditionStatement", "generateReportStatement", 
                   "period", "reorderColumnsStatement", "groupByStatement", 
                   "filterRowsStatement", "value", "searchTextStatement", 
                   "replaceValuesStatement", "values", "addConditionStatement", 
                   "removeDuplicatesStatement", "splitDataStatement", "combineColumnsStatement", 
                   "resizeDataStatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INPUT=9
    OUTPUT=10
    REPORT=11
    WRITE=12
    COMBINE=13
    CONVERT=14
    ADD=15
    RENAME=16
    CHANGE=17
    SORT=18
    DELETE=19
    APPLY=20
    GENERATE=21
    REORDER=22
    GROUP=23
    FILTER=24
    SEARCH=25
    REPLACE=26
    REMOVE=27
    SPLIT=28
    RESIZE=29
    SET=30
    FILE=31
    PATH=32
    FORMAT=33
    DATA=34
    COLUMN=35
    COLUMNS=36
    TYPE=37
    ROWS=38
    ROW=39
    CONDITION=40
    VALUES=41
    IN=42
    RESULT=43
    TO=44
    WITH=45
    AND=46
    BY=47
    FROM=48
    WHERE=49
    ON=50
    OF=51
    FOR=52
    AS=53
    SAVE=54
    BASED=55
    SUM=56
    NEW=57
    MULTIPLYING=58
    DUPLICATE=59
    NUMBER=60
    STRING=61
    ID=62
    WS=63
    RESULTS=64
    SEPARATE=65
    FILES=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(ExampleDSLParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(ExampleDSLParser.EOF, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ExampleDSLParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.program()
            self.state = 67
            self.match(ExampleDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExampleDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.statement()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147475456) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def setFileInputPathStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.SetFileInputPathStatementContext,0)


        def setFileOutputPathStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.SetFileOutputPathStatementContext,0)


        def combineStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.CombineStatementContext,0)


        def convertStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ConvertStatementContext,0)


        def addColumnsStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AddColumnsStatementContext,0)


        def renameColumnStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.RenameColumnStatementContext,0)


        def changeDataTypeStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ChangeDataTypeStatementContext,0)


        def sortDataStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.SortDataStatementContext,0)


        def deleteColumnStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.DeleteColumnStatementContext,0)


        def renameFileStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.RenameFileStatementContext,0)


        def applyConditionStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ApplyConditionStatementContext,0)


        def generateReportStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.GenerateReportStatementContext,0)


        def reorderColumnsStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ReorderColumnsStatementContext,0)


        def groupByStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.GroupByStatementContext,0)


        def filterRowsStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.FilterRowsStatementContext,0)


        def searchTextStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.SearchTextStatementContext,0)


        def replaceValuesStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ReplaceValuesStatementContext,0)


        def addConditionStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AddConditionStatementContext,0)


        def removeDuplicatesStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.RemoveDuplicatesStatementContext,0)


        def splitDataStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.SplitDataStatementContext,0)


        def combineColumnsStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.CombineColumnsStatementContext,0)


        def resizeDataStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ResizeDataStatementContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ExampleDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.setFileInputPathStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.setFileOutputPathStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.combineStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.convertStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.addColumnsStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.renameColumnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.changeDataTypeStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 81
                self.sortDataStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 82
                self.deleteColumnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 83
                self.renameFileStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 84
                self.applyConditionStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 85
                self.generateReportStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 86
                self.reorderColumnsStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 87
                self.groupByStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 88
                self.filterRowsStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 89
                self.searchTextStatement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 90
                self.replaceValuesStatement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 91
                self.addConditionStatement()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 92
                self.removeDuplicatesStatement()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 93
                self.splitDataStatement()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 94
                self.combineColumnsStatement()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 95
                self.resizeDataStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetFileOutputPathStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(ExampleDSLParser.SET, 0)

        def FILE(self):
            return self.getToken(ExampleDSLParser.FILE, 0)

        def PATH(self):
            return self.getToken(ExampleDSLParser.PATH, 0)

        def OUTPUT(self):
            return self.getToken(ExampleDSLParser.OUTPUT, 0)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_setFileOutputPathStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetFileOutputPathStatement" ):
                listener.enterSetFileOutputPathStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetFileOutputPathStatement" ):
                listener.exitSetFileOutputPathStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetFileOutputPathStatement" ):
                return visitor.visitSetFileOutputPathStatement(self)
            else:
                return visitor.visitChildren(self)




    def setFileOutputPathStatement(self):

        localctx = ExampleDSLParser.SetFileOutputPathStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_setFileOutputPathStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ExampleDSLParser.SET)
            self.state = 99
            self.match(ExampleDSLParser.FILE)
            self.state = 100
            self.match(ExampleDSLParser.PATH)
            self.state = 101
            self.match(ExampleDSLParser.OUTPUT)
            self.state = 102
            self.path()
            self.state = 103
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetFileInputPathStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(ExampleDSLParser.SET, 0)

        def FILE(self):
            return self.getToken(ExampleDSLParser.FILE, 0)

        def PATH(self):
            return self.getToken(ExampleDSLParser.PATH, 0)

        def INPUT(self):
            return self.getToken(ExampleDSLParser.INPUT, 0)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_setFileInputPathStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetFileInputPathStatement" ):
                listener.enterSetFileInputPathStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetFileInputPathStatement" ):
                listener.exitSetFileInputPathStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetFileInputPathStatement" ):
                return visitor.visitSetFileInputPathStatement(self)
            else:
                return visitor.visitChildren(self)




    def setFileInputPathStatement(self):

        localctx = ExampleDSLParser.SetFileInputPathStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_setFileInputPathStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ExampleDSLParser.SET)
            self.state = 106
            self.match(ExampleDSLParser.FILE)
            self.state = 107
            self.match(ExampleDSLParser.PATH)
            self.state = 108
            self.match(ExampleDSLParser.INPUT)
            self.state = 109
            self.path()
            self.state = 110
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = ExampleDSLParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ExampleDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = ExampleDSLParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ExampleDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult" ):
                listener.enterResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult" ):
                listener.exitResult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult" ):
                return visitor.visitResult(self)
            else:
                return visitor.visitChildren(self)




    def result(self):

        localctx = ExampleDSLParser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_result)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(ExampleDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CombineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMBINE(self):
            return self.getToken(ExampleDSLParser.COMBINE, 0)

        def FILE(self):
            return self.getToken(ExampleDSLParser.FILE, 0)

        def path(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.PathContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.PathContext,i)


        def WITH(self):
            return self.getToken(ExampleDSLParser.WITH, 0)

        def AND(self):
            return self.getToken(ExampleDSLParser.AND, 0)

        def WRITE(self):
            return self.getToken(ExampleDSLParser.WRITE, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_combineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombineStatement" ):
                listener.enterCombineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombineStatement" ):
                listener.exitCombineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombineStatement" ):
                return visitor.visitCombineStatement(self)
            else:
                return visitor.visitChildren(self)




    def combineStatement(self):

        localctx = ExampleDSLParser.CombineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_combineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ExampleDSLParser.COMBINE)
            self.state = 119
            self.match(ExampleDSLParser.FILE)
            self.state = 120
            self.path()
            self.state = 121
            self.match(ExampleDSLParser.WITH)
            self.state = 122
            self.path()
            self.state = 123
            self.match(ExampleDSLParser.AND)
            self.state = 124
            self.match(ExampleDSLParser.WRITE)
            self.state = 125
            self.match(ExampleDSLParser.TO)
            self.state = 126
            self.path()
            self.state = 127
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConvertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONVERT(self):
            return self.getToken(ExampleDSLParser.CONVERT, 0)

        def FORMAT(self):
            return self.getToken(ExampleDSLParser.FORMAT, 0)

        def FROM(self):
            return self.getToken(ExampleDSLParser.FROM, 0)

        def path(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.PathContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.PathContext,i)


        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_convertStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConvertStatement" ):
                listener.enterConvertStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConvertStatement" ):
                listener.exitConvertStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConvertStatement" ):
                return visitor.visitConvertStatement(self)
            else:
                return visitor.visitChildren(self)




    def convertStatement(self):

        localctx = ExampleDSLParser.ConvertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_convertStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ExampleDSLParser.CONVERT)
            self.state = 130
            self.match(ExampleDSLParser.FORMAT)
            self.state = 131
            self.match(ExampleDSLParser.FROM)
            self.state = 132
            self.path()
            self.state = 133
            self.match(ExampleDSLParser.TO)
            self.state = 134
            self.path()
            self.state = 135
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddColumnsStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ExampleDSLParser.ADD, 0)

        def COLUMNS(self):
            return self.getToken(ExampleDSLParser.COLUMNS, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.AND)
            else:
                return self.getToken(ExampleDSLParser.AND, i)

        def SAVE(self):
            return self.getToken(ExampleDSLParser.SAVE, 0)

        def RESULT(self):
            return self.getToken(ExampleDSLParser.RESULT, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def result(self):
            return self.getTypedRuleContext(ExampleDSLParser.ResultContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_addColumnsStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddColumnsStatement" ):
                listener.enterAddColumnsStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddColumnsStatement" ):
                listener.exitAddColumnsStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddColumnsStatement" ):
                return visitor.visitAddColumnsStatement(self)
            else:
                return visitor.visitChildren(self)




    def addColumnsStatement(self):

        localctx = ExampleDSLParser.AddColumnsStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_addColumnsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ExampleDSLParser.ADD)
            self.state = 138
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 139
            self.column()
            self.state = 140
            self.match(ExampleDSLParser.AND)
            self.state = 141
            self.column()
            self.state = 142
            self.match(ExampleDSLParser.AND)
            self.state = 143
            self.match(ExampleDSLParser.SAVE)
            self.state = 144
            self.match(ExampleDSLParser.RESULT)
            self.state = 145
            self.match(ExampleDSLParser.TO)
            self.state = 146
            self.result()
            self.state = 147
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RenameColumnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RENAME(self):
            return self.getToken(ExampleDSLParser.RENAME, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_renameColumnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRenameColumnStatement" ):
                listener.enterRenameColumnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRenameColumnStatement" ):
                listener.exitRenameColumnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRenameColumnStatement" ):
                return visitor.visitRenameColumnStatement(self)
            else:
                return visitor.visitChildren(self)




    def renameColumnStatement(self):

        localctx = ExampleDSLParser.RenameColumnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_renameColumnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(ExampleDSLParser.RENAME)
            self.state = 150
            self.match(ExampleDSLParser.COLUMN)
            self.state = 151
            self.column()
            self.state = 152
            self.match(ExampleDSLParser.TO)
            self.state = 153
            self.column()
            self.state = 154
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChangeDataTypeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHANGE(self):
            return self.getToken(ExampleDSLParser.CHANGE, 0)

        def DATA(self):
            return self.getToken(ExampleDSLParser.DATA, 0)

        def TYPE(self):
            return self.getToken(ExampleDSLParser.TYPE, 0)

        def OF(self):
            return self.getToken(ExampleDSLParser.OF, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def type_(self):
            return self.getTypedRuleContext(ExampleDSLParser.TypeContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_changeDataTypeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChangeDataTypeStatement" ):
                listener.enterChangeDataTypeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChangeDataTypeStatement" ):
                listener.exitChangeDataTypeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChangeDataTypeStatement" ):
                return visitor.visitChangeDataTypeStatement(self)
            else:
                return visitor.visitChildren(self)




    def changeDataTypeStatement(self):

        localctx = ExampleDSLParser.ChangeDataTypeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_changeDataTypeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ExampleDSLParser.CHANGE)
            self.state = 157
            self.match(ExampleDSLParser.DATA)
            self.state = 158
            self.match(ExampleDSLParser.TYPE)
            self.state = 159
            self.match(ExampleDSLParser.OF)
            self.state = 160
            self.match(ExampleDSLParser.COLUMN)
            self.state = 161
            self.match(ExampleDSLParser.T__1)
            self.state = 162
            self.column()
            self.state = 163
            self.match(ExampleDSLParser.T__2)
            self.state = 164
            self.match(ExampleDSLParser.TO)
            self.state = 165
            self.type_()
            self.state = 166
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(ExampleDSLParser.TYPE, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ExampleDSLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ExampleDSLParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortDataStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SORT(self):
            return self.getToken(ExampleDSLParser.SORT, 0)

        def DATA(self):
            return self.getToken(ExampleDSLParser.DATA, 0)

        def BY(self):
            return self.getToken(ExampleDSLParser.BY, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_sortDataStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortDataStatement" ):
                listener.enterSortDataStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortDataStatement" ):
                listener.exitSortDataStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortDataStatement" ):
                return visitor.visitSortDataStatement(self)
            else:
                return visitor.visitChildren(self)




    def sortDataStatement(self):

        localctx = ExampleDSLParser.SortDataStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sortDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ExampleDSLParser.SORT)
            self.state = 171
            self.match(ExampleDSLParser.DATA)
            self.state = 172
            self.match(ExampleDSLParser.BY)
            self.state = 173
            self.match(ExampleDSLParser.COLUMN)
            self.state = 174
            self.match(ExampleDSLParser.T__1)
            self.state = 175
            self.column()
            self.state = 176
            self.match(ExampleDSLParser.T__2)
            self.state = 177
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteColumnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(ExampleDSLParser.DELETE, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_deleteColumnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteColumnStatement" ):
                listener.enterDeleteColumnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteColumnStatement" ):
                listener.exitDeleteColumnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteColumnStatement" ):
                return visitor.visitDeleteColumnStatement(self)
            else:
                return visitor.visitChildren(self)




    def deleteColumnStatement(self):

        localctx = ExampleDSLParser.DeleteColumnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_deleteColumnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ExampleDSLParser.DELETE)
            self.state = 180
            self.match(ExampleDSLParser.COLUMN)
            self.state = 181
            self.column()
            self.state = 182
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RenameFileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RENAME(self):
            return self.getToken(ExampleDSLParser.RENAME, 0)

        def OUTPUT(self):
            return self.getToken(ExampleDSLParser.OUTPUT, 0)

        def FILE(self):
            return self.getToken(ExampleDSLParser.FILE, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def file_name(self):
            return self.getTypedRuleContext(ExampleDSLParser.File_nameContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_renameFileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRenameFileStatement" ):
                listener.enterRenameFileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRenameFileStatement" ):
                listener.exitRenameFileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRenameFileStatement" ):
                return visitor.visitRenameFileStatement(self)
            else:
                return visitor.visitChildren(self)




    def renameFileStatement(self):

        localctx = ExampleDSLParser.RenameFileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_renameFileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ExampleDSLParser.RENAME)
            self.state = 185
            self.match(ExampleDSLParser.OUTPUT)
            self.state = 186
            self.match(ExampleDSLParser.FILE)
            self.state = 187
            self.match(ExampleDSLParser.TO)
            self.state = 188
            self.file_name()
            self.state = 189
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class File_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_file_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_name" ):
                listener.enterFile_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_name" ):
                listener.exitFile_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_name" ):
                return visitor.visitFile_name(self)
            else:
                return visitor.visitChildren(self)




    def file_name(self):

        localctx = ExampleDSLParser.File_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_file_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(ExampleDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApplyConditionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.from_ = None # Token
            self.to = None # Token

        def APPLY(self):
            return self.getToken(ExampleDSLParser.APPLY, 0)

        def CONDITION(self):
            return self.getToken(ExampleDSLParser.CONDITION, 0)

        def ON(self):
            return self.getToken(ExampleDSLParser.ON, 0)

        def ROWS(self):
            return self.getToken(ExampleDSLParser.ROWS, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.NUMBER)
            else:
                return self.getToken(ExampleDSLParser.NUMBER, i)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_applyConditionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplyConditionStatement" ):
                listener.enterApplyConditionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplyConditionStatement" ):
                listener.exitApplyConditionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplyConditionStatement" ):
                return visitor.visitApplyConditionStatement(self)
            else:
                return visitor.visitChildren(self)




    def applyConditionStatement(self):

        localctx = ExampleDSLParser.ApplyConditionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_applyConditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(ExampleDSLParser.APPLY)
            self.state = 194
            self.match(ExampleDSLParser.CONDITION)
            self.state = 195
            self.match(ExampleDSLParser.ON)
            self.state = 196
            self.match(ExampleDSLParser.ROWS)
            self.state = 197
            localctx.from_ = self.match(ExampleDSLParser.NUMBER)
            self.state = 198
            self.match(ExampleDSLParser.TO)
            self.state = 199
            localctx.to = self.match(ExampleDSLParser.NUMBER)
            self.state = 200
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenerateReportStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GENERATE(self):
            return self.getToken(ExampleDSLParser.GENERATE, 0)

        def REPORT(self):
            return self.getToken(ExampleDSLParser.REPORT, 0)

        def FOR(self):
            return self.getToken(ExampleDSLParser.FOR, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def BY(self):
            return self.getToken(ExampleDSLParser.BY, 0)

        def period(self):
            return self.getTypedRuleContext(ExampleDSLParser.PeriodContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_generateReportStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenerateReportStatement" ):
                listener.enterGenerateReportStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenerateReportStatement" ):
                listener.exitGenerateReportStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenerateReportStatement" ):
                return visitor.visitGenerateReportStatement(self)
            else:
                return visitor.visitChildren(self)




    def generateReportStatement(self):

        localctx = ExampleDSLParser.GenerateReportStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_generateReportStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(ExampleDSLParser.GENERATE)
            self.state = 203
            self.match(ExampleDSLParser.REPORT)
            self.state = 204
            self.match(ExampleDSLParser.FOR)
            self.state = 205
            self.match(ExampleDSLParser.COLUMN)
            self.state = 206
            self.match(ExampleDSLParser.T__1)
            self.state = 207
            self.column()
            self.state = 208
            self.match(ExampleDSLParser.T__2)
            self.state = 209
            self.match(ExampleDSLParser.BY)
            self.state = 210
            self.period()
            self.state = 211
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PeriodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_period

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeriod" ):
                listener.enterPeriod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeriod" ):
                listener.exitPeriod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPeriod" ):
                return visitor.visitPeriod(self)
            else:
                return visitor.visitChildren(self)




    def period(self):

        localctx = ExampleDSLParser.PeriodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_period)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReorderColumnsStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._STRING = None # Token
            self.columns = list() # of Tokens
            self.newOrder = list() # of Tokens

        def REORDER(self):
            return self.getToken(ExampleDSLParser.REORDER, 0)

        def COLUMNS(self):
            return self.getToken(ExampleDSLParser.COLUMNS, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_reorderColumnsStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReorderColumnsStatement" ):
                listener.enterReorderColumnsStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReorderColumnsStatement" ):
                listener.exitReorderColumnsStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReorderColumnsStatement" ):
                return visitor.visitReorderColumnsStatement(self)
            else:
                return visitor.visitChildren(self)




    def reorderColumnsStatement(self):

        localctx = ExampleDSLParser.ReorderColumnsStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_reorderColumnsStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(ExampleDSLParser.REORDER)
            self.state = 216
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 217
            localctx._STRING = self.match(ExampleDSLParser.STRING)
            localctx.columns.append(localctx._STRING)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 218
                self.match(ExampleDSLParser.T__6)
                self.state = 219
                localctx._STRING = self.match(ExampleDSLParser.STRING)
                localctx.columns.append(localctx._STRING)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self.match(ExampleDSLParser.TO)
            self.state = 226
            localctx._STRING = self.match(ExampleDSLParser.STRING)
            localctx.newOrder.append(localctx._STRING)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 227
                self.match(ExampleDSLParser.T__6)
                self.state = 228
                localctx._STRING = self.match(ExampleDSLParser.STRING)
                localctx.newOrder.append(localctx._STRING)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupByStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(ExampleDSLParser.GROUP, 0)

        def BY(self):
            return self.getToken(ExampleDSLParser.BY, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def AND(self):
            return self.getToken(ExampleDSLParser.AND, 0)

        def SUM(self):
            return self.getToken(ExampleDSLParser.SUM, 0)

        def VALUES(self):
            return self.getToken(ExampleDSLParser.VALUES, 0)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_groupByStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupByStatement" ):
                listener.enterGroupByStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupByStatement" ):
                listener.exitGroupByStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupByStatement" ):
                return visitor.visitGroupByStatement(self)
            else:
                return visitor.visitChildren(self)




    def groupByStatement(self):

        localctx = ExampleDSLParser.GroupByStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_groupByStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ExampleDSLParser.GROUP)
            self.state = 237
            self.match(ExampleDSLParser.BY)
            self.state = 238
            self.column()
            self.state = 239
            self.match(ExampleDSLParser.AND)
            self.state = 240
            self.match(ExampleDSLParser.SUM)
            self.state = 241
            self.match(ExampleDSLParser.VALUES)
            self.state = 242
            self.match(ExampleDSLParser.IN)
            self.state = 243
            self.column()
            self.state = 244
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterRowsStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(ExampleDSLParser.FILTER, 0)

        def ROWS(self):
            return self.getToken(ExampleDSLParser.ROWS, 0)

        def WHERE(self):
            return self.getToken(ExampleDSLParser.WHERE, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def value(self):
            return self.getTypedRuleContext(ExampleDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_filterRowsStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterRowsStatement" ):
                listener.enterFilterRowsStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterRowsStatement" ):
                listener.exitFilterRowsStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterRowsStatement" ):
                return visitor.visitFilterRowsStatement(self)
            else:
                return visitor.visitChildren(self)




    def filterRowsStatement(self):

        localctx = ExampleDSLParser.FilterRowsStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_filterRowsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ExampleDSLParser.FILTER)
            self.state = 247
            self.match(ExampleDSLParser.ROWS)
            self.state = 248
            self.match(ExampleDSLParser.WHERE)
            self.state = 249
            self.column()
            self.state = 250
            self.match(ExampleDSLParser.T__7)
            self.state = 251
            self.value()
            self.state = 252
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExampleDSLParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ExampleDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(ExampleDSLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SearchTextStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.text = None # Token

        def SEARCH(self):
            return self.getToken(ExampleDSLParser.SEARCH, 0)

        def FOR(self):
            return self.getToken(ExampleDSLParser.FOR, 0)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_searchTextStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearchTextStatement" ):
                listener.enterSearchTextStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearchTextStatement" ):
                listener.exitSearchTextStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSearchTextStatement" ):
                return visitor.visitSearchTextStatement(self)
            else:
                return visitor.visitChildren(self)




    def searchTextStatement(self):

        localctx = ExampleDSLParser.SearchTextStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_searchTextStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ExampleDSLParser.SEARCH)
            self.state = 257
            self.match(ExampleDSLParser.FOR)
            self.state = 258
            localctx.text = self.match(ExampleDSLParser.STRING)
            self.state = 259
            self.match(ExampleDSLParser.IN)
            self.state = 260
            self.match(ExampleDSLParser.COLUMN)
            self.state = 261
            self.match(ExampleDSLParser.T__1)
            self.state = 262
            self.column()
            self.state = 263
            self.match(ExampleDSLParser.T__2)
            self.state = 264
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReplaceValuesStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPLACE(self):
            return self.getToken(ExampleDSLParser.REPLACE, 0)

        def VALUES(self):
            return self.getToken(ExampleDSLParser.VALUES, 0)

        def values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ValuesContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ValuesContext,i)


        def WITH(self):
            return self.getToken(ExampleDSLParser.WITH, 0)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_replaceValuesStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReplaceValuesStatement" ):
                listener.enterReplaceValuesStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReplaceValuesStatement" ):
                listener.exitReplaceValuesStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplaceValuesStatement" ):
                return visitor.visitReplaceValuesStatement(self)
            else:
                return visitor.visitChildren(self)




    def replaceValuesStatement(self):

        localctx = ExampleDSLParser.ReplaceValuesStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_replaceValuesStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(ExampleDSLParser.REPLACE)
            self.state = 267
            self.match(ExampleDSLParser.VALUES)
            self.state = 268
            self.values()
            self.state = 269
            self.match(ExampleDSLParser.WITH)
            self.state = 270
            self.values()
            self.state = 271
            self.match(ExampleDSLParser.IN)
            self.state = 272
            self.match(ExampleDSLParser.COLUMN)
            self.state = 273
            self.match(ExampleDSLParser.T__1)
            self.state = 274
            self.column()
            self.state = 275
            self.match(ExampleDSLParser.T__2)
            self.state = 276
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExampleDSLParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValues" ):
                return visitor.visitValues(self)
            else:
                return visitor.visitChildren(self)




    def values(self):

        localctx = ExampleDSLParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            _la = self._input.LA(1)
            if not(_la==60 or _la==61):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddConditionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ExampleDSLParser.ADD, 0)

        def CONDITION(self):
            return self.getToken(ExampleDSLParser.CONDITION, 0)

        def WHERE(self):
            return self.getToken(ExampleDSLParser.WHERE, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def value(self):
            return self.getTypedRuleContext(ExampleDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_addConditionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddConditionStatement" ):
                listener.enterAddConditionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddConditionStatement" ):
                listener.exitAddConditionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddConditionStatement" ):
                return visitor.visitAddConditionStatement(self)
            else:
                return visitor.visitChildren(self)




    def addConditionStatement(self):

        localctx = ExampleDSLParser.AddConditionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_addConditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ExampleDSLParser.ADD)
            self.state = 281
            self.match(ExampleDSLParser.CONDITION)
            self.state = 282
            self.match(ExampleDSLParser.WHERE)
            self.state = 283
            self.column()
            self.state = 284
            self.match(ExampleDSLParser.T__7)
            self.state = 285
            self.value()
            self.state = 286
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveDuplicatesStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMOVE(self):
            return self.getToken(ExampleDSLParser.REMOVE, 0)

        def DUPLICATE(self):
            return self.getToken(ExampleDSLParser.DUPLICATE, 0)

        def ROWS(self):
            return self.getToken(ExampleDSLParser.ROWS, 0)

        def BASED(self):
            return self.getToken(ExampleDSLParser.BASED, 0)

        def ON(self):
            return self.getToken(ExampleDSLParser.ON, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_removeDuplicatesStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemoveDuplicatesStatement" ):
                listener.enterRemoveDuplicatesStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemoveDuplicatesStatement" ):
                listener.exitRemoveDuplicatesStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemoveDuplicatesStatement" ):
                return visitor.visitRemoveDuplicatesStatement(self)
            else:
                return visitor.visitChildren(self)




    def removeDuplicatesStatement(self):

        localctx = ExampleDSLParser.RemoveDuplicatesStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_removeDuplicatesStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ExampleDSLParser.REMOVE)
            self.state = 289
            self.match(ExampleDSLParser.DUPLICATE)
            self.state = 290
            self.match(ExampleDSLParser.ROWS)
            self.state = 291
            self.match(ExampleDSLParser.BASED)
            self.state = 292
            self.match(ExampleDSLParser.ON)
            self.state = 293
            self.match(ExampleDSLParser.COLUMN)
            self.state = 294
            self.match(ExampleDSLParser.T__1)
            self.state = 295
            self.column()
            self.state = 296
            self.match(ExampleDSLParser.T__2)
            self.state = 297
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SplitDataStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPLIT(self):
            return self.getToken(ExampleDSLParser.SPLIT, 0)

        def DATA(self):
            return self.getToken(ExampleDSLParser.DATA, 0)

        def BASED(self):
            return self.getToken(ExampleDSLParser.BASED, 0)

        def ON(self):
            return self.getToken(ExampleDSLParser.ON, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def AND(self):
            return self.getToken(ExampleDSLParser.AND, 0)

        def SAVE(self):
            return self.getToken(ExampleDSLParser.SAVE, 0)

        def RESULTS(self):
            return self.getToken(ExampleDSLParser.RESULTS, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def SEPARATE(self):
            return self.getToken(ExampleDSLParser.SEPARATE, 0)

        def FILES(self):
            return self.getToken(ExampleDSLParser.FILES, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_splitDataStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplitDataStatement" ):
                listener.enterSplitDataStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplitDataStatement" ):
                listener.exitSplitDataStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSplitDataStatement" ):
                return visitor.visitSplitDataStatement(self)
            else:
                return visitor.visitChildren(self)




    def splitDataStatement(self):

        localctx = ExampleDSLParser.SplitDataStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_splitDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ExampleDSLParser.SPLIT)
            self.state = 300
            self.match(ExampleDSLParser.DATA)
            self.state = 301
            self.match(ExampleDSLParser.BASED)
            self.state = 302
            self.match(ExampleDSLParser.ON)
            self.state = 303
            self.match(ExampleDSLParser.COLUMN)
            self.state = 304
            self.match(ExampleDSLParser.T__1)
            self.state = 305
            self.column()
            self.state = 306
            self.match(ExampleDSLParser.T__2)
            self.state = 307
            self.match(ExampleDSLParser.AND)
            self.state = 308
            self.match(ExampleDSLParser.SAVE)
            self.state = 309
            self.match(ExampleDSLParser.RESULTS)
            self.state = 310
            self.match(ExampleDSLParser.TO)
            self.state = 311
            self.match(ExampleDSLParser.SEPARATE)
            self.state = 312
            self.match(ExampleDSLParser.FILES)
            self.state = 313
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CombineColumnsStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMBINE(self):
            return self.getToken(ExampleDSLParser.COMBINE, 0)

        def COLUMNS(self):
            return self.getToken(ExampleDSLParser.COLUMNS, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.AND)
            else:
                return self.getToken(ExampleDSLParser.AND, i)

        def SAVE(self):
            return self.getToken(ExampleDSLParser.SAVE, 0)

        def RESULT(self):
            return self.getToken(ExampleDSLParser.RESULT, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def result(self):
            return self.getTypedRuleContext(ExampleDSLParser.ResultContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_combineColumnsStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombineColumnsStatement" ):
                listener.enterCombineColumnsStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombineColumnsStatement" ):
                listener.exitCombineColumnsStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombineColumnsStatement" ):
                return visitor.visitCombineColumnsStatement(self)
            else:
                return visitor.visitChildren(self)




    def combineColumnsStatement(self):

        localctx = ExampleDSLParser.CombineColumnsStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_combineColumnsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ExampleDSLParser.COMBINE)
            self.state = 316
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 317
            self.column()
            self.state = 318
            self.match(ExampleDSLParser.AND)
            self.state = 319
            self.column()
            self.state = 320
            self.match(ExampleDSLParser.AND)
            self.state = 321
            self.match(ExampleDSLParser.SAVE)
            self.state = 322
            self.match(ExampleDSLParser.RESULT)
            self.state = 323
            self.match(ExampleDSLParser.TO)
            self.state = 324
            self.result()
            self.state = 325
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResizeDataStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RESIZE(self):
            return self.getToken(ExampleDSLParser.RESIZE, 0)

        def DATA(self):
            return self.getToken(ExampleDSLParser.DATA, 0)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def BY(self):
            return self.getToken(ExampleDSLParser.BY, 0)

        def MULTIPLYING(self):
            return self.getToken(ExampleDSLParser.MULTIPLYING, 0)

        def WITH(self):
            return self.getToken(ExampleDSLParser.WITH, 0)

        def value(self):
            return self.getTypedRuleContext(ExampleDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_resizeDataStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResizeDataStatement" ):
                listener.enterResizeDataStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResizeDataStatement" ):
                listener.exitResizeDataStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResizeDataStatement" ):
                return visitor.visitResizeDataStatement(self)
            else:
                return visitor.visitChildren(self)




    def resizeDataStatement(self):

        localctx = ExampleDSLParser.ResizeDataStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_resizeDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ExampleDSLParser.RESIZE)
            self.state = 328
            self.match(ExampleDSLParser.DATA)
            self.state = 329
            self.match(ExampleDSLParser.IN)
            self.state = 330
            self.match(ExampleDSLParser.COLUMN)
            self.state = 331
            self.match(ExampleDSLParser.T__1)
            self.state = 332
            self.column()
            self.state = 333
            self.match(ExampleDSLParser.T__2)
            self.state = 334
            self.match(ExampleDSLParser.BY)
            self.state = 335
            self.match(ExampleDSLParser.MULTIPLYING)
            self.state = 336
            self.match(ExampleDSLParser.WITH)
            self.state = 337
            self.value()
            self.state = 338
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





