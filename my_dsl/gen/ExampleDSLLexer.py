# Generated from E:/uni file/compiler/hw5/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,57,435,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,1,0,1,0,1,1,1,1,
        1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,
        22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,
        24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,
        33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,
        37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,
        40,1,40,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,
        43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,
        47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,
        49,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,
        52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,53,4,53,409,8,53,11,53,12,
        53,410,1,54,1,54,5,54,415,8,54,10,54,12,54,418,9,54,1,54,1,54,1,
        55,1,55,5,55,424,8,55,10,55,12,55,427,9,55,1,56,4,56,430,8,56,11,
        56,12,56,431,1,56,1,56,1,416,0,57,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,
        81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,
        51,103,52,105,53,107,54,109,55,111,56,113,57,1,0,4,1,0,48,57,3,0,
        65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,
        32,438,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,
        0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,
        0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,
        0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,
        0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,
        0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,
        0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,
        0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,
        0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,
        1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,1,115,1,0,0,0,3,117,1,0,0,0,
        5,119,1,0,0,0,7,121,1,0,0,0,9,123,1,0,0,0,11,125,1,0,0,0,13,131,
        1,0,0,0,15,138,1,0,0,0,17,146,1,0,0,0,19,154,1,0,0,0,21,158,1,0,
        0,0,23,165,1,0,0,0,25,172,1,0,0,0,27,177,1,0,0,0,29,184,1,0,0,0,
        31,190,1,0,0,0,33,199,1,0,0,0,35,207,1,0,0,0,37,213,1,0,0,0,39,220,
        1,0,0,0,41,227,1,0,0,0,43,235,1,0,0,0,45,242,1,0,0,0,47,248,1,0,
        0,0,49,255,1,0,0,0,51,259,1,0,0,0,53,264,1,0,0,0,55,269,1,0,0,0,
        57,276,1,0,0,0,59,281,1,0,0,0,61,288,1,0,0,0,63,296,1,0,0,0,65,301,
        1,0,0,0,67,306,1,0,0,0,69,310,1,0,0,0,71,320,1,0,0,0,73,327,1,0,
        0,0,75,330,1,0,0,0,77,337,1,0,0,0,79,340,1,0,0,0,81,345,1,0,0,0,
        83,349,1,0,0,0,85,352,1,0,0,0,87,357,1,0,0,0,89,363,1,0,0,0,91,366,
        1,0,0,0,93,369,1,0,0,0,95,373,1,0,0,0,97,376,1,0,0,0,99,381,1,0,
        0,0,101,387,1,0,0,0,103,391,1,0,0,0,105,395,1,0,0,0,107,408,1,0,
        0,0,109,412,1,0,0,0,111,421,1,0,0,0,113,429,1,0,0,0,115,116,5,59,
        0,0,116,2,1,0,0,0,117,118,5,40,0,0,118,4,1,0,0,0,119,120,5,41,0,
        0,120,6,1,0,0,0,121,122,5,44,0,0,122,8,1,0,0,0,123,124,5,62,0,0,
        124,10,1,0,0,0,125,126,5,105,0,0,126,127,5,110,0,0,127,128,5,112,
        0,0,128,129,5,117,0,0,129,130,5,116,0,0,130,12,1,0,0,0,131,132,5,
        111,0,0,132,133,5,117,0,0,133,134,5,116,0,0,134,135,5,112,0,0,135,
        136,5,117,0,0,136,137,5,116,0,0,137,14,1,0,0,0,138,139,5,67,0,0,
        139,140,5,111,0,0,140,141,5,109,0,0,141,142,5,98,0,0,142,143,5,105,
        0,0,143,144,5,110,0,0,144,145,5,101,0,0,145,16,1,0,0,0,146,147,5,
        67,0,0,147,148,5,111,0,0,148,149,5,110,0,0,149,150,5,118,0,0,150,
        151,5,101,0,0,151,152,5,114,0,0,152,153,5,116,0,0,153,18,1,0,0,0,
        154,155,5,65,0,0,155,156,5,100,0,0,156,157,5,100,0,0,157,20,1,0,
        0,0,158,159,5,82,0,0,159,160,5,101,0,0,160,161,5,110,0,0,161,162,
        5,97,0,0,162,163,5,109,0,0,163,164,5,101,0,0,164,22,1,0,0,0,165,
        166,5,67,0,0,166,167,5,104,0,0,167,168,5,97,0,0,168,169,5,110,0,
        0,169,170,5,103,0,0,170,171,5,101,0,0,171,24,1,0,0,0,172,173,5,83,
        0,0,173,174,5,111,0,0,174,175,5,114,0,0,175,176,5,116,0,0,176,26,
        1,0,0,0,177,178,5,68,0,0,178,179,5,101,0,0,179,180,5,108,0,0,180,
        181,5,101,0,0,181,182,5,116,0,0,182,183,5,101,0,0,183,28,1,0,0,0,
        184,185,5,65,0,0,185,186,5,112,0,0,186,187,5,112,0,0,187,188,5,108,
        0,0,188,189,5,121,0,0,189,30,1,0,0,0,190,191,5,71,0,0,191,192,5,
        101,0,0,192,193,5,110,0,0,193,194,5,101,0,0,194,195,5,114,0,0,195,
        196,5,97,0,0,196,197,5,116,0,0,197,198,5,101,0,0,198,32,1,0,0,0,
        199,200,5,82,0,0,200,201,5,101,0,0,201,202,5,111,0,0,202,203,5,114,
        0,0,203,204,5,100,0,0,204,205,5,101,0,0,205,206,5,114,0,0,206,34,
        1,0,0,0,207,208,5,71,0,0,208,209,5,114,0,0,209,210,5,111,0,0,210,
        211,5,117,0,0,211,212,5,112,0,0,212,36,1,0,0,0,213,214,5,70,0,0,
        214,215,5,105,0,0,215,216,5,108,0,0,216,217,5,116,0,0,217,218,5,
        101,0,0,218,219,5,114,0,0,219,38,1,0,0,0,220,221,5,83,0,0,221,222,
        5,101,0,0,222,223,5,97,0,0,223,224,5,114,0,0,224,225,5,99,0,0,225,
        226,5,104,0,0,226,40,1,0,0,0,227,228,5,82,0,0,228,229,5,101,0,0,
        229,230,5,112,0,0,230,231,5,108,0,0,231,232,5,97,0,0,232,233,5,99,
        0,0,233,234,5,101,0,0,234,42,1,0,0,0,235,236,5,82,0,0,236,237,5,
        101,0,0,237,238,5,109,0,0,238,239,5,111,0,0,239,240,5,118,0,0,240,
        241,5,101,0,0,241,44,1,0,0,0,242,243,5,83,0,0,243,244,5,112,0,0,
        244,245,5,108,0,0,245,246,5,105,0,0,246,247,5,116,0,0,247,46,1,0,
        0,0,248,249,5,82,0,0,249,250,5,101,0,0,250,251,5,115,0,0,251,252,
        5,105,0,0,252,253,5,122,0,0,253,254,5,101,0,0,254,48,1,0,0,0,255,
        256,5,83,0,0,256,257,5,101,0,0,257,258,5,116,0,0,258,50,1,0,0,0,
        259,260,5,102,0,0,260,261,5,105,0,0,261,262,5,108,0,0,262,263,5,
        101,0,0,263,52,1,0,0,0,264,265,5,112,0,0,265,266,5,97,0,0,266,267,
        5,116,0,0,267,268,5,104,0,0,268,54,1,0,0,0,269,270,5,102,0,0,270,
        271,5,111,0,0,271,272,5,114,0,0,272,273,5,109,0,0,273,274,5,97,0,
        0,274,275,5,116,0,0,275,56,1,0,0,0,276,277,5,100,0,0,277,278,5,97,
        0,0,278,279,5,116,0,0,279,280,5,97,0,0,280,58,1,0,0,0,281,282,5,
        99,0,0,282,283,5,111,0,0,283,284,5,108,0,0,284,285,5,117,0,0,285,
        286,5,109,0,0,286,287,5,110,0,0,287,60,1,0,0,0,288,289,5,99,0,0,
        289,290,5,111,0,0,290,291,5,108,0,0,291,292,5,117,0,0,292,293,5,
        109,0,0,293,294,5,110,0,0,294,295,5,115,0,0,295,62,1,0,0,0,296,297,
        5,116,0,0,297,298,5,121,0,0,298,299,5,112,0,0,299,300,5,101,0,0,
        300,64,1,0,0,0,301,302,5,114,0,0,302,303,5,111,0,0,303,304,5,119,
        0,0,304,305,5,115,0,0,305,66,1,0,0,0,306,307,5,114,0,0,307,308,5,
        111,0,0,308,309,5,119,0,0,309,68,1,0,0,0,310,311,5,99,0,0,311,312,
        5,111,0,0,312,313,5,110,0,0,313,314,5,100,0,0,314,315,5,105,0,0,
        315,316,5,116,0,0,316,317,5,105,0,0,317,318,5,111,0,0,318,319,5,
        110,0,0,319,70,1,0,0,0,320,321,5,118,0,0,321,322,5,97,0,0,322,323,
        5,108,0,0,323,324,5,117,0,0,324,325,5,101,0,0,325,326,5,115,0,0,
        326,72,1,0,0,0,327,328,5,105,0,0,328,329,5,110,0,0,329,74,1,0,0,
        0,330,331,5,114,0,0,331,332,5,101,0,0,332,333,5,115,0,0,333,334,
        5,117,0,0,334,335,5,108,0,0,335,336,5,116,0,0,336,76,1,0,0,0,337,
        338,5,116,0,0,338,339,5,111,0,0,339,78,1,0,0,0,340,341,5,119,0,0,
        341,342,5,105,0,0,342,343,5,116,0,0,343,344,5,104,0,0,344,80,1,0,
        0,0,345,346,5,97,0,0,346,347,5,110,0,0,347,348,5,100,0,0,348,82,
        1,0,0,0,349,350,5,98,0,0,350,351,5,121,0,0,351,84,1,0,0,0,352,353,
        5,102,0,0,353,354,5,114,0,0,354,355,5,111,0,0,355,356,5,109,0,0,
        356,86,1,0,0,0,357,358,5,119,0,0,358,359,5,104,0,0,359,360,5,101,
        0,0,360,361,5,114,0,0,361,362,5,101,0,0,362,88,1,0,0,0,363,364,5,
        111,0,0,364,365,5,110,0,0,365,90,1,0,0,0,366,367,5,111,0,0,367,368,
        5,102,0,0,368,92,1,0,0,0,369,370,5,102,0,0,370,371,5,111,0,0,371,
        372,5,114,0,0,372,94,1,0,0,0,373,374,5,97,0,0,374,375,5,115,0,0,
        375,96,1,0,0,0,376,377,5,115,0,0,377,378,5,97,0,0,378,379,5,118,
        0,0,379,380,5,101,0,0,380,98,1,0,0,0,381,382,5,98,0,0,382,383,5,
        97,0,0,383,384,5,115,0,0,384,385,5,101,0,0,385,386,5,100,0,0,386,
        100,1,0,0,0,387,388,5,115,0,0,388,389,5,117,0,0,389,390,5,109,0,
        0,390,102,1,0,0,0,391,392,5,110,0,0,392,393,5,101,0,0,393,394,5,
        119,0,0,394,104,1,0,0,0,395,396,5,109,0,0,396,397,5,117,0,0,397,
        398,5,108,0,0,398,399,5,116,0,0,399,400,5,105,0,0,400,401,5,112,
        0,0,401,402,5,108,0,0,402,403,5,121,0,0,403,404,5,105,0,0,404,405,
        5,110,0,0,405,406,5,103,0,0,406,106,1,0,0,0,407,409,7,0,0,0,408,
        407,1,0,0,0,409,410,1,0,0,0,410,408,1,0,0,0,410,411,1,0,0,0,411,
        108,1,0,0,0,412,416,5,34,0,0,413,415,9,0,0,0,414,413,1,0,0,0,415,
        418,1,0,0,0,416,417,1,0,0,0,416,414,1,0,0,0,417,419,1,0,0,0,418,
        416,1,0,0,0,419,420,5,34,0,0,420,110,1,0,0,0,421,425,7,1,0,0,422,
        424,7,2,0,0,423,422,1,0,0,0,424,427,1,0,0,0,425,423,1,0,0,0,425,
        426,1,0,0,0,426,112,1,0,0,0,427,425,1,0,0,0,428,430,7,3,0,0,429,
        428,1,0,0,0,430,431,1,0,0,0,431,429,1,0,0,0,431,432,1,0,0,0,432,
        433,1,0,0,0,433,434,6,56,0,0,434,114,1,0,0,0,5,0,410,416,425,431,
        1,6,0,0
    ]

class ExampleDSLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    INPUT = 6
    OUTPUT = 7
    COMBINE = 8
    CONVERT = 9
    ADD = 10
    RENAME = 11
    CHANGE = 12
    SORT = 13
    DELETE = 14
    APPLY = 15
    GENERATE = 16
    REORDER = 17
    GROUP = 18
    FILTER = 19
    SEARCH = 20
    REPLACE = 21
    REMOVE = 22
    SPLIT = 23
    RESIZE = 24
    SET = 25
    FILE = 26
    PATH = 27
    FORMAT = 28
    DATA = 29
    COLUMN = 30
    COLUMNS = 31
    TYPE = 32
    ROWS = 33
    ROW = 34
    CONDITION = 35
    VALUES = 36
    IN = 37
    RESULT = 38
    TO = 39
    WITH = 40
    AND = 41
    BY = 42
    FROM = 43
    WHERE = 44
    ON = 45
    OF = 46
    FOR = 47
    AS = 48
    SAVE = 49
    BASED = 50
    SUM = 51
    NEW = 52
    MULTIPLYING = 53
    NUMBER = 54
    STRING = 55
    ID = 56
    WS = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "')'", "','", "'>'", "'input'", "'output'", "'Combine'", 
            "'Convert'", "'Add'", "'Rename'", "'Change'", "'Sort'", "'Delete'", 
            "'Apply'", "'Generate'", "'Reorder'", "'Group'", "'Filter'", 
            "'Search'", "'Replace'", "'Remove'", "'Split'", "'Resize'", 
            "'Set'", "'file'", "'path'", "'format'", "'data'", "'column'", 
            "'columns'", "'type'", "'rows'", "'row'", "'condition'", "'values'", 
            "'in'", "'result'", "'to'", "'with'", "'and'", "'by'", "'from'", 
            "'where'", "'on'", "'of'", "'for'", "'as'", "'save'", "'based'", 
            "'sum'", "'new'", "'multiplying'" ]

    symbolicNames = [ "<INVALID>",
            "INPUT", "OUTPUT", "COMBINE", "CONVERT", "ADD", "RENAME", "CHANGE", 
            "SORT", "DELETE", "APPLY", "GENERATE", "REORDER", "GROUP", "FILTER", 
            "SEARCH", "REPLACE", "REMOVE", "SPLIT", "RESIZE", "SET", "FILE", 
            "PATH", "FORMAT", "DATA", "COLUMN", "COLUMNS", "TYPE", "ROWS", 
            "ROW", "CONDITION", "VALUES", "IN", "RESULT", "TO", "WITH", 
            "AND", "BY", "FROM", "WHERE", "ON", "OF", "FOR", "AS", "SAVE", 
            "BASED", "SUM", "NEW", "MULTIPLYING", "NUMBER", "STRING", "ID", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "INPUT", "OUTPUT", 
                  "COMBINE", "CONVERT", "ADD", "RENAME", "CHANGE", "SORT", 
                  "DELETE", "APPLY", "GENERATE", "REORDER", "GROUP", "FILTER", 
                  "SEARCH", "REPLACE", "REMOVE", "SPLIT", "RESIZE", "SET", 
                  "FILE", "PATH", "FORMAT", "DATA", "COLUMN", "COLUMNS", 
                  "TYPE", "ROWS", "ROW", "CONDITION", "VALUES", "IN", "RESULT", 
                  "TO", "WITH", "AND", "BY", "FROM", "WHERE", "ON", "OF", 
                  "FOR", "AS", "SAVE", "BASED", "SUM", "NEW", "MULTIPLYING", 
                  "NUMBER", "STRING", "ID", "WS" ]

    grammarFileName = "ExampleDSL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


