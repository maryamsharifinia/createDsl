from my_dsl.Erorrs.InputError import *


class CustomExampleDSLCodeGenerator:
    def __init__(self, variables):
        self.non_operands = [
            'program', 'import_file', 'as', 'to','export_file', 'combine', 'convert', 'add_columns',
            'rename_column',
            'change_data_type', 'sort_data', 'delete_column', 'rename_file', 'apply_condition',
            'generate_report', 'reorder_columns', 'group_by', 'filter_rows', 'search_text',
            'replace_values', 'add_condition', 'remove_duplicates', 'split_data',
            'combine_columns', 'resize_data'
        ]
        self.operand_stack = []
        self.code_stack = []
        self.variables = variables
        self.set_input = False
        self.set_output = False

    #############################################ok############################################
    def is_operand(self, item):
        return item not in self.non_operands

    #############################################ok############################################
    def generate_code(self, post_order_array):
        #print(self.variables)
        for item in post_order_array:
            if not self.is_operand(item["label"]):
                self.generate_code_based_on_non_operand(item["label"])
            else:
                self.operand_stack.append(item["label"])

        result = ''
        for code_string in self.code_stack:
            if code_string is not None:
                result += code_string
        return result

    #############################################ok############################################
    def generate_code_based_on_non_operand(self, item):
        if item == "program":
            self.generate_program()

        elif item == "as":
            self.as_statement()

        elif item == "to":
            self.to_statement()

        elif item == "import_file":
            self.import_file()

        elif item == "export_file":
            self.export_file()

        elif item == "combine":
            self.combine_files()

        elif item == "convert":
            self.convert_format()

        elif item == "add_columns":
            self.add_columns()

        elif item == "rename_column":
            self.rename_column()

        elif item == "change_data_type":
            self.change_data_type()

        elif item == "sort_data":
            self.sort_data()

        elif item == "delete_column":
            self.delete_column()

        elif item == "rename_file":
            self.rename_file()

        elif item == "apply_condition":
            self.apply_condition()

        elif item == "generate_report":
            self.generate_report()

        elif item == "reorder_columns":
            self.reorder_columns()

        elif item == "group_by":
            self.group_by()

        elif item == "filter_rows":
            self.filter_rows()

        elif item == "search_text":
            self.search_text()

        elif item == "replace_values":
            self.replace_values()

        elif item == "add_condition":
            self.add_condition()

        elif item == "remove_duplicates":
            self.remove_duplicates()

        elif item == "split_data":
            self.split_data()

        elif item == "combine_columns":
            self.combine_columns()

        elif item == "resize_data":
            self.resize_data()

    #############################################ok############################################
    def generate_program(self):
        result_code = '\n'.join(self.code_stack)
        result_code = 'import pandas as pd\n' + result_code
        self.code_stack = [result_code]

    #############################################ok############################################
    def as_statement(self):
        target_val = self.operand_stack.pop()
        code_string = f'{target_val}'
        self.code_stack.append(code_string)
        self.push_as_called()

    #############################################ok############################################
    def to_statement(self):
        target_col_name = self.operand_stack.pop()
        code_string = f'[{target_col_name}]'
        self.code_stack.append(code_string)
        self.push_to_called()

    #############################################ok############################################
    def push_as_called(self):
        self.operand_stack.append("asCalled__")

    #############################################ok############################################
    def push_to_called(self):
        self.operand_stack.append("toCalled__")

    #############################################ok############################################
    def is_as_called(self, item):
        if item == "asCalled__":
            return True
        return False

    #############################################ok############################################
    def is_to_called(self, item):
        if item == "toCalled__":
            return True
        return False

    #############################################ok############################################
    def import_file(self):
        temp = self.operand_stack.pop() # can be used in "if temp is as_called and additional codes"
        file_path = self.operand_stack.pop()[1:-1]
        if file_path.endswith('.xls'):
            code_string = f'pd.read_excel("{file_path}")\n'
        else:
            code_string = f'pd.read_csv("{file_path}")\n'

        self.code_stack.append(self.code_stack.pop() + " = " + code_string)

    #############################################ok############################################
    def export_file(self):
        #print(self.operand_stack)
        target_file = self.operand_stack.pop()
        target_var = self.operand_stack.pop()
        code_string = f'{target_var}.to_csv({target_file}, index=False)\n'
        self.code_stack.append(code_string)

    #############################################ok############################################
    def combine_files(self):
        self.operand_stack.pop()
        code_files = []
        for i in range(len(self.operand_stack)):
            file = self.operand_stack.pop()
            if file[1:-1].endswith(".csv"):
                code_files.append(f"pd.read_csv({file})")
            else:
                code_files.append(file)
        as_code = self.code_stack.pop()
        code_string = ", ".join(code_files[::-1])
        code_string = as_code + " = " + "pd.concat([" + code_string + "])\n"
        self.code_stack.append(code_string)

    
    def convert_format(self):
        output_path = self.operand_stack.pop()
        output_path = output_path.replace('"', '')
        input_path = self.operand_stack.pop()
        if output_path.endswith('.xls'):
            code_string = (f'df = pd.read_csv({input_path})\n'
                           f'df.to_excel("{output_path}", index=False)\n')
        else:
            code_string = (f'df = pd.read_excel({input_path})\n'
                           f'df.to_csv("{output_path}", index=False)\n')
        self.code_stack.append(code_string)

    #############################################ok############################################
    def add_columns(self):
        """
        result_col = self.operand_stack.pop()
        col2 = self.operand_stack.pop()
        col1 = self.operand_stack.pop()
        code_string = f'temp_df[{result_col}] = temp_df[{col1}] + temp_df[{col2}]\n' \
                      f'temp_df.to_csv( output_df , index=False)\n'
        self.code_stack.append(code_string)
        """
        #print(self.operand_stack)
        #print(self.variables)
        temp_or_targetvar = self.operand_stack.pop()
        code_string = ""
        as_code = ""
        to_code = ""

        if self.is_as_called(temp_or_targetvar):
            temp_or_targetvar = self.operand_stack.pop()
            as_code = self.code_stack.pop()
            code_string += f"{as_code} = {temp_or_targetvar}.copy()\n"
        else:
            code_string += f"{temp_or_targetvar}"

        temp_or_col = self.operand_stack.pop()

        if self.is_to_called(temp_or_col):
            to_code = self.code_stack.pop()
        else:
            to_code = f"['addCol{self.variables[temp_or_targetvar][2]}']"
            self.variables[temp_or_targetvar][2] += 1
            self.operand_stack.append(temp_or_col)

        col_code = []
        while len(self.operand_stack) > 0:
            col = self.operand_stack.pop()
            col_code.append(f"{temp_or_targetvar}[{col}]")

        code_string += as_code + to_code + " = " + " + ".join(col_code)

        self.code_stack.append(code_string + "\n")

    #############################################ok############################################
    def rename_column(self):
        """
        if not self.set_input:
            raise InputFileNotFound()
        if not self.set_output:
            raise OutputFileNotFound()
        """
        temp_or_targetvar = self.operand_stack.pop()
        code_string = ""
        as_code = ""

        if self.is_as_called(temp_or_targetvar):
            temp_or_targetvar = self.operand_stack.pop()
            as_code = self.code_stack.pop()
        else:
            code_string += f"{temp_or_targetvar}"

        code_string = as_code+code_string + " = "

        total_size = len(self.operand_stack)
        if total_size % 2 == 0:
            to_arr = []
            from_arr = []
            for i in range(int(total_size / 2)):
                to_arr.append(self.operand_stack.pop())
            for i in range(int(total_size / 2)):
                from_arr.append(self.operand_stack.pop())

            code_string += f'{temp_or_targetvar}.rename(columns={{'
            for i in range(int(total_size / 2)):
                code_string += f"{from_arr[i]}: {to_arr[i]}, "

            code_string += "})\n"

            self.code_stack.append(code_string)

        else:
            print("Error!!!")

    #############################################ok############################################
    def change_data_type(self):
        #print(self.operand_stack)

        temp_or_targetvar = self.operand_stack.pop()
        code_string = ""
        as_code = ""

        if self.is_as_called(temp_or_targetvar):
            temp_or_targetvar = self.operand_stack.pop()
            as_code = self.code_stack.pop()
            code_string += f"{as_code} = {temp_or_targetvar}.copy()\n{as_code}"
        else:
            code_string += f"{temp_or_targetvar}"

        dtype = self.operand_stack.pop()

        cols = []
        while len(self.operand_stack) > 0:
            cols.append(self.operand_stack.pop())

        code_string += "[[" + ", ".join(cols) + f"]].astype({dtype})"

        self.code_stack.append(code_string)

    #ALISHO
    def sort_data(self):
        col_name = self.operand_stack.pop()
        code_string = f'df = df.sort_values(by={col_name})\n'
        self.code_stack.append(code_string)

    #ALISHO
    def delete_column(self):
        col_name = self.operand_stack.pop()
        code_string = f'df = df.drop(columns=[{col_name}])\n'
        self.code_stack.append(code_string)

    #ALISHO
    def rename_file(self):
        new_name = self.operand_stack.pop()
        code_string = f'import os\nos.rename("output.csv", "{new_name}")\n'
        self.code_stack.append(code_string)

    def apply_condition(self):
        end = int(self.operand_stack.pop())
        start = int(self.operand_stack.pop())
        code_string = f'df = df.iloc[{start - 1}:{end}]\n'
        self.code_stack.append(code_string)

    #ALISHO
    def generate_report(self):
        col_name = self.operand_stack.pop()
        code_string = (f'report = df.groupby(df["{col_name}"].dt.to_period("M")).size()\n'
                       f'print(report)\n')
        self.code_stack.append(code_string)

    def reorder_columns(self):
        columns = self.operand_stack.pop().split(", ")
        code_string = f'df = df[{columns}]\n'
        self.code_stack.append(code_string)

    def group_by(self):
        agg_func = self.operand_stack.pop()
        col_name = self.operand_stack.pop()
        group_by_col = self.operand_stack.pop()
        code_string = (f'grouped = df.groupby("{group_by_col}").{agg_func}("{col_name}")\n'
                       f'print(grouped)\n')
        self.code_stack.append(code_string)

    def filter_rows(self):
        condition = self.operand_stack.pop()
        code_string = f'df = df.query("{condition}")\n'
        self.code_stack.append(code_string)

    def search_text(self):
        col_name = self.operand_stack.pop()
        keyword = self.operand_stack.pop()
        code_string = f'results = df[df["{col_name}"].str.contains("{keyword}")]\nprint(results)\n'
        self.code_stack.append(code_string)

    def replace_values(self):
        new_value = self.operand_stack.pop()
        old_value = self.operand_stack.pop()
        col_name = self.operand_stack.pop()
        code_string = f'df["{col_name}"] = df["{col_name}"].replace("{old_value}", "{new_value}")\n'
        self.code_stack.append(code_string)

    def add_condition(self):
        condition = self.operand_stack.pop()
        code_string = f'df = df.query("{condition}")\n'
        self.code_stack.append(code_string)

    def remove_duplicates(self):
        col_name = self.operand_stack.pop()
        code_string = f'df = df.drop_duplicates(subset=["{col_name}"])\n'
        self.code_stack.append(code_string)

    def split_data(self):
        col_name = self.operand_stack.pop()
        # code_string = (f'for key, grp in df.groupby("{col_name}"):\n'
        #                f'    grp.to_csv(f"{col_name}_{key}.csv", index=False)\n')
        # self.code_stack.append(code_string)

    def combine_columns(self):
        result_col = self.operand_stack.pop()
        col2 = self.operand_stack.pop()
        col1 = self.operand_stack.pop()
        code_string = f'df["{result_col}"] = df["{col1}"] + " " + df["{col2}"]\n'
        self.code_stack.append(code_string)

    def resize_data(self):
        factor = float(self.operand_stack.pop())
        col_name = self.operand_stack.pop()
        code_string = f'df["{col_name}"] = df["{col_name}"] * {factor}\n'
        self.code_stack.append(code_string)
