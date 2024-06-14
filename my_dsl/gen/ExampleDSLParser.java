// Generated from E:/uni file/compiler/hw5/my_dsl/grammar/ExampleDSL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExampleDSLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, INPUT=6, OUTPUT=7, COMBINE=8, 
		CONVERT=9, ADD=10, RENAME=11, CHANGE=12, SORT=13, DELETE=14, APPLY=15, 
		GENERATE=16, REORDER=17, GROUP=18, FILTER=19, SEARCH=20, REPLACE=21, REMOVE=22, 
		SPLIT=23, RESIZE=24, SET=25, FILE=26, PATH=27, FORMAT=28, DATA=29, COLUMN=30, 
		COLUMNS=31, TYPE=32, ROWS=33, ROW=34, CONDITION=35, VALUES=36, IN=37, 
		RESULT=38, TO=39, WITH=40, AND=41, BY=42, FROM=43, WHERE=44, ON=45, OF=46, 
		FOR=47, AS=48, SAVE=49, BASED=50, SUM=51, NEW=52, MULTIPLYING=53, NUMBER=54, 
		STRING=55, ID=56, WS=57, WRITE=58, REPORT=59, DUPLICATE=60, RESULTS=61, 
		SEPARATE=62, FILES=63;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_setFilePathStatement = 2, RULE_combineStatement = 3, 
		RULE_convertStatement = 4, RULE_addColumnsStatement = 5, RULE_renameColumnStatement = 6, 
		RULE_changeDataTypeStatement = 7, RULE_sortDataStatement = 8, RULE_deleteColumnStatement = 9, 
		RULE_renameFileStatement = 10, RULE_applyConditionStatement = 11, RULE_generateReportStatement = 12, 
		RULE_reorderColumnsStatement = 13, RULE_groupByStatement = 14, RULE_filterRowsStatement = 15, 
		RULE_searchTextStatement = 16, RULE_replaceValuesStatement = 17, RULE_addConditionStatement = 18, 
		RULE_removeDuplicatesStatement = 19, RULE_splitDataStatement = 20, RULE_combineColumnsStatement = 21, 
		RULE_resizeDataStatement = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "setFilePathStatement", "combineStatement", "convertStatement", 
			"addColumnsStatement", "renameColumnStatement", "changeDataTypeStatement", 
			"sortDataStatement", "deleteColumnStatement", "renameFileStatement", 
			"applyConditionStatement", "generateReportStatement", "reorderColumnsStatement", 
			"groupByStatement", "filterRowsStatement", "searchTextStatement", "replaceValuesStatement", 
			"addConditionStatement", "removeDuplicatesStatement", "splitDataStatement", 
			"combineColumnsStatement", "resizeDataStatement"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'('", "')'", "','", "'>'", "'input'", "'output'", "'Combine'", 
			"'Convert'", "'Add'", "'Rename'", "'Change'", "'Sort'", "'Delete'", "'Apply'", 
			"'Generate'", "'Reorder'", "'Group'", "'Filter'", "'Search'", "'Replace'", 
			"'Remove'", "'Split'", "'Resize'", "'Set'", "'file'", "'path'", "'format'", 
			"'data'", "'column'", "'columns'", "'type'", "'rows'", "'row'", "'condition'", 
			"'values'", "'in'", "'result'", "'to'", "'with'", "'and'", "'by'", "'from'", 
			"'where'", "'on'", "'of'", "'for'", "'as'", "'save'", "'based'", "'sum'", 
			"'new'", "'multiplying'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "INPUT", "OUTPUT", "COMBINE", "CONVERT", 
			"ADD", "RENAME", "CHANGE", "SORT", "DELETE", "APPLY", "GENERATE", "REORDER", 
			"GROUP", "FILTER", "SEARCH", "REPLACE", "REMOVE", "SPLIT", "RESIZE", 
			"SET", "FILE", "PATH", "FORMAT", "DATA", "COLUMN", "COLUMNS", "TYPE", 
			"ROWS", "ROW", "CONDITION", "VALUES", "IN", "RESULT", "TO", "WITH", "AND", 
			"BY", "FROM", "WHERE", "ON", "OF", "FOR", "AS", "SAVE", "BASED", "SUM", 
			"NEW", "MULTIPLYING", "NUMBER", "STRING", "ID", "WS", "WRITE", "REPORT", 
			"DUPLICATE", "RESULTS", "SEPARATE", "FILES"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ExampleDSL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExampleDSLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(46);
				statement();
				}
				}
				setState(49); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 67108608L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public SetFilePathStatementContext setFilePathStatement() {
			return getRuleContext(SetFilePathStatementContext.class,0);
		}
		public CombineStatementContext combineStatement() {
			return getRuleContext(CombineStatementContext.class,0);
		}
		public ConvertStatementContext convertStatement() {
			return getRuleContext(ConvertStatementContext.class,0);
		}
		public AddColumnsStatementContext addColumnsStatement() {
			return getRuleContext(AddColumnsStatementContext.class,0);
		}
		public RenameColumnStatementContext renameColumnStatement() {
			return getRuleContext(RenameColumnStatementContext.class,0);
		}
		public ChangeDataTypeStatementContext changeDataTypeStatement() {
			return getRuleContext(ChangeDataTypeStatementContext.class,0);
		}
		public SortDataStatementContext sortDataStatement() {
			return getRuleContext(SortDataStatementContext.class,0);
		}
		public DeleteColumnStatementContext deleteColumnStatement() {
			return getRuleContext(DeleteColumnStatementContext.class,0);
		}
		public RenameFileStatementContext renameFileStatement() {
			return getRuleContext(RenameFileStatementContext.class,0);
		}
		public ApplyConditionStatementContext applyConditionStatement() {
			return getRuleContext(ApplyConditionStatementContext.class,0);
		}
		public GenerateReportStatementContext generateReportStatement() {
			return getRuleContext(GenerateReportStatementContext.class,0);
		}
		public ReorderColumnsStatementContext reorderColumnsStatement() {
			return getRuleContext(ReorderColumnsStatementContext.class,0);
		}
		public GroupByStatementContext groupByStatement() {
			return getRuleContext(GroupByStatementContext.class,0);
		}
		public FilterRowsStatementContext filterRowsStatement() {
			return getRuleContext(FilterRowsStatementContext.class,0);
		}
		public SearchTextStatementContext searchTextStatement() {
			return getRuleContext(SearchTextStatementContext.class,0);
		}
		public ReplaceValuesStatementContext replaceValuesStatement() {
			return getRuleContext(ReplaceValuesStatementContext.class,0);
		}
		public AddConditionStatementContext addConditionStatement() {
			return getRuleContext(AddConditionStatementContext.class,0);
		}
		public RemoveDuplicatesStatementContext removeDuplicatesStatement() {
			return getRuleContext(RemoveDuplicatesStatementContext.class,0);
		}
		public SplitDataStatementContext splitDataStatement() {
			return getRuleContext(SplitDataStatementContext.class,0);
		}
		public CombineColumnsStatementContext combineColumnsStatement() {
			return getRuleContext(CombineColumnsStatementContext.class,0);
		}
		public ResizeDataStatementContext resizeDataStatement() {
			return getRuleContext(ResizeDataStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(72);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				setFilePathStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
				combineStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(53);
				convertStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(54);
				addColumnsStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(55);
				renameColumnStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(56);
				changeDataTypeStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(57);
				sortDataStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(58);
				deleteColumnStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(59);
				renameFileStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(60);
				applyConditionStatement();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(61);
				generateReportStatement();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(62);
				reorderColumnsStatement();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(63);
				groupByStatement();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(64);
				filterRowsStatement();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(65);
				searchTextStatement();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(66);
				replaceValuesStatement();
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(67);
				addConditionStatement();
				}
				break;
			case 18:
				enterOuterAlt(_localctx, 18);
				{
				setState(68);
				removeDuplicatesStatement();
				}
				break;
			case 19:
				enterOuterAlt(_localctx, 19);
				{
				setState(69);
				splitDataStatement();
				}
				break;
			case 20:
				enterOuterAlt(_localctx, 20);
				{
				setState(70);
				combineColumnsStatement();
				}
				break;
			case 21:
				enterOuterAlt(_localctx, 21);
				{
				setState(71);
				resizeDataStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetFilePathStatementContext extends ParserRuleContext {
		public TerminalNode SET() { return getToken(ExampleDSLParser.SET, 0); }
		public TerminalNode FILE() { return getToken(ExampleDSLParser.FILE, 0); }
		public TerminalNode PATH() { return getToken(ExampleDSLParser.PATH, 0); }
		public TerminalNode INPUT() { return getToken(ExampleDSLParser.INPUT, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public TerminalNode OUTPUT() { return getToken(ExampleDSLParser.OUTPUT, 0); }
		public SetFilePathStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setFilePathStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterSetFilePathStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitSetFilePathStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitSetFilePathStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SetFilePathStatementContext setFilePathStatement() throws RecognitionException {
		SetFilePathStatementContext _localctx = new SetFilePathStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_setFilePathStatement);
		try {
			setState(86);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				match(SET);
				setState(75);
				match(FILE);
				setState(76);
				match(PATH);
				setState(77);
				match(INPUT);
				setState(78);
				match(STRING);
				setState(79);
				match(T__0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				match(SET);
				setState(81);
				match(FILE);
				setState(82);
				match(PATH);
				setState(83);
				match(OUTPUT);
				setState(84);
				match(STRING);
				setState(85);
				match(T__0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CombineStatementContext extends ParserRuleContext {
		public TerminalNode COMBINE() { return getToken(ExampleDSLParser.COMBINE, 0); }
		public List<TerminalNode> FILE() { return getTokens(ExampleDSLParser.FILE); }
		public TerminalNode FILE(int i) {
			return getToken(ExampleDSLParser.FILE, i);
		}
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public TerminalNode WITH() { return getToken(ExampleDSLParser.WITH, 0); }
		public TerminalNode AND() { return getToken(ExampleDSLParser.AND, 0); }
		public TerminalNode WRITE() { return getToken(ExampleDSLParser.WRITE, 0); }
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public CombineStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_combineStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterCombineStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitCombineStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitCombineStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CombineStatementContext combineStatement() throws RecognitionException {
		CombineStatementContext _localctx = new CombineStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_combineStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(COMBINE);
			setState(89);
			match(FILE);
			setState(90);
			match(STRING);
			setState(91);
			match(WITH);
			setState(92);
			match(FILE);
			setState(93);
			match(STRING);
			setState(94);
			match(AND);
			setState(95);
			match(WRITE);
			setState(96);
			match(TO);
			setState(97);
			match(STRING);
			setState(98);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConvertStatementContext extends ParserRuleContext {
		public TerminalNode CONVERT() { return getToken(ExampleDSLParser.CONVERT, 0); }
		public TerminalNode FORMAT() { return getToken(ExampleDSLParser.FORMAT, 0); }
		public TerminalNode FROM() { return getToken(ExampleDSLParser.FROM, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public ConvertStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_convertStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterConvertStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitConvertStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitConvertStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ConvertStatementContext convertStatement() throws RecognitionException {
		ConvertStatementContext _localctx = new ConvertStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_convertStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(CONVERT);
			setState(101);
			match(FORMAT);
			setState(102);
			match(FROM);
			setState(103);
			match(STRING);
			setState(104);
			match(TO);
			setState(105);
			match(STRING);
			setState(106);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddColumnsStatementContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(ExampleDSLParser.ADD, 0); }
		public TerminalNode COLUMNS() { return getToken(ExampleDSLParser.COLUMNS, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public List<TerminalNode> AND() { return getTokens(ExampleDSLParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(ExampleDSLParser.AND, i);
		}
		public TerminalNode SAVE() { return getToken(ExampleDSLParser.SAVE, 0); }
		public TerminalNode RESULT() { return getToken(ExampleDSLParser.RESULT, 0); }
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public AddColumnsStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addColumnsStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterAddColumnsStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitAddColumnsStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitAddColumnsStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AddColumnsStatementContext addColumnsStatement() throws RecognitionException {
		AddColumnsStatementContext _localctx = new AddColumnsStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_addColumnsStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(ADD);
			setState(109);
			match(COLUMNS);
			setState(110);
			match(STRING);
			setState(111);
			match(AND);
			setState(112);
			match(STRING);
			setState(113);
			match(AND);
			setState(114);
			match(SAVE);
			setState(115);
			match(RESULT);
			setState(116);
			match(TO);
			setState(117);
			match(STRING);
			setState(118);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RenameColumnStatementContext extends ParserRuleContext {
		public TerminalNode RENAME() { return getToken(ExampleDSLParser.RENAME, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public RenameColumnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_renameColumnStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterRenameColumnStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitRenameColumnStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitRenameColumnStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RenameColumnStatementContext renameColumnStatement() throws RecognitionException {
		RenameColumnStatementContext _localctx = new RenameColumnStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_renameColumnStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(RENAME);
			setState(121);
			match(COLUMN);
			setState(122);
			match(STRING);
			setState(123);
			match(TO);
			setState(124);
			match(STRING);
			setState(125);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChangeDataTypeStatementContext extends ParserRuleContext {
		public TerminalNode CHANGE() { return getToken(ExampleDSLParser.CHANGE, 0); }
		public TerminalNode DATA() { return getToken(ExampleDSLParser.DATA, 0); }
		public List<TerminalNode> TYPE() { return getTokens(ExampleDSLParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(ExampleDSLParser.TYPE, i);
		}
		public TerminalNode OF() { return getToken(ExampleDSLParser.OF, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public ChangeDataTypeStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_changeDataTypeStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterChangeDataTypeStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitChangeDataTypeStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitChangeDataTypeStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ChangeDataTypeStatementContext changeDataTypeStatement() throws RecognitionException {
		ChangeDataTypeStatementContext _localctx = new ChangeDataTypeStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_changeDataTypeStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(CHANGE);
			setState(128);
			match(DATA);
			setState(129);
			match(TYPE);
			setState(130);
			match(OF);
			setState(131);
			match(COLUMN);
			setState(132);
			match(T__1);
			setState(133);
			match(STRING);
			setState(134);
			match(T__2);
			setState(135);
			match(TO);
			setState(136);
			match(TYPE);
			setState(137);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SortDataStatementContext extends ParserRuleContext {
		public TerminalNode SORT() { return getToken(ExampleDSLParser.SORT, 0); }
		public TerminalNode DATA() { return getToken(ExampleDSLParser.DATA, 0); }
		public TerminalNode BY() { return getToken(ExampleDSLParser.BY, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public SortDataStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sortDataStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterSortDataStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitSortDataStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitSortDataStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SortDataStatementContext sortDataStatement() throws RecognitionException {
		SortDataStatementContext _localctx = new SortDataStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_sortDataStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(SORT);
			setState(140);
			match(DATA);
			setState(141);
			match(BY);
			setState(142);
			match(COLUMN);
			setState(143);
			match(T__1);
			setState(144);
			match(STRING);
			setState(145);
			match(T__2);
			setState(146);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeleteColumnStatementContext extends ParserRuleContext {
		public TerminalNode DELETE() { return getToken(ExampleDSLParser.DELETE, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public DeleteColumnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_deleteColumnStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterDeleteColumnStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitDeleteColumnStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitDeleteColumnStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DeleteColumnStatementContext deleteColumnStatement() throws RecognitionException {
		DeleteColumnStatementContext _localctx = new DeleteColumnStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_deleteColumnStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(DELETE);
			setState(149);
			match(COLUMN);
			setState(150);
			match(STRING);
			setState(151);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RenameFileStatementContext extends ParserRuleContext {
		public TerminalNode RENAME() { return getToken(ExampleDSLParser.RENAME, 0); }
		public TerminalNode OUTPUT() { return getToken(ExampleDSLParser.OUTPUT, 0); }
		public TerminalNode FILE() { return getToken(ExampleDSLParser.FILE, 0); }
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public RenameFileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_renameFileStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterRenameFileStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitRenameFileStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitRenameFileStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RenameFileStatementContext renameFileStatement() throws RecognitionException {
		RenameFileStatementContext _localctx = new RenameFileStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_renameFileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(RENAME);
			setState(154);
			match(OUTPUT);
			setState(155);
			match(FILE);
			setState(156);
			match(TO);
			setState(157);
			match(STRING);
			setState(158);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ApplyConditionStatementContext extends ParserRuleContext {
		public TerminalNode APPLY() { return getToken(ExampleDSLParser.APPLY, 0); }
		public TerminalNode CONDITION() { return getToken(ExampleDSLParser.CONDITION, 0); }
		public TerminalNode ON() { return getToken(ExampleDSLParser.ON, 0); }
		public TerminalNode ROWS() { return getToken(ExampleDSLParser.ROWS, 0); }
		public List<TerminalNode> NUMBER() { return getTokens(ExampleDSLParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(ExampleDSLParser.NUMBER, i);
		}
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public ApplyConditionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_applyConditionStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterApplyConditionStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitApplyConditionStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitApplyConditionStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ApplyConditionStatementContext applyConditionStatement() throws RecognitionException {
		ApplyConditionStatementContext _localctx = new ApplyConditionStatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_applyConditionStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(APPLY);
			setState(161);
			match(CONDITION);
			setState(162);
			match(ON);
			setState(163);
			match(ROWS);
			setState(164);
			match(NUMBER);
			setState(165);
			match(TO);
			setState(166);
			match(NUMBER);
			setState(167);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GenerateReportStatementContext extends ParserRuleContext {
		public TerminalNode GENERATE() { return getToken(ExampleDSLParser.GENERATE, 0); }
		public TerminalNode REPORT() { return getToken(ExampleDSLParser.REPORT, 0); }
		public TerminalNode FOR() { return getToken(ExampleDSLParser.FOR, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public TerminalNode BY() { return getToken(ExampleDSLParser.BY, 0); }
		public GenerateReportStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_generateReportStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterGenerateReportStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitGenerateReportStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitGenerateReportStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final GenerateReportStatementContext generateReportStatement() throws RecognitionException {
		GenerateReportStatementContext _localctx = new GenerateReportStatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_generateReportStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(GENERATE);
			setState(170);
			match(REPORT);
			setState(171);
			match(FOR);
			setState(172);
			match(COLUMN);
			setState(173);
			match(T__1);
			setState(174);
			match(STRING);
			setState(175);
			match(T__2);
			setState(176);
			match(BY);
			setState(177);
			match(STRING);
			setState(178);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReorderColumnsStatementContext extends ParserRuleContext {
		public TerminalNode REORDER() { return getToken(ExampleDSLParser.REORDER, 0); }
		public TerminalNode COLUMNS() { return getToken(ExampleDSLParser.COLUMNS, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public ReorderColumnsStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reorderColumnsStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterReorderColumnsStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitReorderColumnsStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitReorderColumnsStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReorderColumnsStatementContext reorderColumnsStatement() throws RecognitionException {
		ReorderColumnsStatementContext _localctx = new ReorderColumnsStatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_reorderColumnsStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			match(REORDER);
			setState(181);
			match(COLUMNS);
			setState(182);
			match(STRING);
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(183);
				match(T__3);
				setState(184);
				match(STRING);
				}
				}
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(190);
			match(TO);
			setState(191);
			match(STRING);
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(192);
				match(T__3);
				setState(193);
				match(STRING);
				}
				}
				setState(198);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(199);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GroupByStatementContext extends ParserRuleContext {
		public TerminalNode GROUP() { return getToken(ExampleDSLParser.GROUP, 0); }
		public TerminalNode BY() { return getToken(ExampleDSLParser.BY, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public TerminalNode AND() { return getToken(ExampleDSLParser.AND, 0); }
		public TerminalNode SUM() { return getToken(ExampleDSLParser.SUM, 0); }
		public TerminalNode VALUES() { return getToken(ExampleDSLParser.VALUES, 0); }
		public TerminalNode IN() { return getToken(ExampleDSLParser.IN, 0); }
		public GroupByStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_groupByStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterGroupByStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitGroupByStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitGroupByStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final GroupByStatementContext groupByStatement() throws RecognitionException {
		GroupByStatementContext _localctx = new GroupByStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_groupByStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			match(GROUP);
			setState(202);
			match(BY);
			setState(203);
			match(STRING);
			setState(204);
			match(AND);
			setState(205);
			match(SUM);
			setState(206);
			match(VALUES);
			setState(207);
			match(IN);
			setState(208);
			match(STRING);
			setState(209);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FilterRowsStatementContext extends ParserRuleContext {
		public TerminalNode FILTER() { return getToken(ExampleDSLParser.FILTER, 0); }
		public TerminalNode ROWS() { return getToken(ExampleDSLParser.ROWS, 0); }
		public TerminalNode WHERE() { return getToken(ExampleDSLParser.WHERE, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(ExampleDSLParser.NUMBER, 0); }
		public FilterRowsStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterRowsStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterFilterRowsStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitFilterRowsStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitFilterRowsStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FilterRowsStatementContext filterRowsStatement() throws RecognitionException {
		FilterRowsStatementContext _localctx = new FilterRowsStatementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_filterRowsStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(FILTER);
			setState(212);
			match(ROWS);
			setState(213);
			match(WHERE);
			setState(214);
			match(STRING);
			setState(215);
			match(T__4);
			setState(216);
			match(NUMBER);
			setState(217);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SearchTextStatementContext extends ParserRuleContext {
		public TerminalNode SEARCH() { return getToken(ExampleDSLParser.SEARCH, 0); }
		public TerminalNode FOR() { return getToken(ExampleDSLParser.FOR, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public TerminalNode IN() { return getToken(ExampleDSLParser.IN, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public SearchTextStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_searchTextStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterSearchTextStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitSearchTextStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitSearchTextStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SearchTextStatementContext searchTextStatement() throws RecognitionException {
		SearchTextStatementContext _localctx = new SearchTextStatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_searchTextStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			match(SEARCH);
			setState(220);
			match(FOR);
			setState(221);
			match(STRING);
			setState(222);
			match(IN);
			setState(223);
			match(COLUMN);
			setState(224);
			match(T__1);
			setState(225);
			match(STRING);
			setState(226);
			match(T__2);
			setState(227);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReplaceValuesStatementContext extends ParserRuleContext {
		public TerminalNode REPLACE() { return getToken(ExampleDSLParser.REPLACE, 0); }
		public TerminalNode VALUES() { return getToken(ExampleDSLParser.VALUES, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public TerminalNode WITH() { return getToken(ExampleDSLParser.WITH, 0); }
		public TerminalNode IN() { return getToken(ExampleDSLParser.IN, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public ReplaceValuesStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_replaceValuesStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterReplaceValuesStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitReplaceValuesStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitReplaceValuesStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReplaceValuesStatementContext replaceValuesStatement() throws RecognitionException {
		ReplaceValuesStatementContext _localctx = new ReplaceValuesStatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_replaceValuesStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(REPLACE);
			setState(230);
			match(VALUES);
			setState(231);
			match(STRING);
			setState(232);
			match(WITH);
			setState(233);
			match(STRING);
			setState(234);
			match(IN);
			setState(235);
			match(COLUMN);
			setState(236);
			match(T__1);
			setState(237);
			match(STRING);
			setState(238);
			match(T__2);
			setState(239);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddConditionStatementContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(ExampleDSLParser.ADD, 0); }
		public TerminalNode CONDITION() { return getToken(ExampleDSLParser.CONDITION, 0); }
		public TerminalNode WHERE() { return getToken(ExampleDSLParser.WHERE, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(ExampleDSLParser.NUMBER, 0); }
		public AddConditionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addConditionStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterAddConditionStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitAddConditionStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitAddConditionStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AddConditionStatementContext addConditionStatement() throws RecognitionException {
		AddConditionStatementContext _localctx = new AddConditionStatementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_addConditionStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(ADD);
			setState(242);
			match(CONDITION);
			setState(243);
			match(WHERE);
			setState(244);
			match(STRING);
			setState(245);
			match(T__4);
			setState(246);
			match(NUMBER);
			setState(247);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RemoveDuplicatesStatementContext extends ParserRuleContext {
		public TerminalNode REMOVE() { return getToken(ExampleDSLParser.REMOVE, 0); }
		public TerminalNode DUPLICATE() { return getToken(ExampleDSLParser.DUPLICATE, 0); }
		public TerminalNode ROWS() { return getToken(ExampleDSLParser.ROWS, 0); }
		public TerminalNode BASED() { return getToken(ExampleDSLParser.BASED, 0); }
		public TerminalNode ON() { return getToken(ExampleDSLParser.ON, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public RemoveDuplicatesStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_removeDuplicatesStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterRemoveDuplicatesStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitRemoveDuplicatesStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitRemoveDuplicatesStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RemoveDuplicatesStatementContext removeDuplicatesStatement() throws RecognitionException {
		RemoveDuplicatesStatementContext _localctx = new RemoveDuplicatesStatementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_removeDuplicatesStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			match(REMOVE);
			setState(250);
			match(DUPLICATE);
			setState(251);
			match(ROWS);
			setState(252);
			match(BASED);
			setState(253);
			match(ON);
			setState(254);
			match(COLUMN);
			setState(255);
			match(T__1);
			setState(256);
			match(STRING);
			setState(257);
			match(T__2);
			setState(258);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SplitDataStatementContext extends ParserRuleContext {
		public TerminalNode SPLIT() { return getToken(ExampleDSLParser.SPLIT, 0); }
		public TerminalNode DATA() { return getToken(ExampleDSLParser.DATA, 0); }
		public TerminalNode BASED() { return getToken(ExampleDSLParser.BASED, 0); }
		public TerminalNode ON() { return getToken(ExampleDSLParser.ON, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public TerminalNode AND() { return getToken(ExampleDSLParser.AND, 0); }
		public TerminalNode SAVE() { return getToken(ExampleDSLParser.SAVE, 0); }
		public TerminalNode RESULTS() { return getToken(ExampleDSLParser.RESULTS, 0); }
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public TerminalNode SEPARATE() { return getToken(ExampleDSLParser.SEPARATE, 0); }
		public TerminalNode FILES() { return getToken(ExampleDSLParser.FILES, 0); }
		public SplitDataStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_splitDataStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterSplitDataStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitSplitDataStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitSplitDataStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SplitDataStatementContext splitDataStatement() throws RecognitionException {
		SplitDataStatementContext _localctx = new SplitDataStatementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_splitDataStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(SPLIT);
			setState(261);
			match(DATA);
			setState(262);
			match(BASED);
			setState(263);
			match(ON);
			setState(264);
			match(COLUMN);
			setState(265);
			match(T__1);
			setState(266);
			match(STRING);
			setState(267);
			match(T__2);
			setState(268);
			match(AND);
			setState(269);
			match(SAVE);
			setState(270);
			match(RESULTS);
			setState(271);
			match(TO);
			setState(272);
			match(SEPARATE);
			setState(273);
			match(FILES);
			setState(274);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CombineColumnsStatementContext extends ParserRuleContext {
		public TerminalNode COMBINE() { return getToken(ExampleDSLParser.COMBINE, 0); }
		public TerminalNode COLUMNS() { return getToken(ExampleDSLParser.COLUMNS, 0); }
		public List<TerminalNode> STRING() { return getTokens(ExampleDSLParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ExampleDSLParser.STRING, i);
		}
		public List<TerminalNode> AND() { return getTokens(ExampleDSLParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(ExampleDSLParser.AND, i);
		}
		public TerminalNode SAVE() { return getToken(ExampleDSLParser.SAVE, 0); }
		public TerminalNode RESULT() { return getToken(ExampleDSLParser.RESULT, 0); }
		public TerminalNode TO() { return getToken(ExampleDSLParser.TO, 0); }
		public CombineColumnsStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_combineColumnsStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterCombineColumnsStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitCombineColumnsStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitCombineColumnsStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CombineColumnsStatementContext combineColumnsStatement() throws RecognitionException {
		CombineColumnsStatementContext _localctx = new CombineColumnsStatementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_combineColumnsStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			match(COMBINE);
			setState(277);
			match(COLUMNS);
			setState(278);
			match(STRING);
			setState(279);
			match(AND);
			setState(280);
			match(STRING);
			setState(281);
			match(AND);
			setState(282);
			match(SAVE);
			setState(283);
			match(RESULT);
			setState(284);
			match(TO);
			setState(285);
			match(STRING);
			setState(286);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ResizeDataStatementContext extends ParserRuleContext {
		public TerminalNode RESIZE() { return getToken(ExampleDSLParser.RESIZE, 0); }
		public TerminalNode DATA() { return getToken(ExampleDSLParser.DATA, 0); }
		public TerminalNode IN() { return getToken(ExampleDSLParser.IN, 0); }
		public TerminalNode COLUMN() { return getToken(ExampleDSLParser.COLUMN, 0); }
		public TerminalNode STRING() { return getToken(ExampleDSLParser.STRING, 0); }
		public TerminalNode BY() { return getToken(ExampleDSLParser.BY, 0); }
		public TerminalNode MULTIPLYING() { return getToken(ExampleDSLParser.MULTIPLYING, 0); }
		public TerminalNode WITH() { return getToken(ExampleDSLParser.WITH, 0); }
		public TerminalNode NUMBER() { return getToken(ExampleDSLParser.NUMBER, 0); }
		public ResizeDataStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_resizeDataStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).enterResizeDataStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExampleDSLListener ) ((ExampleDSLListener)listener).exitResizeDataStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExampleDSLVisitor ) return ((ExampleDSLVisitor<? extends T>)visitor).visitResizeDataStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ResizeDataStatementContext resizeDataStatement() throws RecognitionException {
		ResizeDataStatementContext _localctx = new ResizeDataStatementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_resizeDataStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			match(RESIZE);
			setState(289);
			match(DATA);
			setState(290);
			match(IN);
			setState(291);
			match(COLUMN);
			setState(292);
			match(T__1);
			setState(293);
			match(STRING);
			setState(294);
			match(T__2);
			setState(295);
			match(BY);
			setState(296);
			match(MULTIPLYING);
			setState(297);
			match(WITH);
			setState(298);
			match(NUMBER);
			setState(299);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001?\u012e\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0001\u0000\u0004\u00000\b\u0000\u000b\u0000"+
		"\f\u00001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001I\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002W\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u00ba\b\r\n\r\f\r\u00bd\t\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u00c3\b\r\n\r\f\r\u00c6\t\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0000\u0000\u0017\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,\u0000\u0000\u012e\u0000/\u0001"+
		"\u0000\u0000\u0000\u0002H\u0001\u0000\u0000\u0000\u0004V\u0001\u0000\u0000"+
		"\u0000\u0006X\u0001\u0000\u0000\u0000\bd\u0001\u0000\u0000\u0000\nl\u0001"+
		"\u0000\u0000\u0000\fx\u0001\u0000\u0000\u0000\u000e\u007f\u0001\u0000"+
		"\u0000\u0000\u0010\u008b\u0001\u0000\u0000\u0000\u0012\u0094\u0001\u0000"+
		"\u0000\u0000\u0014\u0099\u0001\u0000\u0000\u0000\u0016\u00a0\u0001\u0000"+
		"\u0000\u0000\u0018\u00a9\u0001\u0000\u0000\u0000\u001a\u00b4\u0001\u0000"+
		"\u0000\u0000\u001c\u00c9\u0001\u0000\u0000\u0000\u001e\u00d3\u0001\u0000"+
		"\u0000\u0000 \u00db\u0001\u0000\u0000\u0000\"\u00e5\u0001\u0000\u0000"+
		"\u0000$\u00f1\u0001\u0000\u0000\u0000&\u00f9\u0001\u0000\u0000\u0000("+
		"\u0104\u0001\u0000\u0000\u0000*\u0114\u0001\u0000\u0000\u0000,\u0120\u0001"+
		"\u0000\u0000\u0000.0\u0003\u0002\u0001\u0000/.\u0001\u0000\u0000\u0000"+
		"01\u0001\u0000\u0000\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000"+
		"\u00002\u0001\u0001\u0000\u0000\u00003I\u0003\u0004\u0002\u00004I\u0003"+
		"\u0006\u0003\u00005I\u0003\b\u0004\u00006I\u0003\n\u0005\u00007I\u0003"+
		"\f\u0006\u00008I\u0003\u000e\u0007\u00009I\u0003\u0010\b\u0000:I\u0003"+
		"\u0012\t\u0000;I\u0003\u0014\n\u0000<I\u0003\u0016\u000b\u0000=I\u0003"+
		"\u0018\f\u0000>I\u0003\u001a\r\u0000?I\u0003\u001c\u000e\u0000@I\u0003"+
		"\u001e\u000f\u0000AI\u0003 \u0010\u0000BI\u0003\"\u0011\u0000CI\u0003"+
		"$\u0012\u0000DI\u0003&\u0013\u0000EI\u0003(\u0014\u0000FI\u0003*\u0015"+
		"\u0000GI\u0003,\u0016\u0000H3\u0001\u0000\u0000\u0000H4\u0001\u0000\u0000"+
		"\u0000H5\u0001\u0000\u0000\u0000H6\u0001\u0000\u0000\u0000H7\u0001\u0000"+
		"\u0000\u0000H8\u0001\u0000\u0000\u0000H9\u0001\u0000\u0000\u0000H:\u0001"+
		"\u0000\u0000\u0000H;\u0001\u0000\u0000\u0000H<\u0001\u0000\u0000\u0000"+
		"H=\u0001\u0000\u0000\u0000H>\u0001\u0000\u0000\u0000H?\u0001\u0000\u0000"+
		"\u0000H@\u0001\u0000\u0000\u0000HA\u0001\u0000\u0000\u0000HB\u0001\u0000"+
		"\u0000\u0000HC\u0001\u0000\u0000\u0000HD\u0001\u0000\u0000\u0000HE\u0001"+
		"\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000HG\u0001\u0000\u0000\u0000"+
		"I\u0003\u0001\u0000\u0000\u0000JK\u0005\u0019\u0000\u0000KL\u0005\u001a"+
		"\u0000\u0000LM\u0005\u001b\u0000\u0000MN\u0005\u0006\u0000\u0000NO\u0005"+
		"7\u0000\u0000OW\u0005\u0001\u0000\u0000PQ\u0005\u0019\u0000\u0000QR\u0005"+
		"\u001a\u0000\u0000RS\u0005\u001b\u0000\u0000ST\u0005\u0007\u0000\u0000"+
		"TU\u00057\u0000\u0000UW\u0005\u0001\u0000\u0000VJ\u0001\u0000\u0000\u0000"+
		"VP\u0001\u0000\u0000\u0000W\u0005\u0001\u0000\u0000\u0000XY\u0005\b\u0000"+
		"\u0000YZ\u0005\u001a\u0000\u0000Z[\u00057\u0000\u0000[\\\u0005(\u0000"+
		"\u0000\\]\u0005\u001a\u0000\u0000]^\u00057\u0000\u0000^_\u0005)\u0000"+
		"\u0000_`\u0005:\u0000\u0000`a\u0005\'\u0000\u0000ab\u00057\u0000\u0000"+
		"bc\u0005\u0001\u0000\u0000c\u0007\u0001\u0000\u0000\u0000de\u0005\t\u0000"+
		"\u0000ef\u0005\u001c\u0000\u0000fg\u0005+\u0000\u0000gh\u00057\u0000\u0000"+
		"hi\u0005\'\u0000\u0000ij\u00057\u0000\u0000jk\u0005\u0001\u0000\u0000"+
		"k\t\u0001\u0000\u0000\u0000lm\u0005\n\u0000\u0000mn\u0005\u001f\u0000"+
		"\u0000no\u00057\u0000\u0000op\u0005)\u0000\u0000pq\u00057\u0000\u0000"+
		"qr\u0005)\u0000\u0000rs\u00051\u0000\u0000st\u0005&\u0000\u0000tu\u0005"+
		"\'\u0000\u0000uv\u00057\u0000\u0000vw\u0005\u0001\u0000\u0000w\u000b\u0001"+
		"\u0000\u0000\u0000xy\u0005\u000b\u0000\u0000yz\u0005\u001e\u0000\u0000"+
		"z{\u00057\u0000\u0000{|\u0005\'\u0000\u0000|}\u00057\u0000\u0000}~\u0005"+
		"\u0001\u0000\u0000~\r\u0001\u0000\u0000\u0000\u007f\u0080\u0005\f\u0000"+
		"\u0000\u0080\u0081\u0005\u001d\u0000\u0000\u0081\u0082\u0005 \u0000\u0000"+
		"\u0082\u0083\u0005.\u0000\u0000\u0083\u0084\u0005\u001e\u0000\u0000\u0084"+
		"\u0085\u0005\u0002\u0000\u0000\u0085\u0086\u00057\u0000\u0000\u0086\u0087"+
		"\u0005\u0003\u0000\u0000\u0087\u0088\u0005\'\u0000\u0000\u0088\u0089\u0005"+
		" \u0000\u0000\u0089\u008a\u0005\u0001\u0000\u0000\u008a\u000f\u0001\u0000"+
		"\u0000\u0000\u008b\u008c\u0005\r\u0000\u0000\u008c\u008d\u0005\u001d\u0000"+
		"\u0000\u008d\u008e\u0005*\u0000\u0000\u008e\u008f\u0005\u001e\u0000\u0000"+
		"\u008f\u0090\u0005\u0002\u0000\u0000\u0090\u0091\u00057\u0000\u0000\u0091"+
		"\u0092\u0005\u0003\u0000\u0000\u0092\u0093\u0005\u0001\u0000\u0000\u0093"+
		"\u0011\u0001\u0000\u0000\u0000\u0094\u0095\u0005\u000e\u0000\u0000\u0095"+
		"\u0096\u0005\u001e\u0000\u0000\u0096\u0097\u00057\u0000\u0000\u0097\u0098"+
		"\u0005\u0001\u0000\u0000\u0098\u0013\u0001\u0000\u0000\u0000\u0099\u009a"+
		"\u0005\u000b\u0000\u0000\u009a\u009b\u0005\u0007\u0000\u0000\u009b\u009c"+
		"\u0005\u001a\u0000\u0000\u009c\u009d\u0005\'\u0000\u0000\u009d\u009e\u0005"+
		"7\u0000\u0000\u009e\u009f\u0005\u0001\u0000\u0000\u009f\u0015\u0001\u0000"+
		"\u0000\u0000\u00a0\u00a1\u0005\u000f\u0000\u0000\u00a1\u00a2\u0005#\u0000"+
		"\u0000\u00a2\u00a3\u0005-\u0000\u0000\u00a3\u00a4\u0005!\u0000\u0000\u00a4"+
		"\u00a5\u00056\u0000\u0000\u00a5\u00a6\u0005\'\u0000\u0000\u00a6\u00a7"+
		"\u00056\u0000\u0000\u00a7\u00a8\u0005\u0001\u0000\u0000\u00a8\u0017\u0001"+
		"\u0000\u0000\u0000\u00a9\u00aa\u0005\u0010\u0000\u0000\u00aa\u00ab\u0005"+
		";\u0000\u0000\u00ab\u00ac\u0005/\u0000\u0000\u00ac\u00ad\u0005\u001e\u0000"+
		"\u0000\u00ad\u00ae\u0005\u0002\u0000\u0000\u00ae\u00af\u00057\u0000\u0000"+
		"\u00af\u00b0\u0005\u0003\u0000\u0000\u00b0\u00b1\u0005*\u0000\u0000\u00b1"+
		"\u00b2\u00057\u0000\u0000\u00b2\u00b3\u0005\u0001\u0000\u0000\u00b3\u0019"+
		"\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005\u0011\u0000\u0000\u00b5\u00b6"+
		"\u0005\u001f\u0000\u0000\u00b6\u00bb\u00057\u0000\u0000\u00b7\u00b8\u0005"+
		"\u0004\u0000\u0000\u00b8\u00ba\u00057\u0000\u0000\u00b9\u00b7\u0001\u0000"+
		"\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000\u0000\u00bb\u00b9\u0001\u0000"+
		"\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00be\u0001\u0000"+
		"\u0000\u0000\u00bd\u00bb\u0001\u0000\u0000\u0000\u00be\u00bf\u0005\'\u0000"+
		"\u0000\u00bf\u00c4\u00057\u0000\u0000\u00c0\u00c1\u0005\u0004\u0000\u0000"+
		"\u00c1\u00c3\u00057\u0000\u0000\u00c2\u00c0\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c6\u0001\u0000\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000\u0000\u00c4"+
		"\u00c5\u0001\u0000\u0000\u0000\u00c5\u00c7\u0001\u0000\u0000\u0000\u00c6"+
		"\u00c4\u0001\u0000\u0000\u0000\u00c7\u00c8\u0005\u0001\u0000\u0000\u00c8"+
		"\u001b\u0001\u0000\u0000\u0000\u00c9\u00ca\u0005\u0012\u0000\u0000\u00ca"+
		"\u00cb\u0005*\u0000\u0000\u00cb\u00cc\u00057\u0000\u0000\u00cc\u00cd\u0005"+
		")\u0000\u0000\u00cd\u00ce\u00053\u0000\u0000\u00ce\u00cf\u0005$\u0000"+
		"\u0000\u00cf\u00d0\u0005%\u0000\u0000\u00d0\u00d1\u00057\u0000\u0000\u00d1"+
		"\u00d2\u0005\u0001\u0000\u0000\u00d2\u001d\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d4\u0005\u0013\u0000\u0000\u00d4\u00d5\u0005!\u0000\u0000\u00d5\u00d6"+
		"\u0005,\u0000\u0000\u00d6\u00d7\u00057\u0000\u0000\u00d7\u00d8\u0005\u0005"+
		"\u0000\u0000\u00d8\u00d9\u00056\u0000\u0000\u00d9\u00da\u0005\u0001\u0000"+
		"\u0000\u00da\u001f\u0001\u0000\u0000\u0000\u00db\u00dc\u0005\u0014\u0000"+
		"\u0000\u00dc\u00dd\u0005/\u0000\u0000\u00dd\u00de\u00057\u0000\u0000\u00de"+
		"\u00df\u0005%\u0000\u0000\u00df\u00e0\u0005\u001e\u0000\u0000\u00e0\u00e1"+
		"\u0005\u0002\u0000\u0000\u00e1\u00e2\u00057\u0000\u0000\u00e2\u00e3\u0005"+
		"\u0003\u0000\u0000\u00e3\u00e4\u0005\u0001\u0000\u0000\u00e4!\u0001\u0000"+
		"\u0000\u0000\u00e5\u00e6\u0005\u0015\u0000\u0000\u00e6\u00e7\u0005$\u0000"+
		"\u0000\u00e7\u00e8\u00057\u0000\u0000\u00e8\u00e9\u0005(\u0000\u0000\u00e9"+
		"\u00ea\u00057\u0000\u0000\u00ea\u00eb\u0005%\u0000\u0000\u00eb\u00ec\u0005"+
		"\u001e\u0000\u0000\u00ec\u00ed\u0005\u0002\u0000\u0000\u00ed\u00ee\u0005"+
		"7\u0000\u0000\u00ee\u00ef\u0005\u0003\u0000\u0000\u00ef\u00f0\u0005\u0001"+
		"\u0000\u0000\u00f0#\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005\n\u0000"+
		"\u0000\u00f2\u00f3\u0005#\u0000\u0000\u00f3\u00f4\u0005,\u0000\u0000\u00f4"+
		"\u00f5\u00057\u0000\u0000\u00f5\u00f6\u0005\u0005\u0000\u0000\u00f6\u00f7"+
		"\u00056\u0000\u0000\u00f7\u00f8\u0005\u0001\u0000\u0000\u00f8%\u0001\u0000"+
		"\u0000\u0000\u00f9\u00fa\u0005\u0016\u0000\u0000\u00fa\u00fb\u0005<\u0000"+
		"\u0000\u00fb\u00fc\u0005!\u0000\u0000\u00fc\u00fd\u00052\u0000\u0000\u00fd"+
		"\u00fe\u0005-\u0000\u0000\u00fe\u00ff\u0005\u001e\u0000\u0000\u00ff\u0100"+
		"\u0005\u0002\u0000\u0000\u0100\u0101\u00057\u0000\u0000\u0101\u0102\u0005"+
		"\u0003\u0000\u0000\u0102\u0103\u0005\u0001\u0000\u0000\u0103\'\u0001\u0000"+
		"\u0000\u0000\u0104\u0105\u0005\u0017\u0000\u0000\u0105\u0106\u0005\u001d"+
		"\u0000\u0000\u0106\u0107\u00052\u0000\u0000\u0107\u0108\u0005-\u0000\u0000"+
		"\u0108\u0109\u0005\u001e\u0000\u0000\u0109\u010a\u0005\u0002\u0000\u0000"+
		"\u010a\u010b\u00057\u0000\u0000\u010b\u010c\u0005\u0003\u0000\u0000\u010c"+
		"\u010d\u0005)\u0000\u0000\u010d\u010e\u00051\u0000\u0000\u010e\u010f\u0005"+
		"=\u0000\u0000\u010f\u0110\u0005\'\u0000\u0000\u0110\u0111\u0005>\u0000"+
		"\u0000\u0111\u0112\u0005?\u0000\u0000\u0112\u0113\u0005\u0001\u0000\u0000"+
		"\u0113)\u0001\u0000\u0000\u0000\u0114\u0115\u0005\b\u0000\u0000\u0115"+
		"\u0116\u0005\u001f\u0000\u0000\u0116\u0117\u00057\u0000\u0000\u0117\u0118"+
		"\u0005)\u0000\u0000\u0118\u0119\u00057\u0000\u0000\u0119\u011a\u0005)"+
		"\u0000\u0000\u011a\u011b\u00051\u0000\u0000\u011b\u011c\u0005&\u0000\u0000"+
		"\u011c\u011d\u0005\'\u0000\u0000\u011d\u011e\u00057\u0000\u0000\u011e"+
		"\u011f\u0005\u0001\u0000\u0000\u011f+\u0001\u0000\u0000\u0000\u0120\u0121"+
		"\u0005\u0018\u0000\u0000\u0121\u0122\u0005\u001d\u0000\u0000\u0122\u0123"+
		"\u0005%\u0000\u0000\u0123\u0124\u0005\u001e\u0000\u0000\u0124\u0125\u0005"+
		"\u0002\u0000\u0000\u0125\u0126\u00057\u0000\u0000\u0126\u0127\u0005\u0003"+
		"\u0000\u0000\u0127\u0128\u0005*\u0000\u0000\u0128\u0129\u00055\u0000\u0000"+
		"\u0129\u012a\u0005(\u0000\u0000\u012a\u012b\u00056\u0000\u0000\u012b\u012c"+
		"\u0005\u0001\u0000\u0000\u012c-\u0001\u0000\u0000\u0000\u00051HV\u00bb"+
		"\u00c4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}