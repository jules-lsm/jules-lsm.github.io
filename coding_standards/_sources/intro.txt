Introduction
============


This document specifies the software standards and coding styles to be used when writing new code files for JULES. When making extensive changes to an existing file, a rewrite should be done to ensure that the routine meets the JULES standard and style.


Why have standards?
-------------------

This document is intended for new as well as experienced programmers, so a few words about why there is a need for software standards and styles may be in order.

Coding standards specify a standard working practice for a project with the aim of both reducing portability and maintainability problems and improving the readability of code. This process makes code development and reviewing easier for all developers involved in the project. Remember that software should be written for people and not just for computers! As long as the syntax rules of the programming language (e.g. Fortran 90) are followed, the computer does not care how the code is written. You could use archaic language structures, add no comments, leave no spaces etc. However, another programmer trying to use, maintain or alter the code will have trouble working out what the code does and how it does it. A little extra effort whilst writing the code can greatly simplify the task of this other programmer (which might be the original author a year or so after writing the code, when details of it are bound to have been forgotten). In addition, following these standards may well help you to write better, more efficient, programs containing fewer bugs.


Units
-----

All routines and documentation must be written using SI units. Standard SI prefixes may be used. Where relevant, the units used must be clearly stated in both code and documentation.