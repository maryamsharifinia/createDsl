grammar ExampleDSL;

start: program EOF;
program:statement+;
statement
    : importFileStatement
    | exportFileStatement
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

importFileStatement
    : IMPORT path asStatement ';';

exportFileStatement
    : EXPORT id TO path ';';


asStatement: AS id;
toStatement: TO column;
path : STRING;
column : STRING;
result : STRING;

combineStatement
    : COMBINE (((path|id) ',' (path|id))(',' (path|id))*) asStatement';'
    ;

convertStatement
    : CONVERT FORMAT FROM (path|id) TO (path|id) ';'
    ;

addColumnsStatement
    : ADD COLUMNS (column(',' column)*) (toStatement)? IN (path|id) (asStatement)?';'
    ;

renameColumnStatement
    : RENAME COLUMN (column(',' column)*) TO (column(',' column)*) IN (path|id) (asStatement)?';'
    ;

changeDataTypeStatement
    : CHANGE DATA TYPE OF COLUMN (column(',' column)*) TO type IN (path|id) (asStatement)?';'
    ;

type:TYPE;

sortDataStatement
    : SORT DATA BY COLUMN column IN (path|id) (asStatement)?';'
    ;

deleteColumnStatement
    : DELETE COLUMN (column(',' column)*) IN (path|id) (asStatement)?';'
    ;

renameFileStatement
    : RENAME OUTPUT FILE TO file_name ';'
    ;
file_name:STRING;

applyConditionStatement
    : APPLY CONDITION ON ROWS from=NUMBER TO to=NUMBER IN (path|id)';'
    ;

generateReportStatement
    : GENERATE REPORT FOR COLUMN column BY period IN (path|id)';'
    ;

period:'day'|'month'| 'year';

reorderColumnsStatement
    : REORDER COLUMNS (column(',' column)*) TO (column(',' column)*) IN (path|id) (asStatement)?';'
    ;

groupByStatement
    : GROUP BY column AND SUM VALUES TO column IN (path|id) (asStatement)?';'
    ;

filterRowsStatement
    : FILTER ROWS WHERE column comparison_operator value IN (path|id) (asStatement)?';'
    ;
value : NUMBER;
text:STRING;
comparison_operator : COMPARISON_OPERATOR;
searchTextStatement
    : SEARCH FOR text IN COLUMN '(' column ')' IN (path|id) (asStatement)?';'
    ;

replaceValuesStatement
    : REPLACE VALUES values WITH values IN COLUMN '(' column ')' ';'
    ;
values:NUMBER|STRING;
addConditionStatement
    : ADD CONDITION WHERE column '>' value ';'
    ;

removeDuplicatesStatement
    : REMOVE DUPLICATE ROWS BASED ON COLUMN '(' column ')' ';'
    ;

splitDataStatement
    : SPLIT DATA BASED ON COLUMN '(' column ')' AND SAVE RESULTS TO SEPARATE FILES ';'
    ;

combineColumnsStatement
    : COMBINE COLUMNS column AND column AND SAVE RESULT TO result ';'
    ;

resizeDataStatement
    : RESIZE DATA IN COLUMN '(' column ')' BY MULTIPLYING WITH value ';'
    ;

id returns[value_attr = str(), type_attr = str()]: ID;
ADD: 'Add';
AS: 'as';
APPLY: 'Apply';
AND: 'and';
BY: 'by';
BASED: 'based';
COLUMN: 'column';
COLUMNS: 'columns';
COMBINE: 'Combine';
CONDITION: 'condition';
COMPARISON_OPERATOR : '>'|'<'|'>='|'<='|'=='|'!=';
CONVERT: 'Convert';
CHANGE: 'Change';
DUPLICATE: 'duplicate';
DELETE: 'Delete';
DATA: 'data';
EXPORT: 'export';
FROM: 'from';
FILTER: 'Filter';
FILE: 'file';
FOR: 'for';
FORMAT: 'format';
GROUP: 'Group';
GENERATE: 'Generate';
IN: 'in';
IMPORT: 'import';
INPUT: 'input';
MULTIPLYING: 'multiplying';
NEW: 'new';
OUTPUT: 'output';
ON: 'on';
OF: 'of';
PATH: 'path';
REPORT:'report';
REORDER: 'Reorder';
RENAME: 'Rename';
REPLACE: 'Replace';
REMOVE: 'Remove';
RESIZE: 'Resize';
ROWS: 'rows';
ROW: 'row';
RESULT: 'result';
SORT: 'Sort';
SEARCH: 'Search';
SPLIT: 'Split';
SET: 'Set';
SAVE: 'save';
SUM: 'sum';
TO: 'to';
TYPE: 'float'| 'str' | 'int'| 'bool'| 'date' | 'type';
WRITE: 'write';
WITH: 'with';
WHERE: 'where';
VALUES: 'values';


NUMBER: [0-9]+;
STRING: '"' .*? '"';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;
