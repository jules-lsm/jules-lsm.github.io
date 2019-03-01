General principles
==================

JULES supports the input and output of gridded data on both 1D (e.g. vector of land points) and 2D (e.g. latitude/longitude) grids, with zero or more additional 'levels' dimensions (e.g. for soil layers). A 2D grid is the usual way to think about gridded data, i.e. with x and y dimensions; however a 1D grid can be more flexible and space-efficient. An example of a 1D grid is a land-points-only grid (as used in the GSWP2 and WATCH datasets). In this case, these data are supplied as a vector of land points, which avoids storing information about sea and sea-ice points that are not being processed.

In JULES, the input grid is comprised of the following information:

#. Whether the grid is 1D or 2D (ASCII or NetCDF).
#. The size of each grid dimension (ASCII or NetCDF).
#. The name of each dimension in the file(s) (NetCDF only).

The input grid is specified by the user in the namelist :nml:lst:`JULES_INPUT_GRID`. The model grid is then constructed by selecting the desired points from this input grid, the default being that only the land points in the input grid will be processed. All output is on the model grid.

.. note::
   All input data must use the same grid, including any ancillaries and initial conditions.

JULES infers the format of input files from the file extension. The recognised file extensions are:

ASCII files
    ``.asc``, ``.txt`` and ``.dat``

NetCDF files
    ``.nc`` and ``.cdf``