# -*- coding: utf-8 -*-
"""
    Fortran namelist lexer for Pygments
"""

from pygments.lexer import RegexLexer
from pygments.token import Text, Comment, Operator, Name, String, \
    Number, Punctuation


class FortranNmlLexer(RegexLexer):
    """Pygments lexer for Fortran Namelists"""
    name = 'Fortran Namelists'
    aliases = ['nml']
    filenames = ['*.nml']

    tokens = {
        'root': [
            # Consume any runs of whitespace as normal text
            (r'\s+', Text),
            
            # Anything from ! or # to the end of a line is rendered as a comment
            (r'[#!].*$', Comment.Single),
            
            # Check for constants next, as some things that might be interpreted as variable name might be in here (i.e. T/F for logicals)
            # String literals
            (r'\'[^\']*\'', String.Single),
            (r'"[^"]*"', String.Double),
            # Logicals
            # .TRUE./.FALSE. form
            (r'(?i)\.(true|false)\.', String.Symbol),
            # T/F form (i.e. a T or an F followed by any non-alpha-numeric character
            (r'(?i)[tf](?=[^\w])', String.Symbol),
            # Real numbers, with optional sign, optional integer part and optional exponent
            (r'[+-]?\d*\.\d+([eE][+-]?\d+)?', Number.Float),
            # Integers with optional sign
            (r'[+-]?\d+', Number.Integer),
            
            # Match a namelist identifier as a namespace
            (r'&\w+', Name.Namespace),
            
            # Also match namelist terminators as namespace objects so they match the namespace identifiers
            (r'/', Name.Namespace),
            
            # Any run of alphanumeric characters not in quotes is treated as a variable name
            (r'[a-zA-Z]\w*', Name.Variable),
            
            # = is the assignment operator, % is the "structure member" operator and : is the range operator
            (r'[\*=%:]', Operator),
            
            # Significant punctuation
            (r'[\(\),]', Punctuation),
        ]
    }


def setup(app):
    """Makes the lexer known to Pygments through Sphinx"""
    app.add_lexer('nml', FortranNmlLexer)