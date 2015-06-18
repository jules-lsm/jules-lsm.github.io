``drive.nml``
=============


This file contains a single namelist called :nml:lst:`JULES_DRIVE` that indicates how meteorological driving data is input.


``JULES_DRIVE`` namelist members
--------------------------------

.. nml:namelist:: JULES_DRIVE

.. note::
   If IMOGEN is enabled (:nml:mem:`JULES_SWITCHES::l_imogen` = TRUE), then meteorological forcing is provided by IMOGEN. In this case, only :nml:mem:`z1_tq_in` and :nml:mem:`z1_uv_in` are used from this namelist.


.. nml:member:: z1_uv_in

   :type: real
   :permitted: > 0.0
   :default: 10.0

   The height (m) at which the wind data are valid. This height is relative to the zero-plane, not the ground.


.. nml:member:: z1_tq_in

   :type: real
   :permitted: > 0.0
   :default: 10.0

   The height (m) at which the temperature and humidity data are valid. This height is relative to the zero-plane, not the ground.


.. nml:member:: t_for_snow

   :type: real
   :default: 274.0

   If total precipitation is given as a forcing variable, then :nml:mem:`t_for_snow` is the near-surface air temperature (K) at or below which the precipitation is assumed to be snowfall. At higher temperatures, all the precipitation is assumed to be liquid.


.. nml:member:: t_for_con_rain

   :type: real
   :default: 373.15

   If total preciption or total rainfall are given, then :nml:mem:`t_for_con_rain` is the near-surface air temperature (K) at or above which rainfall is assumed to be convective in origin. At lower temperatures, all the rainfall is assumed to be large-scale in origin.

   Also see :nml:mem:`JULES_SOIL_PARAM::confrac`.

   :nml:mem:`t_for_con_rain` is not used if :nml:mem:`JULES_SWITCHES::l_point_data` = TRUE, since then there is no convective precipitation.

   All snow is assumed to be large-scale in origin.


.. nml:member:: diff_frac_const

   :type: real
   :default: 0.0

   A constant value used to calculate diffuse radiation from the total downward shortwave radiation.

   Only used if diffuse radiation is not given as a forcing variable (see :ref:`list-of-jules-forcing-variables`).


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
   
      -1. Monthly data
      -2. Yearly data


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
      :default: None
   
      For each JULES variable specified in :nml:mem:`var`, this is the name of the variable in the file(s) containing the data.
   
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

All of the available forcing variables listed below are expected to have no levels dimensions, but must have a time dimension called :nml:mem:`JULES_INPUT_GRID::time_dim_name`.

Variables that are always required
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

Radiaton variables
^^^^^^^^^^^^^^^^^^

The radiation forcing variables can be given in one of three ways:

``rad_net`` and ``sw_down``
    Downward shortwave and net (all wavelengths) downward radiation are input. The modelled albedo and surface temperature are used to calculate the downward longwave flux.

``lw_net`` and ``sw_net``
    Net downward fluxes of short- and longwave radiation are input. The modelled albedo and surface temperature are used to calculate the downward fluxes of shortwave and longwave radiation.

``sw_down`` and ``lw_down``
    Downward fluxes of short- and longwave radiation are input. *Normally this is the preferred option.*

If ``rad_net`` is present in the given list of variables, the first method is used. If ``rad_net`` is not present but ``lw_net`` is, then the second method is used. The third method is used in all other cases.

``diff_rad`` can be used with any of the three methods. If it is given, diffuse radiation is input from file. If it is not given, :nml:mem:`JULES_DRIVE::diff_frac_const` is used instead to partition the downward shortwave radiation into diffuse and direct.

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
    Three precipitation fields are input: large-scale rainfall, convective rainfall and total snowfall. This cannot be used with :nml:mem:`JULES_SWITCHES::l_point_data` = TRUE. Convective snowfall is assumed to be zero.

``ls_rain``, ``con_rain``, ``ls_snow`` and ``con_snow``
    Four precipitation fields are input: large-scale rainfall, convective rainfall, large-scale snowfall and convective snowfall. This cannot be used with :nml:mem:`JULES_SWITCHES::l_point_data` = TRUE. Note that this is the only option that considers convective snowfall.

If ``precip`` is given, the first method is used. If ``precip`` is *not* given but ``tot_rain`` is, the second method is used. If *neither* ``precip`` *nor* ``tot_rain`` are given but ``tot_snow`` is, the third method is used. The fourth method is used in all other cases.

The concept of convective and large-scale (or dynamical) components of precipitation comes from atmospheric models, in which the precipitation from small-scale (convective) and large-scale motions is often calculated separately. If JULES is to be driven by the output from such a model, the driving data might include these components.

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



Examples of specifying driving data
-----------------------------------

Single point ASCII driving data for one year
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    &JULES_DRIVE
      diff_frac_const = 0.1,

      data_start  = '1997-01-01 00:00:00',
      data_end    = '1998-01-01 00:00:00',
      data_period = 1800,

      file = "met_data.dat",

      nvars = 8,
      var    = 'sw_down'  'lw_down'  'tot_rain'  'tot_snow'   't'  'wind'  'pstar'   'q',
      interp =      'nf'       'nf'        'nf'        'nf'  'nf'    'nf'     'nf'  'nf'
    /

:nml:mem:`JULES_DRIVE::data_start`, :nml:mem:`JULES_DRIVE::data_end` and :nml:mem:`JULES_DRIVE::data_period` specify that the driving dataset provides one year (1997) of half-hourly data.

:nml:mem:`JULES_DRIVE::read_list` is not given, so takes its default value of FALSE. This means that :nml:mem:`JULES_DRIVE::file` is used as either the single data file or a file name template. In this case there is no templating, so JULES treats the given file as the single data file for all data times.

Neither ``rad_net`` nor ``lw_net`` are given, so the third radiation scheme (above) is used.

``precip`` is not given but ``tot_rain`` is, so the second precipitation scheme (above) is used.

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

      nvars = 8,
      var      = 'sw_down'  'lw_down'  'tot_rain'  'tot_snow'     't'  'wind'  'pstar'     'q',
      var_name =  'SWdown'   'LWdown'     'Rainf'     'Snowf'  'Tair'  'Wind'  'PSurf'  'Qair',
      tpl_name =  'SWdown'   'LWdown'     'Rainf'     'Snowf'  'Tair'  'Wind'  'PSurf'  'Qair',
      interp   =      'nb'       'nb'        'nb'        'nb'     'i'     'i'      'i'     'i'
    /

In this example, the driving dataset provides 13.5 years of driving data on a 3 hourly timestep.

:nml:mem:`JULES_DRIVE::read_list` = TRUE indicates that the names and start times of the data files should be read from ``file_list.txt``. The first few lines of this file are::

    'met_data/%vv_data/%vv198207.nc', '1982-07-01 03:00:00'
    'met_data/%vv_data/%vv198208.nc', '1982-08-01 03:00:00'
    'met_data/%vv_data/%vv198209.nc', '1982-09-01 03:00:00'
    # ------ rest of file not shown -----

The presence of the variable name templating string in each file name shows that we are using :doc:`variable name templating </input/file-name-templating>`. The dates show that we do in fact have monthly files, but we cannot use time templating for these files because the start time of 03H does not conform to the requirements.

Furthermore, files for each variable are stored in separate directories. The values from :nml:mem:`JULES_DRIVE::tpl_name` will be substituted into the file name templates in place of the substitution string (``%vv``). For example, pressure is held in files with names like ``met_data/PSurf_data/PSurf198207.nc``, and temperature in files like ``met_data/Tair_data/Tair198207.nc``.

The driving variable setup is as the previous example, except that :nml:mem:`JULES_DRIVE::diff_frac_const` takes its default value of 0.0.
