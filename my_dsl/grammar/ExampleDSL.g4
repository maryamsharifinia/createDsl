grammar ExampleDSL;

program:  statement+ EOF;


statement
    : setFilePathStatement
    | combineStatement
    | convertStatement
    | addColumnsStatement
    | renameColumnStatement
    | changeDataTypeStatement
    | sortDataStatement
    | deleteColumnStatement
    | renameFileStatement
    | applyConditionStatement
    | generateReportStatement
    | reorderColumnsStatement
    | groupByStatement
    | filterRowsStatement
    | searchTextStatement
    | replaceValuesStatement
    | addConditionStatement
    | removeDuplicatesStatement
    | splitDataStatement
    | combineColumnsStatement
    | resizeDataStatement
    ;

setFilePathStatement
    : SET FILE PATH INPUT STRING ';'
    | SET FILE PATH OUTPUT STRING ';'
    ;

combineStatement
    : COMBINE FILE STRING WITH FILE STRING AND WRITE TO STRING ';'
    ;

convertStatement
    : CONVERT FORMAT FROM STRING TO STRING ';'
    ;

addColumnsStatement
    : ADD COLUMNS STRING AND STRING AND SAVE RESULT TO STRING ';'
    ;

renameColumnStatement
    : RENAME COLUMN STRING TO STRING ';'
    ;

changeDataTypeStatement
    : CHANGE DATA TYPE OF COLUMN '(' STRING ')' TO TYPE ';'
    ;

sortDataStatement
    : SORT DATA BY COLUMN '(' STRING ')' ';'
    ;

deleteColumnStatement
    : DELETE COLUMN STRING ';'
    ;

renameFileStatement
    : RENAME OUTPUT FILE TO STRING ';'
    ;

applyConditionStatement
    : APPLY CONDITION ON ROWS NUMBER TO NUMBER ';'
    ;

generateReportStatement
    : GENERATE REPORT FOR COLUMN '(' STRING ')' BY STRING ';'
    ;

reorderColumnsStatement
    : REORDER COLUMNS STRING (',' STRING)* TO STRING (',' STRING)* ';'
    ;

groupByStatement
    : GROUP BY STRING AND SUM VALUES IN STRING ';'
    ;

filterRowsStatement
    : FILTER ROWS WHERE STRING '>' NUMBER ';'
    ;

searchTextStatement
    : SEARCH FOR STRING IN COLUMN '(' STRING ')' ';'
    ;

replaceValuesStatement
    : REPLACE VALUES STRING WITH STRING IN COLUMN '(' STRING ')' ';'
    ;

addConditionStatement
    : ADD CONDITION WHERE STRING '>' NUMBER ';'
    ;

removeDuplicatesStatement
    : REMOVE DUPLICATE ROWS BASED ON COLUMN '(' STRING ')' ';'
    ;

splitDataStatement
    : SPLIT DATA BASED ON COLUMN '(' STRING ')' AND SAVE RESULTS TO SEPARATE FILES ';'
    ;

combineColumnsStatement
    : COMBINE COLUMNS STRING AND STRING AND SAVE RESULT TO STRING ';'
    ;

resizeDataStatement
    : RESIZE DATA IN COLUMN '(' STRING ')' BY MULTIPLYING WITH NUMBER ';'
    ;

INPUT : 'input';
OUTPUT : 'output';

COMBINE     : 'Combine';
CONVERT     : 'Convert';
ADD         : 'Add';
RENAME      : 'Rename';
CHANGE      : 'Change';
SORT        : 'Sort';
DELETE      : 'Delete';
APPLY       : 'Apply';
GENERATE    : 'Generate';
REORDER     : 'Reorder';
GROUP       : 'Group';
FILTER      : 'Filter';
SEARCH      : 'Search';
REPLACE     : 'Replace';
REMOVE      : 'Remove';
SPLIT       : 'Split';
RESIZE      : 'Resize';
SET         : 'Set';
FILE        : 'file';
PATH        : 'path';
FORMAT      : 'format';
DATA        : 'data';
COLUMN      : 'column';
COLUMNS     : 'columns';
TYPE        : 'type';
ROWS        : 'rows';
ROW         : 'row';
CONDITION   : 'condition';
VALUES      : 'values';
IN          : 'in';
RESULT      : 'result';
TO          : 'to';
WITH        : 'with';
AND         : 'and';
BY          : 'by';
FROM        : 'from';
WHERE       : 'where';
ON          : 'on';
OF          : 'of';
FOR         : 'for';
AS          : 'as';
SAVE        : 'save';
BASED       : 'based';
SUM         : 'sum';
NEW         : 'new';
MULTIPLYING : 'multiplying';
DUPLICATE : 'duplicate';

NUMBER      : [0-9]+;
STRING      : '"' .*? '"';
ID          : [a-zA-Z_][a-zA-Z_0-9]*;
WS          : [ \t\r\n]+ -> skip;



