# Generated from C:/Users/yasin/Desktop/project_c/createDsl/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
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
        4,1,70,481,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,1,1,4,1,
        81,8,1,11,1,12,1,82,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,109,8,2,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,
        1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,3,10,137,8,10,1,10,1,
        10,1,10,3,10,142,8,10,1,10,1,10,1,10,3,10,147,8,10,5,10,149,8,10,
        10,10,12,10,152,9,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,
        162,8,11,1,11,1,11,1,11,3,11,167,8,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,5,12,176,8,12,10,12,12,12,179,9,12,1,12,3,12,182,8,12,1,
        12,1,12,1,12,3,12,187,8,12,1,12,3,12,190,8,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,13,5,13,199,8,13,10,13,12,13,202,9,13,1,13,1,13,1,13,
        1,13,5,13,208,8,13,10,13,12,13,211,9,13,1,13,1,13,1,13,3,13,216,
        8,13,1,13,3,13,219,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,5,14,231,8,14,10,14,12,14,234,9,14,1,14,1,14,1,14,1,14,
        1,14,3,14,241,8,14,1,14,3,14,244,8,14,1,14,1,14,1,15,1,15,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,258,8,16,1,16,3,16,261,8,16,
        1,16,1,16,1,17,1,17,1,17,1,17,1,17,5,17,270,8,17,10,17,12,17,273,
        9,17,1,17,1,17,1,17,3,17,278,8,17,1,17,3,17,281,8,17,1,17,1,17,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,3,20,304,8,20,1,20,1,20,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,318,8,21,1,21,1,21,1,
        22,1,22,1,23,1,23,1,23,1,23,1,23,5,23,329,8,23,10,23,12,23,332,9,
        23,1,23,1,23,1,23,1,23,5,23,338,8,23,10,23,12,23,341,9,23,1,23,1,
        23,1,23,3,23,346,8,23,1,23,3,23,349,8,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,364,8,24,1,24,3,24,
        367,8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,
        1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,3,35,468,8,35,
        1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,0,0,
        38,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,0,2,1,0,3,5,1,0,
        64,65,497,0,76,1,0,0,0,2,80,1,0,0,0,4,108,1,0,0,0,6,110,1,0,0,0,
        8,115,1,0,0,0,10,121,1,0,0,0,12,124,1,0,0,0,14,127,1,0,0,0,16,129,
        1,0,0,0,18,131,1,0,0,0,20,133,1,0,0,0,22,156,1,0,0,0,24,170,1,0,
        0,0,26,193,1,0,0,0,28,222,1,0,0,0,30,247,1,0,0,0,32,249,1,0,0,0,
        34,264,1,0,0,0,36,284,1,0,0,0,38,291,1,0,0,0,40,293,1,0,0,0,42,307,
        1,0,0,0,44,321,1,0,0,0,46,323,1,0,0,0,48,352,1,0,0,0,50,370,1,0,
        0,0,52,378,1,0,0,0,54,380,1,0,0,0,56,390,1,0,0,0,58,402,1,0,0,0,
        60,404,1,0,0,0,62,412,1,0,0,0,64,423,1,0,0,0,66,439,1,0,0,0,68,451,
        1,0,0,0,70,464,1,0,0,0,72,473,1,0,0,0,74,478,1,0,0,0,76,77,3,2,1,
        0,77,78,5,0,0,1,78,1,1,0,0,0,79,81,3,4,2,0,80,79,1,0,0,0,81,82,1,
        0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,3,1,0,0,0,84,109,3,6,3,0,85,
        109,3,8,4,0,86,109,3,20,10,0,87,109,3,22,11,0,88,109,3,24,12,0,89,
        109,3,26,13,0,90,109,3,28,14,0,91,109,3,32,16,0,92,109,3,34,17,0,
        93,109,3,36,18,0,94,109,3,40,20,0,95,109,3,42,21,0,96,109,3,46,23,
        0,97,109,3,48,24,0,98,109,3,50,25,0,99,109,3,54,27,0,100,109,3,56,
        28,0,101,109,3,60,30,0,102,109,3,62,31,0,103,109,3,64,32,0,104,109,
        3,66,33,0,105,109,3,68,34,0,106,109,3,70,35,0,107,109,3,72,36,0,
        108,84,1,0,0,0,108,85,1,0,0,0,108,86,1,0,0,0,108,87,1,0,0,0,108,
        88,1,0,0,0,108,89,1,0,0,0,108,90,1,0,0,0,108,91,1,0,0,0,108,92,1,
        0,0,0,108,93,1,0,0,0,108,94,1,0,0,0,108,95,1,0,0,0,108,96,1,0,0,
        0,108,97,1,0,0,0,108,98,1,0,0,0,108,99,1,0,0,0,108,100,1,0,0,0,108,
        101,1,0,0,0,108,102,1,0,0,0,108,103,1,0,0,0,108,104,1,0,0,0,108,
        105,1,0,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,5,1,0,0,0,110,111,
        5,10,0,0,111,112,3,14,7,0,112,113,3,10,5,0,113,114,5,1,0,0,114,7,
        1,0,0,0,115,116,5,9,0,0,116,117,3,74,37,0,117,118,5,46,0,0,118,119,
        3,14,7,0,119,120,5,1,0,0,120,9,1,0,0,0,121,122,5,55,0,0,122,123,
        3,74,37,0,123,11,1,0,0,0,124,125,5,46,0,0,125,126,3,16,8,0,126,13,
        1,0,0,0,127,128,5,65,0,0,128,15,1,0,0,0,129,130,5,65,0,0,130,17,
        1,0,0,0,131,132,5,65,0,0,132,19,1,0,0,0,133,136,5,15,0,0,134,137,
        3,14,7,0,135,137,3,74,37,0,136,134,1,0,0,0,136,135,1,0,0,0,137,138,
        1,0,0,0,138,141,5,2,0,0,139,142,3,14,7,0,140,142,3,74,37,0,141,139,
        1,0,0,0,141,140,1,0,0,0,142,150,1,0,0,0,143,146,5,2,0,0,144,147,
        3,14,7,0,145,147,3,74,37,0,146,144,1,0,0,0,146,145,1,0,0,0,147,149,
        1,0,0,0,148,143,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,
        1,0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,154,3,10,5,0,154,155,
        5,1,0,0,155,21,1,0,0,0,156,157,5,16,0,0,157,158,5,35,0,0,158,161,
        5,50,0,0,159,162,3,14,7,0,160,162,3,74,37,0,161,159,1,0,0,0,161,
        160,1,0,0,0,162,163,1,0,0,0,163,166,5,46,0,0,164,167,3,14,7,0,165,
        167,3,74,37,0,166,164,1,0,0,0,166,165,1,0,0,0,167,168,1,0,0,0,168,
        169,5,1,0,0,169,23,1,0,0,0,170,171,5,17,0,0,171,172,5,38,0,0,172,
        177,3,16,8,0,173,174,5,2,0,0,174,176,3,16,8,0,175,173,1,0,0,0,176,
        179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,181,1,0,0,0,179,
        177,1,0,0,0,180,182,3,12,6,0,181,180,1,0,0,0,181,182,1,0,0,0,182,
        183,1,0,0,0,183,186,5,44,0,0,184,187,3,14,7,0,185,187,3,74,37,0,
        186,184,1,0,0,0,186,185,1,0,0,0,187,189,1,0,0,0,188,190,3,10,5,0,
        189,188,1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,192,5,1,0,0,
        192,25,1,0,0,0,193,194,5,18,0,0,194,195,5,37,0,0,195,200,3,16,8,
        0,196,197,5,2,0,0,197,199,3,16,8,0,198,196,1,0,0,0,199,202,1,0,0,
        0,200,198,1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,200,1,0,0,
        0,203,204,5,46,0,0,204,209,3,16,8,0,205,206,5,2,0,0,206,208,3,16,
        8,0,207,205,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,
        0,0,210,212,1,0,0,0,211,209,1,0,0,0,212,215,5,44,0,0,213,216,3,14,
        7,0,214,216,3,74,37,0,215,213,1,0,0,0,215,214,1,0,0,0,216,218,1,
        0,0,0,217,219,3,10,5,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,
        0,0,0,220,221,5,1,0,0,221,27,1,0,0,0,222,223,5,19,0,0,223,224,5,
        36,0,0,224,225,5,39,0,0,225,226,5,53,0,0,226,227,5,37,0,0,227,232,
        3,16,8,0,228,229,5,2,0,0,229,231,3,16,8,0,230,228,1,0,0,0,231,234,
        1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,235,1,0,0,0,234,232,
        1,0,0,0,235,236,5,46,0,0,236,237,3,30,15,0,237,240,5,44,0,0,238,
        241,3,14,7,0,239,241,3,74,37,0,240,238,1,0,0,0,240,239,1,0,0,0,241,
        243,1,0,0,0,242,244,3,10,5,0,243,242,1,0,0,0,243,244,1,0,0,0,244,
        245,1,0,0,0,245,246,5,1,0,0,246,29,1,0,0,0,247,248,5,39,0,0,248,
        31,1,0,0,0,249,250,5,20,0,0,250,251,5,36,0,0,251,252,5,49,0,0,252,
        253,5,37,0,0,253,254,3,16,8,0,254,257,5,44,0,0,255,258,3,14,7,0,
        256,258,3,74,37,0,257,255,1,0,0,0,257,256,1,0,0,0,258,260,1,0,0,
        0,259,261,3,10,5,0,260,259,1,0,0,0,260,261,1,0,0,0,261,262,1,0,0,
        0,262,263,5,1,0,0,263,33,1,0,0,0,264,265,5,21,0,0,265,266,5,37,0,
        0,266,271,3,16,8,0,267,268,5,2,0,0,268,270,3,16,8,0,269,267,1,0,
        0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,274,1,0,
        0,0,273,271,1,0,0,0,274,277,5,44,0,0,275,278,3,14,7,0,276,278,3,
        74,37,0,277,275,1,0,0,0,277,276,1,0,0,0,278,280,1,0,0,0,279,281,
        3,10,5,0,280,279,1,0,0,0,280,281,1,0,0,0,281,282,1,0,0,0,282,283,
        5,1,0,0,283,35,1,0,0,0,284,285,5,18,0,0,285,286,5,12,0,0,286,287,
        5,33,0,0,287,288,5,46,0,0,288,289,3,38,19,0,289,290,5,1,0,0,290,
        37,1,0,0,0,291,292,5,65,0,0,292,39,1,0,0,0,293,294,5,22,0,0,294,
        295,5,42,0,0,295,296,5,52,0,0,296,297,5,40,0,0,297,298,5,64,0,0,
        298,299,5,46,0,0,299,300,5,64,0,0,300,303,5,44,0,0,301,304,3,14,
        7,0,302,304,3,74,37,0,303,301,1,0,0,0,303,302,1,0,0,0,304,305,1,
        0,0,0,305,306,5,1,0,0,306,41,1,0,0,0,307,308,5,23,0,0,308,309,5,
        13,0,0,309,310,5,54,0,0,310,311,5,37,0,0,311,312,3,16,8,0,312,313,
        5,49,0,0,313,314,3,44,22,0,314,317,5,44,0,0,315,318,3,14,7,0,316,
        318,3,74,37,0,317,315,1,0,0,0,317,316,1,0,0,0,318,319,1,0,0,0,319,
        320,5,1,0,0,320,43,1,0,0,0,321,322,7,0,0,0,322,45,1,0,0,0,323,324,
        5,24,0,0,324,325,5,38,0,0,325,330,3,16,8,0,326,327,5,2,0,0,327,329,
        3,16,8,0,328,326,1,0,0,0,329,332,1,0,0,0,330,328,1,0,0,0,330,331,
        1,0,0,0,331,333,1,0,0,0,332,330,1,0,0,0,333,334,5,46,0,0,334,339,
        3,16,8,0,335,336,5,2,0,0,336,338,3,16,8,0,337,335,1,0,0,0,338,341,
        1,0,0,0,339,337,1,0,0,0,339,340,1,0,0,0,340,342,1,0,0,0,341,339,
        1,0,0,0,342,345,5,44,0,0,343,346,3,14,7,0,344,346,3,74,37,0,345,
        343,1,0,0,0,345,344,1,0,0,0,346,348,1,0,0,0,347,349,3,10,5,0,348,
        347,1,0,0,0,348,349,1,0,0,0,349,350,1,0,0,0,350,351,5,1,0,0,351,
        47,1,0,0,0,352,353,5,25,0,0,353,354,5,49,0,0,354,355,3,16,8,0,355,
        356,5,48,0,0,356,357,5,58,0,0,357,358,5,43,0,0,358,359,5,46,0,0,
        359,360,3,16,8,0,360,363,5,44,0,0,361,364,3,14,7,0,362,364,3,74,
        37,0,363,361,1,0,0,0,363,362,1,0,0,0,364,366,1,0,0,0,365,367,3,10,
        5,0,366,365,1,0,0,0,366,367,1,0,0,0,367,368,1,0,0,0,368,369,5,1,
        0,0,369,49,1,0,0,0,370,371,5,26,0,0,371,372,5,40,0,0,372,373,5,51,
        0,0,373,374,3,16,8,0,374,375,5,6,0,0,375,376,3,52,26,0,376,377,5,
        1,0,0,377,51,1,0,0,0,378,379,5,64,0,0,379,53,1,0,0,0,380,381,5,27,
        0,0,381,382,5,54,0,0,382,383,5,65,0,0,383,384,5,44,0,0,384,385,5,
        37,0,0,385,386,5,7,0,0,386,387,3,16,8,0,387,388,5,8,0,0,388,389,
        5,1,0,0,389,55,1,0,0,0,390,391,5,28,0,0,391,392,5,43,0,0,392,393,
        3,58,29,0,393,394,5,47,0,0,394,395,3,58,29,0,395,396,5,44,0,0,396,
        397,5,37,0,0,397,398,5,7,0,0,398,399,3,16,8,0,399,400,5,8,0,0,400,
        401,5,1,0,0,401,57,1,0,0,0,402,403,7,1,0,0,403,59,1,0,0,0,404,405,
        5,17,0,0,405,406,5,42,0,0,406,407,5,51,0,0,407,408,3,16,8,0,408,
        409,5,6,0,0,409,410,3,52,26,0,410,411,5,1,0,0,411,61,1,0,0,0,412,
        413,5,29,0,0,413,414,5,61,0,0,414,415,5,40,0,0,415,416,5,57,0,0,
        416,417,5,52,0,0,417,418,5,37,0,0,418,419,5,7,0,0,419,420,3,16,8,
        0,420,421,5,8,0,0,421,422,5,1,0,0,422,63,1,0,0,0,423,424,5,30,0,
        0,424,425,5,36,0,0,425,426,5,57,0,0,426,427,5,52,0,0,427,428,5,37,
        0,0,428,429,5,7,0,0,429,430,3,16,8,0,430,431,5,8,0,0,431,432,5,48,
        0,0,432,433,5,56,0,0,433,434,5,68,0,0,434,435,5,46,0,0,435,436,5,
        69,0,0,436,437,5,70,0,0,437,438,5,1,0,0,438,65,1,0,0,0,439,440,5,
        15,0,0,440,441,5,38,0,0,441,442,3,16,8,0,442,443,5,48,0,0,443,444,
        3,16,8,0,444,445,5,48,0,0,445,446,5,56,0,0,446,447,5,45,0,0,447,
        448,5,46,0,0,448,449,3,18,9,0,449,450,5,1,0,0,450,67,1,0,0,0,451,
        452,5,31,0,0,452,453,5,36,0,0,453,454,5,44,0,0,454,455,5,37,0,0,
        455,456,5,7,0,0,456,457,3,16,8,0,457,458,5,8,0,0,458,459,5,49,0,
        0,459,460,5,60,0,0,460,461,5,47,0,0,461,462,3,52,26,0,462,463,5,
        1,0,0,463,69,1,0,0,0,464,467,5,62,0,0,465,468,3,14,7,0,466,468,3,
        74,37,0,467,465,1,0,0,0,467,466,1,0,0,0,468,469,1,0,0,0,469,470,
        5,50,0,0,470,471,3,14,7,0,471,472,5,1,0,0,472,71,1,0,0,0,473,474,
        5,63,0,0,474,475,5,50,0,0,475,476,3,14,7,0,476,477,5,1,0,0,477,73,
        1,0,0,0,478,479,5,66,0,0,479,75,1,0,0,0,33,82,108,136,141,146,150,
        161,166,177,181,186,189,200,209,215,218,232,240,243,257,260,271,
        277,280,303,317,330,339,345,348,363,366,467
    ]

class ExampleDSLParser ( Parser ):

    grammarFileName = "ExampleDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'day'", "'month'", "'year'", 
                     "'>'", "'('", "')'", "'export'", "'import'", "'input'", 
                     "'output'", "'report'", "'write'", "'Combine'", "'Convert'", 
                     "'Add'", "'Rename'", "'Change'", "'Sort'", "'Delete'", 
                     "'Apply'", "'Generate'", "'Reorder'", "'Group'", "'Filter'", 
                     "'Search'", "'Replace'", "'Remove'", "'Split'", "'Resize'", 
                     "'Set'", "'file'", "'path'", "'format'", "'data'", 
                     "'column'", "'columns'", "<INVALID>", "'rows'", "'row'", 
                     "'condition'", "'values'", "'in'", "'result'", "'to'", 
                     "'with'", "'and'", "'by'", "'from'", "'where'", "'on'", 
                     "'of'", "'for'", "'as'", "'save'", "'based'", "'sum'", 
                     "'new'", "'multiplying'", "'duplicate'", "'update'", 
                     "'extract'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "EXPORT", "IMPORT", "INPUT", "OUTPUT", 
                      "REPORT", "WRITE", "COMBINE", "CONVERT", "ADD", "RENAME", 
                      "CHANGE", "SORT", "DELETE", "APPLY", "GENERATE", "REORDER", 
                      "GROUP", "FILTER", "SEARCH", "REPLACE", "REMOVE", 
                      "SPLIT", "RESIZE", "SET", "FILE", "PATH", "FORMAT", 
                      "DATA", "COLUMN", "COLUMNS", "TYPE", "ROWS", "ROW", 
                      "CONDITION", "VALUES", "IN", "RESULT", "TO", "WITH", 
                      "AND", "BY", "FROM", "WHERE", "ON", "OF", "FOR", "AS", 
                      "SAVE", "BASED", "SUM", "NEW", "MULTIPLYING", "DUPLICATE", 
                      "Update", "EXTRACT", "NUMBER", "STRING", "ID", "WS", 
                      "RESULTS", "SEPARATE", "FILES" ]

    RULE_start = 0
    RULE_program = 1
    RULE_statement = 2
    RULE_importFileStatement = 3
    RULE_exportFileStatement = 4
    RULE_asStatement = 5
    RULE_toStatement = 6
    RULE_path = 7
    RULE_column = 8
    RULE_result = 9
    RULE_combineStatement = 10
    RULE_convertStatement = 11
    RULE_addColumnsStatement = 12
    RULE_renameColumnStatement = 13
    RULE_changeDataTypeStatement = 14
    RULE_type = 15
    RULE_sortDataStatement = 16
    RULE_deleteColumnStatement = 17
    RULE_renameFileStatement = 18
    RULE_file_name = 19
    RULE_applyConditionStatement = 20
    RULE_generateReportStatement = 21
    RULE_period = 22
    RULE_reorderColumnsStatement = 23
    RULE_groupByStatement = 24
    RULE_filterRowsStatement = 25
    RULE_value = 26
    RULE_searchTextStatement = 27
    RULE_replaceValuesStatement = 28
    RULE_values = 29
    RULE_addConditionStatement = 30
    RULE_removeDuplicatesStatement = 31
    RULE_splitDataStatement = 32
    RULE_combineColumnsStatement = 33
    RULE_resizeDataStatement = 34
    RULE_updateFromsheetStatement = 35
    RULE_extractTablesFromWebStatement = 36
    RULE_id = 37

    ruleNames =  [ "start", "program", "statement", "importFileStatement", 
                   "exportFileStatement", "asStatement", "toStatement", 
                   "path", "column", "result", "combineStatement", "convertStatement", 
                   "addColumnsStatement", "renameColumnStatement", "changeDataTypeStatement", 
                   "type", "sortDataStatement", "deleteColumnStatement", 
                   "renameFileStatement", "file_name", "applyConditionStatement", 
                   "generateReportStatement", "period", "reorderColumnsStatement", 
                   "groupByStatement", "filterRowsStatement", "value", "searchTextStatement", 
                   "replaceValuesStatement", "values", "addConditionStatement", 
                   "removeDuplicatesStatement", "splitDataStatement", "combineColumnsStatement", 
                   "resizeDataStatement", "updateFromsheetStatement", "extractTablesFromWebStatement", 
                   "id" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    EXPORT=9
    IMPORT=10
    INPUT=11
    OUTPUT=12
    REPORT=13
    WRITE=14
    COMBINE=15
    CONVERT=16
    ADD=17
    RENAME=18
    CHANGE=19
    SORT=20
    DELETE=21
    APPLY=22
    GENERATE=23
    REORDER=24
    GROUP=25
    FILTER=26
    SEARCH=27
    REPLACE=28
    REMOVE=29
    SPLIT=30
    RESIZE=31
    SET=32
    FILE=33
    PATH=34
    FORMAT=35
    DATA=36
    COLUMN=37
    COLUMNS=38
    TYPE=39
    ROWS=40
    ROW=41
    CONDITION=42
    VALUES=43
    IN=44
    RESULT=45
    TO=46
    WITH=47
    AND=48
    BY=49
    FROM=50
    WHERE=51
    ON=52
    OF=53
    FOR=54
    AS=55
    SAVE=56
    BASED=57
    SUM=58
    NEW=59
    MULTIPLYING=60
    DUPLICATE=61
    Update=62
    EXTRACT=63
    NUMBER=64
    STRING=65
    ID=66
    WS=67
    RESULTS=68
    SEPARATE=69
    FILES=70

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
            self.state = 76
            self.program()
            self.state = 77
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
            self.state = 80 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self.statement()
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -4611686014132451840) != 0)):
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

        def importFileStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ImportFileStatementContext,0)


        def exportFileStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ExportFileStatementContext,0)


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


        def updateFromsheetStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.UpdateFromsheetStatementContext,0)


        def extractTablesFromWebStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ExtractTablesFromWebStatementContext,0)


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
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.importFileStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.exportFileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.combineStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.convertStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.addColumnsStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.renameColumnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 90
                self.changeDataTypeStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 91
                self.sortDataStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 92
                self.deleteColumnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 93
                self.renameFileStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 94
                self.applyConditionStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 95
                self.generateReportStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 96
                self.reorderColumnsStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 97
                self.groupByStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 98
                self.filterRowsStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 99
                self.searchTextStatement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 100
                self.replaceValuesStatement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 101
                self.addConditionStatement()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 102
                self.removeDuplicatesStatement()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 103
                self.splitDataStatement()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 104
                self.combineColumnsStatement()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 105
                self.resizeDataStatement()
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 106
                self.updateFromsheetStatement()
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 107
                self.extractTablesFromWebStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportFileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(ExampleDSLParser.IMPORT, 0)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_importFileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportFileStatement" ):
                listener.enterImportFileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportFileStatement" ):
                listener.exitImportFileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportFileStatement" ):
                return visitor.visitImportFileStatement(self)
            else:
                return visitor.visitChildren(self)




    def importFileStatement(self):

        localctx = ExampleDSLParser.ImportFileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importFileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ExampleDSLParser.IMPORT)
            self.state = 111
            self.path()
            self.state = 112
            self.asStatement()
            self.state = 113
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExportFileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORT(self):
            return self.getToken(ExampleDSLParser.EXPORT, 0)

        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_exportFileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExportFileStatement" ):
                listener.enterExportFileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExportFileStatement" ):
                listener.exitExportFileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExportFileStatement" ):
                return visitor.visitExportFileStatement(self)
            else:
                return visitor.visitChildren(self)




    def exportFileStatement(self):

        localctx = ExampleDSLParser.ExportFileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exportFileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(ExampleDSLParser.EXPORT)
            self.state = 116
            self.id_()
            self.state = 117
            self.match(ExampleDSLParser.TO)
            self.state = 118
            self.path()
            self.state = 119
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS(self):
            return self.getToken(ExampleDSLParser.AS, 0)

        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_asStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsStatement" ):
                listener.enterAsStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsStatement" ):
                listener.exitAsStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsStatement" ):
                return visitor.visitAsStatement(self)
            else:
                return visitor.visitChildren(self)




    def asStatement(self):

        localctx = ExampleDSLParser.AsStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ExampleDSLParser.AS)
            self.state = 122
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_toStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToStatement" ):
                listener.enterToStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToStatement" ):
                listener.exitToStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToStatement" ):
                return visitor.visitToStatement(self)
            else:
                return visitor.visitChildren(self)




    def toStatement(self):

        localctx = ExampleDSLParser.ToStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_toStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ExampleDSLParser.TO)
            self.state = 125
            self.column()
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
        self.enterRule(localctx, 14, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
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
        self.enterRule(localctx, 16, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
        self.enterRule(localctx, 18, self.RULE_result)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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

        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


        def path(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.PathContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.PathContext,i)


        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.IdContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.IdContext,i)


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
        self.enterRule(localctx, 20, self.RULE_combineStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ExampleDSLParser.COMBINE)

            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 134
                self.path()
                pass
            elif token in [66]:
                self.state = 135
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 138
            self.match(ExampleDSLParser.T__1)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 139
                self.path()
                pass
            elif token in [66]:
                self.state = 140
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 143
                self.match(ExampleDSLParser.T__1)
                self.state = 146
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [65]:
                    self.state = 144
                    self.path()
                    pass
                elif token in [66]:
                    self.state = 145
                    self.id_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.asStatement()
            self.state = 154
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

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def path(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.PathContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.PathContext,i)


        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.IdContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.IdContext,i)


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
        self.enterRule(localctx, 22, self.RULE_convertStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ExampleDSLParser.CONVERT)
            self.state = 157
            self.match(ExampleDSLParser.FORMAT)
            self.state = 158
            self.match(ExampleDSLParser.FROM)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 159
                self.path()
                pass
            elif token in [66]:
                self.state = 160
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 163
            self.match(ExampleDSLParser.TO)
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 164
                self.path()
                pass
            elif token in [66]:
                self.state = 165
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
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

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def toStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.ToStatementContext,0)


        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


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
        self.enterRule(localctx, 24, self.RULE_addColumnsStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ExampleDSLParser.ADD)
            self.state = 171
            self.match(ExampleDSLParser.COLUMNS)

            self.state = 172
            self.column()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 173
                self.match(ExampleDSLParser.T__1)
                self.state = 174
                self.column()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 180
                self.toStatement()


            self.state = 183
            self.match(ExampleDSLParser.IN)
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 184
                self.path()
                pass
            elif token in [66]:
                self.state = 185
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 188
                self.asStatement()


            self.state = 191
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

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


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
        self.enterRule(localctx, 26, self.RULE_renameColumnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(ExampleDSLParser.RENAME)
            self.state = 194
            self.match(ExampleDSLParser.COLUMN)

            self.state = 195
            self.column()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 196
                self.match(ExampleDSLParser.T__1)
                self.state = 197
                self.column()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self.match(ExampleDSLParser.TO)

            self.state = 204
            self.column()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 205
                self.match(ExampleDSLParser.T__1)
                self.state = 206
                self.column()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(ExampleDSLParser.IN)
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 213
                self.path()
                pass
            elif token in [66]:
                self.state = 214
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 217
                self.asStatement()


            self.state = 220
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

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def type_(self):
            return self.getTypedRuleContext(ExampleDSLParser.TypeContext,0)


        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


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
        self.enterRule(localctx, 28, self.RULE_changeDataTypeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(ExampleDSLParser.CHANGE)
            self.state = 223
            self.match(ExampleDSLParser.DATA)
            self.state = 224
            self.match(ExampleDSLParser.TYPE)
            self.state = 225
            self.match(ExampleDSLParser.OF)
            self.state = 226
            self.match(ExampleDSLParser.COLUMN)

            self.state = 227
            self.column()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 228
                self.match(ExampleDSLParser.T__1)
                self.state = 229
                self.column()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self.match(ExampleDSLParser.TO)
            self.state = 236
            self.type_()
            self.state = 237
            self.match(ExampleDSLParser.IN)
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 238
                self.path()
                pass
            elif token in [66]:
                self.state = 239
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 242
                self.asStatement()


            self.state = 245
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
        self.enterRule(localctx, 30, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
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


        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


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
        self.enterRule(localctx, 32, self.RULE_sortDataStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ExampleDSLParser.SORT)
            self.state = 250
            self.match(ExampleDSLParser.DATA)
            self.state = 251
            self.match(ExampleDSLParser.BY)
            self.state = 252
            self.match(ExampleDSLParser.COLUMN)
            self.state = 253
            self.column()
            self.state = 254
            self.match(ExampleDSLParser.IN)
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 255
                self.path()
                pass
            elif token in [66]:
                self.state = 256
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 259
                self.asStatement()


            self.state = 262
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

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


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
        self.enterRule(localctx, 34, self.RULE_deleteColumnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ExampleDSLParser.DELETE)
            self.state = 265
            self.match(ExampleDSLParser.COLUMN)

            self.state = 266
            self.column()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 267
                self.match(ExampleDSLParser.T__1)
                self.state = 268
                self.column()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 274
            self.match(ExampleDSLParser.IN)
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 275
                self.path()
                pass
            elif token in [66]:
                self.state = 276
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 279
                self.asStatement()


            self.state = 282
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
        self.enterRule(localctx, 36, self.RULE_renameFileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ExampleDSLParser.RENAME)
            self.state = 285
            self.match(ExampleDSLParser.OUTPUT)
            self.state = 286
            self.match(ExampleDSLParser.FILE)
            self.state = 287
            self.match(ExampleDSLParser.TO)
            self.state = 288
            self.file_name()
            self.state = 289
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
        self.enterRule(localctx, 38, self.RULE_file_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
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

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.NUMBER)
            else:
                return self.getToken(ExampleDSLParser.NUMBER, i)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


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
        self.enterRule(localctx, 40, self.RULE_applyConditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ExampleDSLParser.APPLY)
            self.state = 294
            self.match(ExampleDSLParser.CONDITION)
            self.state = 295
            self.match(ExampleDSLParser.ON)
            self.state = 296
            self.match(ExampleDSLParser.ROWS)
            self.state = 297
            localctx.from_ = self.match(ExampleDSLParser.NUMBER)
            self.state = 298
            self.match(ExampleDSLParser.TO)
            self.state = 299
            localctx.to = self.match(ExampleDSLParser.NUMBER)
            self.state = 300
            self.match(ExampleDSLParser.IN)
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 301
                self.path()
                pass
            elif token in [66]:
                self.state = 302
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 305
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


        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


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
        self.enterRule(localctx, 42, self.RULE_generateReportStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(ExampleDSLParser.GENERATE)
            self.state = 308
            self.match(ExampleDSLParser.REPORT)
            self.state = 309
            self.match(ExampleDSLParser.FOR)
            self.state = 310
            self.match(ExampleDSLParser.COLUMN)
            self.state = 311
            self.column()
            self.state = 312
            self.match(ExampleDSLParser.BY)
            self.state = 313
            self.period()
            self.state = 314
            self.match(ExampleDSLParser.IN)
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 315
                self.path()
                pass
            elif token in [66]:
                self.state = 316
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 319
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
        self.enterRule(localctx, 44, self.RULE_period)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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

        def REORDER(self):
            return self.getToken(ExampleDSLParser.REORDER, 0)

        def COLUMNS(self):
            return self.getToken(ExampleDSLParser.COLUMNS, 0)

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,i)


        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


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
        self.enterRule(localctx, 46, self.RULE_reorderColumnsStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ExampleDSLParser.REORDER)
            self.state = 324
            self.match(ExampleDSLParser.COLUMNS)

            self.state = 325
            self.column()
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 326
                self.match(ExampleDSLParser.T__1)
                self.state = 327
                self.column()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 333
            self.match(ExampleDSLParser.TO)

            self.state = 334
            self.column()
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 335
                self.match(ExampleDSLParser.T__1)
                self.state = 336
                self.column()
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 342
            self.match(ExampleDSLParser.IN)
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 343
                self.path()
                pass
            elif token in [66]:
                self.state = 344
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 347
                self.asStatement()


            self.state = 350
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

        def TO(self):
            return self.getToken(ExampleDSLParser.TO, 0)

        def IN(self):
            return self.getToken(ExampleDSLParser.IN, 0)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def asStatement(self):
            return self.getTypedRuleContext(ExampleDSLParser.AsStatementContext,0)


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
        self.enterRule(localctx, 48, self.RULE_groupByStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ExampleDSLParser.GROUP)
            self.state = 353
            self.match(ExampleDSLParser.BY)
            self.state = 354
            self.column()
            self.state = 355
            self.match(ExampleDSLParser.AND)
            self.state = 356
            self.match(ExampleDSLParser.SUM)
            self.state = 357
            self.match(ExampleDSLParser.VALUES)
            self.state = 358
            self.match(ExampleDSLParser.TO)
            self.state = 359
            self.column()
            self.state = 360
            self.match(ExampleDSLParser.IN)
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 361
                self.path()
                pass
            elif token in [66]:
                self.state = 362
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 365
                self.asStatement()


            self.state = 368
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
        self.enterRule(localctx, 50, self.RULE_filterRowsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(ExampleDSLParser.FILTER)
            self.state = 371
            self.match(ExampleDSLParser.ROWS)
            self.state = 372
            self.match(ExampleDSLParser.WHERE)
            self.state = 373
            self.column()
            self.state = 374
            self.match(ExampleDSLParser.T__5)
            self.state = 375
            self.value()
            self.state = 376
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
        self.enterRule(localctx, 52, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
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
        self.enterRule(localctx, 54, self.RULE_searchTextStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ExampleDSLParser.SEARCH)
            self.state = 381
            self.match(ExampleDSLParser.FOR)
            self.state = 382
            localctx.text = self.match(ExampleDSLParser.STRING)
            self.state = 383
            self.match(ExampleDSLParser.IN)
            self.state = 384
            self.match(ExampleDSLParser.COLUMN)
            self.state = 385
            self.match(ExampleDSLParser.T__6)
            self.state = 386
            self.column()
            self.state = 387
            self.match(ExampleDSLParser.T__7)
            self.state = 388
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
        self.enterRule(localctx, 56, self.RULE_replaceValuesStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(ExampleDSLParser.REPLACE)
            self.state = 391
            self.match(ExampleDSLParser.VALUES)
            self.state = 392
            self.values()
            self.state = 393
            self.match(ExampleDSLParser.WITH)
            self.state = 394
            self.values()
            self.state = 395
            self.match(ExampleDSLParser.IN)
            self.state = 396
            self.match(ExampleDSLParser.COLUMN)
            self.state = 397
            self.match(ExampleDSLParser.T__6)
            self.state = 398
            self.column()
            self.state = 399
            self.match(ExampleDSLParser.T__7)
            self.state = 400
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
        self.enterRule(localctx, 58, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            _la = self._input.LA(1)
            if not(_la==64 or _la==65):
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
        self.enterRule(localctx, 60, self.RULE_addConditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(ExampleDSLParser.ADD)
            self.state = 405
            self.match(ExampleDSLParser.CONDITION)
            self.state = 406
            self.match(ExampleDSLParser.WHERE)
            self.state = 407
            self.column()
            self.state = 408
            self.match(ExampleDSLParser.T__5)
            self.state = 409
            self.value()
            self.state = 410
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
        self.enterRule(localctx, 62, self.RULE_removeDuplicatesStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(ExampleDSLParser.REMOVE)
            self.state = 413
            self.match(ExampleDSLParser.DUPLICATE)
            self.state = 414
            self.match(ExampleDSLParser.ROWS)
            self.state = 415
            self.match(ExampleDSLParser.BASED)
            self.state = 416
            self.match(ExampleDSLParser.ON)
            self.state = 417
            self.match(ExampleDSLParser.COLUMN)
            self.state = 418
            self.match(ExampleDSLParser.T__6)
            self.state = 419
            self.column()
            self.state = 420
            self.match(ExampleDSLParser.T__7)
            self.state = 421
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
        self.enterRule(localctx, 64, self.RULE_splitDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(ExampleDSLParser.SPLIT)
            self.state = 424
            self.match(ExampleDSLParser.DATA)
            self.state = 425
            self.match(ExampleDSLParser.BASED)
            self.state = 426
            self.match(ExampleDSLParser.ON)
            self.state = 427
            self.match(ExampleDSLParser.COLUMN)
            self.state = 428
            self.match(ExampleDSLParser.T__6)
            self.state = 429
            self.column()
            self.state = 430
            self.match(ExampleDSLParser.T__7)
            self.state = 431
            self.match(ExampleDSLParser.AND)
            self.state = 432
            self.match(ExampleDSLParser.SAVE)
            self.state = 433
            self.match(ExampleDSLParser.RESULTS)
            self.state = 434
            self.match(ExampleDSLParser.TO)
            self.state = 435
            self.match(ExampleDSLParser.SEPARATE)
            self.state = 436
            self.match(ExampleDSLParser.FILES)
            self.state = 437
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
        self.enterRule(localctx, 66, self.RULE_combineColumnsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(ExampleDSLParser.COMBINE)
            self.state = 440
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 441
            self.column()
            self.state = 442
            self.match(ExampleDSLParser.AND)
            self.state = 443
            self.column()
            self.state = 444
            self.match(ExampleDSLParser.AND)
            self.state = 445
            self.match(ExampleDSLParser.SAVE)
            self.state = 446
            self.match(ExampleDSLParser.RESULT)
            self.state = 447
            self.match(ExampleDSLParser.TO)
            self.state = 448
            self.result()
            self.state = 449
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
        self.enterRule(localctx, 68, self.RULE_resizeDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ExampleDSLParser.RESIZE)
            self.state = 452
            self.match(ExampleDSLParser.DATA)
            self.state = 453
            self.match(ExampleDSLParser.IN)
            self.state = 454
            self.match(ExampleDSLParser.COLUMN)
            self.state = 455
            self.match(ExampleDSLParser.T__6)
            self.state = 456
            self.column()
            self.state = 457
            self.match(ExampleDSLParser.T__7)
            self.state = 458
            self.match(ExampleDSLParser.BY)
            self.state = 459
            self.match(ExampleDSLParser.MULTIPLYING)
            self.state = 460
            self.match(ExampleDSLParser.WITH)
            self.state = 461
            self.value()
            self.state = 462
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateFromsheetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Update(self):
            return self.getToken(ExampleDSLParser.Update, 0)

        def FROM(self):
            return self.getToken(ExampleDSLParser.FROM, 0)

        def path(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.PathContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.PathContext,i)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_updateFromsheetStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateFromsheetStatement" ):
                listener.enterUpdateFromsheetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateFromsheetStatement" ):
                listener.exitUpdateFromsheetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateFromsheetStatement" ):
                return visitor.visitUpdateFromsheetStatement(self)
            else:
                return visitor.visitChildren(self)




    def updateFromsheetStatement(self):

        localctx = ExampleDSLParser.UpdateFromsheetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_updateFromsheetStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(ExampleDSLParser.Update)
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.state = 465
                self.path()
                pass
            elif token in [66]:
                self.state = 466
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 469
            self.match(ExampleDSLParser.FROM)
            self.state = 470
            self.path()
            self.state = 471
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtractTablesFromWebStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTRACT(self):
            return self.getToken(ExampleDSLParser.EXTRACT, 0)

        def FROM(self):
            return self.getToken(ExampleDSLParser.FROM, 0)

        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_extractTablesFromWebStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtractTablesFromWebStatement" ):
                listener.enterExtractTablesFromWebStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtractTablesFromWebStatement" ):
                listener.exitExtractTablesFromWebStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtractTablesFromWebStatement" ):
                return visitor.visitExtractTablesFromWebStatement(self)
            else:
                return visitor.visitChildren(self)




    def extractTablesFromWebStatement(self):

        localctx = ExampleDSLParser.ExtractTablesFromWebStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_extractTablesFromWebStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(ExampleDSLParser.EXTRACT)
            self.state = 474
            self.match(ExampleDSLParser.FROM)
            self.state = 475
            self.path()
            self.state = 476
            self.match(ExampleDSLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(ExampleDSLParser.ID, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = ExampleDSLParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(ExampleDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





