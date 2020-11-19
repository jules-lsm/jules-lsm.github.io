JULES version 2.1 Release Notes
===============================

Versions 2.1.1 and 2.1.2 were released to fix major bugs found in v2.1 - they contain no new features.

Version 2.1 of JULES includes extensive modifications to the descriptions of the processes and to the control-level code (such as input and output). These are covered briefly below. Several bug fixes and minor changes to make the code more robust have also been applied. All files are now technically FORTRAN90 (.f90) although many are simply reformatted FORTRAN77 files in which continuation lines are now indicated by the use of the '&' character.


Process descriptions
--------------------

The main change is that a new multi-layer snow scheme is available. This scheme was developed by Richard Essery at the University of Edinburgh and co-workers. At the time of writing there is little scientific documentation of this development, but this will be made available as soon as possible. In brief, the older, simple scheme represents the snowpack as a single layer with prescribed properties such as density, whereas the new scheme has a variable number of layers according to the depth of snow present, and each layer has prognostic temperature, density, grain size, and solid and liquid water content. The new scheme reverts to the previous, simpler scheme if ``nsmax = 0`` or when the snowpack becomes very thin.

A four-pool soil carbon model based on the RothC model now replaces the single pool model when dynamic vegetation (TRIFFID) is selected.

There have been several major changes that most users will not notice or need be concerned about. These include a change in the linearization procedure that is used in the calculation of surface energy fluxes (described in the technical documentation). A standard interface is now used to calculate fluxes over land, sea and sea ice. Each surface tile now has an elevation relative to the gridbox mean.

These changes mean that, even with the new snow scheme switched off (``nsmax=0``), results from v2.1 will generally not be identical to those from v2.0.


Control-level code
------------------

The major change at v2.1 to the control-level code is that NetCDF output is now supported. Both diagnostic and restart files (dumps) can be in NetCDF format. There have been several changes to the run control file, partly to reflect new science but also in an attempt to organise the file better. These changes mean that run control and restart files from JULES v2.0 are not compatible with v2.1 (although they could be reformatted without too much difficulty).

Finally, since JULESvn1.0 the MOSES and JULES code bases have been evolving separately, but with JULES v2.1 these differences have been reconciled with the UM.
