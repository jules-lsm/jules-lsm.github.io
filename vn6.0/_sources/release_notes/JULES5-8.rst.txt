JULES version 5.8 Release Notes
===============================


The JULES vn5.8 release consists of approximately 19 tickets from 9 authors, including work by many other people. This was an unusual release cycle as it was primarily aimed at technical developments in support of changes to the Unified Model system.

Full details of the tickets committed for JULES vn5.8 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.8+(Jun-20)>`_.

Ticket numbers are indicated below, e.g. #919.


General/Technical changes
-------------------------

 *  The surf_couple* routines have been restructured to separate land and sea/sea-ice parts - making the code clearer and facilitating the implementation of CABLE into the JULES framework. (#919)
 *  Fields passed by argument rather than via USE statements. (#1022, #1024, #1025, #1028, #1029, #1030, #1037, #1038, #1043)
 *  Added :nml:mem:`JULES_OUTPUT::dump_period_unit` to allow the units of :nml:mem:`JULES_OUTPUT::dump_period` to be years or seconds. (#1021)
 *  Removal of the old qsat routines. (#1015)
 *  Access the gather_field and scatter_field subroutines via modules. (#1051)
 *  The url fields in HEAD metadata now have the "latest" tag, allowing both the UM and JULES to have the same url field. (#1017)

    
Bugs fixed
----------

 *  Bug fix to allow runs with soil tiling that do not rely on broadcastng values. (#1048)
 *  Bug fix to prevent array bounds error with river routing, and other minor changes to river routing. (#1049)
 *  Fix to allow compilation with pgfortran as part of UM-JULES. (#1010)


Changes to testing
------------------

 *  Tidied some rose stem apps. (#1050)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1040)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
