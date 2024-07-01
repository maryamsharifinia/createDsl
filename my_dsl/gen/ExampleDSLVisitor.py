# Generated from C:/Users/Ali/Desktop/test_compiler/createDsl/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExampleDSLParser import ExampleDSLParser
else:
    from ExampleDSLParser import ExampleDSLParser

# This class defines a complete generic visitor for a parse tree produced by ExampleDSLParser.

class ExampleDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExampleDSLParser#start.
    def visitStart(self, ctx:ExampleDSLParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#program.
    def visitProgram(self, ctx:ExampleDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#statement.
    def visitStatement(self, ctx:ExampleDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#importFileStatement.
    def visitImportFileStatement(self, ctx:ExampleDSLParser.ImportFileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#exportFileStatement.
    def visitExportFileStatement(self, ctx:ExampleDSLParser.ExportFileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#asStatement.
    def visitAsStatement(self, ctx:ExampleDSLParser.AsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#toStatement.
    def visitToStatement(self, ctx:ExampleDSLParser.ToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#path.
    def visitPath(self, ctx:ExampleDSLParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#column.
    def visitColumn(self, ctx:ExampleDSLParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#result_column.
    def visitResult_column(self, ctx:ExampleDSLParser.Result_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#combineStatement.
    def visitCombineStatement(self, ctx:ExampleDSLParser.CombineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#convertStatement.
    def visitConvertStatement(self, ctx:ExampleDSLParser.ConvertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#addColumnsStatement.
    def visitAddColumnsStatement(self, ctx:ExampleDSLParser.AddColumnsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#renameColumnStatement.
    def visitRenameColumnStatement(self, ctx:ExampleDSLParser.RenameColumnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#changeDataTypeStatement.
    def visitChangeDataTypeStatement(self, ctx:ExampleDSLParser.ChangeDataTypeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#type.
    def visitType(self, ctx:ExampleDSLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#sortDataStatement.
    def visitSortDataStatement(self, ctx:ExampleDSLParser.SortDataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#deleteColumnStatement.
    def visitDeleteColumnStatement(self, ctx:ExampleDSLParser.DeleteColumnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#renameFileStatement.
    def visitRenameFileStatement(self, ctx:ExampleDSLParser.RenameFileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#file_name.
    def visitFile_name(self, ctx:ExampleDSLParser.File_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#applyConditionStatement.
    def visitApplyConditionStatement(self, ctx:ExampleDSLParser.ApplyConditionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#generateReportStatement.
    def visitGenerateReportStatement(self, ctx:ExampleDSLParser.GenerateReportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#period.
    def visitPeriod(self, ctx:ExampleDSLParser.PeriodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#reorderColumnsStatement.
    def visitReorderColumnsStatement(self, ctx:ExampleDSLParser.ReorderColumnsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#groupByStatement.
    def visitGroupByStatement(self, ctx:ExampleDSLParser.GroupByStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#filterRowsStatement.
    def visitFilterRowsStatement(self, ctx:ExampleDSLParser.FilterRowsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#value.
    def visitValue(self, ctx:ExampleDSLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#text.
    def visitText(self, ctx:ExampleDSLParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#comparison_operator.
    def visitComparison_operator(self, ctx:ExampleDSLParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#searchTextStatement.
    def visitSearchTextStatement(self, ctx:ExampleDSLParser.SearchTextStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#replaceValuesStatement.
    def visitReplaceValuesStatement(self, ctx:ExampleDSLParser.ReplaceValuesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#values.
    def visitValues(self, ctx:ExampleDSLParser.ValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#addConditionStatement.
    def visitAddConditionStatement(self, ctx:ExampleDSLParser.AddConditionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#removeDuplicatesStatement.
    def visitRemoveDuplicatesStatement(self, ctx:ExampleDSLParser.RemoveDuplicatesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#splitDataStatement.
    def visitSplitDataStatement(self, ctx:ExampleDSLParser.SplitDataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#combineColumnsStatement.
    def visitCombineColumnsStatement(self, ctx:ExampleDSLParser.CombineColumnsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#resizeDataStatement.
    def visitResizeDataStatement(self, ctx:ExampleDSLParser.ResizeDataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#id.
    def visitId(self, ctx:ExampleDSLParser.IdContext):
        return self.visitChildren(ctx)



del ExampleDSLParser