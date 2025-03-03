JULES version 5.6 Release Notes
===============================


The JULES vn5.6 release consists of approximately 14 tickets from 11 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.6 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.6+release>`_.

Ticket numbers are indicated below, e.g. #864.

Science changes
---------------

 *  Added the Farquhar model of photosynthesis for C\ :sub:`3` plants - see :nml:mem:`JULES_VEGETATION::photo_model`. (#864)
 *  Added the COARE algorithm for drag over sea, including functionality to reduce the drag at very high wind speeds - only affects runs with the UM. (#848)


General/Technical changes
-------------------------

 *  UM and JULES metadata consolidated for namelists :nml:lst:`JULES_RADIATION` and :nml:lst:`JULES_VEGETATION`. (#822)
 *  Preparatory work towards including irrigation demand in the UM. (#811)
 *  Allowed the dimension names :nml:mem:`JULES_INPUT_GRID::sclayer_dim_name`, :nml:mem:`JULES_INPUT_GRID::tracer_dim_name`, :nml:mem:`JULES_INPUT_GRID::bl_level_dim_name` to be read from namelist :nml:lst:`JULES_INPUT_GRID`. (#937)
 *  Improved error handling in subroutines ``set_levels_list`` and ``set_pseudo_list``. (#935)
 *  Updated the UM STASH diagnostics routines to use a modularised version of copydiag. (#938)
 *  Added further OpenMP optimisations for GA8 model routines. (#941)
 *  Additions of ``#if defined(LFRIC)`` to allow coupling of ``surf_couple_extra`` to LFRic. (#943)
 *  Altered OMP directives to remove data race conditions. (#952)
 *  Removed the requirement to have some environment variables that are used in build configs defined/initiliased at the app/suite level. (#939)

    
Changes to testing
------------------
 *  Updated rose stem testing to include JULES-ES-1.0 configuration. (#915)
 *  JULES can be built at the Bureau of Meteorology (Australia). (#930)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#950)

Note that compilation of the User Guide now requires Sphinx 1.4 or higher.

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
