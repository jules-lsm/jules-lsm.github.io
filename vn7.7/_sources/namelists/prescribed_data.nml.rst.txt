``prescribed_data.nml``
=======================


This file contains a variable number of namelists that are used to prescribe time-varying input data that is not meteorological forcing. The namelist :nml:lst:`JULES_PRESCRIBED` should occur only once at the top of the file. The value of :nml:mem:`JULES_PRESCRIBED::n_datasets` in :nml:lst:`JULES_PRESCRIBED` then determines how many times the namelist :nml:lst:`JULES_PRESCRIBED_DATASET` should occur.


``JULES_PRESCRIBED`` namelist members
-------------------------------------

.. nml:namelist:: JULES_PRESCRIBED


.. nml:member:: n_datasets

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of datasets that will be specified using instances of the :nml:lst:`JULES_PRESCRIBED_DATASET` namelist.



``JULES_PRESCRIBED_DATASET`` namelist members
---------------------------------------------

.. nml:namelist:: JULES_PRESCRIBED_DATASET

This namelist should occur :nml:mem:`JULES_PRESCRIBED::n_datasets` times. Each occurrence of this namelist contains information about a single dataset (i.e. set of related files).


.. nml:group:: Members used to specify the start, end and period of the data

   .. nml:member:: data_start
   .. nml:member:: data_end
      
      :type: character
      :default: None
   
      The times of the start of the first timestep of data and the end of the last timestep of data.
   
      Each run of JULES (configured in :doc:`timesteps.nml`) can use part or all of the specified data. However, there must be data for all times between run start and run end (determined by :nml:mem:`JULES_TIME::main_run_start`, :nml:mem:`JULES_TIME::main_run_end`, :nml:mem:`JULES_SPINUP::spinup_start` and :nml:mem:`JULES_SPINUP::spinup_end`).
    
      The times must be given in the format::
   
           "yyyy-mm-dd hh:mm:ss"
   
   
   .. nml:member:: data_period
   
      :type: integer
      :permitted: -2, -1 or > 0
      :default: None
   
      The period, in seconds, of the data.
   
      Special cases:
   
      | **-1:** Monthly data
      | **-2:** Yearly data
   
   
   .. nml:member:: is_climatology
   
      :type: logical
      :default: F
   
      Indicates whether the data is to be used as a climatology (use the same data for every year).
   
      TRUE
          Interpret the data as a climatology. :nml:mem:`data_start` and :nml:mem:`data_end` must be such that exactly one year of data is specified.
   
      FALSE
          Do not interpret the data as a climatology.


.. nml:group:: Members used to specify the files containing the data

   .. nml:member:: read_list
   
      :type: logical
      :default: F
   
      Switch controlling how data file names are determined for a given time.
   
      TRUE
          Use a list of data file names with times of first data.
   
      FALSE
          Use a single data file for all times or a template describing the names of the data files.
   
   
   .. nml:member:: nfiles
   
      :type: integer
      :permitted: >= 0
      :default: 0
   
      Only used if :nml:mem:`read_list` = TRUE.
   
      The number of data files to read name and time of first data for.
   
   
   .. nml:member:: file
   
      :type: character
      :default: None
   
      If :nml:mem:`read_list` = TRUE, this is the file to read the list of data file names and times from. Each line should be of the form::
   
          '/data/file', 'yyyy-mm-dd hh:mm:ss'
   
      In this case data file names may contain variable name templating only, with the proviso that either no file names use variable name templating or all file names do. The files must appear in chronological order.
   
      If :nml:mem:`read_list` = FALSE, this is either the single data file (if no templating is used) or a template for data file names. Both :doc:`time and variable name templating </input/file-name-templating>` may be used.


.. nml:group:: Members used to specify the provided variables

   .. nml:member:: nvars
   
      :type: integer
      :permitted: >= 0
      :default: 0
   
      The number of variables that the dataset will provide.
   
      See :ref:`supported-prescribed-variables` for the supported variables.
   
   
   .. nml:member:: var
   
      :type: character(nvars)
      :default: None
   
      List of variable names as recognised by JULES (see :ref:`supported-prescribed-variables`). Names are case sensitive.
   
      .. note:: For ASCII files, variable names must be in the order they appear in the file.
   
   
   .. nml:member:: var_name
   
      :type: character(nvars)
      :default: '' (empty string)
   
      For each JULES variable specified in :nml:mem:`var`, this is the name of the variable in the file(s) containing the data.

      If the empty string (the default) is given for any variable, then the corresponding value from :nml:mem:`var` is used instead.
   
      .. note:: For ASCII files, this is not used - only the order in the file matters, as described above.
   
   
   .. nml:member:: tpl_name
   
      :type: character(nvars)
      :default: None
   
      For each JULES variable specified in :nml:mem:`var`, this is the string to substitute into the file name(s) in place of the variable name substitution string.
   
      If the file name(s) do not use variable name templating, this is not used.
   
   
   .. nml:member:: interp
   
      :type: character(nvars)
      :default: None
   
      For each JULES variable specified in :nml:mem:`var`, this indicates how the variable is to be interpolated in time (see :doc:`/input/temporal-interpolation`).


   .. nml:member:: prescribed_levels

      :type: integer(n) where n ranges from 1 (one level prescribed) to :nml:mem:`JULES_SOIL::sm_levels` (all levels prescribed)
      :default: 1, ..., :nml:mem:`JULES_SOIL::sm_levels` i.e. all levels prescribed

      Indices of the subset of levels to be prescribed. Currently only implemented for :nml:mem:`var` = ``sthuf`` and :nml:mem:`nvars` = 1. The numbering of the soil level indices starts at 1 (corresponding to the layer touching the surface). Note that ``sthuf`` data must be provided for all soil levels, but can be set to dummy values for the levels that are not prescribed.


.. _supported-prescribed-variables:

List of supported variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

All variables input using :doc:`prescribed_data.nml` must have a time dimension using :nml:mem:`JULES_INPUT_GRID::time_dim_name`.

In theory, any variable with an entry in the subroutine ``populate_var`` in ``model_interface_mod`` (see :doc:`/code/io`) can be updated via this mechanism, and the use of any of these variables is not explicitly prevented. However, it is up to the user to assess whether using this mechanism to update any particular variable is appropriate or desirable.

The use of the following variables is explicitly supported:

.. tabularcolumns:: |p{2.5cm}|p{8cm}|p{4cm}|

+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| Name                      | Description                                                       | Levels dimension(s) required in files             |
+===========================+===================================================================+===================================================+
| ``ozone``                 | Surface ozone concentration (ppb).                                | None                                              |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Required if :nml:mem:`JULES_VEGETATION::l_o3_damage` = TRUE.    |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``canht``                 | PFT canopy height (m).                                            | Single levels dimension of size                   |
|                           |                                                                   | :nml:mem:`JULES_SURFACE_TYPES::npft` using        |
|                           | .. note::                                                         | :nml:mem:`JULES_INPUT_GRID::pft_dim_name`.        |
|                           |   Not possible if :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE   |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``lai``                   | PFT leaf area index.                                              | Single levels dimension of size                   |
|                           |                                                                   | :nml:mem:`JULES_SURFACE_TYPES::npft` using        |
|                           | .. note::                                                         | :nml:mem:`JULES_INPUT_GRID::pft_dim_name`.        |
|                           |   Not possible if :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE   |                                                   |
|                           |   or :nml:mem:`JULES_VEGETATION::l_phenol` = TRUE                 |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``albobs_sw``             | Observed SW diffuse albedo.                                       | None                                              |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Required if :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and |                                                   |
|                           |   :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE.              |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``albobs_vis``            | Observed VIS diffuse albedo.                                      | None                                              |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Required if :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and |                                                   |
|                           |   :nml:mem:`JULES_RADIATION::l_spec_albedo` = TRUE.               |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``albobs_nir``            | Observed NIR diffuse albedo.                                      | None                                              |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Required if :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and |                                                   |
|                           |   :nml:mem:`JULES_RADIATION::l_spec_albedo` = TRUE.               |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``co2_mmr``               | Concentration of atmospheric CO2, expressed as a mass mixing      | None                                              |
|                           | ratio.                                                            |                                                   |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   A single value of co2_mmr is applied globally. Data must be     |                                                   |
|                           |   supplied for each gridpoint, but only the value of the first    |                                                   |
|                           |   grid-point is used.                                             |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``sthuf``                 | Soil wetness for each soil layer. This is the mass of soil water  | Single levels dimension of size                   |
|                           | (liquid and frozen), expressed as a fraction of the water         | :nml:mem:`JULES_SOIL::sm_levels` using            |
|                           | content at saturation.                                            | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`.       |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Soil wetness will be set to the prescribed value at the         |                                                   |
|                           |   beginning of each timestep but will be incremented during       |                                                   |
|                           |   that timestep. Also, it is recommended that the prescribed      |                                                   |
|                           |   ``sthuf`` does not exceed one.                                  |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``frac_agr``              | Fractional area of agricultural land in each gridbox.             | None                                              |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``frac_past``             | Fractional area of pasture land in each gridbox.                  | None                                              |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``frac_biocrop``          | Fractional area of bioenergy cropland in each gridbox.            | None                                              |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``tracer_field``          | Surface concentration of atmospheric chemical tracers in the      | Single levels dimension of size                   |
|                           | atmosphere, for calculation of deposition, as mass mixing ratio   | :nml:mem:`JULES_DEPOSITION::ndry_dep_species`     |
|                           | (kg kg :sup:`-1`).                                                | using                                             |
|                           |                                                                   | :nml:mem:`JULES_INPUT_GRID::tracer_dim_name`.     |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``bl_height``             | Height above surface of top of atmospheric boundary layer (m).    | None                                              |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``level_separation``      | Separation of boundary layer levels (m).                          | Single levels dimension of size                   |
|                           | The levels are listed starting at the surface and working up.     | :nml:mem:`JULES_NLSIZES::bl_levels` using         |
|                           |                                                                   | :nml:mem:`JULES_INPUT_GRID::bl_level_dim_name`.   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``demand_rate_domestic``  | Demand for water for domestic use (kg kg :sup:`-1`)               | None                                              |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Required if :nml:mem:`JULES_WATER_RESOURCES::l_water_domestic`  |                                                   |
|                           |   = TRUE.                                                         |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``demand_rate_industry``  | Demand for water for industrial use (kg kg :sup:`-1`)             | None                                              |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Required if :nml:mem:`JULES_WATER_RESOURCES::l_water_industry`  |                                                   |
|                           |   = TRUE.                                                         |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``demand_rate_livestock`` | Demand for water for livestock (kg kg :sup:`-1`)                  | None                                              |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Required if :nml:mem:`JULES_WATER_RESOURCES::l_water_livestock` |                                                   |
|                           |   = TRUE.                                                         |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+
| ``demand_rate_trasnfers`` | Demand for water for transfers (kg kg :sup:`-1`)                  | None                                              |
|                           |                                                                   |                                                   |
|                           | .. note::                                                         |                                                   |
|                           |   Required if :nml:mem:`JULES_WATER_RESOURCES::l_water_transfers` |                                                   |
|                           |   = TRUE.                                                         |                                                   |
+---------------------------+-------------------------------------------------------------------+---------------------------------------------------+

