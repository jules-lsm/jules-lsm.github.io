JULES version 8.0 Release Notes
===============================

The JULES vn8.0 release consists of approximately 10 tickets from 7 authors, including work by many other people.

Full details of the tickets committed for JULES vn8.0 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v8.0+(Oct-25)>`_.

Ticket numbers are indicated below, e.g. #1088.


Science changes
---------------

 *  Demands for water for human uses can be met from local water sources (surface and ground waters) - see :nml:lst:`JULES_WATER_RESOURCES`. (#1088)
 *  Added option for urban anthropogenic heat flux with diurnal and latitude-dependent annual cycles following the scheme of Flanner (2009) - see :nml:mem:`JULES_SURFACE::anthrop_heat_option`. (#1371)


General/Technical changes
-------------------------

 *  River storage can be initialised from a 12-month climatological ancillary file (motivated by the needs of LFRic coupled modelling) - see :nml:lst:`JULES_RIVERS_PROPS`. (#1392)
 *  The river number ancillary (used for coupling to the ocean model) has been updated with one consistent with the river routing ancillary. They now pass the rivers ancillary checking routine, hence `l_ignore_ancil_rivers_check` has been removed. (#1460)
 *  Code for CABLE removed for licensing purposes. The CABLE code will only reside within its own repository and will be included at compilation time in future releases. (#1633)

    
Bugs fixed
----------

 *  An upgrade macro that was missied from the previous release has been added. (#1619)
 *  Removed default diagnostic flags used for LFRic. (#1627)


Changes to testing
------------------

 *  Cylc7 deprecated for rose-stem testing. (#1564)
 *  Modified usage of umdp3_fixer.py. (#1635)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1638)


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

