Introduction to Fortran namelists
=================================

Each namelist file read by JULES contains one or more Fortran namelists. Any content that does not form part of a namelist group is not read or interpreted in any way by Fortran, and so can be used as comments.

A Fortran namelist combines several related variables (referred to as 'members' of the namelist) together, which are then read with a single statement. The members can appear in any order. A Fortran namelist takes the following format::

    &GROUP_NAME
      char_variable = "a char variable",
      logical_variable = T,
      nitems = 5,
      list_variable = 0.1  0.2  0.3  0.4  0.5
    /

The namelist definition is anything that appears between ``&GROUP_NAME`` and ``/``. Values are then declared for the namelist members using the form ``member_name = member_value``. The member names are determined by the definition of the namelist in the Fortran source code. The member names for the JULES namelists are documented in the following sections.

Values for character variables must be enclosed in either single(' ') or double (" ") quotes. Logical values can be specified using ``.TRUE.``/``.FALSE.`` or with the shorthand ``T``/``F``. Integer and real values are specified simply by giving the value. The vast majority of compilers (all tested compilers) allow lists to be specified either horizontally or vertically, depending on preference. The following definitions are
identical::

    list_variable = 0.1  0.2  0.3  0.4  0.5
    
    list_variable(1) = 0.1
    list_variable(2) = 0.2
    list_variable(3) = 0.3
    list_variable(4) = 0.4
    list_variable(5) = 0.5
    
Namelists are an ideal input mechanism for programs like JULES that have a large number of inputs, most of which users never change from the default. Since each variable can have a sensible default value specified in the code, the user need only specify variables they wish to change from the default. This can substantially reduce the size and complexity of the namelist files. For example, suppose that in the above
example the namelist member ``logical_variable`` has a default value of ``.TRUE.``. Then the following namelist specification is equivalent to that above::

    &GROUP_NAME
      char_variable = "a char variable",
      nitems = 5,
      list_variable = 0.1  0.2  0.3  0.4  0.5
    /
