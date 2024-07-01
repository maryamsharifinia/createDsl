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
        4,1,69,473,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,4,1,79,8,1,11,
        1,12,1,80,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,106,8,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,
        8,1,8,1,9,1,9,1,10,1,10,1,10,3,10,134,8,10,1,10,1,10,1,10,3,10,139,
        8,10,1,10,1,10,1,10,3,10,144,8,10,5,10,146,8,10,10,10,12,10,149,
        9,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,159,8,11,1,11,
        1,11,1,11,3,11,164,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,5,12,
        173,8,12,10,12,12,12,176,9,12,1,12,3,12,179,8,12,1,12,1,12,1,12,
        3,12,184,8,12,1,12,3,12,187,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        13,5,13,196,8,13,10,13,12,13,199,9,13,1,13,1,13,1,13,1,13,5,13,205,
        8,13,10,13,12,13,208,9,13,1,13,1,13,1,13,3,13,213,8,13,1,13,3,13,
        216,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,
        228,8,14,10,14,12,14,231,9,14,1,14,1,14,1,14,1,14,1,14,3,14,238,
        8,14,1,14,3,14,241,8,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,255,8,16,1,16,3,16,258,8,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,5,17,267,8,17,10,17,12,17,270,9,17,1,17,1,
        17,1,17,3,17,275,8,17,1,17,3,17,278,8,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,3,20,301,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,3,21,315,8,21,1,21,1,21,1,22,1,22,1,23,
        1,23,1,23,1,23,1,23,5,23,326,8,23,10,23,12,23,329,9,23,1,23,1,23,
        1,23,1,23,5,23,335,8,23,10,23,12,23,338,9,23,1,23,1,23,1,23,3,23,
        343,8,23,1,23,3,23,346,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,3,24,361,8,24,1,24,3,24,364,8,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,35,1,35,1,35,3,35,465,8,35,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,0,0,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,0,2,1,0,3,5,1,0,63,64,489,0,74,1,0,0,0,2,78,1,0,0,0,4,105,1,0,
        0,0,6,107,1,0,0,0,8,112,1,0,0,0,10,118,1,0,0,0,12,121,1,0,0,0,14,
        124,1,0,0,0,16,126,1,0,0,0,18,128,1,0,0,0,20,130,1,0,0,0,22,153,
        1,0,0,0,24,167,1,0,0,0,26,190,1,0,0,0,28,219,1,0,0,0,30,244,1,0,
        0,0,32,246,1,0,0,0,34,261,1,0,0,0,36,281,1,0,0,0,38,288,1,0,0,0,
        40,290,1,0,0,0,42,304,1,0,0,0,44,318,1,0,0,0,46,320,1,0,0,0,48,349,
        1,0,0,0,50,367,1,0,0,0,52,375,1,0,0,0,54,377,1,0,0,0,56,387,1,0,
        0,0,58,399,1,0,0,0,60,401,1,0,0,0,62,409,1,0,0,0,64,420,1,0,0,0,
        66,436,1,0,0,0,68,448,1,0,0,0,70,461,1,0,0,0,72,470,1,0,0,0,74,75,
        3,2,1,0,75,76,5,0,0,1,76,1,1,0,0,0,77,79,3,4,2,0,78,77,1,0,0,0,79,
        80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,3,1,0,0,0,82,106,3,6,3,
        0,83,106,3,8,4,0,84,106,3,20,10,0,85,106,3,22,11,0,86,106,3,24,12,
        0,87,106,3,26,13,0,88,106,3,28,14,0,89,106,3,32,16,0,90,106,3,34,
        17,0,91,106,3,36,18,0,92,106,3,40,20,0,93,106,3,42,21,0,94,106,3,
        46,23,0,95,106,3,48,24,0,96,106,3,50,25,0,97,106,3,54,27,0,98,106,
        3,56,28,0,99,106,3,60,30,0,100,106,3,62,31,0,101,106,3,64,32,0,102,
        106,3,66,33,0,103,106,3,68,34,0,104,106,3,70,35,0,105,82,1,0,0,0,
        105,83,1,0,0,0,105,84,1,0,0,0,105,85,1,0,0,0,105,86,1,0,0,0,105,
        87,1,0,0,0,105,88,1,0,0,0,105,89,1,0,0,0,105,90,1,0,0,0,105,91,1,
        0,0,0,105,92,1,0,0,0,105,93,1,0,0,0,105,94,1,0,0,0,105,95,1,0,0,
        0,105,96,1,0,0,0,105,97,1,0,0,0,105,98,1,0,0,0,105,99,1,0,0,0,105,
        100,1,0,0,0,105,101,1,0,0,0,105,102,1,0,0,0,105,103,1,0,0,0,105,
        104,1,0,0,0,106,5,1,0,0,0,107,108,5,10,0,0,108,109,3,14,7,0,109,
        110,3,10,5,0,110,111,5,1,0,0,111,7,1,0,0,0,112,113,5,9,0,0,113,114,
        3,72,36,0,114,115,5,46,0,0,115,116,3,14,7,0,116,117,5,1,0,0,117,
        9,1,0,0,0,118,119,5,55,0,0,119,120,3,72,36,0,120,11,1,0,0,0,121,
        122,5,46,0,0,122,123,3,16,8,0,123,13,1,0,0,0,124,125,5,64,0,0,125,
        15,1,0,0,0,126,127,5,64,0,0,127,17,1,0,0,0,128,129,5,64,0,0,129,
        19,1,0,0,0,130,133,5,15,0,0,131,134,3,14,7,0,132,134,3,72,36,0,133,
        131,1,0,0,0,133,132,1,0,0,0,134,135,1,0,0,0,135,138,5,2,0,0,136,
        139,3,14,7,0,137,139,3,72,36,0,138,136,1,0,0,0,138,137,1,0,0,0,139,
        147,1,0,0,0,140,143,5,2,0,0,141,144,3,14,7,0,142,144,3,72,36,0,143,
        141,1,0,0,0,143,142,1,0,0,0,144,146,1,0,0,0,145,140,1,0,0,0,146,
        149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,
        147,1,0,0,0,150,151,3,10,5,0,151,152,5,1,0,0,152,21,1,0,0,0,153,
        154,5,16,0,0,154,155,5,35,0,0,155,158,5,50,0,0,156,159,3,14,7,0,
        157,159,3,72,36,0,158,156,1,0,0,0,158,157,1,0,0,0,159,160,1,0,0,
        0,160,163,5,46,0,0,161,164,3,14,7,0,162,164,3,72,36,0,163,161,1,
        0,0,0,163,162,1,0,0,0,164,165,1,0,0,0,165,166,5,1,0,0,166,23,1,0,
        0,0,167,168,5,17,0,0,168,169,5,38,0,0,169,174,3,16,8,0,170,171,5,
        2,0,0,171,173,3,16,8,0,172,170,1,0,0,0,173,176,1,0,0,0,174,172,1,
        0,0,0,174,175,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,177,179,3,
        12,6,0,178,177,1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,183,5,
        44,0,0,181,184,3,14,7,0,182,184,3,72,36,0,183,181,1,0,0,0,183,182,
        1,0,0,0,184,186,1,0,0,0,185,187,3,10,5,0,186,185,1,0,0,0,186,187,
        1,0,0,0,187,188,1,0,0,0,188,189,5,1,0,0,189,25,1,0,0,0,190,191,5,
        18,0,0,191,192,5,37,0,0,192,197,3,16,8,0,193,194,5,2,0,0,194,196,
        3,16,8,0,195,193,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,
        1,0,0,0,198,200,1,0,0,0,199,197,1,0,0,0,200,201,5,46,0,0,201,206,
        3,16,8,0,202,203,5,2,0,0,203,205,3,16,8,0,204,202,1,0,0,0,205,208,
        1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,206,
        1,0,0,0,209,212,5,44,0,0,210,213,3,14,7,0,211,213,3,72,36,0,212,
        210,1,0,0,0,212,211,1,0,0,0,213,215,1,0,0,0,214,216,3,10,5,0,215,
        214,1,0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,218,5,1,0,0,218,
        27,1,0,0,0,219,220,5,19,0,0,220,221,5,36,0,0,221,222,5,39,0,0,222,
        223,5,53,0,0,223,224,5,37,0,0,224,229,3,16,8,0,225,226,5,2,0,0,226,
        228,3,16,8,0,227,225,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,
        230,1,0,0,0,230,232,1,0,0,0,231,229,1,0,0,0,232,233,5,46,0,0,233,
        234,3,30,15,0,234,237,5,44,0,0,235,238,3,14,7,0,236,238,3,72,36,
        0,237,235,1,0,0,0,237,236,1,0,0,0,238,240,1,0,0,0,239,241,3,10,5,
        0,240,239,1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,243,5,1,0,
        0,243,29,1,0,0,0,244,245,5,39,0,0,245,31,1,0,0,0,246,247,5,20,0,
        0,247,248,5,36,0,0,248,249,5,49,0,0,249,250,5,37,0,0,250,251,3,16,
        8,0,251,254,5,44,0,0,252,255,3,14,7,0,253,255,3,72,36,0,254,252,
        1,0,0,0,254,253,1,0,0,0,255,257,1,0,0,0,256,258,3,10,5,0,257,256,
        1,0,0,0,257,258,1,0,0,0,258,259,1,0,0,0,259,260,5,1,0,0,260,33,1,
        0,0,0,261,262,5,21,0,0,262,263,5,37,0,0,263,268,3,16,8,0,264,265,
        5,2,0,0,265,267,3,16,8,0,266,264,1,0,0,0,267,270,1,0,0,0,268,266,
        1,0,0,0,268,269,1,0,0,0,269,271,1,0,0,0,270,268,1,0,0,0,271,274,
        5,44,0,0,272,275,3,14,7,0,273,275,3,72,36,0,274,272,1,0,0,0,274,
        273,1,0,0,0,275,277,1,0,0,0,276,278,3,10,5,0,277,276,1,0,0,0,277,
        278,1,0,0,0,278,279,1,0,0,0,279,280,5,1,0,0,280,35,1,0,0,0,281,282,
        5,18,0,0,282,283,5,12,0,0,283,284,5,33,0,0,284,285,5,46,0,0,285,
        286,3,38,19,0,286,287,5,1,0,0,287,37,1,0,0,0,288,289,5,64,0,0,289,
        39,1,0,0,0,290,291,5,22,0,0,291,292,5,42,0,0,292,293,5,52,0,0,293,
        294,5,40,0,0,294,295,5,63,0,0,295,296,5,46,0,0,296,297,5,63,0,0,
        297,300,5,44,0,0,298,301,3,14,7,0,299,301,3,72,36,0,300,298,1,0,
        0,0,300,299,1,0,0,0,301,302,1,0,0,0,302,303,5,1,0,0,303,41,1,0,0,
        0,304,305,5,23,0,0,305,306,5,13,0,0,306,307,5,54,0,0,307,308,5,37,
        0,0,308,309,3,16,8,0,309,310,5,49,0,0,310,311,3,44,22,0,311,314,
        5,44,0,0,312,315,3,14,7,0,313,315,3,72,36,0,314,312,1,0,0,0,314,
        313,1,0,0,0,315,316,1,0,0,0,316,317,5,1,0,0,317,43,1,0,0,0,318,319,
        7,0,0,0,319,45,1,0,0,0,320,321,5,24,0,0,321,322,5,38,0,0,322,327,
        3,16,8,0,323,324,5,2,0,0,324,326,3,16,8,0,325,323,1,0,0,0,326,329,
        1,0,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,330,1,0,0,0,329,327,
        1,0,0,0,330,331,5,46,0,0,331,336,3,16,8,0,332,333,5,2,0,0,333,335,
        3,16,8,0,334,332,1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,336,337,
        1,0,0,0,337,339,1,0,0,0,338,336,1,0,0,0,339,342,5,44,0,0,340,343,
        3,14,7,0,341,343,3,72,36,0,342,340,1,0,0,0,342,341,1,0,0,0,343,345,
        1,0,0,0,344,346,3,10,5,0,345,344,1,0,0,0,345,346,1,0,0,0,346,347,
        1,0,0,0,347,348,5,1,0,0,348,47,1,0,0,0,349,350,5,25,0,0,350,351,
        5,49,0,0,351,352,3,16,8,0,352,353,5,48,0,0,353,354,5,58,0,0,354,
        355,5,43,0,0,355,356,5,46,0,0,356,357,3,16,8,0,357,360,5,44,0,0,
        358,361,3,14,7,0,359,361,3,72,36,0,360,358,1,0,0,0,360,359,1,0,0,
        0,361,363,1,0,0,0,362,364,3,10,5,0,363,362,1,0,0,0,363,364,1,0,0,
        0,364,365,1,0,0,0,365,366,5,1,0,0,366,49,1,0,0,0,367,368,5,26,0,
        0,368,369,5,40,0,0,369,370,5,51,0,0,370,371,3,16,8,0,371,372,5,6,
        0,0,372,373,3,52,26,0,373,374,5,1,0,0,374,51,1,0,0,0,375,376,5,63,
        0,0,376,53,1,0,0,0,377,378,5,27,0,0,378,379,5,54,0,0,379,380,5,64,
        0,0,380,381,5,44,0,0,381,382,5,37,0,0,382,383,5,7,0,0,383,384,3,
        16,8,0,384,385,5,8,0,0,385,386,5,1,0,0,386,55,1,0,0,0,387,388,5,
        28,0,0,388,389,5,43,0,0,389,390,3,58,29,0,390,391,5,47,0,0,391,392,
        3,58,29,0,392,393,5,44,0,0,393,394,5,37,0,0,394,395,5,7,0,0,395,
        396,3,16,8,0,396,397,5,8,0,0,397,398,5,1,0,0,398,57,1,0,0,0,399,
        400,7,1,0,0,400,59,1,0,0,0,401,402,5,17,0,0,402,403,5,42,0,0,403,
        404,5,51,0,0,404,405,3,16,8,0,405,406,5,6,0,0,406,407,3,52,26,0,
        407,408,5,1,0,0,408,61,1,0,0,0,409,410,5,29,0,0,410,411,5,61,0,0,
        411,412,5,40,0,0,412,413,5,57,0,0,413,414,5,52,0,0,414,415,5,37,
        0,0,415,416,5,7,0,0,416,417,3,16,8,0,417,418,5,8,0,0,418,419,5,1,
        0,0,419,63,1,0,0,0,420,421,5,30,0,0,421,422,5,36,0,0,422,423,5,57,
        0,0,423,424,5,52,0,0,424,425,5,37,0,0,425,426,5,7,0,0,426,427,3,
        16,8,0,427,428,5,8,0,0,428,429,5,48,0,0,429,430,5,56,0,0,430,431,
        5,67,0,0,431,432,5,46,0,0,432,433,5,68,0,0,433,434,5,69,0,0,434,
        435,5,1,0,0,435,65,1,0,0,0,436,437,5,15,0,0,437,438,5,38,0,0,438,
        439,3,16,8,0,439,440,5,48,0,0,440,441,3,16,8,0,441,442,5,48,0,0,
        442,443,5,56,0,0,443,444,5,45,0,0,444,445,5,46,0,0,445,446,3,18,
        9,0,446,447,5,1,0,0,447,67,1,0,0,0,448,449,5,31,0,0,449,450,5,36,
        0,0,450,451,5,44,0,0,451,452,5,37,0,0,452,453,5,7,0,0,453,454,3,
        16,8,0,454,455,5,8,0,0,455,456,5,49,0,0,456,457,5,60,0,0,457,458,
        5,47,0,0,458,459,3,52,26,0,459,460,5,1,0,0,460,69,1,0,0,0,461,464,
        5,62,0,0,462,465,3,14,7,0,463,465,3,72,36,0,464,462,1,0,0,0,464,
        463,1,0,0,0,465,466,1,0,0,0,466,467,5,50,0,0,467,468,3,14,7,0,468,
        469,5,1,0,0,469,71,1,0,0,0,470,471,5,65,0,0,471,73,1,0,0,0,33,80,
        105,133,138,143,147,158,163,174,178,183,186,197,206,212,215,229,
        237,240,254,257,268,274,277,300,314,327,336,342,345,360,363,464
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
                     "'new'", "'multiplying'", "'duplicate'", "'update'" ]

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
                      "Update", "NUMBER", "STRING", "ID", "WS", "RESULTS", 
                      "SEPARATE", "FILES" ]

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
    RULE_id = 36

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
                   "resizeDataStatement", "updateFromsheetStatement", "id" ]

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
    NUMBER=63
    STRING=64
    ID=65
    WS=66
    RESULTS=67
    SEPARATE=68
    FILES=69

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
            self.state = 74
            self.program()
            self.state = 75
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
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.statement()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686022722323968) != 0)):
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
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.importFileStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.exportFileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.combineStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.convertStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.addColumnsStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.renameColumnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 88
                self.changeDataTypeStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 89
                self.sortDataStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 90
                self.deleteColumnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 91
                self.renameFileStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 92
                self.applyConditionStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 93
                self.generateReportStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 94
                self.reorderColumnsStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 95
                self.groupByStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 96
                self.filterRowsStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 97
                self.searchTextStatement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 98
                self.replaceValuesStatement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 99
                self.addConditionStatement()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 100
                self.removeDuplicatesStatement()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 101
                self.splitDataStatement()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 102
                self.combineColumnsStatement()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 103
                self.resizeDataStatement()
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 104
                self.updateFromsheetStatement()
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
            self.state = 107
            self.match(ExampleDSLParser.IMPORT)
            self.state = 108
            self.path()
            self.state = 109
            self.asStatement()
            self.state = 110
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
            self.state = 112
            self.match(ExampleDSLParser.EXPORT)
            self.state = 113
            self.id_()
            self.state = 114
            self.match(ExampleDSLParser.TO)
            self.state = 115
            self.path()
            self.state = 116
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
            self.state = 118
            self.match(ExampleDSLParser.AS)
            self.state = 119
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
            self.state = 121
            self.match(ExampleDSLParser.TO)
            self.state = 122
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
            self.state = 124
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
            self.state = 126
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
            self.state = 128
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
            self.state = 130
            self.match(ExampleDSLParser.COMBINE)

            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 131
                self.path()
                pass
            elif token in [65]:
                self.state = 132
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 135
            self.match(ExampleDSLParser.T__1)
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 136
                self.path()
                pass
            elif token in [65]:
                self.state = 137
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 140
                self.match(ExampleDSLParser.T__1)
                self.state = 143
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [64]:
                    self.state = 141
                    self.path()
                    pass
                elif token in [65]:
                    self.state = 142
                    self.id_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.asStatement()
            self.state = 151
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
            self.state = 153
            self.match(ExampleDSLParser.CONVERT)
            self.state = 154
            self.match(ExampleDSLParser.FORMAT)
            self.state = 155
            self.match(ExampleDSLParser.FROM)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 156
                self.path()
                pass
            elif token in [65]:
                self.state = 157
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 160
            self.match(ExampleDSLParser.TO)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 161
                self.path()
                pass
            elif token in [65]:
                self.state = 162
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 165
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
            self.state = 167
            self.match(ExampleDSLParser.ADD)
            self.state = 168
            self.match(ExampleDSLParser.COLUMNS)

            self.state = 169
            self.column()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 170
                self.match(ExampleDSLParser.T__1)
                self.state = 171
                self.column()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 177
                self.toStatement()


            self.state = 180
            self.match(ExampleDSLParser.IN)
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 181
                self.path()
                pass
            elif token in [65]:
                self.state = 182
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 185
                self.asStatement()


            self.state = 188
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
            self.state = 190
            self.match(ExampleDSLParser.RENAME)
            self.state = 191
            self.match(ExampleDSLParser.COLUMN)

            self.state = 192
            self.column()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 193
                self.match(ExampleDSLParser.T__1)
                self.state = 194
                self.column()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self.match(ExampleDSLParser.TO)

            self.state = 201
            self.column()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 202
                self.match(ExampleDSLParser.T__1)
                self.state = 203
                self.column()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
            self.match(ExampleDSLParser.IN)
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 210
                self.path()
                pass
            elif token in [65]:
                self.state = 211
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 214
                self.asStatement()


            self.state = 217
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
            self.state = 219
            self.match(ExampleDSLParser.CHANGE)
            self.state = 220
            self.match(ExampleDSLParser.DATA)
            self.state = 221
            self.match(ExampleDSLParser.TYPE)
            self.state = 222
            self.match(ExampleDSLParser.OF)
            self.state = 223
            self.match(ExampleDSLParser.COLUMN)

            self.state = 224
            self.column()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 225
                self.match(ExampleDSLParser.T__1)
                self.state = 226
                self.column()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.match(ExampleDSLParser.TO)
            self.state = 233
            self.type_()
            self.state = 234
            self.match(ExampleDSLParser.IN)
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 235
                self.path()
                pass
            elif token in [65]:
                self.state = 236
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 239
                self.asStatement()


            self.state = 242
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
            self.state = 244
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
            self.state = 246
            self.match(ExampleDSLParser.SORT)
            self.state = 247
            self.match(ExampleDSLParser.DATA)
            self.state = 248
            self.match(ExampleDSLParser.BY)
            self.state = 249
            self.match(ExampleDSLParser.COLUMN)
            self.state = 250
            self.column()
            self.state = 251
            self.match(ExampleDSLParser.IN)
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 252
                self.path()
                pass
            elif token in [65]:
                self.state = 253
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 256
                self.asStatement()


            self.state = 259
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
            self.state = 261
            self.match(ExampleDSLParser.DELETE)
            self.state = 262
            self.match(ExampleDSLParser.COLUMN)

            self.state = 263
            self.column()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 264
                self.match(ExampleDSLParser.T__1)
                self.state = 265
                self.column()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self.match(ExampleDSLParser.IN)
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 272
                self.path()
                pass
            elif token in [65]:
                self.state = 273
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 276
                self.asStatement()


            self.state = 279
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
            self.state = 281
            self.match(ExampleDSLParser.RENAME)
            self.state = 282
            self.match(ExampleDSLParser.OUTPUT)
            self.state = 283
            self.match(ExampleDSLParser.FILE)
            self.state = 284
            self.match(ExampleDSLParser.TO)
            self.state = 285
            self.file_name()
            self.state = 286
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
            self.state = 288
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
            self.state = 290
            self.match(ExampleDSLParser.APPLY)
            self.state = 291
            self.match(ExampleDSLParser.CONDITION)
            self.state = 292
            self.match(ExampleDSLParser.ON)
            self.state = 293
            self.match(ExampleDSLParser.ROWS)
            self.state = 294
            localctx.from_ = self.match(ExampleDSLParser.NUMBER)
            self.state = 295
            self.match(ExampleDSLParser.TO)
            self.state = 296
            localctx.to = self.match(ExampleDSLParser.NUMBER)
            self.state = 297
            self.match(ExampleDSLParser.IN)
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 298
                self.path()
                pass
            elif token in [65]:
                self.state = 299
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 302
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
            self.state = 304
            self.match(ExampleDSLParser.GENERATE)
            self.state = 305
            self.match(ExampleDSLParser.REPORT)
            self.state = 306
            self.match(ExampleDSLParser.FOR)
            self.state = 307
            self.match(ExampleDSLParser.COLUMN)
            self.state = 308
            self.column()
            self.state = 309
            self.match(ExampleDSLParser.BY)
            self.state = 310
            self.period()
            self.state = 311
            self.match(ExampleDSLParser.IN)
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 312
                self.path()
                pass
            elif token in [65]:
                self.state = 313
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 316
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
            self.state = 318
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
            self.state = 320
            self.match(ExampleDSLParser.REORDER)
            self.state = 321
            self.match(ExampleDSLParser.COLUMNS)

            self.state = 322
            self.column()
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 323
                self.match(ExampleDSLParser.T__1)
                self.state = 324
                self.column()
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 330
            self.match(ExampleDSLParser.TO)

            self.state = 331
            self.column()
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 332
                self.match(ExampleDSLParser.T__1)
                self.state = 333
                self.column()
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 339
            self.match(ExampleDSLParser.IN)
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 340
                self.path()
                pass
            elif token in [65]:
                self.state = 341
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 344
                self.asStatement()


            self.state = 347
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
            self.state = 349
            self.match(ExampleDSLParser.GROUP)
            self.state = 350
            self.match(ExampleDSLParser.BY)
            self.state = 351
            self.column()
            self.state = 352
            self.match(ExampleDSLParser.AND)
            self.state = 353
            self.match(ExampleDSLParser.SUM)
            self.state = 354
            self.match(ExampleDSLParser.VALUES)
            self.state = 355
            self.match(ExampleDSLParser.TO)
            self.state = 356
            self.column()
            self.state = 357
            self.match(ExampleDSLParser.IN)
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 358
                self.path()
                pass
            elif token in [65]:
                self.state = 359
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 362
                self.asStatement()


            self.state = 365
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
            self.state = 367
            self.match(ExampleDSLParser.FILTER)
            self.state = 368
            self.match(ExampleDSLParser.ROWS)
            self.state = 369
            self.match(ExampleDSLParser.WHERE)
            self.state = 370
            self.column()
            self.state = 371
            self.match(ExampleDSLParser.T__5)
            self.state = 372
            self.value()
            self.state = 373
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
            self.state = 375
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
            self.state = 377
            self.match(ExampleDSLParser.SEARCH)
            self.state = 378
            self.match(ExampleDSLParser.FOR)
            self.state = 379
            localctx.text = self.match(ExampleDSLParser.STRING)
            self.state = 380
            self.match(ExampleDSLParser.IN)
            self.state = 381
            self.match(ExampleDSLParser.COLUMN)
            self.state = 382
            self.match(ExampleDSLParser.T__6)
            self.state = 383
            self.column()
            self.state = 384
            self.match(ExampleDSLParser.T__7)
            self.state = 385
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
            self.state = 387
            self.match(ExampleDSLParser.REPLACE)
            self.state = 388
            self.match(ExampleDSLParser.VALUES)
            self.state = 389
            self.values()
            self.state = 390
            self.match(ExampleDSLParser.WITH)
            self.state = 391
            self.values()
            self.state = 392
            self.match(ExampleDSLParser.IN)
            self.state = 393
            self.match(ExampleDSLParser.COLUMN)
            self.state = 394
            self.match(ExampleDSLParser.T__6)
            self.state = 395
            self.column()
            self.state = 396
            self.match(ExampleDSLParser.T__7)
            self.state = 397
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
            self.state = 399
            _la = self._input.LA(1)
            if not(_la==63 or _la==64):
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
            self.state = 401
            self.match(ExampleDSLParser.ADD)
            self.state = 402
            self.match(ExampleDSLParser.CONDITION)
            self.state = 403
            self.match(ExampleDSLParser.WHERE)
            self.state = 404
            self.column()
            self.state = 405
            self.match(ExampleDSLParser.T__5)
            self.state = 406
            self.value()
            self.state = 407
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
            self.state = 409
            self.match(ExampleDSLParser.REMOVE)
            self.state = 410
            self.match(ExampleDSLParser.DUPLICATE)
            self.state = 411
            self.match(ExampleDSLParser.ROWS)
            self.state = 412
            self.match(ExampleDSLParser.BASED)
            self.state = 413
            self.match(ExampleDSLParser.ON)
            self.state = 414
            self.match(ExampleDSLParser.COLUMN)
            self.state = 415
            self.match(ExampleDSLParser.T__6)
            self.state = 416
            self.column()
            self.state = 417
            self.match(ExampleDSLParser.T__7)
            self.state = 418
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
            self.state = 420
            self.match(ExampleDSLParser.SPLIT)
            self.state = 421
            self.match(ExampleDSLParser.DATA)
            self.state = 422
            self.match(ExampleDSLParser.BASED)
            self.state = 423
            self.match(ExampleDSLParser.ON)
            self.state = 424
            self.match(ExampleDSLParser.COLUMN)
            self.state = 425
            self.match(ExampleDSLParser.T__6)
            self.state = 426
            self.column()
            self.state = 427
            self.match(ExampleDSLParser.T__7)
            self.state = 428
            self.match(ExampleDSLParser.AND)
            self.state = 429
            self.match(ExampleDSLParser.SAVE)
            self.state = 430
            self.match(ExampleDSLParser.RESULTS)
            self.state = 431
            self.match(ExampleDSLParser.TO)
            self.state = 432
            self.match(ExampleDSLParser.SEPARATE)
            self.state = 433
            self.match(ExampleDSLParser.FILES)
            self.state = 434
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
            self.state = 436
            self.match(ExampleDSLParser.COMBINE)
            self.state = 437
            self.match(ExampleDSLParser.COLUMNS)
            self.state = 438
            self.column()
            self.state = 439
            self.match(ExampleDSLParser.AND)
            self.state = 440
            self.column()
            self.state = 441
            self.match(ExampleDSLParser.AND)
            self.state = 442
            self.match(ExampleDSLParser.SAVE)
            self.state = 443
            self.match(ExampleDSLParser.RESULT)
            self.state = 444
            self.match(ExampleDSLParser.TO)
            self.state = 445
            self.result()
            self.state = 446
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
            self.state = 448
            self.match(ExampleDSLParser.RESIZE)
            self.state = 449
            self.match(ExampleDSLParser.DATA)
            self.state = 450
            self.match(ExampleDSLParser.IN)
            self.state = 451
            self.match(ExampleDSLParser.COLUMN)
            self.state = 452
            self.match(ExampleDSLParser.T__6)
            self.state = 453
            self.column()
            self.state = 454
            self.match(ExampleDSLParser.T__7)
            self.state = 455
            self.match(ExampleDSLParser.BY)
            self.state = 456
            self.match(ExampleDSLParser.MULTIPLYING)
            self.state = 457
            self.match(ExampleDSLParser.WITH)
            self.state = 458
            self.value()
            self.state = 459
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
            self.state = 461
            self.match(ExampleDSLParser.Update)
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 462
                self.path()
                pass
            elif token in [65]:
                self.state = 463
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 466
            self.match(ExampleDSLParser.FROM)
            self.state = 467
            self.path()
            self.state = 468
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
        self.enterRule(localctx, 72, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(ExampleDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





