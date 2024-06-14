// Generated from E:/uni file/compiler/hw5/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExampleDSLParser}.
 */
public interface ExampleDSLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ExampleDSLParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ExampleDSLParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ExampleDSLParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ExampleDSLParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#setFilePathStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetFilePathStatement(ExampleDSLParser.SetFilePathStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#setFilePathStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetFilePathStatement(ExampleDSLParser.SetFilePathStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#combineStatement}.
	 * @param ctx the parse tree
	 */
	void enterCombineStatement(ExampleDSLParser.CombineStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#combineStatement}.
	 * @param ctx the parse tree
	 */
	void exitCombineStatement(ExampleDSLParser.CombineStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#convertStatement}.
	 * @param ctx the parse tree
	 */
	void enterConvertStatement(ExampleDSLParser.ConvertStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#convertStatement}.
	 * @param ctx the parse tree
	 */
	void exitConvertStatement(ExampleDSLParser.ConvertStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#addColumnsStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddColumnsStatement(ExampleDSLParser.AddColumnsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#addColumnsStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddColumnsStatement(ExampleDSLParser.AddColumnsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#renameColumnStatement}.
	 * @param ctx the parse tree
	 */
	void enterRenameColumnStatement(ExampleDSLParser.RenameColumnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#renameColumnStatement}.
	 * @param ctx the parse tree
	 */
	void exitRenameColumnStatement(ExampleDSLParser.RenameColumnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#changeDataTypeStatement}.
	 * @param ctx the parse tree
	 */
	void enterChangeDataTypeStatement(ExampleDSLParser.ChangeDataTypeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#changeDataTypeStatement}.
	 * @param ctx the parse tree
	 */
	void exitChangeDataTypeStatement(ExampleDSLParser.ChangeDataTypeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#sortDataStatement}.
	 * @param ctx the parse tree
	 */
	void enterSortDataStatement(ExampleDSLParser.SortDataStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#sortDataStatement}.
	 * @param ctx the parse tree
	 */
	void exitSortDataStatement(ExampleDSLParser.SortDataStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#deleteColumnStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeleteColumnStatement(ExampleDSLParser.DeleteColumnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#deleteColumnStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeleteColumnStatement(ExampleDSLParser.DeleteColumnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#renameFileStatement}.
	 * @param ctx the parse tree
	 */
	void enterRenameFileStatement(ExampleDSLParser.RenameFileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#renameFileStatement}.
	 * @param ctx the parse tree
	 */
	void exitRenameFileStatement(ExampleDSLParser.RenameFileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#applyConditionStatement}.
	 * @param ctx the parse tree
	 */
	void enterApplyConditionStatement(ExampleDSLParser.ApplyConditionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#applyConditionStatement}.
	 * @param ctx the parse tree
	 */
	void exitApplyConditionStatement(ExampleDSLParser.ApplyConditionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#generateReportStatement}.
	 * @param ctx the parse tree
	 */
	void enterGenerateReportStatement(ExampleDSLParser.GenerateReportStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#generateReportStatement}.
	 * @param ctx the parse tree
	 */
	void exitGenerateReportStatement(ExampleDSLParser.GenerateReportStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#reorderColumnsStatement}.
	 * @param ctx the parse tree
	 */
	void enterReorderColumnsStatement(ExampleDSLParser.ReorderColumnsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#reorderColumnsStatement}.
	 * @param ctx the parse tree
	 */
	void exitReorderColumnsStatement(ExampleDSLParser.ReorderColumnsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#groupByStatement}.
	 * @param ctx the parse tree
	 */
	void enterGroupByStatement(ExampleDSLParser.GroupByStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#groupByStatement}.
	 * @param ctx the parse tree
	 */
	void exitGroupByStatement(ExampleDSLParser.GroupByStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#filterRowsStatement}.
	 * @param ctx the parse tree
	 */
	void enterFilterRowsStatement(ExampleDSLParser.FilterRowsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#filterRowsStatement}.
	 * @param ctx the parse tree
	 */
	void exitFilterRowsStatement(ExampleDSLParser.FilterRowsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#searchTextStatement}.
	 * @param ctx the parse tree
	 */
	void enterSearchTextStatement(ExampleDSLParser.SearchTextStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#searchTextStatement}.
	 * @param ctx the parse tree
	 */
	void exitSearchTextStatement(ExampleDSLParser.SearchTextStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#replaceValuesStatement}.
	 * @param ctx the parse tree
	 */
	void enterReplaceValuesStatement(ExampleDSLParser.ReplaceValuesStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#replaceValuesStatement}.
	 * @param ctx the parse tree
	 */
	void exitReplaceValuesStatement(ExampleDSLParser.ReplaceValuesStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#addConditionStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddConditionStatement(ExampleDSLParser.AddConditionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#addConditionStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddConditionStatement(ExampleDSLParser.AddConditionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#removeDuplicatesStatement}.
	 * @param ctx the parse tree
	 */
	void enterRemoveDuplicatesStatement(ExampleDSLParser.RemoveDuplicatesStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#removeDuplicatesStatement}.
	 * @param ctx the parse tree
	 */
	void exitRemoveDuplicatesStatement(ExampleDSLParser.RemoveDuplicatesStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#splitDataStatement}.
	 * @param ctx the parse tree
	 */
	void enterSplitDataStatement(ExampleDSLParser.SplitDataStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#splitDataStatement}.
	 * @param ctx the parse tree
	 */
	void exitSplitDataStatement(ExampleDSLParser.SplitDataStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#combineColumnsStatement}.
	 * @param ctx the parse tree
	 */
	void enterCombineColumnsStatement(ExampleDSLParser.CombineColumnsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#combineColumnsStatement}.
	 * @param ctx the parse tree
	 */
	void exitCombineColumnsStatement(ExampleDSLParser.CombineColumnsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExampleDSLParser#resizeDataStatement}.
	 * @param ctx the parse tree
	 */
	void enterResizeDataStatement(ExampleDSLParser.ResizeDataStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleDSLParser#resizeDataStatement}.
	 * @param ctx the parse tree
	 */
	void exitResizeDataStatement(ExampleDSLParser.ResizeDataStatementContext ctx);
}