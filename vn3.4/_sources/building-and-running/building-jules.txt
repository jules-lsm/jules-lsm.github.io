Building JULES
==============

As of version 3.2, JULES executables can now be built in one of two ways:

* Using FCM, a code management and build system developed by the Met Office with a particular focus on simplifying the process of building large Fortran programs.
* The "traditional" way using make, a well known utility for building software.

Using FCM is of particular benefit to developers of JULES. As part of the build process, FCM will analyse the dependencies of every Fortran file and automatically compile them in the correct order. With make, a ``Makefile`` is required in every source directory that lists the dependencies manually (e.g. ``src/science/surface/Makefile``). These are automatically generated for the official JULES releases, but must be manually modified during the development process to ensure compilation of new routines happens in the correct order (sometimes this just happens by luck!).

See the following for more information on building JULES using your preferred build system:

.. toctree::
   :maxdepth: 1
   
   fcm
   make
