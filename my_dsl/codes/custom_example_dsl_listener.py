from my_dsl.default_codes.ast import AST
from my_dsl.default_codes.make_ast_subtree import make_ast_subtree
from my_dsl.gen.ExampleDSLListener import ExampleDSLListener

class CustomExampleDSLListener(ExampleDSLListener):
    def __init__(self, rule_names):
        self.overridden_rules = [
            'program',
            "setFileInputPathStatement",
            "setFileOutputPathStatement",
            "combineStatement",
            "convertStatement",
            "addColumnsStatement",
            "renameColumnStatement",
            "changeDataTypeStatement",
            "sortDataStatement",
            "deleteColumnStatement",
            "renameFileStatement",
            "applyConditionStatement",
            "generateReportStatement",
            "reorderColumnsStatement",
            "groupByStatement",
            "filterRowsStatement",
            "searchTextStatement",
            "replaceValuesStatement",
            "addConditionStatement",
            "removeDuplicatesStatement",
            "splitDataStatement",
            "combineColumnsStatement",
            "resizeDataStatement",
        ]
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitProgram(self, ctx):
        make_ast_subtree(self.ast, ctx, "program", keep_node=True)

    def exitSetFileInputPathStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "set_file_input_path", keep_node=True)

    def exitSetFileOutputPathStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "set_file_output_path", keep_node=True)

    def exitCombineStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "combine", keep_node=True)

    def exitConvertStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "convert", keep_node=True)

    def exitAddColumnsStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "add_columns", keep_node=True)

    def exitRenameColumnStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "rename_column", keep_node=True)

    def exitChangeDataTypeStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "change_data_type", keep_node=True)

    def exitSortDataStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "sort_data", keep_node=True)

    def exitDeleteColumnStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "delete_column", keep_node=True)

    def exitRenameFileStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "rename_file", keep_node=True)

    def exitApplyConditionStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "apply_condition", keep_node=True)

    def exitGenerateReportStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "generate_report", keep_node=True)

    def exitReorderColumnsStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "reorder_columns", keep_node=True)

    def exitGroupByStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "group_by", keep_node=True)

    def exitFilterRowsStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "filter_rows", keep_node=True)

    def exitSearchTextStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "search_text", keep_node=True)

    def exitReplaceValuesStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "replace_values", keep_node=True)

    def exitAddConditionStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "add_condition", keep_node=True)

    def exitRemoveDuplicatesStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "remove_duplicates", keep_node=True)

    def exitSplitDataStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "split_data", keep_node=True)

    def exitCombineColumnsStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "combine_columns", keep_node=True)

    def exitResizeDataStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "resize_data", keep_node=True)
