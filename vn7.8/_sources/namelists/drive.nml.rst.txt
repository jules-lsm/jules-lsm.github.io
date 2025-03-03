``drive.nml``
=============


This file contains a single namelist called :nml:lst:`JULES_DRIVE` that indicates how meteorological driving data is input.


``JULES_DRIVE`` namelist members
--------------------------------

.. nml:namelist:: JULES_DRIVE

.. nml:member:: t_for_snow

   :type: real
   :default: None

   If total precipitation is given as a forcing variable, then :nml:mem:`t_for_snow` is the near-surface air temperature (K) at or below which the precipitation is assumed to be snowfall. At higher temperatures, all the precipitation is assumed to be liquid. The default value used to be 274.0 K.


.. nml:member:: t_for_con_rain

   :type: real
   :default: None

   If total preciption or total rainfall are given, then :nml:mem:`t_for_con_rain` is the near-surface air temperature (K) at or above which rainfall is assumed to be convective in origin. At lower temperatures, all the rainfall is assumed to be large-scale in origin. In this configuration all snow is assumed to be large-scale in origin. The default value used to be 373.15 K but in general this is not recommended as it effectively means all precipitation is large-scale; a value of 293.15 K might be more appropriate.

   Also see :nml:mem:`JULES_SOIL::confrac`.

   :nml:mem:`t_for_con_rain` is not used if :nml:mem:`JULES_SURFACE::l_point_data` = TRUE, since then there is no convective precipitation.


.. nml:member:: diff_frac_const

   :type: real
   :default: None

   A constant value used to calculate diffuse radiation from the total downward shortwave radiation.

   Only used if diffuse radiation is not given as a forcing variable (see :ref:`list-of-jules-forcing-variables`).


.. nml:group:: Members used to control the daily disaggregator

   HCTN96 refer to Hadley Centre technical note 96, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_.

   .. nml:member:: l_daily_disagg

      :type: logical
      :default: F

      Switch controlling whether the disaggregator is used to convert daily data driving data to driving data at the model timestep. See HCTN96 for a description of the disaggregation methods used.

      TRUE
          Disaggregator is used.
       
          .. warning::
             The disaggregator requires:
          
             #. Daily forcing data, i.e. :nml:mem:`data_period` = 86400
             #. :nml:mem:`JULES_TIME::main_run_start`, :nml:mem:`JULES_SPINUP::spinup_start` and :nml:mem:`data_start` to be 00:00:00 for some day.

      FALSE
          Disaggregator is not used.
       
       
   .. nml:member:: l_disagg_const_rh
 
      :type: logical
      :default: F

      Switch controlling sub-daily disaggregation of humidity.
   
      Only used if :nml:mem:`l_daily_disagg` = TRUE.

      TRUE
          Relative humidity is kept constant over day.  

      FALSE
          Specific humidity is kept constant over day (apart from when limited by specific humidity at saturation).
       
       
   .. nml:member:: dur_conv_rain

      :type: real
      :default: None

      Duration of a convective rainfall event in seconds for use in the disaggregator. See HCTN96 section 2.4. A value of 21600s (6 hours) used to be the default.
   
      Only used if :nml:mem:`l_daily_disagg` = TRUE.
   
    
   .. nml:member:: dur_ls_rain

      :type: real
      :default: None

      Duration of a large-scale rainfall event in seconds for use in the disaggregator. See HCTN96 section 2.4. A value of 3600s (1 hour) used to be the default.
   
      Only used if :nml:mem:`l_daily_disagg` = TRUE.
   
   
   .. nml:member:: dur_conv_snow

      :type: real
      :default: None

      Duration of a convective snowfall event in seconds for use in the disaggregator. See HCTN96 section 2.4. A value of 3600s (1 hour) used to be the default.
   
      Only used if :nml:mem:`l_daily_disagg` = TRUE.
   
   
   .. nml:member:: dur_ls_snow

      :type: real
      :default: None

      Duration of a large-scale snowfall event in seconds for use in the disaggregator. See HCTN96 section 2.4. A value of 3600s (1 hour) used to be the default.
   
      Only used if :nml:mem:`l_daily_disagg` = TRUE.
       
       
   .. nml:member:: precip_disagg_method 

      :type: integer
      :permitted: 1, 2, 3 or 4
      :default: None

      Switch controlling the disaggregation method for precipitation. See HCTN96 section 2.4. The default value used to be 2.
   
      Only used if :nml:mem:`l_daily_disagg` = TRUE.

      1.  Do not disaggregate precipitation.
      2.  Disaggregate precipitation using the method implemented in IMOGEN, which allocates the daily precipitation each type into one event of duration :nml:mem:`dur_conv_rain`, :nml:mem:`dur_ls_rain`, :nml:mem:`dur_conv_snow` and :nml:mem:`dur_ls_snow` for convective rain, large-scale rain, convective snow and large-scale snow respectively.
          The start time of this event is randomly distributed from the beginning of the day to the end of the day minus the event duration.
          If the rate of precipitation in any timestep of any type is greater than a hard-coded maximum (currently 350 mm/day), the precipitation is redistributed by the ``redis`` routine in IMOGEN.
      3.  As for 2, except no upper limit on the precipitation in a timestep.
      4.  The event duration variable is used to determine the fraction of wet and dry timesteps, which are then distributed randomly throughout the day.


.. nml:group:: Members used to specify perturbations to the driving data

   .. nml:member:: l_perturb_driving

      :type: logical
      :default: F

      Apply perturbation to driving data.

   .. nml:member:: temperature_abs_perturbation

      :type: real
      :default: None

      Absolute perturbation amount to add to temperature. Can be positive or negative. Only used if :nml:mem:`l_perturb_driving` = TRUE.

   .. nml:member:: precip_rel_perturbation

      :type: real
      :permitted: >= 0.0
      :default: None

      Relative perturbation for precipitation variables (a multiplicative factor). Only used if :nml:mem:`l_perturb_driving` = TRUE.
      

.. nml:group:: Members used to specify ``z1_tq`` and ``z1_uv``

   .. nml:member:: z1_uv_in

      :type: real
      :permitted: > 0.0
      :default: None

      Constant value for the height (m) at which the wind data are valid for every point. This height is relative to the zero-plane, not the ground.


   .. nml:member:: z1_tq_vary

      :type: logical 
      :default: F 
     
      Switch to indicate whether ``z1_tq`` (the height (m) at which the temperature and humidity data are valid) should be constant for all points or spatially varying. The height is relative to the zero-plane, not the ground.  

      TRUE 
          Spatially varying ``z1_tq`` will be read from the file specified in :nml:mem:`z1_tq_file`. 

      FALSE 
          ``z1_tq`` will be set to a constant value, specified in :nml:mem:`z1_tq_in`, at all points.


   .. nml:member:: z1_tq_in

      :type: real
      :permitted: > 0.0
      :default: None

      Constant value for ``z1_tq`` to be used for every point.
      
      Only required if :nml:mem:`z1_tq_vary` = F.


   .. nml:member:: z1_tq_file 

      :type: character 
      :default: None 
   
      File to read spatially varying ``z1_tq`` from.
      
      Only required if :nml:mem:`z1_tq_vary` = T.


   .. nml:member:: z1_tq_var_name 

      :type: character 
      :default: 'z1_tq_in'

      The name of the variable in :nml:mem:`z1_tq_file` containing the data for ``z1_tq``.
      
      The variable should have no levels dimensions and no time dimension.
      
      .. note::
         This is not used for ASCII files.
         
         However, since ASCII files can only be used for single-point runs, it is recommended to set :nml:mem:`z1_tq_vary` = F and use :nml:mem:`z1_tq_in` anyway.

       
.. nml:group:: Members used to specify boundary layer height

   .. nml:member:: bl_height

      :type: real
      :permitted: > 0.0
      :default: 1000.0

      Height above ground to top of the atmospheric boundary layer (m). This value is disregarded if ``bl_height`` is provided as prescribed data (see :ref:`supported-prescribed-variables`).

       
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
   
      The number of forcing variables that will be provided.
   
      See :ref:`list-of-jules-forcing-variables` for the available forcing variables and their possible configurations.
   
   
   .. nml:member:: var
   
      :type: character(nvars)
      :default: None
   
      List of forcing variable names as recognised by JULES (see :ref:`list-of-jules-forcing-variables`). Names are case sensitive.
   
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


.. _list-of-jules-forcing-variables:

List of JULES forcing variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All of the available forcing variables listed in the sections below, are expected to have no levels dimensions, but must have a time dimension called :nml:mem:`JULES_INPUT_GRID::time_dim_name`.

Pressure, Humidity and Temperature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``pstar``                  | Air pressure (Pa).                                                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``q``                      | Specific humidity (kg kg\ :sup:`-1`).                                                                     |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``t``                      | Air temperature (K).                                                                                      |
+----------------------------+-----------------------------------------------------------------------------------------------------------+

Radiation variables
^^^^^^^^^^^^^^^^^^^

The radiation forcing variables can be given in one of four ways:

``sw_down`` and ``lw_down``
    Downward fluxes of short- and longwave radiation are input. *This is the preferred option.*

``rad_net`` and ``sw_down``
    Downward shortwave and net all wavelength (downward is positive) radiation are input. The modelled albedo and surface temperature are used to calculate the downward longwave flux.

``lw_net`` and ``sw_net``
    Net downward fluxes of short- and longwave radiation are input. The modelled albedo and surface temperature are used to calculate the downward fluxes of shortwave and longwave radiation.

``lw_down`` and ``sw_net``
    Downward flux of longwave radiation and net downward flux of shortwave radiation are input. The modelled albedo is used to calculate the downward flux of shortwave radiation.

If any of the four combinations of radiation variables listed above are provided, then these are used to drive JULES. There is no default option. JULES will give a fatal error and stop if there are too many, too few or invalid forcing variables provided in the variable list.

.. warning:: If :nml:mem:`l_daily_disagg` = TRUE, then the first method must be used.

``diff_rad`` can be used with any of the four methods. If it is given, diffuse radiation is input from file. If it is not given, :nml:mem:`JULES_DRIVE::diff_frac_const` is used instead to partition the downward shortwave radiation into diffuse and direct.

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``rad_net``                | Net (all wavelength) downward radiation (W m\ :sup:`-2`).                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``lw_net``                 | Net downward longwave radiation (W m\ :sup:`-2`).                                                         |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``sw_net``                 | Net downward shortwave radiation (W m\ :sup:`-2`).                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``lw_down``                | Downward longwave radiation (W m\ :sup:`-2`).                                                             |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``sw_down``                | Downward shortwave radiation (W m\ :sup:`-2`).                                                            |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``diff_rad``               | Diffuse radiation (W m\ :sup:`-2`).                                                                       |
+----------------------------+-----------------------------------------------------------------------------------------------------------+

Precipitation variables
^^^^^^^^^^^^^^^^^^^^^^^

The precipitation variables can be specified in one of four ways:

``precip``
    A single precipitation field is input. This represents the total precipitation (rainfall and snowfall). The total is partitioned between snowfall and rainfall using :nml:mem:`JULES_DRIVE::t_for_snow`, and rainfall is then further partitioned into large-scale and convective components using :nml:mem:`JULES_DRIVE::t_for_con_rain`. Convective snowfall is assumed to be zero.

``tot_rain`` and ``tot_snow``
    Two precipitation fields are input: total rainfall and total snowfall. The rainfall is partitioned between large-scale and convective, using :nml:mem:`JULES_DRIVE::t_for_con_rain`. Convective snowfall is assumed to be zero.

``ls_rain``, ``con_rain`` and ``tot_snow``
    Three precipitation fields are input: large-scale rainfall, convective rainfall and total snowfall. This cannot be used with :nml:mem:`JULES_SURFACE::l_point_data` = TRUE. Convective snowfall is assumed to be zero.

``ls_rain``, ``con_rain``, ``ls_snow`` and ``con_snow``
    Four precipitation fields are input: large-scale rainfall, convective rainfall, large-scale snowfall and convective snowfall. This cannot be used with :nml:mem:`JULES_SURFACE::l_point_data` = TRUE. Note that this is the only option that considers convective snowfall.

If ``precip`` is given, the first method is used. If ``precip`` is *not* given but ``tot_rain`` is, the second method is used. If *neither* ``precip`` *nor* ``tot_rain`` are given but ``tot_snow`` is, the third method is used. The fourth method is used in all other cases.

The concept of convective and large-scale (or dynamical) components of precipitation comes from atmospheric models, in which the precipitation from small-scale (convective) and large-scale motions is often calculated separately. If JULES is to be driven by the output from such a model, the driving data might include these components.

.. warning:: If :nml:mem:`l_daily_disagg` = TRUE, then :nml:mem:`interp` for each precipitation variable should be ``f`` or ``nf``.

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``precip``                 | Precipitation rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``tot_rain``               | Rainfall rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                                             |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``tot_snow``               | Snowfall rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                                             |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``ls_rain``                | Large-scale rainfall rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``con_rain``               | Convective rainfall rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``ls_snow``                | Large-scale snowfall rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``con_snow``               | Convective snowfall rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------+

Wind variables
^^^^^^^^^^^^^^

The wind variables can be given in one of two ways:

``wind``
    The wind speed is input.

``u`` and ``v``
    The two components of the horizontal wind (e.g. the southerly and westerly components) are input.

If ``wind`` is given, then the first method is used. The second method is used in all other cases.

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``wind``                   | Total wind speed (m s\ :sup:`-1`).                                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``u``                      | Zonal component of the wind (m s\ :sup:`-1`).                                                             |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``v``                      | Meridional component of the wind (m s\ :sup:`-1`).                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+


Daily disaggregator variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If :nml:mem:`l_daily_disagg` = TRUE, then the diurnal temperature range is also required:

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``dt_range``               | Diurnal temperature range (K).                                                                            |
+----------------------------+-----------------------------------------------------------------------------------------------------------+


Examples of specifying driving data
-----------------------------------

The examples below illustrate the use of some of the key settings in the namelist; other settings are omitted for clarity.

Single point ASCII driving data for one year
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    &JULES_DRIVE

      data_start  = '1997-01-01 00:00:00',
      data_end    = '1998-01-01 00:00:00',
      data_period = 1800,

      file = "met_data.dat",

      nvars  = 8,
      var    = 'sw_down'  'lw_down'  'tot_rain'  'tot_snow'   't'  'wind'  'pstar'   'q',
      interp =      'nf'       'nf'        'nf'        'nf'  'nf'    'nf'     'nf'  'nf',

      diff_frac_const = 0.1,
      t_for_con_rain  = 293.15
    /

:nml:mem:`JULES_DRIVE::data_start`, :nml:mem:`JULES_DRIVE::data_end` and :nml:mem:`JULES_DRIVE::data_period` specify that the driving dataset provides one year (1997) of half-hourly data.

:nml:mem:`JULES_DRIVE::read_list` is not given, so takes its default value of FALSE. This means that :nml:mem:`JULES_DRIVE::file` is used as either the single data file or a file name template. In this case there is no templating, so JULES treats the given file as the single data file for all data times.

``sw_down`` and ``lw_down`` are given, so the first radiation scheme (above) is used.

``precip`` is not given but ``tot_rain`` is, so the second precipitation scheme (above) is used. :nml:mem:`JULES_DRIVE::t_for_con_rain` = 293.15K means that rainfall is treated as convective in nature for temperatures at or above that threshold (not used if :nml:mem:`JULES_SURFACE::l_point_data` = TRUE).

``wind`` is given, so total wind speed is used (first scheme above).

``diff_rad`` is not given, so the diffuse radiation is calculated as 0.1 (the value of :nml:mem:`JULES_DRIVE::diff_frac_const`) times the total shortwave radiation.

The driving data file (``met_data.dat``) should look similar to::

    # solar   long  rain  snow    temp   wind     press      humid
        3.3  187.8   0.0   0.0  259.10  3.610  102400.5  1.351E-03
       89.5  185.8   0.0   0.0  259.45  3.140  102401.9  1.357E-03
      142.3  186.4   0.0   0.0  259.85  2.890  102401.0  1.369E-03
    # ----- data for later times ----


Driving data from NetCDF files with one variable per file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    &JULES_DRIVE

      data_start  = '1982-07-01 03:00:00',
      data_end    = '1996-01-01 00:00:00',
      data_period = 10800,

      read_list = T,
      nfiles    = 162,

      file = "./file_list.txt",

      nvars    = 8,
      var      = 'sw_down'  'lw_down'  'tot_rain'  'tot_snow'     't'  'wind'  'pstar'     'q',
      var_name =  'SWdown'   'LWdown'     'Rainf'     'Snowf'  'Tair'  'Wind'  'PSurf'  'Qair',
      tpl_name =  'SWdown'   'LWdown'     'Rainf'     'Snowf'  'Tair'  'Wind'  'PSurf'  'Qair',
      interp   =      'nb'       'nb'        'nb'        'nb'     'i'     'i'      'i'     'i',

      diff_frac_const = 0.1,
      t_for_con_rain  = 293.15
    /

In this example, the driving dataset provides 13.5 years of driving data on a 3 hourly timestep.

:nml:mem:`JULES_DRIVE::read_list` = TRUE indicates that the names and start times of the data files should be read from ``file_list.txt``. The first few lines of this file are::

    'met_data/%vv_data/%vv198207.nc', '1982-07-01 03:00:00'
    'met_data/%vv_data/%vv198208.nc', '1982-08-01 03:00:00'
    'met_data/%vv_data/%vv198209.nc', '1982-09-01 03:00:00'
    # ------ rest of file not shown -----

The presence of the variable name templating string in each file name shows that we are using :doc:`variable name templating </input/file-name-templating>`. The dates show that we do in fact have monthly files, but we cannot use time templating for these files because the start time of 03H does not conform to the requirements.

Furthermore, files for each variable are stored in separate directories. The values from :nml:mem:`JULES_DRIVE::tpl_name` will be substituted into the file name templates in place of the substitution string (``%vv``). For example, pressure is held in files with names like ``met_data/PSurf_data/PSurf198207.nc``, and temperature in files like ``met_data/Tair_data/Tair198207.nc``.

The driving variable setup is as the previous example.


