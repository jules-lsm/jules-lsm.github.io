JULES version 4.2 Release Notes
===============================


JULES version 4.2 is the first release where all development has taken place in the Met Office collaboration repository. On the whole, this has been a success, with module leaders beginning to use the Trac system to track and approve developments in their areas.

The JULES vn4.2 release consists of 35 tickets from 13 authors across 39 commits.


Science changes
---------------

*  TRIP and RFM river routing (see :doc:`/namelists/jules_rivers.nml`)
*  Incorporation of widely used fire risk indices (see :doc:`/namelists/fire.nml`)
*  New soil thermal conductivity model that is more appropriate for organic soils (see :nml:mem:`JULES_SOIL::soilhc_method`)
*  Addition of "bedrock" column beneath the soil column, in which only thermal diffusion occurs (see :nml:mem:`JULES_SOIL::l_bedrock`)
*  New canopy radiation scheme in which the nitrogen follows an exponential decay (see :nml:mem:`JULES_VEGETATION::can_rad_mod`)
*  Updates to trait PFTs (see :nml:mem:`JULES_VEGETATION::l_trait_phys`) to ensure that the dynamic and equilibrium solutions for vegetation fraction are equivalent
*  Crop model now conserves carbon


Technical changes
-----------------

*  Added flag to force the model grid to be 1D (see :nml:mem:`JULES_MODEL_GRID::force_1d_grid`)
*  Several new diagnostics added (see :doc:`/output-variables`)
*  New rose-stem regression tests added
*  All rose-stem tests migrated to use NetCDF and ``nccmp``
*  Retirement of several include files
*  Removal of logging namelist - output location should now be controlled using pipes (i.e. ``1>/my/file 2>&1``) or features of your ``mpiexec`` or ``mpirun`` program
*  Additional consolidation of shared (i.e. standalone and UM) control and initialisation routines
*  Optimisation of ``sf_stom`` and ``leaf_limits``, resulting in ~20% speedup for :nml:mem:`JULES_VEGETATION::can_rad_mod` = 4


Bugs fixed
----------

*  Bug in calculation of ``n_leaf`` and ``n_stem`` in ``sf_stom``
*  Memory overwriting bug in TRIFFID
*  Differing error message lengths in UM
*  ``hcons`` now passed to the snow scheme instead of ``hcon(:,0)``
*  Several bug fixes for IMOGEN
*  Patch to enable collective access for parallel NetCDF in NetCDF 4.2 onwards
*  ``soil_hyd`` now declares ``ksz`` correctly (i.e. ``ksz(npnts,0:nshyd)`` instead of ``ksz(npnts,nshyd)``) - this only affects runs where the soil properties vary for each layer
*  Correction to the accumulation of ``g_leaf_phen`` in-between calls to TRIFFID


Full details of the tickets committed for JULES vn4.2 can be found on the `collaboration repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v4.2+release>`_.
