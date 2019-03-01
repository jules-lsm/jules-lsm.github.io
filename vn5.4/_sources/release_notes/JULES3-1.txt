JULES version 3.1 Release Notes
===============================


JULES version 3.1 sees little change to the science of JULES, but contains several major developments intended to make development easier going forward.


Restructuring of the code
-------------------------

The directory structure of the JULES code has been changed to be more logical and allow for a cleaner separation between control, initialisation, I/O and science code. This includes the introduction of directories containing UM-specific code for initialisation in the UM. This was done as part of the work to completely remove (MOSES and) JULES code from the UM code repository - it now sits in its own repository.


New I/O framework
-----------------

The input and output code has been completely revamped in order to modularise and simplify the code. It allows for data to be input on any timestep and interpolated down to the model timestep. Support for outputting of means and accumulations remains. NetCDF is now the only supported binary format (although it should be relatively simple to write drivers for other output formats if desired), and ASCII files are allowed for data at a single location only. Support for the GrADS flat binary format has been dropped, although the NetCDF output should be usable with GrADS with very little work.


User Interface changes
----------------------

The user interface also sees significant changes. The monolithic .jin run control file has been replaced by several smaller files containing Fortran namelists for input of options and parameters. This is more consistent with the UM, and offers the opportunity to adapt UM tools to provide a GUI for running JULES in the future.


Other changes
-------------

There are several not-insignificant changes to the science code:

* Structures are now used for dimensioning variables - this allows for more flexibility of grids than the old system of row_length/rows and halos.
* Move to a new implicit solver - ``sf_impl2`` is now used rather than ``sf_impl`` for consistency with the UM. However, the way the implicit coupling is set up means it operates in a similar way to the old scheme.
* A change in the way fresh snow is handled in the multi-layer snow scheme - the density of fresh snow is now prescribed by a new variable (``rho_snow_fresh``). Suggested by Cécile Ménard and implemented by Doug Clark.
* Bug fix from Doug Clark for the multi-layer snow scheme that fixes problems with the model oscillating between 0 and 1 snow layers every timestep, preventing snow melt.
* Changes to the sea-ice surface exchange when operating as part of the UM. This will not affect the majority of users.
* Slight changes to the coupling between the explicit and implicit schemes. The vast majority of users will not need to worry about this.
