``imogen.nml``
==============


This file contains two namelists called :nml:lst:`IMOGEN_RUN_LIST` and :nml:lst:`IMOGEN_ANLG_VALS_LIST`. Values from this section are only used if IMOGEN is enabled (i.e. :nml:mem:`JULES_SWITCHES::l_imogen` = TRUE).

A full IMOGEN experiment consists of three JULES runs, called spin_eq, spin_dyn and tran. Each run is started from the final dump of the previous run. The first two runs behave like an extended spin-up for the full transient run, and as such runs with IMOGEN must have no spin-up (i.e. :nml:mem:`JULES_SPINUP::max_spinup_cycles` = 0).

Since IMOGEN calculates the forcing for an entire year at once, an IMOGEN run must have a start time of 00:00:00 on the 1st of January for some year.

IMOGEN is currently restricted to run only on the HadCM3LC grid, i.e. there are 96 x 56 grid cells where each cell has size 3.75 degrees longitude by 2.5 degrees latitude with no Antarctica. This means that:

* :nml:mem:`JULES_INPUT_GRID::nx` = 96 and :nml:mem:`JULES_INPUT_GRID::ny` = 56.
* The file ``examples/imogen/data/jules/grid_info.nc`` should be used to set up the correct latitude, longitude and land fraction, as in the given example.

IMOGEN also uses its own I/O, so it expects IMOGEN specific files in a different format to JULES - this may change in the future. An example of setting up IMOGEN is provided in ``examples/imogen`` - this should be used as a guide if creating new files for IMOGEN.


``IMOGEN_RUN_LIST`` namelist members
------------------------------------

.. nml:namelist:: IMOGEN_RUN_LIST


.. nml:member:: co2_init_ppmv

   :type: real
   :default: 286.085

   Initial CO2 concentration (ppmv).


.. nml:member:: file_scen_emits

   :type: character
   :default: None

   If used, file containing CO2 emissions.

   This file is expected to be in a specific format - see the IMOGEN example.


.. nml:member:: file_non_co2_vals

   :type: character
   :default: None

   If used, file containing non-CO2 values.

   This file is expected to be in a specific format - see the IMOGEN example.


.. nml:member:: file_scen_co2_ppmv

   :type: character
   :default: None

   If used, file containing CO2 values.

   This file is expected to be in a specific format - see the IMOGEN example.


.. nml:member:: anlg

   :type: logical
   :default: T

   If TRUE, then use the GCM analogue model.


.. nml:member:: anom

   :type: logical
   :default: T

   If TRUE, then incorporate anomalies.


.. nml:member:: c_emissions

   :type: logical
   :default: T

   If TRUE, CO2 concentration is calculated.


.. nml:member:: include_co2

   :type: logical
   :default: T

   If TRUE, include adjustments to CO2 values.


.. nml:member:: include_non_co2

   :type: logical
   :default: T

   If TRUE, include adjustments to non-CO2 values.


.. nml:member:: land_feed

   :type: logical
   :default: F

   If TRUE, include land feedbacks on atmospheric CO2.


.. nml:member:: ocean_feed

   :type: logical
   :default: F

   If TRUE, include ocean feedbacks on atmospheric CO2.


.. nml:member:: nyr_emiss

   :type: integer
   :default: 241

   Number of years of emission data in file.


.. nml:member:: file_points_order

   :type: character
   :default: None

   File containing the mapping of IMOGEN global grid points onto IMOGEN land points (different from the JULES land points).


.. nml:member:: initialise_from_dump

   :type: logical
   :default: F

   Indicates how the IMOGEN prognostic variables will be initialised.

   TRUE
       Use a dump file (specified in :nml:mem:`dump_file` below) from a previous run with IMOGEN to initialise the IMOGEN prognostics.

   FALSE
       IMOGEN will handle the initialisation of its prognostics internally.


.. nml:member:: dump_file

   :type: character
   :default: None

   The name of the dump file to initialise from.

   Only used if :nml:mem:`initialise_from_dump` = TRUE.




``IMOGEN_ANLG_VALS_LIST`` namelist members
------------------------------------------

.. nml:namelist:: IMOGEN_ANLG_VALS_LIST


.. nml:member:: q2co2

   :type: real
   :default: 3.74

   Radiative forcing due to doubling CO2 (W m\ :sup:`-2`).


.. nml:member:: f_ocean

   :type: real
   :default: 0.711

   Fractional coverage of the ocean.


.. nml:member:: kappa_o

   :type: real
   :default: 383.8

   Ocean eddy diffusivity (W m\ :sup:`-1` K\ :sup:`-1`).


.. nml:member:: lambda_l

   :type: real
   :default: 0.52

   Inverse of climate sensitivity over land (W m\ :sup:`-2` K\ :sup:`-1`).


.. nml:member:: lambda_o

   :type: real
   :default: 1.75

   Inverse of climate sensitivity over ocean (W m\ :sup:`-2` K\ :sup:`-1`).


.. nml:member:: mu

   :type: real
   :default: 1.87

   Ratio of land to ocean temperature anomalies.


.. nml:member:: t_ocean_init

   :type: real
   :default: 289.28

   Initial ocean temperature (K).


.. nml:member:: nyr_non_co2

   :type: integer
   :default: 21

   Number of years for which non-co2 forcing is prescribed.


.. nml:member:: dir_patt

   :type: character
   :default: None

   Directory containing the patterns.

   Files in this directory are expected to be in a specific format - see the IMOGEN example.


.. nml:member:: dir_clim

   :type: character
   :default: None

   Directory containing initialising climatology.

   Files in this directory are expected to be in a specific format - see the IMOGEN example.


.. nml:member:: dir_anom

   :type: character
   :default: None

   Directory containing prescribed anomalies.

   Files in this directory are expected to be in a specific format - see the IMOGEN example.


.. nml:member:: file_non_co2

   :type: logical
   :default: F

   If true, then non-CO2 radiative forcings are contained within a file.

