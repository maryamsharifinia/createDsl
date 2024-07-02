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
    | selectStatement
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
result_column : STRING;


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
    : RENAME COLUMNS (column(',' column)*) TO (column(',' column)*) IN (path|id) (asStatement)?';'
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

number: NUMBER;
from: FROM number;
to: TO number;
step: STEP number;
query: (from)? (to)? (step)?;

rows: ROWS ((number(',' number)*)|(query));
columns: COLUMNS ((column(',' column)*)|(number(',' number)*)|(query));

assign: ASSIGN values IN;
selectStatement
    : (assign)? SELECT (rows)? (columns)? IN ((path asStatement)|(id (asStatement)?))';'
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
    : REPLACE VALUES values WITH values IN COLUMN '(' column ')' IN (path|id) (asStatement)?';'
    ;

values:NUMBER|STRING;
addConditionStatement
    : ADD CONDITION WHERE column '>' value ';'
    ;

removeDuplicatesStatement
    : REMOVE DUPLICATE ROWS BASED ON COLUMN '(' column ')' IN (path|id) (asStatement)?';'
    ;

splitDataStatement
    : SPLIT DATA BASED ON COLUMN '(' column ')' IN (path|id) (asStatement)? AND SAVE RESULTS TO SEPARATE FILES ';'
    ;

combineColumnsStatement
    : COMBINE COLUMNS column (AND column)+ IN (path|id) (asStatement)? AND SAVE RESULT TO result_column ';'
    ;

resizeDataStatement
    : RESIZE DATA IN COLUMN '(' column ')' BY MULTIPLYING WITH value ';'
    ;

id returns[value_attr = str(), type_attr = str()]: ID;
ASSIGN: 'assign';
STEP: 'step';
SELECT: 'select';
EXPORT: 'export';
IMPORT: 'import';
INPUT: 'input';
OUTPUT: 'output';
REPORT:'report';
WRITE: 'write';
COMBINE: 'Combine';
COMPARISON_OPERATOR : '>'|'<'|'>='|'<='|'=='|'!=';
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
RESULTS:'results';
SPLIT: 'Split';
RESIZE: 'Resize';
SET: 'Set';
SEPARATE:'separate';
FILE: 'file';
FILES:'files';
PATH: 'path';
FORMAT: 'format';
DATA: 'data';
COLUMN: 'column';
COLUMNS: 'columns';
TYPE: 'float'| 'str' | 'int'| 'bool'| 'date' | 'type';
ROWS: 'rows';
ROW: 'row';
CONDITION: 'condition';
VALUES: 'values';
IN: 'in';
RESULT: 'result';
SAVE: 'save';
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
BASED: 'based';
SUM: 'sum';
NEW: 'new';
MULTIPLYING: 'multiplying';
DUPLICATE: 'duplicate';

NUMBER: [0-9]+;
STRING: '"' .*? '"';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;
