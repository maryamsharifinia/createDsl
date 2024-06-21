grammar ExampleDSL;

start: program EOF;
program:statement+;
statement
    : setFileInputPathStatement
    | setFileOutputPathStatement
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

setFileOutputPathStatement
    :  SET FILE PATH OUTPUT path ';';

setFileInputPathStatement
    : SET FILE PATH INPUT path ';';

path: STRING;
column : STRING;
result : STRING;
combineStatement
    : COMBINE FILE path WITH path AND WRITE TO path';'
    ;
convertStatement
    : CONVERT FORMAT FROM path TO path ';'
    ;

addColumnsStatement
    : ADD COLUMNS column AND column AND SAVE RESULT TO result';'
    ;

renameColumnStatement
    : RENAME COLUMN column TO column ';'
    ;

changeDataTypeStatement
    : CHANGE DATA TYPE OF COLUMN '(' column')' TO type ';'
    ;

type:TYPE;

sortDataStatement
    : SORT DATA BY COLUMN '(' column')' ';'
    ;

deleteColumnStatement
    : DELETE COLUMN column ';'
    ;

renameFileStatement
    : RENAME OUTPUT FILE TO file_name ';'
    ;
file_name:STRING;
applyConditionStatement
    : APPLY CONDITION ON ROWS from=NUMBER TO to=NUMBER ';'
    ;

generateReportStatement
    : GENERATE REPORT FOR COLUMN '(' column ')' BY period ';'
    ;

period:'day'|'month'| 'year';

reorderColumnsStatement
    : REORDER COLUMNS columns+=STRING (',' columns+=STRING)* TO newOrder+=STRING (',' newOrder+=STRING)* ';'
    ;

groupByStatement
    : GROUP BY column AND SUM VALUES IN column ';'
    ;

filterRowsStatement
    : FILTER ROWS WHERE column '>' value';'
    ;
value : NUMBER;
searchTextStatement
    : SEARCH FOR text=STRING IN COLUMN '(' column ')' ';'
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

INPUT: 'input';
OUTPUT: 'output';
REPORT:'report';
WRITE: 'write';
COMBINE: 'Combine';
CONVERT: 'Convert';
ADD: 'Add';
RENAME: 'Rename';
CHANGE: 'Change';
SORT: 'Sort';
DELETE: 'Delete';
APPLY: 'Apply';
GENERATE: 'Generate';
REORDER: 'Reorder';
GROUP: 'Group';
FILTER: 'Filter';
SEARCH: 'Search';
REPLACE: 'Replace';
REMOVE: 'Remove';
SPLIT: 'Split';
RESIZE: 'Resize';
SET: 'Set';
FILE: 'file';
PATH: 'path';
FORMAT: 'format';
DATA: 'data';
COLUMN: 'column';
COLUMNS: 'columns';
TYPE: 'type';
ROWS: 'rows';
ROW: 'row';
CONDITION: 'condition';
VALUES: 'values';
IN: 'in';
RESULT: 'result';
TO: 'to';
WITH: 'with';
AND: 'and';
BY: 'by';
FROM: 'from';
WHERE: 'where';
ON: 'on';
OF: 'of';
FOR: 'for';
AS: 'as';
SAVE: 'save';
BASED: 'based';
SUM: 'sum';
NEW: 'new';
MULTIPLYING: 'multiplying';
DUPLICATE: 'duplicate';

NUMBER: [0-9]+;
STRING: '"' .*? '"';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;
