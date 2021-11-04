JULES version 4.1 Release Notes
===============================


Irrigation demand
----------------- 

When enabled, irrigation demand adds water to the soil moisture up to the critical point, meaning that vegetation does not experience water stress. At the moment the amount of water added is not limited, although it will be limited in a future version.

There are two schemes that can be used to determine when to irrigate: 
 
1. This method calculates optimum planting dates for non-rice crops using averages from driving data and so requires at least one year of driving data. It was written by Nic Gedney and is based on the crop calendar from Doell & Siebert (2002).
2. Uses development index (dvi) across all tiles from JULES-crop (written by Rutger Dankers). Maximum dvi must exceed -1 (indicates sowing) for irrigation to occur. 

See the documentation for :nml:mem:`JULES_IRRIG::l_irrig_dmd` for more details.


Carbon cycle developments
-------------------------

A number of carbon cycle developments are included in this release:

#.  Changes to the competition code to allow for flexible, height-based competition in TRIFFID. See :nml:mem:`JULES_VEGETATION::l_ht_compete`.
#.  Trait-based plant physiology that allows the plant physiology to be defined by parameters that are more readily definable from observations. See :nml:mem:`JULES_VEGETATION::l_trait_phys`.
#.  Code for simulating land-use change (e.g. forest clearance) including product pools (previously implemented in HadGEM2-ES). See :nml:mem:`JULES_VEGETATION::l_landuse`.
#.  Time-varying agricultural fraction now officially supported. Time-varying CO2 concentration is also supported with some caveats. See :ref:`the list of supported prescribed data variables <supported-prescribed-variables>`.
#.  Switch to enable/disable the adjustment of fractions during initialisation. See :nml:mem:`JULES_VEGETATION::l_recon`.


Maximum and minimum output types
--------------------------------

It is now possible to output the maximum and minimum value over the output period of any variable, e.g. monthly maximum.

See :nml:mem:`JULES_OUTPUT_PROFILE::output_type` for more information.


Changes to the coupling routines
--------------------------------

The routines that couple the JULES science to the UM and to the standalone wrapper have changed - see ``src/control/standalone/control.F90``.

This is mainly in order to simplify the coupling with the UM and to facilitate upcoming developments.


Bugs and other changes
----------------------

*  It is now possible to run with a fixed 365-day calender (i.e. no leap years) using the :nml:mem:`JULES_TIME::l_leap` flag.
*  Corrected temperature limitation on soil respiration to be consistent with HadGEM2-ES.
*  Minor tweaks to the crop model.
*  Improvements to the BVOC emissions model, including linking with UKCA via the UM for coupled studies.
*  Changes to introduce the COARE algorithm for surface exchange over the ocean.
*  Improved error messages for I/O errors (e.g. namelist reading)
*  Fixed a bug where the start and end time of data are not initialised correctly when using the daily disaggregator.
*  Fixed a bug in tilepts caused by the use of short-circuiting logic that is not supported by some compilers.
