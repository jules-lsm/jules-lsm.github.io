JULES version 3.4 Release Notes
===============================


n.b. A critical memory leak was found in JULES v3.4 that necessitated a new release, designated v3.4.1.


Changes to semantics of output
------------------------------

The output semantics used since JULES vn3.2 (i.e. state variables captured at the start of a timestep, flux variables captured at the end) were confusing some users. The semi-implicit scheme in JULES is designed so that the state and fluxes at the end of a timestep are consistent with each other, but under the previous semantics these were staggered by one timestep in output files.

All variables are now captured at the end of a timestep, so state and flux variables at a particular timestep in output files will be consistent with each other. A new option has been added to request the output of initial state, however very few users will have a use for this. It is still the case that the value in the ``time`` variable can be used to place snapshot data in time, and the values in ``time_bounds`` represent the interval over which a mean or accumulation applies.

More details can be found at :doc:`/output`.


Input and/or output of variables with multiple 'levels' dimensions has been improved
------------------------------------------------------------------------------------

In previous versions of JULES since vn3.1, variables could only be input or output with a single 'levels' dimension. In particular, this caused problems with variables in the new snow scheme, which have two 'levels' dimensions on top of the grid dimensions (tiles and snow levels). This led to compromises being made with the snow layer variables:

*   It was only possible to initialise the snow layer variables using a constant value, from a previous dump or using :nml:mem:`JULES_INITIAL::total_snow`
*   In output files, the snow layer variables were represented using a separate variable for each tile

This problem is solved in JULES vn3.4 - it is now possible to input and output variables with multiple 'levels' dimensions (there is not even a restriction to two 'levels' dimensions). This means that both compromises for snow layer variables detailed above have been removed.


Streamlined process for adding new variables for input and/or output
--------------------------------------------------------------------

Although fairly simple, the process for adding a new variable for input and/or output in JULES vn3.1 - vn3.3 required several edits to be made, and hence provided many opportunities to make mistakes. This process is simplified in JULES vn3.4 to require fewer edits. More details can be found at :ref:`implementing-new-variables-for-input-and-output`.


Other changes
---------------

Tidying of boundary layer code
    Some small changes have been made to tidy up some of the boundary layer code (i.e. routines in ``src/science/surface``) - this is mostly removing unused variables and tidying up subroutine argument lists.
    
OpenMP related changes
    Some `OpenMP <http://en.wikipedia.org/wiki/OpenMP>`_ directives have been added to certain loops. OpenMP is a form of shared-memory parallelism in which the user inserts directives (specially formatted code comments) providing information that allows the compiler to parallelise sections of code (in particular loops) without worrying about corrupting data. It is used in the UM, but is currently not enabled when compiling JULES standalone.


Bugs fixed
----------

*   Output (including dump files) not correctly generated for the last spin-up cycle when spin-up fails and :nml:mem:`JULES_SPINUP::terminate_on_spinup_fail` = TRUE
*   ``lw_net`` diagnostic does not include the contribution from the reflected incoming longwave if the emissivity is less than zero
