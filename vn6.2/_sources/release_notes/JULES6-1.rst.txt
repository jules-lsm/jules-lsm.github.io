JULES version 6.1 Release Notes
===============================


The JULES vn6.1 release consists of approximately 21 tickets from 13 authors, including work by many other people.

Full details of the tickets committed for JULES vn6.1 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v6.1+(Jun-21)>`_.

Ticket numbers are indicated below, e.g. #949.


General/Technical changes
-------------------------

 *  Added the technical infrastructure to activate irrigation in the UM (atmosphere model). (#949)
 *  Irrigation timestep is controlled by :nml:mem:`JULES_IRRIG::nstep_irrig`. (#1146)
 *  Minor restructuring of water resources code. (#1122)
 *  The handling of the MORUSES roughness length in the surface exchange has been made more robust and the functionality for calculating urban morphology from the empirical relationships of Bohnenstengel et al. 2011 has also been fixed. (#1106)
 *  Forcing and lake variables bundled into TYPEs. (#1136, 1135)
 *  Conversion of initialisation and io/dump include files to modules, including some reorganisation required for River.Exe (standalone rivers-only executable). (#1158)
 *  CABLE lai_pft and canht_pft initialised from new namelist :nml:lst:`CABLE_PFTPARM`. (#1119)
 *  Miscellaneous small corrections to code and documentation. (#1143)
 *  Added new 1.5m visibility diagnostics to sfdiags (only for UM). (#1134)
 *  Improved performance in RA3 configurations. (#1113)
 *  Added further platform files for JASMIN. (#1145)

    
Bugs fixed
----------

 *  Corrected previously uninitialised PFT parameters when coupled to the UM. (#1137)
 *  Minor bug fixes and metadata updates for IMOGEN. (#1126)
 *  Bug fixes for seed_rain. (#1129, 1166)
 *  Prevent memory issues when using the INFERNO fire scheme in UM configurations. (#1149)
 *  Bug fix to add Rose metadata and upgrade macro for :nml:lst:`JULES_VEGETATION_PROPS` namelist. (#1141)

    
Changes to testing
------------------

 *  Reflected changes in the JASMIN environment (parallel netcdf and SLURM scheduler) in the settings for rose stem. (#1120)


Documentation updates
---------------------

 *  Revised presentation of the available diagnostics. (#1139)
 *  Updates associated with many of the above changes, and release notes. (#1157)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

