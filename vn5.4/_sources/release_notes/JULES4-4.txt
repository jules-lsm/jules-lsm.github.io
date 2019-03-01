JULES version 4.4 Release Notes
===============================


The JULES vn4.4 release consists of 31 tickets from 17 authors across 35 commits. Two further tickets were removed from the release due to issues.

Full details of the tickets committed for JULES vn4.4 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v4.4+release>`_.

Science changes
---------------

 * Add an option to set tile elevations to have absolute values above sea-level - see :nml:mem:`JULES_SURF_HGT::l_elev_absolute_height`
 * Adjustment to downward longwave radiation for elevated tiles - see :nml:mem:`JULES_SURFACE::l_elev_lw_down`
 * Nitrogen cycling - improved process representation for UKESM
 * Use bare soil momentum roughness length, if supplied as an ancillary field
 * Irrigation water taken first from deep soil layer then the river (code from the JULES Impact Model)
 * Improvements to rivers_type='trip','rfm': storage in dump and partial parallelisation
 * Alternative forms for methane emissions from wetlands, using different substrates
 * Allow landuse with variable number of PFTs
 * BVOC emissions allowed with trait physiology
 * Change multi-layer snow indices of first layer

Technical changes
-----------------

 * JULES fcm-make configs updated to be incompatible with FCM 2015.07.0 and later
 * Rose-stem support for alternative Rose, Cylc and FCM versions
 * Addition of OpenMP directives to some JULES code.
 * Code coverage metrics for rose-stem suite
 * Preparation for JULES memory duplication
 * Removed snow_grnd_gb from closures benchmark test


Bugs fixed
----------

 * Remove factor of 0.5 from snow albedo temperature dependence
 * Fix a bug in the Nitrogen scheme for the implicit update of soil respiration when the soil C pool is exhausted.
 * Fix drift in vegetation fractions
 * Scaling bug in Taux
 * Bug fix for irrig_water diagnostic - between crop seasons this is now zero
 * Met Office VM: fix for update-jules-scripts file for JULES 4.3
 * JULES namelist broadcasts are out of sync
