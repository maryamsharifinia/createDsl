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
        4,1,71,488,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,1,
        0,1,1,4,1,83,8,1,11,1,12,1,84,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,111,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,3,
        11,141,8,11,1,11,1,11,1,11,3,11,146,8,11,1,11,1,11,1,11,3,11,151,
        8,11,5,11,153,8,11,10,11,12,11,156,9,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,3,12,166,8,12,1,12,1,12,1,12,3,12,171,8,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,5,13,180,8,13,10,13,12,13,183,9,13,1,
        13,3,13,186,8,13,1,13,1,13,1,13,3,13,191,8,13,1,13,3,13,194,8,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,203,8,14,10,14,12,14,206,
        9,14,1,14,1,14,1,14,1,14,5,14,212,8,14,10,14,12,14,215,9,14,1,14,
        1,14,1,14,3,14,220,8,14,1,14,3,14,223,8,14,1,14,1,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,5,15,235,8,15,10,15,12,15,238,9,15,1,
        15,1,15,1,15,1,15,1,15,3,15,245,8,15,1,15,3,15,248,8,15,1,15,1,15,
        1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,262,8,17,
        1,17,3,17,265,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,5,18,274,8,
        18,10,18,12,18,277,9,18,1,18,1,18,1,18,3,18,282,8,18,1,18,3,18,285,
        8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,308,8,21,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,322,
        8,22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,5,24,333,8,24,
        10,24,12,24,336,9,24,1,24,1,24,1,24,1,24,5,24,342,8,24,10,24,12,
        24,345,9,24,1,24,1,24,1,24,3,24,350,8,24,1,24,3,24,353,8,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,
        368,8,25,1,25,3,25,371,8,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,468,8,35,1,
        35,1,35,1,36,1,36,1,36,3,36,475,8,36,1,36,1,36,1,36,1,36,1,37,1,
        37,1,37,1,37,1,37,1,38,1,38,1,38,0,0,39,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,72,74,76,0,2,1,0,3,5,1,0,65,66,504,0,78,1,0,0,0,2,82,
        1,0,0,0,4,110,1,0,0,0,6,112,1,0,0,0,8,117,1,0,0,0,10,123,1,0,0,0,
        12,126,1,0,0,0,14,129,1,0,0,0,16,131,1,0,0,0,18,133,1,0,0,0,20,135,
        1,0,0,0,22,137,1,0,0,0,24,160,1,0,0,0,26,174,1,0,0,0,28,197,1,0,
        0,0,30,226,1,0,0,0,32,251,1,0,0,0,34,253,1,0,0,0,36,268,1,0,0,0,
        38,288,1,0,0,0,40,295,1,0,0,0,42,297,1,0,0,0,44,311,1,0,0,0,46,325,
        1,0,0,0,48,327,1,0,0,0,50,356,1,0,0,0,52,374,1,0,0,0,54,382,1,0,
        0,0,56,384,1,0,0,0,58,394,1,0,0,0,60,406,1,0,0,0,62,408,1,0,0,0,
        64,416,1,0,0,0,66,427,1,0,0,0,68,443,1,0,0,0,70,455,1,0,0,0,72,471,
        1,0,0,0,74,480,1,0,0,0,76,485,1,0,0,0,78,79,3,2,1,0,79,80,5,0,0,
        1,80,1,1,0,0,0,81,83,3,4,2,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,
        0,0,0,84,85,1,0,0,0,85,3,1,0,0,0,86,111,3,6,3,0,87,111,3,8,4,0,88,
        111,3,22,11,0,89,111,3,24,12,0,90,111,3,26,13,0,91,111,3,28,14,0,
        92,111,3,30,15,0,93,111,3,34,17,0,94,111,3,36,18,0,95,111,3,38,19,
        0,96,111,3,42,21,0,97,111,3,44,22,0,98,111,3,48,24,0,99,111,3,50,
        25,0,100,111,3,52,26,0,101,111,3,56,28,0,102,111,3,58,29,0,103,111,
        3,62,31,0,104,111,3,64,32,0,105,111,3,66,33,0,106,111,3,68,34,0,
        107,111,3,70,35,0,108,111,3,72,36,0,109,111,3,74,37,0,110,86,1,0,
        0,0,110,87,1,0,0,0,110,88,1,0,0,0,110,89,1,0,0,0,110,90,1,0,0,0,
        110,91,1,0,0,0,110,92,1,0,0,0,110,93,1,0,0,0,110,94,1,0,0,0,110,
        95,1,0,0,0,110,96,1,0,0,0,110,97,1,0,0,0,110,98,1,0,0,0,110,99,1,
        0,0,0,110,100,1,0,0,0,110,101,1,0,0,0,110,102,1,0,0,0,110,103,1,
        0,0,0,110,104,1,0,0,0,110,105,1,0,0,0,110,106,1,0,0,0,110,107,1,
        0,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,5,1,0,0,0,112,113,5,10,
        0,0,113,114,3,14,7,0,114,115,3,10,5,0,115,116,5,1,0,0,116,7,1,0,
        0,0,117,118,5,9,0,0,118,119,3,76,38,0,119,120,5,46,0,0,120,121,3,
        14,7,0,121,122,5,1,0,0,122,9,1,0,0,0,123,124,5,55,0,0,124,125,3,
        76,38,0,125,11,1,0,0,0,126,127,5,46,0,0,127,128,3,16,8,0,128,13,
        1,0,0,0,129,130,5,66,0,0,130,15,1,0,0,0,131,132,5,66,0,0,132,17,
        1,0,0,0,133,134,5,66,0,0,134,19,1,0,0,0,135,136,5,61,0,0,136,21,
        1,0,0,0,137,140,5,15,0,0,138,141,3,14,7,0,139,141,3,76,38,0,140,
        138,1,0,0,0,140,139,1,0,0,0,141,142,1,0,0,0,142,145,5,2,0,0,143,
        146,3,14,7,0,144,146,3,76,38,0,145,143,1,0,0,0,145,144,1,0,0,0,146,
        154,1,0,0,0,147,150,5,2,0,0,148,151,3,14,7,0,149,151,3,76,38,0,150,
        148,1,0,0,0,150,149,1,0,0,0,151,153,1,0,0,0,152,147,1,0,0,0,153,
        156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,
        154,1,0,0,0,157,158,3,10,5,0,158,159,5,1,0,0,159,23,1,0,0,0,160,
        161,5,16,0,0,161,162,5,35,0,0,162,165,5,50,0,0,163,166,3,14,7,0,
        164,166,3,76,38,0,165,163,1,0,0,0,165,164,1,0,0,0,166,167,1,0,0,
        0,167,170,5,46,0,0,168,171,3,14,7,0,169,171,3,76,38,0,170,168,1,
        0,0,0,170,169,1,0,0,0,171,172,1,0,0,0,172,173,5,1,0,0,173,25,1,0,
        0,0,174,175,5,17,0,0,175,176,5,38,0,0,176,181,3,16,8,0,177,178,5,
        2,0,0,178,180,3,16,8,0,179,177,1,0,0,0,180,183,1,0,0,0,181,179,1,
        0,0,0,181,182,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,184,186,3,
        12,6,0,185,184,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,190,5,
        44,0,0,188,191,3,14,7,0,189,191,3,76,38,0,190,188,1,0,0,0,190,189,
        1,0,0,0,191,193,1,0,0,0,192,194,3,10,5,0,193,192,1,0,0,0,193,194,
        1,0,0,0,194,195,1,0,0,0,195,196,5,1,0,0,196,27,1,0,0,0,197,198,5,
        18,0,0,198,199,5,37,0,0,199,204,3,16,8,0,200,201,5,2,0,0,201,203,
        3,16,8,0,202,200,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,
        1,0,0,0,205,207,1,0,0,0,206,204,1,0,0,0,207,208,5,46,0,0,208,213,
        3,16,8,0,209,210,5,2,0,0,210,212,3,16,8,0,211,209,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,213,
        1,0,0,0,216,219,5,44,0,0,217,220,3,14,7,0,218,220,3,76,38,0,219,
        217,1,0,0,0,219,218,1,0,0,0,220,222,1,0,0,0,221,223,3,10,5,0,222,
        221,1,0,0,0,222,223,1,0,0,0,223,224,1,0,0,0,224,225,5,1,0,0,225,
        29,1,0,0,0,226,227,5,19,0,0,227,228,5,36,0,0,228,229,5,39,0,0,229,
        230,5,53,0,0,230,231,5,37,0,0,231,236,3,16,8,0,232,233,5,2,0,0,233,
        235,3,16,8,0,234,232,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,
        237,1,0,0,0,237,239,1,0,0,0,238,236,1,0,0,0,239,240,5,46,0,0,240,
        241,3,32,16,0,241,244,5,44,0,0,242,245,3,14,7,0,243,245,3,76,38,
        0,244,242,1,0,0,0,244,243,1,0,0,0,245,247,1,0,0,0,246,248,3,10,5,
        0,247,246,1,0,0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,250,5,1,0,
        0,250,31,1,0,0,0,251,252,5,39,0,0,252,33,1,0,0,0,253,254,5,20,0,
        0,254,255,5,36,0,0,255,256,5,49,0,0,256,257,5,37,0,0,257,258,3,16,
        8,0,258,261,5,44,0,0,259,262,3,14,7,0,260,262,3,76,38,0,261,259,
        1,0,0,0,261,260,1,0,0,0,262,264,1,0,0,0,263,265,3,10,5,0,264,263,
        1,0,0,0,264,265,1,0,0,0,265,266,1,0,0,0,266,267,5,1,0,0,267,35,1,
        0,0,0,268,269,5,21,0,0,269,270,5,37,0,0,270,275,3,16,8,0,271,272,
        5,2,0,0,272,274,3,16,8,0,273,271,1,0,0,0,274,277,1,0,0,0,275,273,
        1,0,0,0,275,276,1,0,0,0,276,278,1,0,0,0,277,275,1,0,0,0,278,281,
        5,44,0,0,279,282,3,14,7,0,280,282,3,76,38,0,281,279,1,0,0,0,281,
        280,1,0,0,0,282,284,1,0,0,0,283,285,3,10,5,0,284,283,1,0,0,0,284,
        285,1,0,0,0,285,286,1,0,0,0,286,287,5,1,0,0,287,37,1,0,0,0,288,289,
        5,18,0,0,289,290,5,12,0,0,290,291,5,33,0,0,291,292,5,46,0,0,292,
        293,3,40,20,0,293,294,5,1,0,0,294,39,1,0,0,0,295,296,5,66,0,0,296,
        41,1,0,0,0,297,298,5,22,0,0,298,299,5,42,0,0,299,300,5,52,0,0,300,
        301,5,40,0,0,301,302,5,65,0,0,302,303,5,46,0,0,303,304,5,65,0,0,
        304,307,5,44,0,0,305,308,3,14,7,0,306,308,3,76,38,0,307,305,1,0,
        0,0,307,306,1,0,0,0,308,309,1,0,0,0,309,310,5,1,0,0,310,43,1,0,0,
        0,311,312,5,23,0,0,312,313,5,13,0,0,313,314,5,54,0,0,314,315,5,37,
        0,0,315,316,3,16,8,0,316,317,5,49,0,0,317,318,3,46,23,0,318,321,
        5,44,0,0,319,322,3,14,7,0,320,322,3,76,38,0,321,319,1,0,0,0,321,
        320,1,0,0,0,322,323,1,0,0,0,323,324,5,1,0,0,324,45,1,0,0,0,325,326,
        7,0,0,0,326,47,1,0,0,0,327,328,5,24,0,0,328,329,5,38,0,0,329,334,
        3,16,8,0,330,331,5,2,0,0,331,333,3,16,8,0,332,330,1,0,0,0,333,336,
        1,0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,337,1,0,0,0,336,334,
        1,0,0,0,337,338,5,46,0,0,338,343,3,16,8,0,339,340,5,2,0,0,340,342,
        3,16,8,0,341,339,1,0,0,0,342,345,1,0,0,0,343,341,1,0,0,0,343,344,
        1,0,0,0,344,346,1,0,0,0,345,343,1,0,0,0,346,349,5,44,0,0,347,350,
        3,14,7,0,348,350,3,76,38,0,349,347,1,0,0,0,349,348,1,0,0,0,350,352,
        1,0,0,0,351,353,3,10,5,0,352,351,1,0,0,0,352,353,1,0,0,0,353,354,
        1,0,0,0,354,355,5,1,0,0,355,49,1,0,0,0,356,357,5,25,0,0,357,358,
        5,49,0,0,358,359,3,16,8,0,359,360,5,48,0,0,360,361,5,58,0,0,361,
        362,5,43,0,0,362,363,5,46,0,0,363,364,3,16,8,0,364,367,5,44,0,0,
        365,368,3,14,7,0,366,368,3,76,38,0,367,365,1,0,0,0,367,366,1,0,0,
        0,368,370,1,0,0,0,369,371,3,10,5,0,370,369,1,0,0,0,370,371,1,0,0,
        0,371,372,1,0,0,0,372,373,5,1,0,0,373,51,1,0,0,0,374,375,5,26,0,
        0,375,376,5,40,0,0,376,377,5,51,0,0,377,378,3,16,8,0,378,379,5,6,
        0,0,379,380,3,54,27,0,380,381,5,1,0,0,381,53,1,0,0,0,382,383,5,65,
        0,0,383,55,1,0,0,0,384,385,5,27,0,0,385,386,5,54,0,0,386,387,5,66,
        0,0,387,388,5,44,0,0,388,389,5,37,0,0,389,390,5,7,0,0,390,391,3,
        16,8,0,391,392,5,8,0,0,392,393,5,1,0,0,393,57,1,0,0,0,394,395,5,
        28,0,0,395,396,5,43,0,0,396,397,3,60,30,0,397,398,5,47,0,0,398,399,
        3,60,30,0,399,400,5,44,0,0,400,401,5,37,0,0,401,402,5,7,0,0,402,
        403,3,16,8,0,403,404,5,8,0,0,404,405,5,1,0,0,405,59,1,0,0,0,406,
        407,7,1,0,0,407,61,1,0,0,0,408,409,5,17,0,0,409,410,5,42,0,0,410,
        411,5,51,0,0,411,412,3,16,8,0,412,413,5,6,0,0,413,414,3,54,27,0,
        414,415,5,1,0,0,415,63,1,0,0,0,416,417,5,29,0,0,417,418,5,62,0,0,
        418,419,5,40,0,0,419,420,5,57,0,0,420,421,5,52,0,0,421,422,5,37,
        0,0,422,423,5,7,0,0,423,424,3,16,8,0,424,425,5,8,0,0,425,426,5,1,
        0,0,426,65,1,0,0,0,427,428,5,30,0,0,428,429,5,36,0,0,429,430,5,57,
        0,0,430,431,5,52,0,0,431,432,5,37,0,0,432,433,5,7,0,0,433,434,3,
        16,8,0,434,435,5,8,0,0,435,436,5,48,0,0,436,437,5,56,0,0,437,438,
        5,69,0,0,438,439,5,46,0,0,439,440,5,70,0,0,440,441,5,71,0,0,441,
        442,5,1,0,0,442,67,1,0,0,0,443,444,5,15,0,0,444,445,5,38,0,0,445,
        446,3,16,8,0,446,447,5,48,0,0,447,448,3,16,8,0,448,449,5,48,0,0,
        449,450,5,56,0,0,450,451,5,45,0,0,451,452,5,46,0,0,452,453,3,18,
        9,0,453,454,5,1,0,0,454,69,1,0,0,0,455,456,5,31,0,0,456,457,5,36,
        0,0,457,458,5,44,0,0,458,459,5,37,0,0,459,460,3,16,8,0,460,461,5,
        49,0,0,461,462,3,20,10,0,462,463,5,47,0,0,463,464,3,54,27,0,464,
        467,5,44,0,0,465,468,3,14,7,0,466,468,3,76,38,0,467,465,1,0,0,0,
        467,466,1,0,0,0,468,469,1,0,0,0,469,470,5,1,0,0,470,71,1,0,0,0,471,
        474,5,63,0,0,472,475,3,14,7,0,473,475,3,76,38,0,474,472,1,0,0,0,
        474,473,1,0,0,0,475,476,1,0,0,0,476,477,5,50,0,0,477,478,3,14,7,
        0,478,479,5,1,0,0,479,73,1,0,0,0,480,481,5,64,0,0,481,482,5,50,0,
        0,482,483,3,14,7,0,483,484,5,1,0,0,484,75,1,0,0,0,485,486,5,67,0,
        0,486,77,1,0,0,0,34,84,110,140,145,150,154,165,170,181,185,190,193,
        204,213,219,222,236,244,247,261,264,275,281,284,307,321,334,343,
        349,352,367,370,467,474
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
                     "'new'", "'multiplying'", "<INVALID>", "'duplicate'", 
                     "'update'", "'extract'" ]

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
                      "SAVE", "BASED", "SUM", "NEW", "MULTIPLYING", "OPERATION", 
                      "DUPLICATE", "Update", "EXTRACT", "NUMBER", "STRING", 
                      "ID", "WS", "RESULTS", "SEPARATE", "FILES" ]

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
    RULE_operation = 10
    RULE_combineStatement = 11
    RULE_convertStatement = 12
    RULE_addColumnsStatement = 13
    RULE_renameColumnStatement = 14
    RULE_changeDataTypeStatement = 15
    RULE_type = 16
    RULE_sortDataStatement = 17
    RULE_deleteColumnStatement = 18
    RULE_renameFileStatement = 19
    RULE_file_name = 20
    RULE_applyConditionStatement = 21
    RULE_generateReportStatement = 22
    RULE_period = 23
    RULE_reorderColumnsStatement = 24
    RULE_groupByStatement = 25
    RULE_filterRowsStatement = 26
    RULE_value = 27
    RULE_searchTextStatement = 28
    RULE_replaceValuesStatement = 29
    RULE_values = 30
    RULE_addConditionStatement = 31
    RULE_removeDuplicatesStatement = 32
    RULE_splitDataStatement = 33
    RULE_combineColumnsStatement = 34
    RULE_resizeDataStatement = 35
    RULE_updateFromsheetStatement = 36
    RULE_extractTablesFromWebStatement = 37
    RULE_id = 38

    ruleNames =  [ "start", "program", "statement", "importFileStatement", 
                   "exportFileStatement", "asStatement", "toStatement", 
                   "path", "column", "result", "operation", "combineStatement", 
                   "convertStatement", "addColumnsStatement", "renameColumnStatement", 
                   "changeDataTypeStatement", "type", "sortDataStatement", 
                   "deleteColumnStatement", "renameFileStatement", "file_name", 
                   "applyConditionStatement", "generateReportStatement", 
                   "period", "reorderColumnsStatement", "groupByStatement", 
                   "filterRowsStatement", "value", "searchTextStatement", 
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
    OPERATION=61
    DUPLICATE=62
    Update=63
    EXTRACT=64
    NUMBER=65
    STRING=66
    ID=67
    WS=68
    RESULTS=69
    SEPARATE=70
    FILES=71

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
            self.state = 78
            self.program()
            self.state = 79
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
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.statement()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & 54043195536834499) != 0)):
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
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.importFileStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.exportFileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.combineStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.convertStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.addColumnsStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.renameColumnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 92
                self.changeDataTypeStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 93
                self.sortDataStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 94
                self.deleteColumnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 95
                self.renameFileStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 96
                self.applyConditionStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 97
                self.generateReportStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 98
                self.reorderColumnsStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 99
                self.groupByStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 100
                self.filterRowsStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 101
                self.searchTextStatement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 102
                self.replaceValuesStatement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 103
                self.addConditionStatement()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 104
                self.removeDuplicatesStatement()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 105
                self.splitDataStatement()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 106
                self.combineColumnsStatement()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 107
                self.resizeDataStatement()
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 108
                self.updateFromsheetStatement()
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 109
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
            self.state = 112
            self.match(ExampleDSLParser.IMPORT)
            self.state = 113
            self.path()
            self.state = 114
            self.asStatement()
            self.state = 115
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
            self.state = 117
            self.match(ExampleDSLParser.EXPORT)
            self.state = 118
            self.id_()
            self.state = 119
            self.match(ExampleDSLParser.TO)
            self.state = 120
            self.path()
            self.state = 121
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
            self.state = 123
            self.match(ExampleDSLParser.AS)
            self.state = 124
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
            self.state = 126
            self.match(ExampleDSLParser.TO)
            self.state = 127
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
            self.state = 129
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
            self.state = 131
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
            self.state = 133
            self.match(ExampleDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATION(self):
            return self.getToken(ExampleDSLParser.OPERATION, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = ExampleDSLParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ExampleDSLParser.OPERATION)
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
        self.enterRule(localctx, 22, self.RULE_combineStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ExampleDSLParser.COMBINE)

            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 138
                self.path()
                pass
            elif token in [67]:
                self.state = 139
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 142
            self.match(ExampleDSLParser.T__1)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 143
                self.path()
                pass
            elif token in [67]:
                self.state = 144
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 147
                self.match(ExampleDSLParser.T__1)
                self.state = 150
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [66]:
                    self.state = 148
                    self.path()
                    pass
                elif token in [67]:
                    self.state = 149
                    self.id_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.asStatement()
            self.state = 158
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
        self.enterRule(localctx, 24, self.RULE_convertStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ExampleDSLParser.CONVERT)
            self.state = 161
            self.match(ExampleDSLParser.FORMAT)
            self.state = 162
            self.match(ExampleDSLParser.FROM)
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 163
                self.path()
                pass
            elif token in [67]:
                self.state = 164
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 167
            self.match(ExampleDSLParser.TO)
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 168
                self.path()
                pass
            elif token in [67]:
                self.state = 169
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 172
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
        self.enterRule(localctx, 26, self.RULE_addColumnsStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ExampleDSLParser.ADD)
            self.state = 175
            self.match(ExampleDSLParser.COLUMNS)

            self.state = 176
            self.column()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 177
                self.match(ExampleDSLParser.T__1)
                self.state = 178
                self.column()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 184
                self.toStatement()


            self.state = 187
            self.match(ExampleDSLParser.IN)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 188
                self.path()
                pass
            elif token in [67]:
                self.state = 189
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 192
                self.asStatement()


            self.state = 195
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
        self.enterRule(localctx, 28, self.RULE_renameColumnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ExampleDSLParser.RENAME)
            self.state = 198
            self.match(ExampleDSLParser.COLUMN)

            self.state = 199
            self.column()
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 200
                self.match(ExampleDSLParser.T__1)
                self.state = 201
                self.column()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(ExampleDSLParser.TO)

            self.state = 208
            self.column()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 209
                self.match(ExampleDSLParser.T__1)
                self.state = 210
                self.column()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(ExampleDSLParser.IN)
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 217
                self.path()
                pass
            elif token in [67]:
                self.state = 218
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 221
                self.asStatement()


            self.state = 224
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
        self.enterRule(localctx, 30, self.RULE_changeDataTypeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(ExampleDSLParser.CHANGE)
            self.state = 227
            self.match(ExampleDSLParser.DATA)
            self.state = 228
            self.match(ExampleDSLParser.TYPE)
            self.state = 229
            self.match(ExampleDSLParser.OF)
            self.state = 230
            self.match(ExampleDSLParser.COLUMN)

            self.state = 231
            self.column()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 232
                self.match(ExampleDSLParser.T__1)
                self.state = 233
                self.column()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(ExampleDSLParser.TO)
            self.state = 240
            self.type_()
            self.state = 241
            self.match(ExampleDSLParser.IN)
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 242
                self.path()
                pass
            elif token in [67]:
                self.state = 243
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 246
                self.asStatement()


            self.state = 249
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
        self.enterRule(localctx, 32, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
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
        self.enterRule(localctx, 34, self.RULE_sortDataStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ExampleDSLParser.SORT)
            self.state = 254
            self.match(ExampleDSLParser.DATA)
            self.state = 255
            self.match(ExampleDSLParser.BY)
            self.state = 256
            self.match(ExampleDSLParser.COLUMN)
            self.state = 257
            self.column()
            self.state = 258
            self.match(ExampleDSLParser.IN)
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 259
                self.path()
                pass
            elif token in [67]:
                self.state = 260
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 263
                self.asStatement()


            self.state = 266
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
        self.enterRule(localctx, 36, self.RULE_deleteColumnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ExampleDSLParser.DELETE)
            self.state = 269
            self.match(ExampleDSLParser.COLUMN)

            self.state = 270
            self.column()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 271
                self.match(ExampleDSLParser.T__1)
                self.state = 272
                self.column()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 278
            self.match(ExampleDSLParser.IN)
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 279
                self.path()
                pass
            elif token in [67]:
                self.state = 280
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 283
                self.asStatement()


            self.state = 286
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
        self.enterRule(localctx, 38, self.RULE_renameFileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ExampleDSLParser.RENAME)
            self.state = 289
            self.match(ExampleDSLParser.OUTPUT)
            self.state = 290
            self.match(ExampleDSLParser.FILE)
            self.state = 291
            self.match(ExampleDSLParser.TO)
            self.state = 292
            self.file_name()
            self.state = 293
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
        self.enterRule(localctx, 40, self.RULE_file_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
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
        self.enterRule(localctx, 42, self.RULE_applyConditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ExampleDSLParser.APPLY)
            self.state = 298
            self.match(ExampleDSLParser.CONDITION)
            self.state = 299
            self.match(ExampleDSLParser.ON)
            self.state = 300
            self.match(ExampleDSLParser.ROWS)
            self.state = 301
            localctx.from_ = self.match(ExampleDSLParser.NUMBER)
            self.state = 302
            self.match(ExampleDSLParser.TO)
            self.state = 303
            localctx.to = self.match(ExampleDSLParser.NUMBER)
            self.state = 304
            self.match(ExampleDSLParser.IN)
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 305
                self.path()
                pass
            elif token in [67]:
                self.state = 306
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 309
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
        self.enterRule(localctx, 44, self.RULE_generateReportStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ExampleDSLParser.GENERATE)
            self.state = 312
            self.match(ExampleDSLParser.REPORT)
            self.state = 313
            self.match(ExampleDSLParser.FOR)
            self.state = 314
            self.match(ExampleDSLParser.COLUMN)
            self.state = 315
            self.column()
            self.state = 316
            self.match(ExampleDSLParser.BY)
            self.state = 317
            self.period()
            self.state = 318
            self.match(ExampleDSLParser.IN)
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 319
                self.path()
                pass
            elif token in [67]:
                self.state = 320
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 323
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
        self.enterRule(localctx, 46, self.RULE_period)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
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
        self.enterRule(localctx, 48, self.RULE_reorderColumnsStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ExampleDSLParser.REORDER)
            self.state = 328
            self.match(ExampleDSLParser.COLUMNS)

            self.state = 329
            self.column()
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 330
                self.match(ExampleDSLParser.T__1)
                self.state = 331
                self.column()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 337
            self.match(ExampleDSLParser.TO)

            self.state = 338
            self.column()
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 339
                self.match(ExampleDSLParser.T__1)
                self.state = 340
                self.column()
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
            self.match(ExampleDSLParser.IN)
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 347
                self.path()
                pass
            elif token in [67]:
                self.state = 348
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 351
                self.asStatement()


            self.state = 354
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
        self.enterRule(localctx, 50, self.RULE_groupByStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ExampleDSLParser.GROUP)
            self.state = 357
            self.match(ExampleDSLParser.BY)
            self.state = 358
            self.column()
            self.state = 359
            self.match(ExampleDSLParser.AND)
            self.state = 360
            self.match(ExampleDSLParser.SUM)
            self.state = 361
            self.match(ExampleDSLParser.VALUES)
            self.state = 362
            self.match(ExampleDSLParser.TO)
            self.state = 363
            self.column()
            self.state = 364
            self.match(ExampleDSLParser.IN)
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 365
                self.path()
                pass
            elif token in [67]:
                self.state = 366
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 369
                self.asStatement()


            self.state = 372
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
        self.enterRule(localctx, 52, self.RULE_filterRowsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(ExampleDSLParser.FILTER)
            self.state = 375
            self.match(ExampleDSLParser.ROWS)
            self.state = 376
            self.match(ExampleDSLParser.WHERE)
            self.state = 377
            self.column()
            self.state = 378
            self.match(ExampleDSLParser.T__5)
            self.state = 379
            self.value()
            self.state = 380
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
        self.enterRule(localctx, 54, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
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
        self.enterRule(localctx, 56, self.RULE_searchTextStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(ExampleDSLParser.SEARCH)
            self.state = 385
            self.match(ExampleDSLParser.FOR)
            self.state = 386
            localctx.text = self.match(ExampleDSLParser.STRING)
            self.state = 387
            self.match(ExampleDSLParser.IN)
            self.state = 388
            self.match(ExampleDSLParser.COLUMN)
            self.state = 389
            self.match(ExampleDSLParser.T__6)
            self.state = 390
            self.column()
            self.state = 391
            self.match(ExampleDSLParser.T__7)
            self.state = 392
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
        self.enterRule(localctx, 58, self.RULE_replaceValuesStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(ExampleDSLParser.REPLACE)
            self.state = 395
            self.match(ExampleDSLParser.VALUES)
            self.state = 396
            self.values()
            self.state = 397
            self.match(ExampleDSLParser.WITH)
            self.state = 398
            self.values()
            self.state = 399
            self.match(ExampleDSLParser.IN)
            self.state = 400
            self.match(ExampleDSLParser.COLUMN)
            self.state = 401
            self.match(ExampleDSLParser.T__6)
            self.state = 402
            self.column()
            self.state = 403
            self.match(ExampleDSLParser.T__7)
            self.state = 404
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
        self.enterRule(localctx, 60, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            _la = self._input.LA(1)
            if not(_la==65 or _la==66):
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
        self.enterRule(localctx, 62, self.RULE_addConditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(ExampleDSLParser.ADD)
            self.state = 409
            self.match(ExampleDSLParser.CONDITION)
            self.state = 410
            self.match(ExampleDSLParser.WHERE)
            self.state = 411
            self.column()
            self.state = 412
            self.match(ExampleDSLParser.T__5)
            self.state = 413
            self.value()
            self.state = 414
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
        self.enterRule(localctx, 64, self.RULE_removeDuplicatesStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(ExampleDSLParser.REMOVE)
            self.state = 417
            self.match(ExampleDSLParser.DUPLICATE)
            self.state = 418
            self.match(ExampleDSLParser.ROWS)
            self.state = 419
            self.match(ExampleDSLParser.BASED)
            self.state = 420
            self.match(ExampleDSLParser.ON)
            self.state = 421
            self.match(ExampleDSLParser.COLUMN)
            self.state = 422
            self.match(ExampleDSLParser.T__6)
            self.state = 423
            self.column()
            self.state = 424
            self.match(ExampleDSLParser.T__7)
            self.state = 425
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
        self.enterRule(localctx, 66, self.RULE_splitDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(ExampleDSLParser.SPLIT)
            self.state = 428
            self.match(ExampleDSLParser.DATA)
            self.state = 429
            self.match(ExampleDSLParser.BASED)
            self.state = 430
            self.match(ExampleDSLParser.ON)
            self.state = 431
            self.match(ExampleDSLParser.COLUMN)
            self.state = 432
            self.match(ExampleDSLParser.T__6)
            self.state = 433
            self.column()
            self.state = 434
            self.match(ExampleDSLParser.T__7)
            self.state = 435
            self.match(ExampleDSLParser.AND)
            self.state = 436
            self.match(ExampleDSLParser.SAVE)
            self.state = 437
            self.match(ExampleDSLParser.RESULTS)
            self.state = 438
            self.match(ExampleDSLParser.TO)
            self.state = 439
            self.match(ExampleDSLParser.SEPARATE)
            self.state = 440
            self.match(ExampleDSLParser.FILES)
            self.state = 441
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
        self.enterRule(localctx, 68, self.RULE_combineColumnsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(ExampleDSLParser.COMBINE)
            self.state = 444
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 445
            self.column()
            self.state = 446
            self.match(ExampleDSLParser.AND)
            self.state = 447
            self.column()
            self.state = 448
            self.match(ExampleDSLParser.AND)
            self.state = 449
            self.match(ExampleDSLParser.SAVE)
            self.state = 450
            self.match(ExampleDSLParser.RESULT)
            self.state = 451
            self.match(ExampleDSLParser.TO)
            self.state = 452
            self.result()
            self.state = 453
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

        def IN(self, i:int=None):
            if i is None:
                return self.getTokens(ExampleDSLParser.IN)
            else:
                return self.getToken(ExampleDSLParser.IN, i)

        def COLUMN(self):
            return self.getToken(ExampleDSLParser.COLUMN, 0)

        def column(self):
            return self.getTypedRuleContext(ExampleDSLParser.ColumnContext,0)


        def BY(self):
            return self.getToken(ExampleDSLParser.BY, 0)

        def operation(self):
            return self.getTypedRuleContext(ExampleDSLParser.OperationContext,0)


        def WITH(self):
            return self.getToken(ExampleDSLParser.WITH, 0)

        def value(self):
            return self.getTypedRuleContext(ExampleDSLParser.ValueContext,0)


        def path(self):
            return self.getTypedRuleContext(ExampleDSLParser.PathContext,0)


        def id_(self):
            return self.getTypedRuleContext(ExampleDSLParser.IdContext,0)


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
        self.enterRule(localctx, 70, self.RULE_resizeDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(ExampleDSLParser.RESIZE)
            self.state = 456
            self.match(ExampleDSLParser.DATA)
            self.state = 457
            self.match(ExampleDSLParser.IN)
            self.state = 458
            self.match(ExampleDSLParser.COLUMN)
            self.state = 459
            self.column()
            self.state = 460
            self.match(ExampleDSLParser.BY)
            self.state = 461
            self.operation()
            self.state = 462
            self.match(ExampleDSLParser.WITH)
            self.state = 463
            self.value()
            self.state = 464
            self.match(ExampleDSLParser.IN)
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 465
                self.path()
                pass
            elif token in [67]:
                self.state = 466
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 469
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
        self.enterRule(localctx, 72, self.RULE_updateFromsheetStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(ExampleDSLParser.Update)
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.state = 472
                self.path()
                pass
            elif token in [67]:
                self.state = 473
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 476
            self.match(ExampleDSLParser.FROM)
            self.state = 477
            self.path()
            self.state = 478
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
        self.enterRule(localctx, 74, self.RULE_extractTablesFromWebStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(ExampleDSLParser.EXTRACT)
            self.state = 481
            self.match(ExampleDSLParser.FROM)
            self.state = 482
            self.path()
            self.state = 483
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
        self.enterRule(localctx, 76, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(ExampleDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





