from my_dsl.Erorrs.InputError import *


class CustomExampleDSLCodeGenerator:
    def __init__(self, variables):
        self.non_operands = [
            'program', 'import_file', 'export_file', 'combine', 'convert', 'add_columns',
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

    def is_operand(self, item):
        return item not in self.non_operands

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

    def generate_code_based_on_non_operand(self, item):
        if item == "program":
            self.generate_program()

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

    # check =True
    def generate_program(self):
        result_code = '\n'.join(self.code_stack)
        result_code = 'import pandas as pd\n' + result_code
        self.code_stack = [result_code]

    def import_file(self):
        var = self.operand_stack.pop()
        file_path = self.operand_stack.pop()[1:-1]
        if file_path.endswith('.xls'):
            code_string = f'{var} = pd.read_excel("{file_path}")\n'
        else:
            code_string = f'{var} = pd.read_csv("{file_path}")\n'

        self.code_stack.append(code_string)
        """
            code_string = f'output_df={file_path}\n'
        self.code_stack.append(code_string)
        """

    def export_file(self):
        print(self.operand_stack)
        target_file = self.operand_stack.pop()
        target_var = self.operand_stack.pop()
        code_string = f'{target_var}.to_csv({target_file}, index=False)\n'
        self.code_stack.append(code_string)

    # check =True
    def combine_files(self):
        output_path = self.operand_stack.pop()
        file2 = self.operand_stack.pop()
        file1 = self.operand_stack.pop()
        code_string = (f'df1 = pd.read_csv({file1})\n'
                       f'df2 = pd.read_csv({file2})\n'
                       f'df_combined = pd.concat([df1, df2])\n'
                       f'df_combined.to_csv({output_path}, index=False)\n')
        self.code_stack.append(code_string)

    # check =True
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

    # check =True
    def add_columns(self):
        if not self.set_input:
            raise InputFileNotFound()
        if not self.set_output:
            raise OutputFileNotFound()
        result_col = self.operand_stack.pop()
        col2 = self.operand_stack.pop()
        col1 = self.operand_stack.pop()
        code_string = f'temp_df[{result_col}] = temp_df[{col1}] + temp_df[{col2}]\n' \
                      f'temp_df.to_csv( output_df , index=False)\n'
        self.code_stack.append(code_string)

    # check =True
    def rename_column(self):
        """
        if not self.set_input:
            raise InputFileNotFound()
        if not self.set_output:
            raise OutputFileNotFound()
        """
        #print(self.operand_stack)
        target_var = self.operand_stack.pop()
        new_name = self.operand_stack.pop()
        old_name = self.operand_stack.pop()
        code_string = f'{target_var} = {target_var}.rename(columns={{{old_name}: {new_name}}})\n'
        self.code_stack.append(code_string)

    def change_data_type(self):
        data_type = self.operand_stack.pop()
        col_name = self.operand_stack.pop()
        code_string = f'df[{col_name}] = df[{col_name}].astype({data_type})\n'
        self.code_stack.append(code_string)

    def sort_data(self):
        col_name = self.operand_stack.pop()
        code_string = f'df = df.sort_values(by={col_name})\n'
        self.code_stack.append(code_string)

    def delete_column(self):
        col_name = self.operand_stack.pop()
        code_string = f'df = df.drop(columns=[{col_name}])\n'
        self.code_stack.append(code_string)

    def rename_file(self):
        new_name = self.operand_stack.pop()
        code_string = f'import os\nos.rename("output.csv", "{new_name}")\n'
        self.code_stack.append(code_string)

    def apply_condition(self):
        end = int(self.operand_stack.pop())
        start = int(self.operand_stack.pop())
        code_string = f'df = df.iloc[{start - 1}:{end}]\n'
        self.code_stack.append(code_string)

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
