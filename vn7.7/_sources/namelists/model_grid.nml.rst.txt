``model_grid.nml``
==================


This file sets up the grid configuration for the run. It contains seven namelists - :nml:lst:`JULES_INPUT_GRID`, :nml:lst:`JULES_LATLON`, :nml:lst:`JULES_LAND_FRAC`, :nml:lst:`JULES_MODEL_GRID`, :nml:lst:`JULES_NLSIZES`, :nml:lst:`JULES_SURF_HGT` and :nml:lst:`JULES_Z_LAND`

Each run of JULES involves two grids: the input grid and the model grid. The input grid is the grid on which all input data are held. The model grid is the set of points on which the model is run. The model grid is the grid of points that will be processed by JULES, and is a subset of the input grid.

As discussed in :doc:`/input/principles`, the input grid consists of three pieces of information:

#. Whether the grid is 1D or 2D.
#. The size of each dimension.
#. The name of each dimension in the input file(s).

The latitude, longitude and land fraction of each point are then read in on the full input grid as specified by the namelists. A subset of the input grid to use as the model grid can then be specified in various ways described below (e.g. land points only, all points within certain latitude/longitude bounds).

In most cases, the model grid will be represented internally as a vector of points, even when the input grid is 2D. Numerically, this makes no difference. The only time that the model grid will be 2D is when the input grid is 2D, :nml:mem:`JULES_MODEL_GRID::force_1d_grid` = F and the model grid is a contiguous rectangular subsection of the input grid.


``JULES_INPUT_GRID`` namelist members
-------------------------------------

.. nml:namelist:: JULES_INPUT_GRID

.. warning:: The dimension names specified in this namelist will be used for all input files.

.. nml:member:: grid_is_1d

   :type: logical
   :default: F

   Indicates if the input grid is 1D or 2D.                                    

   TRUE
      Variables have one grid dimension in the input file(s) - a points dimensions (e.g. a vector of land points with grid dimension "land").

   FALSE
       Variables have two grid dimensions in the input file(s) - an x and a y dimension.


.. nml:group:: Only used when :nml:mem:`grid_is_1d` = TRUE

   .. nml:member:: grid_dim_name

      :type: character
      :default: "land"

      The name of the single grid dimension.                                      

      .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


   .. nml:member:: npoints

      :type: integer
      :permitted: >= 1
      :default: 0

      The size of the single grid dimension.                                      


.. nml:group:: Only used when :nml:mem:`grid_is_1d` = FALSE

   .. nml:member:: x_dim_name
   
      :type: character
      :default: "x"
   
      The name of the x dimension (it may, but does not have to, coincide with :nml:mem:`JULES_RIVERS_PROPS::x_dim_name`). 

      .. note:: For ASCII files, this can be anything. For NetCDF files, it should be the name of the dimension in the input file(s).
   
   
   .. nml:member:: y_dim_name
   
      :type: character
      :default: "y"
   
      The name of the y dimension (it may, but does not have to, coincide with :nml:mem:`JULES_RIVERS_PROPS::y_dim_name`).
   
      .. note:: For ASCII files, this can be anything. For NetCDF files, it should be the name of the dimension in the input file(s).
   
   
   .. nml:member:: nx
   
      :type: integer
      :permitted: >= 1
      :default: 0
   
      The size of the x dimension.                                                
   
   
   .. nml:member:: ny
   
      :type: integer
      :permitted: >= 1
      :default: 0
   
      The size of the y dimension.                                                


.. nml:member:: time_dim_name

   :type: character
   :default: "time"

   The name of the time dimension in any input files containing time varying data.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: pft_dim_name

   :type: character
   :default: "pft"

   The dimension name used when variables have an additional dimension of size :nml:mem:`JULES_SURFACE_TYPES::npft`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).
   
   
.. nml:member:: cpft_dim_name

   :type: character
   :default: "cpft"

   The dimension name used when variables have an additional dimension of size :nml:mem:`JULES_SURFACE_TYPES::ncpft`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: nvg_dim_name

   :type: character
   :default: "nvg"

   The dimension name used when variables have an additional dimension of size  :nml:mem:`JULES_SURFACE_TYPES::nnvg`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: type_dim_name

   :type: character
   :default: "type"

   The dimension name used when variables have an additional dimension of size  ``ntype``.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: tile_dim_name

   :type: character
   :default: "tile"

   The dimension name used when variables have an additional dimension of size  ``nsurft``.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: soil_dim_name

   :type: character
   :default: "soil"

   The dimension name used when variables have an additional dimension of size  :nml:mem:`JULES_SOIL::sm_levels`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: snow_dim_name

   :type: character
   :default: "snow"

   The dimension name used when variables have an additional dimension of size  :nml:mem:`JULES_SNOW::nsmax`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: sclayer_dim_name

   :type: character
   :default: "sclayer"

   The dimension name used for the soil biogeochemistry when layered soil is used i.e. :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = TRUE. When :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = TRUE the soil biogeochemistry has the same number of layers as the soil hydrology (:nml:mem:`JULES_SOIL::sm_levels`). When :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = FALSE the soil biogeochemistry represents a single bulk layer. Despite the similar name, this parameter is unrelated to :nml:mem:`JULES_SOIL_ECOSSE::dim_cslayer`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: scpool_dim_name

   :type: character
   :default: "scpool"

   The dimension name used when variables have an additional dimension of size  ``dim_cs1``.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).
   
   
.. nml:member:: bedrock_dim_name

   :type: character
   :default: "bedrock"

   The dimension name used when variables have an additional dimension of size  :nml:mem:`JULES_SOIL::ns_deep`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: tracer_dim_name

   :type: character
   :default: "tracer"

   The dimension name used when variables have an additional dimension of size :nml:mem:`JULES_DEPOSITION::ndry_dep_species` (e.g. chemical tracers in the atmosphere).

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: bl_level_dim_name

   :type: character
   :default: "bllevel"

   The dimension name used when variables have an additional dimension of size :nml:mem:`JULES_NLSIZES::bl_levels` (e.g. variables on atmospheric boundary layer levels).

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


``JULES_LATLON`` namelist members
---------------------------------

.. nml:namelist:: JULES_LATLON


.. nml:group:: Members used to determine how gridpoint location variables are set


   .. nml:member:: read_from_dump

      :type: logical
      :default: F

      TRUE
         Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

      FALSE
         Use the other namelist members to determine how to populate variables.


   .. nml:member:: l_coord_latlon

      :type: logical
      :default: F

      TRUE
         The coordinate system used for the model grid is latitude and longitude.

      FALSE
         The model grid is defined by projection coordinates other than latitude and longitude (e.g. northings and eastings, or a rotated grid).


   .. nml:member:: nvars

      :type: integer
      :permitted: >= 2
      :default: 0

      The number of location variables that will be provided (see :ref:`list-of-grid-location-params`).


   .. nml:member:: var

      :type: character(nvars)
      :default: None

      List of location variable names as recognised by JULES (see :ref:`list-of-grid-location-params`). Names are case sensitive.

      .. note:: For ASCII files, variable names must be in the order they appear in the file.


   .. nml:member:: use_file

      :type: logical(nvars)
      :default: T

      For each JULES variable specified in :nml:mem:`var`, this indicates if it should be read from the specified file or whether a constant value is to be used.

      TRUE
         The variable will be read from the file.

      FALSE
         The variable will be set to a constant value everywhere using :nml:mem:`const_val` below.


   .. nml:member:: var_name

      :type: character(nvars)
      :default: '' (empty string)

      For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = TRUE, this is the name of the variable in the file containing the data.

      If the empty string (the default) is given for any variable, then the corresponding value from :nml:mem:`var` is used instead.

      This is not used for variables where :nml:mem:`use_file` = FALSE, but a placeholder must still be given in that case.

      .. note:: For ASCII files, this is not used - only the order in the file matters, as described above.


   .. nml:member:: tpl_name

      :type: character(nvars)
      :default: None

      For each JULES variable specified in :nml:mem:`var`, this is the string to substitute into the file name in place of the variable name substitution string.

      If the file name does not use variable name templating, this is not used.


   .. nml:member:: const_val

      :type: real(nvars)
      :default: None

      For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to at every point.

      This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.


   .. nml:member:: file

      :type: character
      :default: None

      The file to read ancillary properties from.

      If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

      This file name can use :doc:`variable name templating </input/file-name-templating>`.


.. _list-of-grid-location-params:

List of grid location properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table summarises ancillary fields that give the location and related characteristics of each point on the grid, specified from an ancillary file if :nml:mem:`JULES_LATLON::use_file` = TRUE.

.. tabularcolumns:: |p{3cm}|L|

+----------------------------+------------------------------------------------------------------------------------------+
| Name                       | Description                                                                              |
+============================+==========================================================================================+
| ``latitude``               | Latitude of each point. Always required.                                                 |
|                            |                                                                                          |
+----------------------------+------------------------------------------------------------------------------------------+
| ``longitude``              | Longitude of each point. Always required.                                                |
|                            | Values in the range -180 to 360 are allowed.                                             |
+----------------------------+------------------------------------------------------------------------------------------+
| ``projection_x_coord``     | Values of the projection coordinate in the x direction.                                  |
|                            | This is only required if :nml:mem:`l_coord_latlon` = FALSE.                              |
|                            | Note that these can have any valid unit.                                                 |
+----------------------------+------------------------------------------------------------------------------------------+
| ``projection_y_coord``     | Values of the projection coordinate in the y direction.                                  |
|                            | This is only required if :nml:mem:`l_coord_latlon` = FALSE.                              |
|                            | Note that these can have any valid unit.                                                 |
+----------------------------+------------------------------------------------------------------------------------------+
| ``grid_area``              | The area of each gridbox (m\ :sup`2`).                                                   |
|                            | This is requred if irrigation is being modelled with                                     |
|                            | :nml:mem:`JULES_WATER_RESOURCES::l_water_resources` = TRUE and                           |
|                            | :nml:mem:`JULES_WATER_RESOURCES::l_water_irrigation` = TRUE.                             |
|                            | It is also required when using IMOGEN:                                                   |
|                            | :nml:mem:`IMOGEN_ONOFF_SWITCH::l_imogen` = TRUE                                          |
+----------------------------+------------------------------------------------------------------------------------------+

Examples of how to specify the model domain using through this namelist are provided at the end of this section.


``JULES_LAND_FRAC`` namelist members
------------------------------------

.. nml:namelist:: JULES_LAND_FRAC

Land fraction is the fraction of each gridbox that is land. Currently, JULES considers any gridbox with land fraction > 0 to be 100% land, and all others to be 100% sea (or sea-ice). Land fraction data can be used to select only land points from the full input grid (see below).

.. warning::
   When the input grid consists of a single location (1D and :nml:mem:`JULES_INPUT_GRID::npoints` = 1 or 2D and :nml:mem:`JULES_INPUT_GRID::nx` = :nml:mem:`JULES_INPUT_GRID::ny` = 1), that single location is assumed to be 100% land.
   
   IMOGEN also currently assumes 100% land for each land grid cell.


For any input grid with more than a single location, the following are used:


.. nml:member:: file

   :type: character
   :default: None

   The name of the file to read land fraction data from.                       


.. nml:member:: land_frac_name

   :type: character
   :default: 'land_fraction'

   The name of the variable containing the land fraction data.                 

   In the file, the variable must have no levels dimensions and no time dimension.



``JULES_MODEL_GRID`` namelist members
-------------------------------------

.. nml:namelist:: JULES_MODEL_GRID

Members of this namelist are used to select the points to be modelled from the input grid. This can be done in various ways (see the :ref:`grid-examples`).


.. nml:member:: land_only

   :type: logical
   :default: T

   TRUE                                                                        
       Model land points only (from the points that are selected with other options).

   FALSE
       Model all selected points.

   If :nml:mem:`use_subgrid` = FALSE (see below), the land points will be extracted from the full input grid.

   If :nml:mem:`use_subgrid` = TRUE, then the subgrid extraction takes place first, and the land points will be extracted from the specified subgrid.


.. nml:member:: force_1d_grid

   :type: logical
   :default: F

   TRUE                                                                        
       Force the model grid to be 1D, even if it would otherwise have been 2D.

   FALSE
       The model grid takes its default shape.


.. nml:member:: use_subgrid

   :type: logical
   :default: F

   TRUE                                                                        
       The model grid is a subset of the full input grid, specified using some valid combination of the options below.

   FALSE
       The model grid is the full input grid.


.. nml:group:: Only used if :nml:mem:`use_subgrid` = TRUE

   .. nml:member:: l_bounds
   
      :type: logical
      :default: None
   
      TRUE                                                                        
          Subset of points to model will be selected using bounds for the coordinates variables.
   
      FALSE
          Subset of points to model will be selected using a list of coordinate pairs for each point.

      If :nml:mem:`JULES_LATLON::l_coord_latlon` = TRUE, the coordinates used here are latitude and longitude.

      If :nml:mem:`JULES_LATLON::l_coord_latlon` = FALSE, the coordinates used here are the values stored in the variables projection_x_coord and projection_y_coord.
   
   
   .. nml:group:: Only used if :nml:mem:`l_bounds` = TRUE
   
      .. nml:member:: y_bounds
      
         :type: real(2)
         :default: None
      
         The lower and upper bounds (in that order) for the y coordinate used to select points. Assuming that the coordinate is latitude (see  :nml:mem:`JULES_LATLON::l_coord_latlon`) the model grid will comprise the points where ``y_bounds(1) <= latitude <= y_bounds(2)``.
       
       
      .. nml:member:: x_bounds
      
         :type: real(2)
         :default: None
      
         The lower and upper bounds (in that order) for the x coordinate used to select points. Assuming that the coordinate is longitude (see  :nml:mem:`JULES_LATLON::l_coord_latlon`) the model grid will comprise the points where ``x_bounds(1) <= longitude <= x_bounds(2)``.

         If the x coordinate is longitude, the values of x_bounds should lie in the range [-180, 360]. A special case is that in which the desired subgrid straddles the edge of a global input grid. For example, if the input grid has longitudes in [0, 360] and a domain of 20 degrees of longitude centred on 0degE is required, this should be indicated using ``xbounds=-10,10`` (not xbounds=360,370 because values > 360 are not recognised). In this case the JULES code recognises the cyclic nature of longitude and correctly picks up points in both hemispheres, even though -10degE is outwith the longitude values in the input grid.
   
   
   .. nml:group:: Only used if :nml:mem:`l_bounds` = FALSE
   
      .. nml:member:: npoints
   
         :type: integer
         :permitted: >= 1
         :default: 0
      
         The number of points to model.
         
      
      .. nml:member:: points_file
      
         :type: character
         :default: None
      
         The name of the file containing the coordinates for each point.

         If :nml:mem:`JULES_LATLON::l_coord_latlon` = TRUE, the coordinates used here are latitude and longitude. Each line in the file should contain the latitude and longitude (in that order) for a point.

         If :nml:mem:`JULES_LATLON::l_coord_latlon` = FALSE, the coordinates used here are the values stored in the variables projection_x_coord and projection_y_coord. Each line in the file should contain the value for projection_y_coord and projection_x_coord (in that order; note this is y then x) for a point.
     
         An error is raised and the run terminates if any coordinate pair does not match to a location in the input grid.



``JULES_NLSIZES`` namelist members
-------------------------------------

.. nml:namelist:: JULES_NLSIZES

This namelist is used to set the number of levels in the boundary layer.


.. nml:member:: bl_levels

   :type: integer
   :default: 1

   Number of boundary layer levels. This is only used if atmospheric deposition is selected (:nml:mem:`JULES_DEPOSITION::l_deposition` = TRUE) in which case it is used to set the size of input fields.


``JULES_SURF_HGT`` namelist members
-----------------------------------

.. nml:namelist:: JULES_SURF_HGT

This namelist sets the elevation of each surface tile. Elevations can either be *relative to the gridbox mean* or *have constant elevation bands above sea-level*. 
 
If tile elevations are set relative to the gridbox mean, then the gridbox mean elevation is not required. The gridbox mean elevation is implicit in the near-surface meteorological data that are provided (higher locations will tend to be colder, have lower pressure, etc.). The elevation of each tile is used to alter the values of the air temperature and humidity (and possibly downwelling longwave, see :nml:mem:`JULES_SURFACE::l_elev_lw_down`) over that tile relative to the surface. 

If any tile uses absolute heights (i.e. :nml:mem:`JULES_SURF_HGT::l_elev_absolute_height` has at least one element that is .true.), then the gridbox mean elevation must also be supplied. This is read in from the optional :nml:lst:`JULES_Z_LAND` namelist which is described below. The model calculates elevations relative to the gridbox mean by taking the difference between the absolute elevation and the gridbox mean. 

If any tile uses absolute heights, then tile heights are set constant across a domain, regardless of whether each tile's height is specified as a relative offset or absolute. This makes it simple to set zero-offset heights for tiles that should not be considered in the elevation bands. It is no longer possible to have spatially varying tile heights if this option is used.


.. nml:member:: zero_height

   :type: logical
   :default: T

   Switch used to simplify the initialisation of tile elevation.
   
   .. note:: If :nml:mem:`JULES_SURFACE::l_aggregate` = TRUE, this switch is also set to TRUE.

   TRUE
       Set all surface tile elevations to zero. This is a very common configuration.

   FALSE
       Set surface tile heights using specified data.


.. nml:group:: Only used if :nml:mem:`zero_height` = FALSE

   .. nml:member:: l_elev_absolute_height

      :type: logical(nsurft)
      :default: F

      TRUE                                                                    
         Heights of surface tiles are absolute values above sea-level. If this option is used, then the elevation of the forcing data must also be provided (see :nml:lst:`JULES_Z_LAND` namelist below). 

      FALSE
         Surface tile heights are relative to the gridbox mean.  


   .. nml:member:: use_file

      :type: logical
      :default: T

      This indicates if surface tile heights relative to the gridbox mean should be read from a specified file or namelist. 

      TRUE
       The variable will be read from a file if the input grid consists of more than location. 
 
      FALSE
       The variable will be read from a namelist if the input grid is for a single location.  

.. nml:group:: Only used if :nml:mem:`use_file` = TRUE

   .. nml:member:: file
   
      :type: character
      :default: None
   
      The name of the file containing surface tile heights relative to the gridbox mean.                      
   
   .. nml:member:: surf_hgt_name
   
      :type: character
      :default: 'surf_hgt'
   
      The name of the variable containing surface tile heights relative to the gridbox mean. In the file, the variable must have a single levels dimension of size ``nsurft`` called :nml:mem:`JULES_INPUT_GRID::tile_dim_name`.  
   
.. nml:group:: Only used if :nml:mem:`use_file` = FALSE

   .. nml:member:: surf_hgt_io
   
      :type: real(nsurft)
      :default: None
        
      Surface tile heights relative to the gridbox mean for a single location. 
    
  
``JULES_Z_LAND`` namelist members
-----------------------------------

This is an optional namelist and only used if any surface tile has :nml:mem:`JULES_SURF_HGT::l_elev_absolute_height` = TRUE. The namelist sets values for the elevation bands and reads the elevation of the forcing data.  

.. nml:namelist:: JULES_Z_LAND

.. nml:member:: surf_hgt_band
   
   :type: real(nsurft)
   :default: None

   Spatially invariant elevation bands for each surface tile. These may be relative to the gridbox mean or absolute elevations above sea-level depending on :nml:mem:`JULES_SURF_HGT::l_elev_absolute_height`. 

.. nml:member:: use_file
 
   :type: logical
   :default: T
 
   This indicates if the elevation of the forcing data should be read from a file or from a namelist.
 
   TRUE
      The variable will be read from a file if the input grid consists of more than location.  
   FALSE
      The variable will be read from a namelist if the input grid is for a single location.   

.. nml:group:: Used if :nml:mem:`JULES_Z_LAND::use_file` = TRUE 

   .. nml:member:: file
   
      :type: character
      :default: None
   
      The name of the file containing the elevation of the forcing data.

   .. nml:member:: z_land_name
   
      :type: character
      :default: 'z_land'
   
      The name of the variable containing the elevation of the forcing data. In the file, the variable must have no level dimensions and no time dimensions.     

.. nml:group:: Used if :nml:mem:`JULES_Z_LAND::use_file` = FALSE 
 
   .. nml:member:: z_land_io
   
      :type: real
      :default: None
   
      Elevation of the forcing data for a single location.   

Example
~~~~~~~

The following gives an example of how you would set up the namelists to use elevation bands above sea-level. 

::

    &JULES_SURF_HGT

      zero_height            = .false.,

      # No elevation correction to surface tiles 1 to 6, use elevation bands for surface tiles 7 to 9
      l_elev_absolute_height = 6*.false., 3*.true.,

    /

    &JULES_Z_LAND

      # Set values for the elevation bands. 
      surf_hgt_band          = 6*0.0, 1000.0, 2000.0, 3000.0,

      # Read the WFDEI forcing data elevation from a file
      use_file               = .true.,
      file                   = 'WFDEI-elevation.nc',
      z_land_name            = 'elevation'

    /


.. _grid-examples:

Examples of grid setups
-----------------------

A single location
~~~~~~~~~~~~~~~~~

::

    &JULES_INPUT_GRID
      nx = 1,
      ny = 1
    /
    
    &JULES_LATLON
      l_coord_latlon = T
      nvars     = 2,
      var       = 'latitude','longitude',
      use_file  = .false., .false.,
      const_val = 52.168, 5.744
    /
    
    &JULES_LAND_FRAC /

    &JULES_MODEL_GRID /
    
    &JULES_SURF_HGT
      zero_height = T
    /

:nml:lst:`JULES_INPUT_GRID`
    The default value of :nml:mem:`JULES_INPUT_GRID::grid_is_1d`, FALSE, is used. This means the user has to specify the extents, :nml:mem:`JULES_INPUT_GRID::nx` and :nml:mem:`JULES_INPUT_GRID::ny`, of the input grid. Since all the input data is ASCII, no dimension names are required.

:nml:lst:`JULES_LATLON`
    The latitude and longitude of the single location are specified directly in the namelist. :nml:mem:`JULES_LATLON::nvars` = 2 indicates that the two mandatory variables will be provided, and :nml:mem:`JULES_LATLON::var` = 'latitude','longitude' confirms that these are the latitude and longitude. :nml:mem:`JULES_LATLON::use_file` = .false. indicates that the values will be read from the namelist (not from another file) and the values are provided after :nml:mem:`JULES_LATLON::const_val`.

:nml:lst:`JULES_LAND_FRAC`
    The land fraction at the single location is assumed to be 100%, so nothing is required.

:nml:lst:`JULES_MODEL_GRID`
    Use default options to select the model grid (i.e. land points only from the full input grid). In this case, this leaves the single location as the model grid.


Examples of gridded runs
~~~~~~~~~~~~~~~~~~~~~~~~

All the examples in this section assume gridded NetCDF data.

Specifying a 1D input grid
^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, input files contain data on a vector of land points. The land points dimension is called "land". The time dimension for time-varying variables is called "time". The default dimension names are used for all additional dimensions (e.g. pft, tile). ::

    &JULES_INPUT_GRID
      grid_is_1D = T,
      
      npoints = 15238,
      grid_dim_name = "land",
      
      time_dim_name = "time"
    /

Specifying a 2D input grid
^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, input files contain data on a 2D latitude/longitude grid. The x dimension is called "lon" and the y dimension is called "lat". The time dimension for time-varying variables is called "time". Variables with an extra tiles dimension use the dimension name "pseudo" for that dimension. All other additional dimensions use their default names. ::

    &JULES_INPUT_GRID
      grid_is_1D = F,

      nx = 96,
      ny = 56,

      x_dim_name = "lon",
      y_dim_name = "lat",

      tile_dim_name = "pseudo",

      time_dim_name = "time"
    /
    
Specifying a subgrid using a given range of latitude and longitude
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can be used with either a 1D or 2D input grid. ::

    &JULES_LATLON
      l_coord_latlon = T,
      nvars     = 2,
      var       = 'latitude','longitude',
      use_file  = .true., .true.,
      file      = 'lat_lon.nc',
    /
    
    &JULES_LAND_FRAC
      file = 'land_mask.nc',

      land_frac_name = 'land_frac'
    /
    
    &JULES_MODEL_GRID
      land_only = F,

      use_subgrid = T,

      l_bounds = T,

      y_bounds = 55.0  57.0,
      x_bounds = -5.0  -3.0
    /

This setup reads latitude, longitude and land fraction for each gridbox in the full input grid (1D or 2D) from the named variables in the specified files.

In :nml:lst:`JULES_MODEL_GRID`, :nml:mem:`JULES_MODEL_GRID::use_subgrid` indicates that a subset of the input grid will be selected as the model grid. :nml:mem:`JULES_MODEL_GRID::l_bounds` then indicates that latitude and longitude bounds will be used to select the subgrid. :nml:mem:`JULES_MODEL_GRID::land_only` = FALSE means that sea and sea-ice points will remain in the model grid if any are selected. The model grid will then be a vector containing the selected points (those that fall within the latitude/longitude bounds), even if those points could be used to form a rectangular region.
    
Specifying a subgrid using a given range of projection coordinates (not latitude and longitude)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can be used with either a 1D or 2D input grid. ::

    &JULES_LATLON
      l_coord_latlon = F,
      nvars     = 4,
      var       = 'latitude','longitude','projection_x_coord','projection_y_coord'
      use_file  = .true., .true., .true., .true.,
      file      = 'lat_lon.nc',
    /
    
    &JULES_LAND_FRAC
      file = 'land_mask.nc',

      land_frac_name = 'land_frac'
    /
    
    &JULES_MODEL_GRID
      land_only = F,

      use_subgrid = T,

      l_bounds = T,

      y_bounds = 500.0  40500.0,
      x_bounds = 25500.0 55500.0
    /

In this setup :nml:mem:`JULES_LATLON::l_coord_latlon` = FALSE indicates that data will be read from a grid that is not defined by latitude and longitude - rather it uses other projection coordinates such as the northings and eastings of the Ordnance Survey (British) National Grid (BNG) OSGB36. The projection coordinates are read via the variables projection_x_coord and projection_y_coord. Note that the latitude and longitude of each point is also read in; JULES includes these in output files for reference, and they can also be required by the science code (e.g. for solar zenith angle).

In :nml:lst:`JULES_MODEL_GRID`, :nml:mem:`JULES_MODEL_GRID::use_subgrid` indicates that a subset of the input grid will be selected as the model grid. :nml:mem:`JULES_MODEL_GRID::l_bounds` then indicates that bounding values of the projection coordinates will be used to select the subgrid. :nml:mem:`JULES_MODEL_GRID::land_only` = FALSE means that sea and sea-ice points will remain in the model grid if any are selected. The model grid will then be a vector containing the selected points (those that fall within the latitude/longitude bounds), even if those points could be used to form a rectangular region.

Specifying a subgrid using a list of points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can be used with either a 1D or 2D input grid. ::

    &JULES_LATLON
      l_coord_latlon = T,
      nvars     = 2,
      var       = 'latitude','longitude',
      use_file  = .true., .true.,
      file      = 'lat_lon.nc',
    /

    &JULES_LAND_FRAC
      file = 'land_mask.nc',

      land_frac_name = 'land_frac'
    /

    &JULES_MODEL_GRID
      use_subgrid = T,

      l_bounds = F,

      npoints = 4,
      points_file = 'points.txt'
    /
    
This setup reads latitude, longitude and land fraction for each gridbox in the full input grid (1D or 2D) from the named variables in the specified files.

In :nml:lst:`JULES_MODEL_GRID`, :nml:mem:`JULES_MODEL_GRID::use_subgrid` indicates that a subset of the input grid will be selected as the model grid. :nml:mem:`JULES_MODEL_GRID::l_bounds` then indicates that a list of latitudes and longitudes will be used to select the subgrid. :nml:mem:`JULES_MODEL_GRID::land_only` is not given, meaning it takes its default value, TRUE. This means that any sea or sea-ice points specified in the list of points will be discarded. The model grid will then be a vector
containing the selected points (those with the given latitude/longitude).

Assuming that the input grid is a 1 degree grid and the latitude and longitude are given at the centre of the gridbox, ``points.txt`` should look like the following::

    55.5  -4.5
    55.5  -3.5
    56.5  -4.5
    56.5  -3.5

The only configuration that yields a 2D model grid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    &JULES_INPUT_GRID
      grid_is_1d = F,

      nx = 96,
      ny = 56,
      
      # ...
    /

    &JULES_LATLON
      # <specified from file>
    /
    
    &JULES_LAND_FRAC
      # <specified from file>
    /

    &JULES_MODEL_GRID
      land_only = F
    /

In general, the only configuration that yields a 2D model grid is:

* 2D input grid
* The model grid is the full input grid, including any non-land points

If the input grid is a 2D region where every point is land (i.e. not the whole globe), then :nml:mem:`JULES_MODEL_GRID::land_only` = TRUE would also yield a 2D model grid. If any options are set that mean some points from the input grid are not modeled, the model grid will be a vector of points. Computationally, this makes no difference.
