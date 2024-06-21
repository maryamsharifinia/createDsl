# Generated from E:/uni file/compiler/createDsl/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExampleDSLParser import ExampleDSLParser
else:
    from ExampleDSLParser import ExampleDSLParser

# This class defines a complete listener for a parse tree produced by ExampleDSLParser.
class ExampleDSLListener(ParseTreeListener):

    # Enter a parse tree produced by ExampleDSLParser#start.
    def enterStart(self, ctx:ExampleDSLParser.StartContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#start.
    def exitStart(self, ctx:ExampleDSLParser.StartContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#program.
    def enterProgram(self, ctx:ExampleDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#program.
    def exitProgram(self, ctx:ExampleDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#statement.
    def enterStatement(self, ctx:ExampleDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#statement.
    def exitStatement(self, ctx:ExampleDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#setFileOutputPathStatement.
    def enterSetFileOutputPathStatement(self, ctx:ExampleDSLParser.SetFileOutputPathStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#setFileOutputPathStatement.
    def exitSetFileOutputPathStatement(self, ctx:ExampleDSLParser.SetFileOutputPathStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#setFileInputPathStatement.
    def enterSetFileInputPathStatement(self, ctx:ExampleDSLParser.SetFileInputPathStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#setFileInputPathStatement.
    def exitSetFileInputPathStatement(self, ctx:ExampleDSLParser.SetFileInputPathStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#path.
    def enterPath(self, ctx:ExampleDSLParser.PathContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#path.
    def exitPath(self, ctx:ExampleDSLParser.PathContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#column.
    def enterColumn(self, ctx:ExampleDSLParser.ColumnContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#column.
    def exitColumn(self, ctx:ExampleDSLParser.ColumnContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#result.
    def enterResult(self, ctx:ExampleDSLParser.ResultContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#result.
    def exitResult(self, ctx:ExampleDSLParser.ResultContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#combineStatement.
    def enterCombineStatement(self, ctx:ExampleDSLParser.CombineStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#combineStatement.
    def exitCombineStatement(self, ctx:ExampleDSLParser.CombineStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#convertStatement.
    def enterConvertStatement(self, ctx:ExampleDSLParser.ConvertStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#convertStatement.
    def exitConvertStatement(self, ctx:ExampleDSLParser.ConvertStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#addColumnsStatement.
    def enterAddColumnsStatement(self, ctx:ExampleDSLParser.AddColumnsStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#addColumnsStatement.
    def exitAddColumnsStatement(self, ctx:ExampleDSLParser.AddColumnsStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#renameColumnStatement.
    def enterRenameColumnStatement(self, ctx:ExampleDSLParser.RenameColumnStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#renameColumnStatement.
    def exitRenameColumnStatement(self, ctx:ExampleDSLParser.RenameColumnStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#changeDataTypeStatement.
    def enterChangeDataTypeStatement(self, ctx:ExampleDSLParser.ChangeDataTypeStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#changeDataTypeStatement.
    def exitChangeDataTypeStatement(self, ctx:ExampleDSLParser.ChangeDataTypeStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#type.
    def enterType(self, ctx:ExampleDSLParser.TypeContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#type.
    def exitType(self, ctx:ExampleDSLParser.TypeContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#sortDataStatement.
    def enterSortDataStatement(self, ctx:ExampleDSLParser.SortDataStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#sortDataStatement.
    def exitSortDataStatement(self, ctx:ExampleDSLParser.SortDataStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#deleteColumnStatement.
    def enterDeleteColumnStatement(self, ctx:ExampleDSLParser.DeleteColumnStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#deleteColumnStatement.
    def exitDeleteColumnStatement(self, ctx:ExampleDSLParser.DeleteColumnStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#renameFileStatement.
    def enterRenameFileStatement(self, ctx:ExampleDSLParser.RenameFileStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#renameFileStatement.
    def exitRenameFileStatement(self, ctx:ExampleDSLParser.RenameFileStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#file_name.
    def enterFile_name(self, ctx:ExampleDSLParser.File_nameContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#file_name.
    def exitFile_name(self, ctx:ExampleDSLParser.File_nameContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#applyConditionStatement.
    def enterApplyConditionStatement(self, ctx:ExampleDSLParser.ApplyConditionStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#applyConditionStatement.
    def exitApplyConditionStatement(self, ctx:ExampleDSLParser.ApplyConditionStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#generateReportStatement.
    def enterGenerateReportStatement(self, ctx:ExampleDSLParser.GenerateReportStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#generateReportStatement.
    def exitGenerateReportStatement(self, ctx:ExampleDSLParser.GenerateReportStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#period.
    def enterPeriod(self, ctx:ExampleDSLParser.PeriodContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#period.
    def exitPeriod(self, ctx:ExampleDSLParser.PeriodContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#reorderColumnsStatement.
    def enterReorderColumnsStatement(self, ctx:ExampleDSLParser.ReorderColumnsStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#reorderColumnsStatement.
    def exitReorderColumnsStatement(self, ctx:ExampleDSLParser.ReorderColumnsStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#groupByStatement.
    def enterGroupByStatement(self, ctx:ExampleDSLParser.GroupByStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#groupByStatement.
    def exitGroupByStatement(self, ctx:ExampleDSLParser.GroupByStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#filterRowsStatement.
    def enterFilterRowsStatement(self, ctx:ExampleDSLParser.FilterRowsStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#filterRowsStatement.
    def exitFilterRowsStatement(self, ctx:ExampleDSLParser.FilterRowsStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#value.
    def enterValue(self, ctx:ExampleDSLParser.ValueContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#value.
    def exitValue(self, ctx:ExampleDSLParser.ValueContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#searchTextStatement.
    def enterSearchTextStatement(self, ctx:ExampleDSLParser.SearchTextStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#searchTextStatement.
    def exitSearchTextStatement(self, ctx:ExampleDSLParser.SearchTextStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#replaceValuesStatement.
    def enterReplaceValuesStatement(self, ctx:ExampleDSLParser.ReplaceValuesStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#replaceValuesStatement.
    def exitReplaceValuesStatement(self, ctx:ExampleDSLParser.ReplaceValuesStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#values.
    def enterValues(self, ctx:ExampleDSLParser.ValuesContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#values.
    def exitValues(self, ctx:ExampleDSLParser.ValuesContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#addConditionStatement.
    def enterAddConditionStatement(self, ctx:ExampleDSLParser.AddConditionStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#addConditionStatement.
    def exitAddConditionStatement(self, ctx:ExampleDSLParser.AddConditionStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#removeDuplicatesStatement.
    def enterRemoveDuplicatesStatement(self, ctx:ExampleDSLParser.RemoveDuplicatesStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#removeDuplicatesStatement.
    def exitRemoveDuplicatesStatement(self, ctx:ExampleDSLParser.RemoveDuplicatesStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#splitDataStatement.
    def enterSplitDataStatement(self, ctx:ExampleDSLParser.SplitDataStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#splitDataStatement.
    def exitSplitDataStatement(self, ctx:ExampleDSLParser.SplitDataStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#combineColumnsStatement.
    def enterCombineColumnsStatement(self, ctx:ExampleDSLParser.CombineColumnsStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#combineColumnsStatement.
    def exitCombineColumnsStatement(self, ctx:ExampleDSLParser.CombineColumnsStatementContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#resizeDataStatement.
    def enterResizeDataStatement(self, ctx:ExampleDSLParser.ResizeDataStatementContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#resizeDataStatement.
    def exitResizeDataStatement(self, ctx:ExampleDSLParser.ResizeDataStatementContext):
        pass



del ExampleDSLParser