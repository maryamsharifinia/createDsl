# createDsl
In this project, we want to create an DSL using Antler and Python language to make it easier to work with data files like Excel.


Using the defined ANTLR grammar, you can write the following commands in your DSL. Each command is designed to perform specific operations on CSV or XLS files.

### Commands to set the file path
1. **Set the path of the input file:**
 dsl
 Set input file path "input.csv";
 ```
2. **Set the path of the output file:**

 Set output file path "output.csv";
 ```

### Commands to combine files
3. **combining two files and writing to a new file:**
 ```dsl
 Combine file "file1.csv" with "file2.csv" and write to "output.csv";
 ```

### format change commands
4. **Convert the file format from CSV to XLS:**
 ```dsl
 Convert format from "input.csv" to "output.xls";
 ```
5. **Convert the file format from XLS to CSV:**
 ```dsl
 Convert format from "input.xls" to "output.csv";
 ```

### Advanced calculation commands
6. **Adding the values ​​of two columns and saving the result in the new column:**
 ```dsl
 Add columns "sales" and "expenses" and save result to "profit";
 ```

### Column renaming commands
7. **Change the name of a column:**
 ```dsl
 Rename column "age" to "customer_age";
 ```

### commands to change the data type
8. **Changing the type of data:**
 ```dsl
 Change data type of column("price") to float;
 ```

### Data ordering commands
9. Sorting data based on a specific column:
 ```dsl
 Sort data by column("date");
 ```

### Column deletion commands
10. **Remove a specific column:**
 dsl
 Delete column "address";
 ```

### Commands to rename the file
11. **Change the name of the output file:**

 Rename output file to "final_output.csv";
 ```

### Commands to change the range
12. Applying a condition on a range of data:
 ```dsl
 Apply condition on rows 1 to 10;
 ```

### Report generation commands
13. **Production of various reports based on file data:**
 ```dsl
 Generate report for column("sales") by month;
 ```

### Commands to change the order of columns
14. **Changing the order of file columns:**
 ```dsl
 Reorder columns "name", "age", "gender" to "age", "name", "gender";
 ```

### Data aggregation commands
15. ** Aggregate duplicate data based on one or more columns:**
 ```dsl
 Group by "category" and sum values ​​in "quantity";
 ```

### Data filtering commands
16. **Removing rows that do not meet specific conditions:**
 ```dsl
 Filter rows where "price" > 100;
 ```

### Text search commands
17. **Search text strings in one or more columns:**
 ```dsl
 Search for "keyword" in column("description");
 ```

### Commands to change values
18. **Changing specific values ​​in one column to another value:**
 ```dsl
 Replace values ​​"old_value" with "new_value" in column("status");
 ```

### Commands to add a condition
19. **Adding a condition to select properties or columns:**
 ```dsl
 Add condition where "quantity" > 0;
 ```

### Commands to remove duplicate rows
20. **Removing rows whose information is duplicated:**
 ```dsl
 Remove duplicate rows based on column("email");
 ```

### Data division commands
21. Dividing data according to specific conditions and saving the results in separate files:
 ```dsl
 Split data based on column("region") and save results to separate files;
 ```

### Commands to combine columns
22. **combining the values ​​of two or more columns and saving the result in a new column:**
 ```dsl
 Combine columns "first_name" and "last_name" and save result to "full_name";
 ```

### Data resizing commands
23. **Change the size of data according to a formula or mathematical operation:**
 ```dsl
 Resize data in column("price") by multiplying with 0.9;
 ```

### Final description
This grammar and commands allow you to easily manage your CSV and XLS files using DSL and perform various operations on them.