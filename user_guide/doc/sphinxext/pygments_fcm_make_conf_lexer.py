# -*- coding: utf-8 -*-
"""
    FCM make configuration file lexer for Pygments
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class FCMMakeConfLexer(RegexLexer):
    """Pygments lexer for FCM make configuration files"""
    name = 'FCM make'
    aliases = ['fcm_make']
    filenames = ['*.cfg']

    tokens = {
        'root': [
            # Consume any runs of whitespace as normal text
            (r'\s+', Text),
            
            # Anything from # to the end of a line is a comment
            (r'#.*$', Comment.Single),
            
            # Anything starting with a $ is a variable
            # Variables can optionally be appended with {?} to indicate that they can be set as environment variables
            (r'(\$[\w-]+)(\{\?\})?', bygroups(Name.Variable, Punctuation)),
            
            # Anything consisting of only alphanumeric characters (plus .) is rendered as a namespace
            (r'[\w\-_\.]+', Keyword.Namespace),
            
            # Anything between {} is rendered as a tag
            (r'(\{)([\w\-_\.]+)(\})', bygroups(Punctuation, Name.Tag, Punctuation)),
            
            # Anything between [] is rendered as a class
            (r'(\[)([\w\-_\.\/]+)(\])', bygroups(Punctuation, Name.Class, Punctuation)),
            
            # Use a catch-all for anything on the left of an equals sign not already covered
            (r'[\w\-\.\{\}\[\]/\?]+(?=\s*=)', Name.Property),
            
            # = is an operator that puts us into a 'value' state
            (r'=', Operator, 'value'),
        ],
        
        'value' : [
            # Spans of spaces and tabs are treated as normal text
            (r'[ \t]+', Text),
            
            # Whitespace followed by "\" followed by a newline is treated as text, special punctuation then text
            (r'([ \t]*)(\\)([ \t]*\n)', bygroups(Text, Punctuation, Text)),
            
            # Anything starting with a $ is an embedded variable
            (r'\$[\w-]+', Name.Variable),
            
            # Anything not whitespace, "$" or  "\" is treated as a string
            (r'[^\s\\\$]+', String.Double),
            
            # A newline with no \ is rendered as text, but kicks us back into root
            (r'\n', Text, '#pop'),
        ]
    }


def setup(app):
    """Makes the lexer known to Pygments through Sphinx"""
    app.add_lexer('fcm_make', FCMMakeConfLexer)