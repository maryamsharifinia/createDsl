// Generated from E:/University/Term 6/Compiler/Project/createDsl/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link ExampleDSLParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface ExampleDSLVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(ExampleDSLParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(ExampleDSLParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(ExampleDSLParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#importFileStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImportFileStatement(ExampleDSLParser.ImportFileStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#exportFileStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExportFileStatement(ExampleDSLParser.ExportFileStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#asStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAsStatement(ExampleDSLParser.AsStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#toStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToStatement(ExampleDSLParser.ToStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#path}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPath(ExampleDSLParser.PathContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#column}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitColumn(ExampleDSLParser.ColumnContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#result}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitResult(ExampleDSLParser.ResultContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#combineStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCombineStatement(ExampleDSLParser.CombineStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#convertStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConvertStatement(ExampleDSLParser.ConvertStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#addColumnsStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddColumnsStatement(ExampleDSLParser.AddColumnsStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#renameColumnStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRenameColumnStatement(ExampleDSLParser.RenameColumnStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#changeDataTypeStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChangeDataTypeStatement(ExampleDSLParser.ChangeDataTypeStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(ExampleDSLParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#sortDataStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSortDataStatement(ExampleDSLParser.SortDataStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#deleteColumnStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeleteColumnStatement(ExampleDSLParser.DeleteColumnStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#renameFileStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRenameFileStatement(ExampleDSLParser.RenameFileStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#file_name}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFile_name(ExampleDSLParser.File_nameContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#applyConditionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitApplyConditionStatement(ExampleDSLParser.ApplyConditionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#generateReportStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGenerateReportStatement(ExampleDSLParser.GenerateReportStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#period}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPeriod(ExampleDSLParser.PeriodContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#reorderColumnsStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReorderColumnsStatement(ExampleDSLParser.ReorderColumnsStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#groupByStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGroupByStatement(ExampleDSLParser.GroupByStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#filterRowsStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFilterRowsStatement(ExampleDSLParser.FilterRowsStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValue(ExampleDSLParser.ValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#searchTextStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSearchTextStatement(ExampleDSLParser.SearchTextStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#replaceValuesStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReplaceValuesStatement(ExampleDSLParser.ReplaceValuesStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#values}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValues(ExampleDSLParser.ValuesContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#addConditionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddConditionStatement(ExampleDSLParser.AddConditionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#removeDuplicatesStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRemoveDuplicatesStatement(ExampleDSLParser.RemoveDuplicatesStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#splitDataStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSplitDataStatement(ExampleDSLParser.SplitDataStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#combineColumnsStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCombineColumnsStatement(ExampleDSLParser.CombineColumnsStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#resizeDataStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitResizeDataStatement(ExampleDSLParser.ResizeDataStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExampleDSLParser#id}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitId(ExampleDSLParser.IdContext ctx);
}