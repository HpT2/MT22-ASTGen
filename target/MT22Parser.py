# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u0172\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3X\n\3\3")
        buf.write("\4\3\4\3\4\3\4\5\4^\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5g\n\5\3\5\3\5\3\5\3\5\3\5\5\5n\n\5\3\6\3\6\5\6r\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7y\n\7\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u0080\n\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0088\n\t\f\t\16")
        buf.write("\t\u008b\13\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u0093\n\n\f")
        buf.write("\n\16\n\u0096\13\n\3\13\3\13\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u009e\n\13\f\13\16\13\u00a1\13\13\3\f\3\f\3\f\5\f\u00a6")
        buf.write("\n\f\3\r\3\r\3\r\5\r\u00ab\n\r\3\16\3\16\5\16\u00af\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00bd\n\17\3\20\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00c4\n\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\5\23\u00d3\n\23\3\23\3\23\3")
        buf.write("\24\3\24\3\25\3\25\3\25\5\25\u00dc\n\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00e8\n\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u00f4\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\5\32\u0103\n\32\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u0109\n\33\3\34\3\34\5\34\u010d\n\34\3\35\5")
        buf.write("\35\u0110\n\35\3\35\5\35\u0113\n\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u011e\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\5\37\u0127\n\37\3\37\3\37\3\37")
        buf.write("\5\37\u012c\n\37\3\37\3\37\3 \3 \5 \u0132\n \3 \3 \3 ")
        buf.write("\3!\3!\3!\5!\u013a\n!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\5#\u0148\n#\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0152")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u016e\n(\3(\3(")
        buf.write("\3(\2\5\20\22\24)\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLN\2\7\3\2 %\3\2\36")
        buf.write("\37\3\2\30\31\3\2\32\34\6\2\5\5\t\t\r\r\17\17\2\u017b")
        buf.write("\2P\3\2\2\2\4W\3\2\2\2\6]\3\2\2\2\bm\3\2\2\2\nq\3\2\2")
        buf.write("\2\fx\3\2\2\2\16\177\3\2\2\2\20\u0081\3\2\2\2\22\u008c")
        buf.write("\3\2\2\2\24\u0097\3\2\2\2\26\u00a5\3\2\2\2\30\u00aa\3")
        buf.write("\2\2\2\32\u00ae\3\2\2\2\34\u00bc\3\2\2\2\36\u00c3\3\2")
        buf.write("\2\2 \u00c5\3\2\2\2\"\u00ca\3\2\2\2$\u00cf\3\2\2\2&\u00d6")
        buf.write("\3\2\2\2(\u00db\3\2\2\2*\u00e7\3\2\2\2,\u00f3\3\2\2\2")
        buf.write(".\u00f5\3\2\2\2\60\u00fa\3\2\2\2\62\u0102\3\2\2\2\64\u0108")
        buf.write("\3\2\2\2\66\u010c\3\2\2\28\u010f\3\2\2\2:\u011d\3\2\2")
        buf.write("\2<\u011f\3\2\2\2>\u0131\3\2\2\2@\u0136\3\2\2\2B\u013b")
        buf.write("\3\2\2\2D\u0147\3\2\2\2F\u0149\3\2\2\2H\u0153\3\2\2\2")
        buf.write("J\u015d\3\2\2\2L\u0163\3\2\2\2N\u016a\3\2\2\2PQ\5\4\3")
        buf.write("\2QR\7\2\2\3R\3\3\2\2\2ST\5\n\6\2TU\5\4\3\2UX\3\2\2\2")
        buf.write("VX\5\n\6\2WS\3\2\2\2WV\3\2\2\2X\5\3\2\2\2YZ\5\b\5\2Z[")
        buf.write("\5\6\4\2[^\3\2\2\2\\^\5\b\5\2]Y\3\2\2\2]\\\3\2\2\2^\7")
        buf.write("\3\2\2\2_n\5N(\2`n\5*\26\2ag\5> \2bg\5@!\2cg\5L\'\2dg")
        buf.write("\7\4\2\2eg\7\24\2\2fa\3\2\2\2fb\3\2\2\2fc\3\2\2\2fd\3")
        buf.write("\2\2\2fe\3\2\2\2gh\3\2\2\2hn\7-\2\2in\5F$\2jn\5H%\2kn")
        buf.write("\5J&\2ln\5B\"\2m_\3\2\2\2m`\3\2\2\2mf\3\2\2\2mi\3\2\2")
        buf.write("\2mj\3\2\2\2mk\3\2\2\2ml\3\2\2\2n\t\3\2\2\2or\5*\26\2")
        buf.write("pr\5<\37\2qo\3\2\2\2qp\3\2\2\2r\13\3\2\2\2st\5\16\b\2")
        buf.write("tu\7&\2\2uv\5\16\b\2vy\3\2\2\2wy\5\16\b\2xs\3\2\2\2xw")
        buf.write("\3\2\2\2y\r\3\2\2\2z{\5\20\t\2{|\t\2\2\2|}\5\20\t\2}\u0080")
        buf.write("\3\2\2\2~\u0080\5\20\t\2\177z\3\2\2\2\177~\3\2\2\2\u0080")
        buf.write("\17\3\2\2\2\u0081\u0082\b\t\1\2\u0082\u0083\5\22\n\2\u0083")
        buf.write("\u0089\3\2\2\2\u0084\u0085\f\4\2\2\u0085\u0086\t\3\2\2")
        buf.write("\u0086\u0088\5\22\n\2\u0087\u0084\3\2\2\2\u0088\u008b")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\21\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\b\n\1\2\u008d")
        buf.write("\u008e\5\24\13\2\u008e\u0094\3\2\2\2\u008f\u0090\f\4\2")
        buf.write("\2\u0090\u0091\t\4\2\2\u0091\u0093\5\24\13\2\u0092\u008f")
        buf.write("\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\23\3\2\2\2\u0096\u0094\3\2\2\2\u0097")
        buf.write("\u0098\b\13\1\2\u0098\u0099\5\26\f\2\u0099\u009f\3\2\2")
        buf.write("\2\u009a\u009b\f\4\2\2\u009b\u009c\t\5\2\2\u009c\u009e")
        buf.write("\5\26\f\2\u009d\u009a\3\2\2\2\u009e\u00a1\3\2\2\2\u009f")
        buf.write("\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\25\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a2\u00a3\7\35\2\2\u00a3\u00a6\5\26\f")
        buf.write("\2\u00a4\u00a6\5\30\r\2\u00a5\u00a2\3\2\2\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a6\27\3\2\2\2\u00a7\u00a8\7\31\2\2\u00a8\u00ab")
        buf.write("\5\30\r\2\u00a9\u00ab\5\32\16\2\u00aa\u00a7\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\31\3\2\2\2\u00ac\u00af\5 \21\2\u00ad")
        buf.write("\u00af\5\34\17\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2")
        buf.write("\2\u00af\33\3\2\2\2\u00b0\u00bd\7\64\2\2\u00b1\u00bd\7")
        buf.write("\65\2\2\u00b2\u00bd\7\66\2\2\u00b3\u00bd\7\67\2\2\u00b4")
        buf.write("\u00bd\7\20\2\2\u00b5\u00bd\7\b\2\2\u00b6\u00bd\5\"\22")
        buf.write("\2\u00b7\u00bd\5$\23\2\u00b8\u00b9\7\'\2\2\u00b9\u00ba")
        buf.write("\5\f\7\2\u00ba\u00bb\7(\2\2\u00bb\u00bd\3\2\2\2\u00bc")
        buf.write("\u00b0\3\2\2\2\u00bc\u00b1\3\2\2\2\u00bc\u00b2\3\2\2\2")
        buf.write("\u00bc\u00b3\3\2\2\2\u00bc\u00b4\3\2\2\2\u00bc\u00b5\3")
        buf.write("\2\2\2\u00bc\u00b6\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bc\u00b8")
        buf.write("\3\2\2\2\u00bd\35\3\2\2\2\u00be\u00bf\5\f\7\2\u00bf\u00c0")
        buf.write("\7,\2\2\u00c0\u00c1\5\36\20\2\u00c1\u00c4\3\2\2\2\u00c2")
        buf.write("\u00c4\5\f\7\2\u00c3\u00be\3\2\2\2\u00c3\u00c2\3\2\2\2")
        buf.write("\u00c4\37\3\2\2\2\u00c5\u00c6\7\64\2\2\u00c6\u00c7\7)")
        buf.write("\2\2\u00c7\u00c8\5\36\20\2\u00c8\u00c9\7*\2\2\u00c9!\3")
        buf.write("\2\2\2\u00ca\u00cb\7\64\2\2\u00cb\u00cc\7\'\2\2\u00cc")
        buf.write("\u00cd\5D#\2\u00cd\u00ce\7(\2\2\u00ce#\3\2\2\2\u00cf\u00d2")
        buf.write("\7/\2\2\u00d0\u00d3\5\36\20\2\u00d1\u00d3\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\u00d5\7\60\2\2\u00d5%\3\2\2\2\u00d6\u00d7\t\6\2")
        buf.write("\2\u00d7\'\3\2\2\2\u00d8\u00dc\5&\24\2\u00d9\u00dc\7\3")
        buf.write("\2\2\u00da\u00dc\5.\30\2\u00db\u00d8\3\2\2\2\u00db\u00d9")
        buf.write("\3\2\2\2\u00db\u00da\3\2\2\2\u00dc)\3\2\2\2\u00dd\u00de")
        buf.write("\5\64\33\2\u00de\u00df\7.\2\2\u00df\u00e0\5(\25\2\u00e0")
        buf.write("\u00e1\7-\2\2\u00e1\u00e8\3\2\2\2\u00e2\u00e3\7\64\2\2")
        buf.write("\u00e3\u00e4\5,\27\2\u00e4\u00e5\5\f\7\2\u00e5\u00e6\7")
        buf.write("-\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00dd\3\2\2\2\u00e7\u00e2")
        buf.write("\3\2\2\2\u00e8+\3\2\2\2\u00e9\u00ea\7,\2\2\u00ea\u00eb")
        buf.write("\7\64\2\2\u00eb\u00ec\5,\27\2\u00ec\u00ed\5\f\7\2\u00ed")
        buf.write("\u00ee\7,\2\2\u00ee\u00f4\3\2\2\2\u00ef\u00f0\7.\2\2\u00f0")
        buf.write("\u00f1\5(\25\2\u00f1\u00f2\7\61\2\2\u00f2\u00f4\3\2\2")
        buf.write("\2\u00f3\u00e9\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f4-\3\2")
        buf.write("\2\2\u00f5\u00f6\7\27\2\2\u00f6\u00f7\5\60\31\2\u00f7")
        buf.write("\u00f8\7\25\2\2\u00f8\u00f9\5&\24\2\u00f9/\3\2\2\2\u00fa")
        buf.write("\u00fb\7)\2\2\u00fb\u00fc\5\62\32\2\u00fc\u00fd\7*\2\2")
        buf.write("\u00fd\61\3\2\2\2\u00fe\u00ff\7\65\2\2\u00ff\u0100\7,")
        buf.write("\2\2\u0100\u0103\5\62\32\2\u0101\u0103\7\65\2\2\u0102")
        buf.write("\u00fe\3\2\2\2\u0102\u0101\3\2\2\2\u0103\63\3\2\2\2\u0104")
        buf.write("\u0105\7\64\2\2\u0105\u0106\7,\2\2\u0106\u0109\5\64\33")
        buf.write("\2\u0107\u0109\7\64\2\2\u0108\u0104\3\2\2\2\u0108\u0107")
        buf.write("\3\2\2\2\u0109\65\3\2\2\2\u010a\u010d\5(\25\2\u010b\u010d")
        buf.write("\7\22\2\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("\67\3\2\2\2\u010e\u0110\7\26\2\2\u010f\u010e\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0112\3\2\2\2\u0111\u0113\7\23\2")
        buf.write("\2\u0112\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u0114\u0115\7\64\2\2\u0115\u0116\7.\2\2\u0116")
        buf.write("\u0117\5(\25\2\u01179\3\2\2\2\u0118\u0119\58\35\2\u0119")
        buf.write("\u011a\7,\2\2\u011a\u011b\5:\36\2\u011b\u011e\3\2\2\2")
        buf.write("\u011c\u011e\58\35\2\u011d\u0118\3\2\2\2\u011d\u011c\3")
        buf.write("\2\2\2\u011e;\3\2\2\2\u011f\u0120\7\64\2\2\u0120\u0121")
        buf.write("\7.\2\2\u0121\u0122\7\13\2\2\u0122\u0123\5\66\34\2\u0123")
        buf.write("\u0126\7\'\2\2\u0124\u0127\5:\36\2\u0125\u0127\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2\u0127\u0128\3")
        buf.write("\2\2\2\u0128\u012b\7(\2\2\u0129\u012a\7\26\2\2\u012a\u012c")
        buf.write("\7\64\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012e\5N(\2\u012e=\3\2\2\2\u012f")
        buf.write("\u0132\7\64\2\2\u0130\u0132\5 \21\2\u0131\u012f\3\2\2")
        buf.write("\2\u0131\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134")
        buf.write("\7\61\2\2\u0134\u0135\5\f\7\2\u0135?\3\2\2\2\u0136\u0139")
        buf.write("\7\16\2\2\u0137\u013a\5\f\7\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u0137\3\2\2\2\u0139\u0138\3\2\2\2\u013aA\3\2\2\2\u013b")
        buf.write("\u013c\7\64\2\2\u013c\u013d\7\'\2\2\u013d\u013e\5D#\2")
        buf.write("\u013e\u013f\7(\2\2\u013f\u0140\7-\2\2\u0140C\3\2\2\2")
        buf.write("\u0141\u0142\5\f\7\2\u0142\u0143\7,\2\2\u0143\u0144\5")
        buf.write("D#\2\u0144\u0148\3\2\2\2\u0145\u0148\5\f\7\2\u0146\u0148")
        buf.write("\3\2\2\2\u0147\u0141\3\2\2\2\u0147\u0145\3\2\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0148E\3\2\2\2\u0149\u014a\7\f\2\2\u014a")
        buf.write("\u014b\7\'\2\2\u014b\u014c\5\f\7\2\u014c\u014d\7(\2\2")
        buf.write("\u014d\u0151\5\b\5\2\u014e\u014f\7\7\2\2\u014f\u0152\5")
        buf.write("\b\5\2\u0150\u0152\3\2\2\2\u0151\u014e\3\2\2\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152G\3\2\2\2\u0153\u0154\7\n\2\2\u0154\u0155")
        buf.write("\7\'\2\2\u0155\u0156\5> \2\u0156\u0157\7,\2\2\u0157\u0158")
        buf.write("\5\f\7\2\u0158\u0159\7,\2\2\u0159\u015a\5\f\7\2\u015a")
        buf.write("\u015b\7(\2\2\u015b\u015c\5\b\5\2\u015cI\3\2\2\2\u015d")
        buf.write("\u015e\7\21\2\2\u015e\u015f\7\'\2\2\u015f\u0160\5\f\7")
        buf.write("\2\u0160\u0161\7(\2\2\u0161\u0162\5\b\5\2\u0162K\3\2\2")
        buf.write("\2\u0163\u0164\7\6\2\2\u0164\u0165\5N(\2\u0165\u0166\7")
        buf.write("\21\2\2\u0166\u0167\7\'\2\2\u0167\u0168\5\f\7\2\u0168")
        buf.write("\u0169\7(\2\2\u0169M\3\2\2\2\u016a\u016d\7/\2\2\u016b")
        buf.write("\u016e\5\6\4\2\u016c\u016e\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\7")
        buf.write("\60\2\2\u0170O\3\2\2\2\"W]fmqx\177\u0089\u0094\u009f\u00a5")
        buf.write("\u00aa\u00ae\u00bc\u00c3\u00d2\u00db\u00e7\u00f3\u0102")
        buf.write("\u0108\u010c\u010f\u0112\u011d\u0126\u012b\u0131\u0139")
        buf.write("\u0147\u0151\u016d")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'boolean'", "'do'", 
                     "'else'", "'false'", "'float'", "'for'", "'function'", 
                     "'if'", "'integer'", "'return'", "'string'", "'true'", 
                     "'while'", "'void'", "'out'", "'continue'", "'of'", 
                     "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
                     "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                      "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                      "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", 
                      "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", 
                      "MULOP", "DIVOP", "MODULO", "LOGICNOT", "AND", "OR", 
                      "EQ", "NOTEQ", "LESS", "LESSOREQ", "MORE_", "MOREOREQ", 
                      "DBLCOL", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", 
                      "SEMI", "COLON", "LCB", "RCB", "ASSIGN", "COMMENT", 
                      "LINE_COMMENT", "ID", "INT_TYPE", "FLOAT_TYPE", "STRING_TYPE", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_prog = 1
    RULE_stmtlist = 2
    RULE_stmt = 3
    RULE_declaration = 4
    RULE_expr = 5
    RULE_expr1 = 6
    RULE_expr2 = 7
    RULE_expr3 = 8
    RULE_expr4 = 9
    RULE_expr5 = 10
    RULE_expr6 = 11
    RULE_expr7 = 12
    RULE_exprval = 13
    RULE_exprlist = 14
    RULE_indexop = 15
    RULE_func_call = 16
    RULE_indexed_array = 17
    RULE_atomic_type = 18
    RULE_type_ = 19
    RULE_var_declare = 20
    RULE_recur = 21
    RULE_array_type = 22
    RULE_dimension = 23
    RULE_intlist = 24
    RULE_id_list = 25
    RULE_function_type = 26
    RULE_param = 27
    RULE_param_list = 28
    RULE_func_declare = 29
    RULE_assignment = 30
    RULE_return_stmt = 31
    RULE_call_stmt = 32
    RULE_argument = 33
    RULE_if_stmt = 34
    RULE_for_stmt = 35
    RULE_while_stmt = 36
    RULE_do_while_stmt = 37
    RULE_block_stmt = 38

    ruleNames =  [ "program", "prog", "stmtlist", "stmt", "declaration", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "exprval", "exprlist", "indexop", "func_call", 
                   "indexed_array", "atomic_type", "type_", "var_declare", 
                   "recur", "array_type", "dimension", "intlist", "id_list", 
                   "function_type", "param", "param_list", "func_declare", 
                   "assignment", "return_stmt", "call_stmt", "argument", 
                   "if_stmt", "for_stmt", "while_stmt", "do_while_stmt", 
                   "block_stmt" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    BOOLEAN=3
    DO=4
    ELSE=5
    FALSE=6
    FLOAT=7
    FOR=8
    FUNCTION=9
    IF=10
    INTEGER=11
    RETURN=12
    STRING=13
    TRUE=14
    WHILE=15
    VOID=16
    OUT=17
    CONTINUE=18
    OF=19
    INHERIT=20
    ARRAY=21
    ADDOP=22
    SUBOP=23
    MULOP=24
    DIVOP=25
    MODULO=26
    LOGICNOT=27
    AND=28
    OR=29
    EQ=30
    NOTEQ=31
    LESS=32
    LESSOREQ=33
    MORE_=34
    MOREOREQ=35
    DBLCOL=36
    LP=37
    RP=38
    LSB=39
    RSB=40
    DOT=41
    COMMA=42
    SEMI=43
    COLON=44
    LCB=45
    RCB=46
    ASSIGN=47
    COMMENT=48
    LINE_COMMENT=49
    ID=50
    INT_TYPE=51
    FLOAT_TYPE=52
    STRING_TYPE=53
    WS=54
    ILLEGAL_ESCAPE=55
    UNCLOSE_STRING=56
    ERROR_CHAR=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self):
            return self.getTypedRuleContext(MT22Parser.ProgContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.prog()
            self.state = 79
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MT22Parser.DeclarationContext,0)


        def prog(self):
            return self.getTypedRuleContext(MT22Parser.ProgContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MT22Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.declaration()
                self.state = 82
                self.prog()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = MT22Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmtlist)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.stmt()
                self.state = 88
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def var_declare(self):
            return self.getTypedRuleContext(MT22Parser.Var_declareContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def assignment(self):
            return self.getTypedRuleContext(MT22Parser.AssignmentContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Return_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Do_while_stmtContext,0)


        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(MT22Parser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MT22Parser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.While_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Call_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.var_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MT22Parser.ID]:
                    self.state = 95
                    self.assignment()
                    pass
                elif token in [MT22Parser.RETURN]:
                    self.state = 96
                    self.return_stmt()
                    pass
                elif token in [MT22Parser.DO]:
                    self.state = 97
                    self.do_while_stmt()
                    pass
                elif token in [MT22Parser.BREAK]:
                    self.state = 98
                    self.match(MT22Parser.BREAK)
                    pass
                elif token in [MT22Parser.CONTINUE]:
                    self.state = 99
                    self.match(MT22Parser.CONTINUE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 102
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 106
                self.call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(MT22Parser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(MT22Parser.Func_declareContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MT22Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.func_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def DBLCOL(self):
            return self.getToken(MT22Parser.DBLCOL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.expr1()
                self.state = 114
                self.match(MT22Parser.DBLCOL)
                self.state = 115
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def NOTEQ(self):
            return self.getToken(MT22Parser.NOTEQ, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def MORE_(self):
            return self.getToken(MT22Parser.MORE_, 0)

        def LESSOREQ(self):
            return self.getToken(MT22Parser.LESSOREQ, 0)

        def MOREOREQ(self):
            return self.getToken(MT22Parser.MOREOREQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.expr2(0)
                self.state = 121
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQ) | (1 << MT22Parser.NOTEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LESSOREQ) | (1 << MT22Parser.MORE_) | (1 << MT22Parser.MOREOREQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 130
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 131
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 132
                    self.expr3(0) 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def ADDOP(self):
            return self.getToken(MT22Parser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 141
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 142
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADDOP or _la==MT22Parser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 143
                    self.expr4(0) 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MULOP(self):
            return self.getToken(MT22Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MT22Parser.DIVOP, 0)

        def MODULO(self):
            return self.getToken(MT22Parser.MODULO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULOP) | (1 << MT22Parser.DIVOP) | (1 << MT22Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 154
                    self.expr5() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICNOT(self):
            return self.getToken(MT22Parser.LOGICNOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr5)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LOGICNOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(MT22Parser.LOGICNOT)
                self.state = 161
                self.expr5()
                pass
            elif token in [MT22Parser.FALSE, MT22Parser.TRUE, MT22Parser.SUBOP, MT22Parser.LP, MT22Parser.LCB, MT22Parser.ID, MT22Parser.INT_TYPE, MT22Parser.FLOAT_TYPE, MT22Parser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr6)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(MT22Parser.SUBOP)
                self.state = 166
                self.expr6()
                pass
            elif token in [MT22Parser.FALSE, MT22Parser.TRUE, MT22Parser.LP, MT22Parser.LCB, MT22Parser.ID, MT22Parser.INT_TYPE, MT22Parser.FLOAT_TYPE, MT22Parser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def exprval(self):
            return self.getTypedRuleContext(MT22Parser.ExprvalContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr7)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.exprval()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def INT_TYPE(self):
            return self.getToken(MT22Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(MT22Parser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(MT22Parser.STRING_TYPE, 0)

        def TRUE(self):
            return self.getToken(MT22Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MT22Parser.FALSE, 0)

        def func_call(self):
            return self.getTypedRuleContext(MT22Parser.Func_callContext,0)


        def indexed_array(self):
            return self.getTypedRuleContext(MT22Parser.Indexed_arrayContext,0)


        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exprval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprval" ):
                return visitor.visitExprval(self)
            else:
                return visitor.visitChildren(self)




    def exprval(self):

        localctx = MT22Parser.ExprvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprval)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(MT22Parser.INT_TYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(MT22Parser.FLOAT_TYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.match(MT22Parser.STRING_TYPE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.match(MT22Parser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.match(MT22Parser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.func_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 181
                self.indexed_array()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 182
                self.match(MT22Parser.LP)
                self.state = 183
                self.expr()
                self.state = 184
                self.match(MT22Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprlist)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.expr()
                self.state = 189
                self.match(MT22Parser.COMMA)
                self.state = 190
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)




    def indexop(self):

        localctx = MT22Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MT22Parser.ID)
            self.state = 196
            self.match(MT22Parser.LSB)
            self.state = 197
            self.exprlist()
            self.state = 198
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def argument(self):
            return self.getTypedRuleContext(MT22Parser.ArgumentContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MT22Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MT22Parser.ID)
            self.state = 201
            self.match(MT22Parser.LP)
            self.state = 202
            self.argument()
            self.state = 203
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_indexed_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = MT22Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_indexed_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MT22Parser.LCB)
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.FALSE, MT22Parser.TRUE, MT22Parser.SUBOP, MT22Parser.LOGICNOT, MT22Parser.LP, MT22Parser.LCB, MT22Parser.ID, MT22Parser.INT_TYPE, MT22Parser.FLOAT_TYPE, MT22Parser.STRING_TYPE]:
                self.state = 206
                self.exprlist()
                pass
            elif token in [MT22Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 210
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_type" ):
                return visitor.visitAtomic_type(self)
            else:
                return visitor.visitChildren(self)




    def atomic_type(self):

        localctx = MT22Parser.Atomic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_atomic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MT22Parser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_type_)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.atomic_type()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MT22Parser.Type_Context,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def recur(self):
            return self.getTypedRuleContext(MT22Parser.RecurContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = MT22Parser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_declare)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.id_list()
                self.state = 220
                self.match(MT22Parser.COLON)
                self.state = 221
                self.type_()
                self.state = 222
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(MT22Parser.ID)
                self.state = 225
                self.recur()
                self.state = 226
                self.expr()
                self.state = 227
                self.match(MT22Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def recur(self):
            return self.getTypedRuleContext(MT22Parser.RecurContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MT22Parser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_recur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecur" ):
                return visitor.visitRecur(self)
            else:
                return visitor.visitChildren(self)




    def recur(self):

        localctx = MT22Parser.RecurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_recur)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(MT22Parser.COMMA)
                self.state = 232
                self.match(MT22Parser.ID)
                self.state = 233
                self.recur()
                self.state = 234
                self.expr()
                self.state = 235
                self.match(MT22Parser.COMMA)
                pass
            elif token in [MT22Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(MT22Parser.COLON)
                self.state = 238
                self.type_()
                self.state = 239
                self.match(MT22Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MT22Parser.ARRAY)
            self.state = 244
            self.dimension()
            self.state = 245
            self.match(MT22Parser.OF)
            self.state = 246
            self.atomic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def intlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MT22Parser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MT22Parser.LSB)
            self.state = 249
            self.intlist()
            self.state = 250
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(MT22Parser.INT_TYPE, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def intlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_intlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntlist" ):
                return visitor.visitIntlist(self)
            else:
                return visitor.visitChildren(self)




    def intlist(self):

        localctx = MT22Parser.IntlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_intlist)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(MT22Parser.INT_TYPE)
                self.state = 253
                self.match(MT22Parser.COMMA)
                self.state = 254
                self.intlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(MT22Parser.INT_TYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MT22Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_id_list)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(MT22Parser.ID)
                self.state = 259
                self.match(MT22Parser.COMMA)
                self.state = 260
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MT22Parser.Type_Context,0)


        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_function_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_type" ):
                return visitor.visitFunction_type(self)
            else:
                return visitor.visitChildren(self)




    def function_type(self):

        localctx = MT22Parser.Function_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_function_type)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING, MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.type_()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.match(MT22Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MT22Parser.Type_Context,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 268
                self.match(MT22Parser.INHERIT)


            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 271
                self.match(MT22Parser.OUT)


            self.state = 274
            self.match(MT22Parser.ID)
            self.state = 275
            self.match(MT22Parser.COLON)
            self.state = 276
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(MT22Parser.Param_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MT22Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_param_list)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.param()
                self.state = 279
                self.match(MT22Parser.COMMA)
                self.state = 280
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def function_type(self):
            return self.getTypedRuleContext(MT22Parser.Function_typeContext,0)


        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def param_list(self):
            return self.getTypedRuleContext(MT22Parser.Param_listContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = MT22Parser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MT22Parser.ID)
            self.state = 286
            self.match(MT22Parser.COLON)
            self.state = 287
            self.match(MT22Parser.FUNCTION)
            self.state = 288
            self.function_type()
            self.state = 289
            self.match(MT22Parser.LP)
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.ID]:
                self.state = 290
                self.param_list()
                pass
            elif token in [MT22Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 294
            self.match(MT22Parser.RP)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 295
                self.match(MT22Parser.INHERIT)
                self.state = 296
                self.match(MT22Parser.ID)


            self.state = 299
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MT22Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 301
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.state = 302
                self.indexop()
                pass


            self.state = 305
            self.match(MT22Parser.ASSIGN)
            self.state = 306
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MT22Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MT22Parser.RETURN)
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.FALSE, MT22Parser.TRUE, MT22Parser.SUBOP, MT22Parser.LOGICNOT, MT22Parser.LP, MT22Parser.LCB, MT22Parser.ID, MT22Parser.INT_TYPE, MT22Parser.FLOAT_TYPE, MT22Parser.STRING_TYPE]:
                self.state = 309
                self.expr()
                pass
            elif token in [MT22Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def argument(self):
            return self.getTypedRuleContext(MT22Parser.ArgumentContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MT22Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(MT22Parser.ID)
            self.state = 314
            self.match(MT22Parser.LP)
            self.state = 315
            self.argument()
            self.state = 316
            self.match(MT22Parser.RP)
            self.state = 317
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def argument(self):
            return self.getTypedRuleContext(MT22Parser.ArgumentContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = MT22Parser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_argument)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.expr()
                self.state = 320
                self.match(MT22Parser.COMMA)
                self.state = 321
                self.argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MT22Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MT22Parser.IF)
            self.state = 328
            self.match(MT22Parser.LP)
            self.state = 329
            self.expr()
            self.state = 330
            self.match(MT22Parser.RP)

            self.state = 331
            self.stmt()
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 332
                self.match(MT22Parser.ELSE)
                self.state = 333
                self.stmt()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def assignment(self):
            return self.getTypedRuleContext(MT22Parser.AssignmentContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MT22Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MT22Parser.FOR)
            self.state = 338
            self.match(MT22Parser.LP)
            self.state = 339
            self.assignment()
            self.state = 340
            self.match(MT22Parser.COMMA)
            self.state = 341
            self.expr()
            self.state = 342
            self.match(MT22Parser.COMMA)
            self.state = 343
            self.expr()
            self.state = 344
            self.match(MT22Parser.RP)
            self.state = 345
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MT22Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(MT22Parser.WHILE)
            self.state = 348
            self.match(MT22Parser.LP)
            self.state = 349
            self.expr()
            self.state = 350
            self.match(MT22Parser.RP)
            self.state = 351
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = MT22Parser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(MT22Parser.DO)
            self.state = 354
            self.block_stmt()
            self.state = 355
            self.match(MT22Parser.WHILE)
            self.state = 356
            self.match(MT22Parser.LP)
            self.state = 357
            self.expr()
            self.state = 358
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MT22Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MT22Parser.LCB)
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.LCB, MT22Parser.ID]:
                self.state = 361
                self.stmtlist()
                pass
            elif token in [MT22Parser.RCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 365
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr2_sempred
        self._predicates[8] = self.expr3_sempred
        self._predicates[9] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




