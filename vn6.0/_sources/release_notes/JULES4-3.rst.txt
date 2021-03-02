JULES version 4.3 Release Notes
===============================


The JULES vn4.3 release consists of 36 tickets from 18 authors across 39 commits.

Full details of the tickets committed for JULES vn4.3 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v4.3+release>`_.


Science changes
---------------

*  Enhancements to the multi-layer snow scheme for GL7.0 (Global Land configuration, version 7.0)

   *  Addition of ET metamorphism
   *  Infiltration of rain water into the snow pack
   *  Albedo of snow and relationship to plant canopies

*  Generalisation of the crop scheme to work with trait-based plant physiology and BVOC emissions
*  Update to wetland scheme (see :nml:mem:`JULES_HYDROLOGY::l_wetland_unfrozen`)
*  River routing updates to allow RFM with standalone JULES to be run with non-regular lat-lon grids
*  New JULES-C configuration, the prototype configuration for UKESM1
*  Sea-ice changes for GC3.0 (Global Coupled configuration, version 3.0)


Technical changes
-----------------

*  Revamp of compilation procedure (see :doc:`/building-and-running/intro`)

   *  Changes to the environment variables used to specify a build
   *  Option to extract and mirror on local machine, preprocess and build on a remote machine (e.g. Met Office Cray XC40)
   *  Addition of "platform configurations", to reduce the number of environment variable definitions required to build on a known platform

*  Ancillary data (e.g. fractional coverage, soil data) is now saved to the dump file

   *  Each namelist in :doc:`/namelists/ancillaries.nml` gets a new flag, ``read_from_dump``, e.g. :nml:mem:`JULES_SOIL_PROPS::read_from_dump <JULES_SOIL_PROPS::read_from_dump>`
   *  A dump file can now be used initialise an entire run, including ancillaries (except for river routing, for technical reasons)

*  Many additional ``rose-stem`` tests
*  Replace testing for ice using ``sm_sat`` with logical arrays for soil and ice points
*  Restructuring of ``rose-stem`` tests to allow for site configurations with more divergence between sites

   *  As a result, JULES is now routinely tested on 3 platforms - Intel and gfortran compilers on Linux and CCE on the Cray

*  Remove the hijacking of the ice tile as a second urban tile when using two-tile urban schemes in the UM
*  Replacement of old include files with modules


Bugs fixed
----------

*  Fixed a long-standing off-by-one error in the instantaneous interpolation code (mode ``i`` - see :doc:`/input/temporal-interpolation`)
*  Several small fixes to soil carbon and vegetation code
*  Fix in river routing for bit-comparison with different processor decompositions in the UM
*  Fix for IMOGEN in parallel mode
*  Fix initialisation of some diagnostics
