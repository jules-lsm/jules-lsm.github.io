``model_grid.nml``
==================


This file sets up the grid configuration for the run. It contains five namelists - :nml:lst:`JULES_INPUT_GRID`, :nml:lst:`JULES_LATLON`, :nml:lst:`JULES_LAND_FRAC`, :nml:lst:`JULES_MODEL_GRID` and :nml:lst:`JULES_SURF_HGT`.

Each run of JULES involves two grids: the input grid and the model grid. The input grid is the grid on which all input data are held. The model grid is the set of points on which the model is run. The model grid is the grid of points that will be processed by JULES, and is a subset of the input grid.

As discussed in :doc:`/input/principles`, the input grid consists of three pieces of information:

#. Whether the grid is 1D or 2D.
#. The size of each dimension.
#. The name of each dimension in the input file(s).

The latitude, longitude and land fraction of each point are then read in on the full input grid as specified by the namelists. A subset of the input grid to use as the model grid can then be specified in various ways described below (e.g. land points only, all points within certain latitude/longitude bounds).

In most cases, the model grid will be represented internally as a vector of points, even when the input grid is 2D and the model grid is a rectangular sub-region. The only time that the model grid will be represented by a 2D grid is when the input grid is 2D and the model grid is the whole input grid. Numerically, this makes no difference.


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
   
      The name of the x dimension.                                                
   
      .. note:: For ASCII files, this can be anything. For NetCDF files, it  should the name of the dimension in input file(s).
   
   
   .. nml:member:: y_dim_name
   
      :type: character
      :default: "y"
   
      The name of the y dimension.                                                
   
      .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).
   
   
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

   The dimension name used when variables have an additional dimension of size :nml:mem:`JULES_MODEL_LEVELS::npft`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: nvg_dim_name

   :type: character
   :default: "nvg"

   The dimension name used when variables have an additional dimension of size  :nml:mem:`JULES_MODEL_LEVELS::nnvg`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: type_dim_name

   :type: character
   :default: "type"

   The dimension name used when variables have an additional dimension of size  ``ntype``.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: tile_dim_name

   :type: character
   :default: "tile"

   The dimension name used when variables have an additional dimension of size  ``ntiles``.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: soil_dim_name

   :type: character
   :default: "soil"

   The dimension name used when variables have an additional dimension of size  :nml:mem:`JULES_MODEL_LEVELS::sm_levels`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: snow_dim_name

   :type: character
   :default: "snow"

   The dimension name used when variables have an additional dimension of size  :nml:mem:`JULES_MODEL_LEVELS::nsmax`.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).


.. nml:member:: scpool_dim_name

   :type: character
   :default: "scpool"

   The dimension name used when variables have an additional dimension of size  ``dim_cs1``.

   .. note:: For ASCII files, this can be anything. For NetCDF files, it should the name of the dimension in input file(s).



``JULES_LATLON`` namelist members
---------------------------------

.. nml:namelist:: JULES_LATLON

.. nml:group:: Used when input grid consists of a single location (1D and :nml:mem:`JULES_INPUT_GRID::npoints` = 1 or 2D and :nml:mem:`JULES_INPUT_GRID::nx` = :nml:mem:`JULES_INPUT_GRID::ny` = 1

   .. nml:member:: latitude
    
      :type: real
      :default: None
   
      The latitude of the single grid location.                                   


   .. nml:member:: longitude
   
      :type: real
      :default: None
   
      The longitude of the single grid location.                                  


.. nml:group:: Used for any input grid with more than a single location

   .. nml:member:: file
    
      :type: character
      :default: None
   
      The name of the file to read latitude and longitude from.                   
   
   
   .. nml:member:: lat_name
   
      :type: character
      :default: None
   
      The name of the variable containing the latitude data.                      
   
      In the file, the variable must have no levels dimensions and no time dimension.
   
   
   .. nml:member:: lon_name
   
      :type: character
      :default: None
   
      The name of the variable containing the longitude data.                     
   
      In the file, the variable must have no levels dimensions and no time dimension.



``JULES_LAND_FRAC`` namelist members
------------------------------------

.. nml:namelist:: JULES_LAND_FRAC

Land fraction is the fraction of each gridbox that is land. Currently, JULES considers any gridbox with land fraction > 0 to be 100% land, and all others to be 100% sea (or sea-ice). Land fraction data can be used to select only land points from the full input grid (see below).

.. warning::
   When the input grid consists of a single location (1D and :nml:mem:`JULES_INPUT_GRID::npoints` = 1 or 2D and :nml:mem:`JULES_INPUT_GRID::nx` = :nml:mem:`JULES_INPUT_GRID::ny` = 1), that single location is assumed to be 100% land.
   
For any input grid with more than a single location, the following are used:


.. nml:member:: file

   :type: character
   :default: None

   The name of the file to read land fraction data from.                       


.. nml:member:: land_frac_name

   :type: character
   :default: None

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


.. nml:member:: use_subgrid

   :type: logical
   :default: F

   TRUE                                                                        
       The model grid is a subset of the full input grid, specified using some valid combination of the options below.

   FALSE
       The model grid is the full input grid.


.. nml:group:: Only used if :nml:mem:`use_subgrid` = TRUE

   .. nml:member:: latlon_region
   
      :type: logical
      :default: None
   
      TRUE                                                                        
          Subset of points to model will be selected using latitude and longitude bounds.
   
      FALSE
          Subset of points to model will be selected using a list of latitude and longitude for each point.
   
   
   .. nml:group:: Only used if :nml:mem:`latlon_region` = TRUE
   
      .. nml:member:: lat_bounds
      
         :type: real(2)
         :default: None
      
         The lower and upper bounds (in that order) for the latitude to use. The model grid will only contain points where ``lat_bounds(1) <= latitude <= lat_bounds(2)``.
       
       
      .. nml:member:: lon_bounds
      
         :type: real(2)
         :default: None
      
         The lower and upper bounds (in that order) for the longitude to use. The model grid will only contain points where ``lon_bounds(1) <= longitude <= lon_bounds(2)``.
   
   
   
   .. nml:group:: Only used if :nml:mem:`latlon_region` = FALSE
   
      .. nml:member:: npoints
   
         :type: integer
         :permitted: >= 1
         :default: 0
      
         The number of points to model.
         
      
      .. nml:member:: points_file
      
         :type: character
         :default: None
      
         The name of the file containing the latitude and longitude for each point.  
     
         Each line in the file should contain the latitude and longitude (in that  order) for a point.



``JULES_SURF_HGT`` namelist members
-----------------------------------

.. nml:namelist:: JULES_SURF_HGT

This namelist sets the elevation of each surface tile, *relative to the gridbox mean elevation*. Note that the gridbox mean elevation is not required anywhere in JULES but is implicit in the near-surface meteorological data that are provided (higher locations will tend to be colder, have lower pressure, etc.). The elevation of each tile is used to alter the values of the air temperature and humidity over that tile. All tile elevations must be greater than zero, i.e. tile can only be higher than the gridbox average, because the assumptions used to alter the air temperature and humidity only hold for moving to higher elevations. For many applications, the tile elevation can be set to zero.


.. nml:member:: zero_height

   :type: logical
   :default: T

   Switch used to simplify the initialisation of tile elevation.
   
   .. note:: If :nml:mem:`JULES_SWITCHES::l_aggregate` = TRUE, this switch is also set to TRUE.

   TRUE
       Set all tile elevations to zero. This is a very common configuration.

   FALSE
       Set tile heights using specified data.


.. nml:group:: Used if :nml:mem:`zero_height` = FALSE and the input grid consists of a single location

   .. nml:member:: surf_hgt_io
   
      :type: real(ntiles)
      :default: None
   
      The tile elevations for each tile for the single location.                  


.. nml:group:: Used if :nml:mem:`zero_height` = FALSE and the input grid consists of more than one location

   .. nml:member:: file
   
      :type: character
      :default: None
   
      The name of the file to read tile elevation data from.                      
   
   .. nml:member:: surf_hgt_name
   
      :type: character
      :default: None
   
      The name of the variable containing the tile elevation data.                
   
      In the file, the variable must have a single levels dimension of size ``ntiles`` called :nml:mem:`JULES_INPUT_GRID::tile_dim_name`.



.. _grid-examples:

Examples
--------

ASCII data at a single location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    &JULES_INPUT_GRID
      nx = 1,
      ny = 1
    /
    
    &JULES_LATLON
      latitude  = 52.168,
      longitude = 5.744
    /
    
    &JULES_LAND_FRAC /

    &JULES_MODEL_GRID /
    
    &JULES_SURF_HGT
      zero_height = T
    /

:nml:lst:`JULES_INPUT_GRID`
    The default value of :nml:mem:`JULES_INPUT_GRID::grid_is_1d`, FALSE, is used. This means the user has to specify the extents, :nml:mem:`JULES_INPUT_GRID::nx` and :nml:mem:`JULES_INPUT_GRID::ny`, of the input grid. Since all the input data is ASCII, no dimension names are required.

:nml:lst:`JULES_LATLON`
    The latitude and longitude of the single location are specified directly in the namelist.

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
      file = 'lat_lon.nc',
      
      lat_name = 'latitude',
      lon_name = 'longitude'
    /
    
    &JULES_LAND_FRAC
      file = 'land_mask.nc',

      land_frac_name = 'land_frac'
    /
    
    &JULES_MODEL_GRID
      land_only = F,

      use_subgrid = T,

      latlon_region = T,

      lat_bounds = 55.0  57.0,
      lon_bounds = -5.0  -3.0
    /

This setup reads latitude, longitude and land fraction for each gridbox in the full input grid (1D or 2D) from the named variables in the specified files.

In :nml:lst:`JULES_MODEL_GRID`, :nml:mem:`JULES_MODEL_GRID::use_subgrid` indicates that a subset of the input grid will be selected as the model grid. :nml:mem:`JULES_MODEL_GRID::latlon_region` then indicates that latitude and longitude bounds will be used to select the subgrid. :nml:mem:`JULES_MODEL_GRID::land_only` = FALSE means that sea and sea-ice points will remain in the model grid if any are selected. The model grid will then be a vector containing the selected points (those that fall within the latitude/longitude bounds), even if those points could be used to form a rectangular region.

Specifying a subgrid using a list of points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can be used with either a 1D or 2D input grid. ::

    &JULES_LATLON
      file = 'lat_lon.nc',

      lat_name = 'latitude',
      lon_name = 'longitude'
    /

    &JULES_LAND_FRAC
      file = 'land_mask.nc',

      land_frac_name = 'land_frac'
    /

    &JULES_MODEL_GRID
      use_subgrid = T,

      latlon_region = F,

      npoints = 4,
      points_file = 'points.txt'
    /
    
This setup reads latitude, longitude and land fraction for each gridbox in the full input grid (1D or 2D) from the named variables in the specified files.

In :nml:lst:`JULES_MODEL_GRID`, :nml:mem:`JULES_MODEL_GRID::use_subgrid` indicates that a subset of the input grid will be selected as the model grid. :nml:mem:`JULES_MODEL_GRID::latlon_region` then indicates that a list of latitudes and longitudes will be used to select the subgrid. :nml:mem:`JULES_MODEL_GRID::land_only` is not given, meaning it takes its default value, TRUE. This means that any sea or sea-ice points specified in the list of points will be discarded. The model grid will then be a vector
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
