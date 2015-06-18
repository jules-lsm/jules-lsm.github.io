JULES examples
==============

JULES comes with several examples, which can be found in the ``examples`` directory. These show how to set up the namelist files for various situations. The provided examples are:

``point_loobos``
    A single point simulation forced with weather station data. This run requires a single input file (meteorological data) that is also included as part of the JULES distribution, in the ``loobos`` directory. This is a working example.

``point_loobos_esm``
    \ 
    
``point_loobos_euro4``
    \ 
    
``point_loobos_forecast``
    \ 

``point_loobos_gl4.0``
    \ 

``point_loobos_ukv``
    Versions of the ``point_loobos`` example, each set up to use a different :doc:`science configuration </science-configurations>`. These are all working examples.

``point_VL92_1T``
    \ 

``point_VL92_2T``
    \ 

``point_VL92_M``
    Single point simulations that include the urban land surface types, forced with weather station data (although no data is provided). They are given as examples of setting up the three urban schemes - the original one tile urban scheme, the simple two-tile urban scheme (URBAN-2T) and MORUSES respectively.

``grid_gswp2``
    A gridded domain simulation forced with GSWP2 weather data. This run requires a large amount of data that is not distributed with JULES, and merely serves as an example of how to set up a run with a gridded domain. A version of the GSWP2 data is distributed with the JULES benchmarking suite, as well as working distributed runs.

Further examples of JULES runs can be seen in the JULES benchmarking suite.
