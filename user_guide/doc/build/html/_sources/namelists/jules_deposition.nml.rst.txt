``jules_deposition.nml``
=============================


This file contains options and parameters for modelling of dry deposition of atmospheric trace constituents. It contains a variable number of namelists depending on the required model configuration. The namelist :nml:lst:`JULES_DEPOSITION` is always required, and one or more instances of the namelist :nml:lst:`JULES_DEPOSITION_SPECIES` is required if dry deposition has been selected.

.. warning::
   Atmospheric deposition in JULES is still in development and is far from fully functional in this version - the code is included to allow further development. Users should not try to activate the deposition code: leave :nml:mem:`JULES_DEPOSITION::l_deposition` as FALSE.



``JULES_DEPOSITION`` namelist members
------------------------------------------

.. nml:namelist:: JULES_DEPOSITION


.. nml:member:: l_deposition

   :type: logical
   :default: FALSE

   Switch to activate deposition code in JULES.
   
   TRUE
      Model deposition in JULES.

   FALSE
      Do not model deposition in JULES.


.. nml:group:: Only used if :nml:mem:`l_deposition` = TRUE.


   .. nml:member:: dry_dep_model

      :type: integer
      :permitted: 1
      :default: none

      Choice for model of dry deposition.

      Possible values are:

      1. | Parameterisation based on that found in UKCA (but now implemented in JULES).


   .. nml:member:: l_deposition_flux

      :type: logical
      :default: FALSE

      Switch for calculation of deposition fluxes as opposed to deposition velocities.

      TRUE
         Calculate deposition fluxes. This requires that the concentrations of atmopsheric tracer species are provided as prescribed data (see :ref:`supported-prescribed-variables`).

      FALSE
         Calculate deposition velocities.


.. nml:group:: Only used if :nml:mem:`l_deposition` = TRUE and :nml:mem:`dry_dep_model` = 1 (UKCA).


   .. nml:member:: ndry_dep_species

      :type: integer
      :permitted: >= 1
      :default: none

      Number of species for which dry deposition is calculated.


   .. nml:member:: l_ukca_ddep_lev1

      :type: logical
      :default: FALSE

      Switch controlling which atmospheric levels are used for dry deposition.

      TRUE
         Deposition occurs only from the lowest atmospheric level.

      FALSE
         Deposition occurs from all levels within the atmospheric boundary layer.


   .. nml:member:: tundra_s_limit

      :type: real
      :default: none

      Latitude of southern limit of tundra (degrees). This is used to alter the calculation of deposition of certain species in the tundra region (actually for all points north of this limit). Only used if the list of species (see :nml:mem:`JULES_DEPOSITION_SPECIES::dep_species_name_io`) includes one or more of 'CO', 'NO2', 'O3', 'PAN', 'PPAN', 'MPAN' or 'ONITU'. 


   .. nml:member:: dzl_const

      :type: real
      :default: none

      Constant value for separation of boundary layer levels (m). All layer thicknesses are set to this value. This is used as a simple way to prescribe the layer thicknesses in standalone mode. This value can be overriden by prescribed data - see :nml:lst:`JULES_PRESCRIBED`. This can be considered as the representative depth for tracer concentration and the depth over which the deposition flux is removed.


Notes on the ``JULES_DEPOSITION`` namelist
------------------------------------------

The height of the atmospheric boundary layer is required and is set to a default constant value of 1000 m. This value can be overridden via the namelist variable :nml:mem:`JULES_DRIVE::bl_height`, or can be prescribed (i.e. allowed to vary in time and/or space) by providing ``bl_height`` as prescribed data (see :ref:`supported-prescribed-variables`).

The number of model levels in the boundary layer is required and is set to a default balues of 1. This can be overridden via the namelist variable :nml:mem:`JULES_NLSIZES::bl_levels`. The number of levels is only used to communicate with the atmospheric model (e.g. UKCA).

The separation of the model levels in the boundary layer is required and is set to a constant value via :nml:mem:`dzl_const`. The separation can be prescribed (i.e. allowed to vary in time and/or space) by providing ``level_separation`` as prescribed data (see :ref:`supported-prescribed-variables`). This can be considered as the representative depth for tracer concentration and the depth over which the deposition flux is removed.

If deposition fluxes (rather than deposition velocities) are to be calculated (see :nml:mem:`l_deposition_flux`), the concentrations of atmospheric tracer species need to be prescribed (see ``tracer_field`` in :ref:`supported-prescribed-variables`).



``JULES_DEPOSITION_SPECIES`` namelist members
---------------------------------------------

.. nml:namelist:: JULES_DEPOSITION_SPECIES

This namelist should occur :nml:mem:`JULES_DEPOSITION::ndry_dep_species` times, with each occurence containing parameters for an atmospheric tracer species that is to be considered in dry deposition.

.. nml:member:: dep_species_name_io

   :type: character
   :default: none

   Name of an atmospheric tracer species to be included in deposition modelling.


.. nml:member:: diffusion_coeff_io

   :type: real
   :default: none

   Diffusion coefficient (m\ :sup:`-2` s\ :sup:`-1`).


.. nml:member:: rsurf_std_io

   :type: real(ntype)
   :default: none

   Standard value of surface resistance for each surface type (s m\ :sup:`-1`).


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``NO2``, ``O3``, ``PAN``, ``PPAN``, ``MPAN`` or ``ONITU``. Values provided for other species will be ignored.

   .. nml:member:: diffusion_corr_io

      :type: real
      :default: none

      Diffusion correction factor for stomatal resistance, accounting for the different diffusivities of water and other species (dimensionless).


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``CO``, ``NO2``, ``O3``, ``PAN``, ``PPAN``, ``MPAN`` or ``ONITU``. Values provided for other species will be ignored.

   .. nml:member:: r_tundra_io

      :type: real
      :default: none

      Surface resistance used in tundra region (s m\ :sup:`-1`).


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``CH4``.


   .. nml:member:: ch4_scaling_io

      :type: real
      :default: none

      Scaling applied to methane soil uptake (dimensionless). (Originally this was used to match the value from the IPCC Third Assessment Report.)


   .. nml:member:: ch4dd_tundra_io

      :type: real(4)
      :default: none

      Coefficients of cubic polynomial relating methane loss for tundra to temperature. Flux is in units of ug (CH\ :sub:`4`) m\ :sup:`-2` s\ :sup:`-1`.


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``H2``.


   .. nml:member:: h2dd_c_io

      :type: real(ntype)
      :default: none

      Constant in quadratic function relating hydrogen deposition to soil moisture (s m\ :sup:`-1`).


   .. nml:member:: h2dd_m_io

      :type: real(ntype)
      :default: none

      Coefficient of first order term in quadratic function relating hydrogen deposition to soil moisture (s m\ :sup:`-1`).


   .. nml:member:: h2dd_q_io

      :type: real(ntype)
      :default: none

      Coefficient of second order term in quadratic function relating hydrogen deposition to soil moisture (s m\ :sup:`-1`).


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``HNO3``, ``HONO2`` or ``ISON``.

   .. nml:member:: dd_ice_coeff

      :type: real(3)
      :default: none

      Coefficients in quadratic function relating dry deposition over ice to temperature.


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``O3``.


   .. nml:member:: cuticle_o3_io

      :type: real
      :default: none

      Constant for calculation of cuticular resistance for ozone (s m\ :sup:`-1`).


   .. nml:member:: r_wet_soil_o3_io

      :type: real
      :default: none

      Wet soil surface resistance for ozone (s m\ :sup:`-1`).



