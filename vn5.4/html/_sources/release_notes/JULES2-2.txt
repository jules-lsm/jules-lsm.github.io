JULES version 2.2 Release Notes
===============================

Along with fixes for known bugs, the changes made for version 2.2 mostly consist of several small additions to the science code. Changes to the control code have mostly been limited to bug-fixes.

* New options for treatment of urban tiles - inclusion of the Met Office Reading Urban Surface Exchange Scheme (MORUSES) and a simple two tile urban scheme.
* Effects of ozone damage on stomata from Stephen Sitch at the University of Leeds.
* New treatment of direct/diffuse radiation in the canopy from Lina Mercado at CEH.
* A new switch allows the competing vegetation portion of TRIFFID to be switched on and off independently of the rest of TRIFFID (i.e. it is now possible to use the RothC soil carbon without having changing vegetation fractions).

There have also been changes made to the way JULES is compiled, due to the re-integration with the Met Office Unified Model (UM). The UM uses preprocessor directives to compile different versions of routines depending on the selected science options. For compatibility with this system, JULES will now require a compiler with a preprocessor. This should not be noticed by the majority of users - most modern compilers include a preprocessor and the Makefile deals with setting up the appropriate preprocessor options.

Finally, JULES was added to the UM code repository as a mirror of the JULES repository at (UM version vn7.5, JULES vn2.2).
