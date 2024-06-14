# Generated from E:/uni file/compiler/hw5/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
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
        4,1,63,302,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,87,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,5,13,186,8,13,10,13,
        12,13,189,9,13,1,13,1,13,1,13,1,13,5,13,195,8,13,10,13,12,13,198,
        9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        0,0,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,0,0,302,0,47,1,0,0,0,2,72,1,0,0,0,4,86,1,0,0,0,6,88,1,0,0,
        0,8,100,1,0,0,0,10,108,1,0,0,0,12,120,1,0,0,0,14,127,1,0,0,0,16,
        139,1,0,0,0,18,148,1,0,0,0,20,153,1,0,0,0,22,160,1,0,0,0,24,169,
        1,0,0,0,26,180,1,0,0,0,28,201,1,0,0,0,30,211,1,0,0,0,32,219,1,0,
        0,0,34,229,1,0,0,0,36,241,1,0,0,0,38,249,1,0,0,0,40,260,1,0,0,0,
        42,276,1,0,0,0,44,288,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,49,
        1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,1,1,0,0,0,51,73,3,4,2,0,52,
        73,3,6,3,0,53,73,3,8,4,0,54,73,3,10,5,0,55,73,3,12,6,0,56,73,3,14,
        7,0,57,73,3,16,8,0,58,73,3,18,9,0,59,73,3,20,10,0,60,73,3,22,11,
        0,61,73,3,24,12,0,62,73,3,26,13,0,63,73,3,28,14,0,64,73,3,30,15,
        0,65,73,3,32,16,0,66,73,3,34,17,0,67,73,3,36,18,0,68,73,3,38,19,
        0,69,73,3,40,20,0,70,73,3,42,21,0,71,73,3,44,22,0,72,51,1,0,0,0,
        72,52,1,0,0,0,72,53,1,0,0,0,72,54,1,0,0,0,72,55,1,0,0,0,72,56,1,
        0,0,0,72,57,1,0,0,0,72,58,1,0,0,0,72,59,1,0,0,0,72,60,1,0,0,0,72,
        61,1,0,0,0,72,62,1,0,0,0,72,63,1,0,0,0,72,64,1,0,0,0,72,65,1,0,0,
        0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,72,70,
        1,0,0,0,72,71,1,0,0,0,73,3,1,0,0,0,74,75,5,25,0,0,75,76,5,26,0,0,
        76,77,5,27,0,0,77,78,5,6,0,0,78,79,5,55,0,0,79,87,5,1,0,0,80,81,
        5,25,0,0,81,82,5,26,0,0,82,83,5,27,0,0,83,84,5,7,0,0,84,85,5,55,
        0,0,85,87,5,1,0,0,86,74,1,0,0,0,86,80,1,0,0,0,87,5,1,0,0,0,88,89,
        5,8,0,0,89,90,5,26,0,0,90,91,5,55,0,0,91,92,5,40,0,0,92,93,5,26,
        0,0,93,94,5,55,0,0,94,95,5,41,0,0,95,96,5,58,0,0,96,97,5,39,0,0,
        97,98,5,55,0,0,98,99,5,1,0,0,99,7,1,0,0,0,100,101,5,9,0,0,101,102,
        5,28,0,0,102,103,5,43,0,0,103,104,5,55,0,0,104,105,5,39,0,0,105,
        106,5,55,0,0,106,107,5,1,0,0,107,9,1,0,0,0,108,109,5,10,0,0,109,
        110,5,31,0,0,110,111,5,55,0,0,111,112,5,41,0,0,112,113,5,55,0,0,
        113,114,5,41,0,0,114,115,5,49,0,0,115,116,5,38,0,0,116,117,5,39,
        0,0,117,118,5,55,0,0,118,119,5,1,0,0,119,11,1,0,0,0,120,121,5,11,
        0,0,121,122,5,30,0,0,122,123,5,55,0,0,123,124,5,39,0,0,124,125,5,
        55,0,0,125,126,5,1,0,0,126,13,1,0,0,0,127,128,5,12,0,0,128,129,5,
        29,0,0,129,130,5,32,0,0,130,131,5,46,0,0,131,132,5,30,0,0,132,133,
        5,2,0,0,133,134,5,55,0,0,134,135,5,3,0,0,135,136,5,39,0,0,136,137,
        5,32,0,0,137,138,5,1,0,0,138,15,1,0,0,0,139,140,5,13,0,0,140,141,
        5,29,0,0,141,142,5,42,0,0,142,143,5,30,0,0,143,144,5,2,0,0,144,145,
        5,55,0,0,145,146,5,3,0,0,146,147,5,1,0,0,147,17,1,0,0,0,148,149,
        5,14,0,0,149,150,5,30,0,0,150,151,5,55,0,0,151,152,5,1,0,0,152,19,
        1,0,0,0,153,154,5,11,0,0,154,155,5,7,0,0,155,156,5,26,0,0,156,157,
        5,39,0,0,157,158,5,55,0,0,158,159,5,1,0,0,159,21,1,0,0,0,160,161,
        5,15,0,0,161,162,5,35,0,0,162,163,5,45,0,0,163,164,5,33,0,0,164,
        165,5,54,0,0,165,166,5,39,0,0,166,167,5,54,0,0,167,168,5,1,0,0,168,
        23,1,0,0,0,169,170,5,16,0,0,170,171,5,59,0,0,171,172,5,47,0,0,172,
        173,5,30,0,0,173,174,5,2,0,0,174,175,5,55,0,0,175,176,5,3,0,0,176,
        177,5,42,0,0,177,178,5,55,0,0,178,179,5,1,0,0,179,25,1,0,0,0,180,
        181,5,17,0,0,181,182,5,31,0,0,182,187,5,55,0,0,183,184,5,4,0,0,184,
        186,5,55,0,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,
        188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,0,0,190,191,5,39,0,0,191,
        196,5,55,0,0,192,193,5,4,0,0,193,195,5,55,0,0,194,192,1,0,0,0,195,
        198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,
        196,1,0,0,0,199,200,5,1,0,0,200,27,1,0,0,0,201,202,5,18,0,0,202,
        203,5,42,0,0,203,204,5,55,0,0,204,205,5,41,0,0,205,206,5,51,0,0,
        206,207,5,36,0,0,207,208,5,37,0,0,208,209,5,55,0,0,209,210,5,1,0,
        0,210,29,1,0,0,0,211,212,5,19,0,0,212,213,5,33,0,0,213,214,5,44,
        0,0,214,215,5,55,0,0,215,216,5,5,0,0,216,217,5,54,0,0,217,218,5,
        1,0,0,218,31,1,0,0,0,219,220,5,20,0,0,220,221,5,47,0,0,221,222,5,
        55,0,0,222,223,5,37,0,0,223,224,5,30,0,0,224,225,5,2,0,0,225,226,
        5,55,0,0,226,227,5,3,0,0,227,228,5,1,0,0,228,33,1,0,0,0,229,230,
        5,21,0,0,230,231,5,36,0,0,231,232,5,55,0,0,232,233,5,40,0,0,233,
        234,5,55,0,0,234,235,5,37,0,0,235,236,5,30,0,0,236,237,5,2,0,0,237,
        238,5,55,0,0,238,239,5,3,0,0,239,240,5,1,0,0,240,35,1,0,0,0,241,
        242,5,10,0,0,242,243,5,35,0,0,243,244,5,44,0,0,244,245,5,55,0,0,
        245,246,5,5,0,0,246,247,5,54,0,0,247,248,5,1,0,0,248,37,1,0,0,0,
        249,250,5,22,0,0,250,251,5,60,0,0,251,252,5,33,0,0,252,253,5,50,
        0,0,253,254,5,45,0,0,254,255,5,30,0,0,255,256,5,2,0,0,256,257,5,
        55,0,0,257,258,5,3,0,0,258,259,5,1,0,0,259,39,1,0,0,0,260,261,5,
        23,0,0,261,262,5,29,0,0,262,263,5,50,0,0,263,264,5,45,0,0,264,265,
        5,30,0,0,265,266,5,2,0,0,266,267,5,55,0,0,267,268,5,3,0,0,268,269,
        5,41,0,0,269,270,5,49,0,0,270,271,5,61,0,0,271,272,5,39,0,0,272,
        273,5,62,0,0,273,274,5,63,0,0,274,275,5,1,0,0,275,41,1,0,0,0,276,
        277,5,8,0,0,277,278,5,31,0,0,278,279,5,55,0,0,279,280,5,41,0,0,280,
        281,5,55,0,0,281,282,5,41,0,0,282,283,5,49,0,0,283,284,5,38,0,0,
        284,285,5,39,0,0,285,286,5,55,0,0,286,287,5,1,0,0,287,43,1,0,0,0,
        288,289,5,24,0,0,289,290,5,29,0,0,290,291,5,37,0,0,291,292,5,30,
        0,0,292,293,5,2,0,0,293,294,5,55,0,0,294,295,5,3,0,0,295,296,5,42,
        0,0,296,297,5,53,0,0,297,298,5,40,0,0,298,299,5,54,0,0,299,300,5,
        1,0,0,300,45,1,0,0,0,5,49,72,86,187,196
    ]

class ExampleDSLParser ( Parser ):

    grammarFileName = "ExampleDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "','", "'>'", "'input'", 
                     "'output'", "'Combine'", "'Convert'", "'Add'", "'Rename'", 
                     "'Change'", "'Sort'", "'Delete'", "'Apply'", "'Generate'", 
                     "'Reorder'", "'Group'", "'Filter'", "'Search'", "'Replace'", 
                     "'Remove'", "'Split'", "'Resize'", "'Set'", "'file'", 
                     "'path'", "'format'", "'data'", "'column'", "'columns'", 
                     "'type'", "'rows'", "'row'", "'condition'", "'values'", 
                     "'in'", "'result'", "'to'", "'with'", "'and'", "'by'", 
                     "'from'", "'where'", "'on'", "'of'", "'for'", "'as'", 
                     "'save'", "'based'", "'sum'", "'new'", "'multiplying'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INPUT", "OUTPUT", "COMBINE", 
                      "CONVERT", "ADD", "RENAME", "CHANGE", "SORT", "DELETE", 
                      "APPLY", "GENERATE", "REORDER", "GROUP", "FILTER", 
                      "SEARCH", "REPLACE", "REMOVE", "SPLIT", "RESIZE", 
                      "SET", "FILE", "PATH", "FORMAT", "DATA", "COLUMN", 
                      "COLUMNS", "TYPE", "ROWS", "ROW", "CONDITION", "VALUES", 
                      "IN", "RESULT", "TO", "WITH", "AND", "BY", "FROM", 
                      "WHERE", "ON", "OF", "FOR", "AS", "SAVE", "BASED", 
                      "SUM", "NEW", "MULTIPLYING", "NUMBER", "STRING", "ID", 
                      "WS", "WRITE", "REPORT", "DUPLICATE", "RESULTS", "SEPARATE", 
                      "FILES" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_setFilePathStatement = 2
    RULE_combineStatement = 3
    RULE_convertStatement = 4
    RULE_addColumnsStatement = 5
    RULE_renameColumnStatement = 6
    RULE_changeDataTypeStatement = 7
    RULE_sortDataStatement = 8
    RULE_deleteColumnStatement = 9
    RULE_renameFileStatement = 10
    RULE_applyConditionStatement = 11
    RULE_generateReportStatement = 12
    RULE_reorderColumnsStatement = 13
    RULE_groupByStatement = 14
    RULE_filterRowsStatement = 15
    RULE_searchTextStatement = 16
    RULE_replaceValuesStatement = 17
    RULE_addConditionStatement = 18
    RULE_removeDuplicatesStatement = 19
    RULE_splitDataStatement = 20
    RULE_combineColumnsStatement = 21
    RULE_resizeDataStatement = 22

    ruleNames =  [ "program", "statement", "setFilePathStatement", "combineStatement", 
                   "convertStatement", "addColumnsStatement", "renameColumnStatement", 
                   "changeDataTypeStatement", "sortDataStatement", "deleteColumnStatement", 
                   "renameFileStatement", "applyConditionStatement", "generateReportStatement", 
                   "reorderColumnsStatement", "groupByStatement", "filterRowsStatement", 
                   "searchTextStatement", "replaceValuesStatement", "addConditionStatement", 
                   "removeDuplicatesStatement", "splitDataStatement", "combineColumnsStatement", 
                   "resizeDataStatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    INPUT=6
    OUTPUT=7
    COMBINE=8
    CONVERT=9
    ADD=10
    RENAME=11
    CHANGE=12
    SORT=13
    DELETE=14
    APPLY=15
    GENERATE=16
    REORDER=17
    GROUP=18
    FILTER=19
    SEARCH=20
    REPLACE=21
    REMOVE=22
    SPLIT=23
    RESIZE=24
    SET=25
    FILE=26
    PATH=27
    FORMAT=28
    DATA=29
    COLUMN=30
    COLUMNS=31
    TYPE=32
    ROWS=33
    ROW=34
    CONDITION=35
    VALUES=36
    IN=37
    RESULT=38
    TO=39
    WITH=40
    AND=41
    BY=42
    FROM=43
    WHERE=44
    ON=45
    OF=46
    FOR=47
    AS=48
    SAVE=49
    BASED=50
    SUM=51
    NEW=52
    MULTIPLYING=53
    NUMBER=54
    STRING=55
    ID=56
    WS=57
    WRITE=58
    REPORT=59
    DUPLICATE=60
    RESULTS=61
    SEPARATE=62
    FILES=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.statement()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67108608) != 0)):
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

        def setFilePathStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.SetFilePathStatementContext,0)


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
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.setFilePathStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.combineStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.convertStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.addColumnsStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.renameColumnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.changeDataTypeStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.sortDataStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 58
                self.deleteColumnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.renameFileStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 60
                self.applyConditionStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 61
                self.generateReportStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 62
                self.reorderColumnsStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 63
                self.groupByStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 64
                self.filterRowsStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 65
                self.searchTextStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 66
                self.replaceValuesStatement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 67
                self.addConditionStatement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 68
                self.removeDuplicatesStatement()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 69
                self.splitDataStatement()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 70
                self.combineColumnsStatement()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 71
                self.resizeDataStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetFilePathStatementContext(ParserRuleContext):
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def OUTPUT(self):
            return self.getToken(ExampleDSLParser.OUTPUT, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_setFilePathStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetFilePathStatement" ):
                listener.enterSetFilePathStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetFilePathStatement" ):
                listener.exitSetFilePathStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetFilePathStatement" ):
                return visitor.visitSetFilePathStatement(self)
            else:
                return visitor.visitChildren(self)




    def setFilePathStatement(self):

        localctx = ExampleDSLParser.SetFilePathStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_setFilePathStatement)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(ExampleDSLParser.SET)
                self.state = 75
                self.match(ExampleDSLParser.FILE)
                self.state = 76
                self.match(ExampleDSLParser.PATH)
                self.state = 77
                self.match(ExampleDSLParser.INPUT)
                self.state = 78
                self.match(ExampleDSLParser.STRING)
                self.state = 79
                self.match(ExampleDSLParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(ExampleDSLParser.SET)
                self.state = 81
                self.match(ExampleDSLParser.FILE)
                self.state = 82
                self.match(ExampleDSLParser.PATH)
                self.state = 83
                self.match(ExampleDSLParser.OUTPUT)
                self.state = 84
                self.match(ExampleDSLParser.STRING)
                self.state = 85
                self.match(ExampleDSLParser.T__0)
                pass


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

        def FILE(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.FILE)
            else:
                return self.getToken(ExampleDSLParser.FILE, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

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
        self.enterRule(localctx, 6, self.RULE_combineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ExampleDSLParser.COMBINE)
            self.state = 89
            self.match(ExampleDSLParser.FILE)
            self.state = 90
            self.match(ExampleDSLParser.STRING)
            self.state = 91
            self.match(ExampleDSLParser.WITH)
            self.state = 92
            self.match(ExampleDSLParser.FILE)
            self.state = 93
            self.match(ExampleDSLParser.STRING)
            self.state = 94
            self.match(ExampleDSLParser.AND)
            self.state = 95
            self.match(ExampleDSLParser.WRITE)
            self.state = 96
            self.match(ExampleDSLParser.TO)
            self.state = 97
            self.match(ExampleDSLParser.STRING)
            self.state = 98
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

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
        self.enterRule(localctx, 8, self.RULE_convertStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ExampleDSLParser.CONVERT)
            self.state = 101
            self.match(ExampleDSLParser.FORMAT)
            self.state = 102
            self.match(ExampleDSLParser.FROM)
            self.state = 103
            self.match(ExampleDSLParser.STRING)
            self.state = 104
            self.match(ExampleDSLParser.TO)
            self.state = 105
            self.match(ExampleDSLParser.STRING)
            self.state = 106
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

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
        self.enterRule(localctx, 10, self.RULE_addColumnsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(ExampleDSLParser.ADD)
            self.state = 109
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 110
            self.match(ExampleDSLParser.STRING)
            self.state = 111
            self.match(ExampleDSLParser.AND)
            self.state = 112
            self.match(ExampleDSLParser.STRING)
            self.state = 113
            self.match(ExampleDSLParser.AND)
            self.state = 114
            self.match(ExampleDSLParser.SAVE)
            self.state = 115
            self.match(ExampleDSLParser.RESULT)
            self.state = 116
            self.match(ExampleDSLParser.TO)
            self.state = 117
            self.match(ExampleDSLParser.STRING)
            self.state = 118
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

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
        self.enterRule(localctx, 12, self.RULE_renameColumnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ExampleDSLParser.RENAME)
            self.state = 121
            self.match(ExampleDSLParser.COLUMN)
            self.state = 122
            self.match(ExampleDSLParser.STRING)
            self.state = 123
            self.match(ExampleDSLParser.TO)
            self.state = 124
            self.match(ExampleDSLParser.STRING)
            self.state = 125
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

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.TYPE)
            else:
                return self.getToken(ExampleDSLParser.TYPE, i)

        def OF(self):
            return self.getToken(ExampleDSLParser.OF, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

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
        self.enterRule(localctx, 14, self.RULE_changeDataTypeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ExampleDSLParser.CHANGE)
            self.state = 128
            self.match(ExampleDSLParser.DATA)
            self.state = 129
            self.match(ExampleDSLParser.TYPE)
            self.state = 130
            self.match(ExampleDSLParser.OF)
            self.state = 131
            self.match(ExampleDSLParser.COLUMN)
            self.state = 132
            self.match(ExampleDSLParser.T__1)
            self.state = 133
            self.match(ExampleDSLParser.STRING)
            self.state = 134
            self.match(ExampleDSLParser.T__2)
            self.state = 135
            self.match(ExampleDSLParser.TO)
            self.state = 136
            self.match(ExampleDSLParser.TYPE)
            self.state = 137
            self.match(ExampleDSLParser.T__0)
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

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
        self.enterRule(localctx, 16, self.RULE_sortDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ExampleDSLParser.SORT)
            self.state = 140
            self.match(ExampleDSLParser.DATA)
            self.state = 141
            self.match(ExampleDSLParser.BY)
            self.state = 142
            self.match(ExampleDSLParser.COLUMN)
            self.state = 143
            self.match(ExampleDSLParser.T__1)
            self.state = 144
            self.match(ExampleDSLParser.STRING)
            self.state = 145
            self.match(ExampleDSLParser.T__2)
            self.state = 146
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

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
        self.enterRule(localctx, 18, self.RULE_deleteColumnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ExampleDSLParser.DELETE)
            self.state = 149
            self.match(ExampleDSLParser.COLUMN)
            self.state = 150
            self.match(ExampleDSLParser.STRING)
            self.state = 151
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

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
        self.enterRule(localctx, 20, self.RULE_renameFileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ExampleDSLParser.RENAME)
            self.state = 154
            self.match(ExampleDSLParser.OUTPUT)
            self.state = 155
            self.match(ExampleDSLParser.FILE)
            self.state = 156
            self.match(ExampleDSLParser.TO)
            self.state = 157
            self.match(ExampleDSLParser.STRING)
            self.state = 158
            self.match(ExampleDSLParser.T__0)
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

        def APPLY(self):
            return self.getToken(ExampleDSLParser.APPLY, 0)

        def CONDITION(self):
            return self.getToken(ExampleDSLParser.CONDITION, 0)

        def ON(self):
            return self.getToken(ExampleDSLParser.ON, 0)

        def ROWS(self):
            return self.getToken(ExampleDSLParser.ROWS, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.NUMBER)
            else:
                return self.getToken(ExampleDSLParser.NUMBER, i)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

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
        self.enterRule(localctx, 22, self.RULE_applyConditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ExampleDSLParser.APPLY)
            self.state = 161
            self.match(ExampleDSLParser.CONDITION)
            self.state = 162
            self.match(ExampleDSLParser.ON)
            self.state = 163
            self.match(ExampleDSLParser.ROWS)
            self.state = 164
            self.match(ExampleDSLParser.NUMBER)
            self.state = 165
            self.match(ExampleDSLParser.TO)
            self.state = 166
            self.match(ExampleDSLParser.NUMBER)
            self.state = 167
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

        def BY(self):
            return self.getToken(ExampleDSLParser.BY, 0)

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
        self.enterRule(localctx, 24, self.RULE_generateReportStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ExampleDSLParser.GENERATE)
            self.state = 170
            self.match(ExampleDSLParser.REPORT)
            self.state = 171
            self.match(ExampleDSLParser.FOR)
            self.state = 172
            self.match(ExampleDSLParser.COLUMN)
            self.state = 173
            self.match(ExampleDSLParser.T__1)
            self.state = 174
            self.match(ExampleDSLParser.STRING)
            self.state = 175
            self.match(ExampleDSLParser.T__2)
            self.state = 176
            self.match(ExampleDSLParser.BY)
            self.state = 177
            self.match(ExampleDSLParser.STRING)
            self.state = 178
            self.match(ExampleDSLParser.T__0)
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

        def REORDER(self):
            return self.getToken(ExampleDSLParser.REORDER, 0)

        def COLUMNS(self):
            return self.getToken(ExampleDSLParser.COLUMNS, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

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
        self.enterRule(localctx, 26, self.RULE_reorderColumnsStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ExampleDSLParser.REORDER)
            self.state = 181
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 182
            self.match(ExampleDSLParser.STRING)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 183
                self.match(ExampleDSLParser.T__3)
                self.state = 184
                self.match(ExampleDSLParser.STRING)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.match(ExampleDSLParser.TO)
            self.state = 191
            self.match(ExampleDSLParser.STRING)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 192
                self.match(ExampleDSLParser.T__3)
                self.state = 193
                self.match(ExampleDSLParser.STRING)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

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
        self.enterRule(localctx, 28, self.RULE_groupByStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(ExampleDSLParser.GROUP)
            self.state = 202
            self.match(ExampleDSLParser.BY)
            self.state = 203
            self.match(ExampleDSLParser.STRING)
            self.state = 204
            self.match(ExampleDSLParser.AND)
            self.state = 205
            self.match(ExampleDSLParser.SUM)
            self.state = 206
            self.match(ExampleDSLParser.VALUES)
            self.state = 207
            self.match(ExampleDSLParser.IN)
            self.state = 208
            self.match(ExampleDSLParser.STRING)
            self.state = 209
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ExampleDSLParser.NUMBER, 0)

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
        self.enterRule(localctx, 30, self.RULE_filterRowsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(ExampleDSLParser.FILTER)
            self.state = 212
            self.match(ExampleDSLParser.ROWS)
            self.state = 213
            self.match(ExampleDSLParser.WHERE)
            self.state = 214
            self.match(ExampleDSLParser.STRING)
            self.state = 215
            self.match(ExampleDSLParser.T__4)
            self.state = 216
            self.match(ExampleDSLParser.NUMBER)
            self.state = 217
            self.match(ExampleDSLParser.T__0)
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

        def SEARCH(self):
            return self.getToken(ExampleDSLParser.SEARCH, 0)

        def FOR(self):
            return self.getToken(ExampleDSLParser.FOR, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

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
        self.enterRule(localctx, 32, self.RULE_searchTextStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(ExampleDSLParser.SEARCH)
            self.state = 220
            self.match(ExampleDSLParser.FOR)
            self.state = 221
            self.match(ExampleDSLParser.STRING)
            self.state = 222
            self.match(ExampleDSLParser.IN)
            self.state = 223
            self.match(ExampleDSLParser.COLUMN)
            self.state = 224
            self.match(ExampleDSLParser.T__1)
            self.state = 225
            self.match(ExampleDSLParser.STRING)
            self.state = 226
            self.match(ExampleDSLParser.T__2)
            self.state = 227
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

        def WITH(self):
            return self.getToken(ExampleDSLParser.WITH, 0)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

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
        self.enterRule(localctx, 34, self.RULE_replaceValuesStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ExampleDSLParser.REPLACE)
            self.state = 230
            self.match(ExampleDSLParser.VALUES)
            self.state = 231
            self.match(ExampleDSLParser.STRING)
            self.state = 232
            self.match(ExampleDSLParser.WITH)
            self.state = 233
            self.match(ExampleDSLParser.STRING)
            self.state = 234
            self.match(ExampleDSLParser.IN)
            self.state = 235
            self.match(ExampleDSLParser.COLUMN)
            self.state = 236
            self.match(ExampleDSLParser.T__1)
            self.state = 237
            self.match(ExampleDSLParser.STRING)
            self.state = 238
            self.match(ExampleDSLParser.T__2)
            self.state = 239
            self.match(ExampleDSLParser.T__0)
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ExampleDSLParser.NUMBER, 0)

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
        self.enterRule(localctx, 36, self.RULE_addConditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ExampleDSLParser.ADD)
            self.state = 242
            self.match(ExampleDSLParser.CONDITION)
            self.state = 243
            self.match(ExampleDSLParser.WHERE)
            self.state = 244
            self.match(ExampleDSLParser.STRING)
            self.state = 245
            self.match(ExampleDSLParser.T__4)
            self.state = 246
            self.match(ExampleDSLParser.NUMBER)
            self.state = 247
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

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
        self.enterRule(localctx, 38, self.RULE_removeDuplicatesStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ExampleDSLParser.REMOVE)
            self.state = 250
            self.match(ExampleDSLParser.DUPLICATE)
            self.state = 251
            self.match(ExampleDSLParser.ROWS)
            self.state = 252
            self.match(ExampleDSLParser.BASED)
            self.state = 253
            self.match(ExampleDSLParser.ON)
            self.state = 254
            self.match(ExampleDSLParser.COLUMN)
            self.state = 255
            self.match(ExampleDSLParser.T__1)
            self.state = 256
            self.match(ExampleDSLParser.STRING)
            self.state = 257
            self.match(ExampleDSLParser.T__2)
            self.state = 258
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

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
        self.enterRule(localctx, 40, self.RULE_splitDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(ExampleDSLParser.SPLIT)
            self.state = 261
            self.match(ExampleDSLParser.DATA)
            self.state = 262
            self.match(ExampleDSLParser.BASED)
            self.state = 263
            self.match(ExampleDSLParser.ON)
            self.state = 264
            self.match(ExampleDSLParser.COLUMN)
            self.state = 265
            self.match(ExampleDSLParser.T__1)
            self.state = 266
            self.match(ExampleDSLParser.STRING)
            self.state = 267
            self.match(ExampleDSLParser.T__2)
            self.state = 268
            self.match(ExampleDSLParser.AND)
            self.state = 269
            self.match(ExampleDSLParser.SAVE)
            self.state = 270
            self.match(ExampleDSLParser.RESULTS)
            self.state = 271
            self.match(ExampleDSLParser.TO)
            self.state = 272
            self.match(ExampleDSLParser.SEPARATE)
            self.state = 273
            self.match(ExampleDSLParser.FILES)
            self.state = 274
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.STRING)
            else:
                return self.getToken(ExampleDSLParser.STRING, i)

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
        self.enterRule(localctx, 42, self.RULE_combineColumnsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ExampleDSLParser.COMBINE)
            self.state = 277
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 278
            self.match(ExampleDSLParser.STRING)
            self.state = 279
            self.match(ExampleDSLParser.AND)
            self.state = 280
            self.match(ExampleDSLParser.STRING)
            self.state = 281
            self.match(ExampleDSLParser.AND)
            self.state = 282
            self.match(ExampleDSLParser.SAVE)
            self.state = 283
            self.match(ExampleDSLParser.RESULT)
            self.state = 284
            self.match(ExampleDSLParser.TO)
            self.state = 285
            self.match(ExampleDSLParser.STRING)
            self.state = 286
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

        def STRING(self):
            return self.getToken(ExampleDSLParser.STRING, 0)

        def BY(self):
            return self.getToken(ExampleDSLParser.BY, 0)

        def MULTIPLYING(self):
            return self.getToken(ExampleDSLParser.MULTIPLYING, 0)

        def WITH(self):
            return self.getToken(ExampleDSLParser.WITH, 0)

        def NUMBER(self):
            return self.getToken(ExampleDSLParser.NUMBER, 0)

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
        self.enterRule(localctx, 44, self.RULE_resizeDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ExampleDSLParser.RESIZE)
            self.state = 289
            self.match(ExampleDSLParser.DATA)
            self.state = 290
            self.match(ExampleDSLParser.IN)
            self.state = 291
            self.match(ExampleDSLParser.COLUMN)
            self.state = 292
            self.match(ExampleDSLParser.T__1)
            self.state = 293
            self.match(ExampleDSLParser.STRING)
            self.state = 294
            self.match(ExampleDSLParser.T__2)
            self.state = 295
            self.match(ExampleDSLParser.BY)
            self.state = 296
            self.match(ExampleDSLParser.MULTIPLYING)
            self.state = 297
            self.match(ExampleDSLParser.WITH)
            self.state = 298
            self.match(ExampleDSLParser.NUMBER)
            self.state = 299
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





