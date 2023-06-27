.. JULES (Joint UK Land Environment Simulator) documentation master file, created by
   sphinx-quickstart on Thu Mar 21 11:40:02 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

======================================================
Joint UK Land Environment Simulator (JULES) User Guide
======================================================


The Joint UK Land Environment Simulator (JULES) is a computer model that simulates many soil and vegetation processes. This guide primarily describes the format of the input and output files, and does not include detailed descriptions of the science and representation of the processes in the model.

The first version of JULES was based on the Met Office Surface Exchange System (MOSES), the land surface model used in the `Unified Model <http://www.metoffice.gov.uk/research/modelling-systems/unified-model>`_ (UM) of the `UK Met Office <http://www.metoffice.gov.uk>`_. After that initial split, the MOSES and JULES code bases evolved separately, but with JULES v2.1 these differences were reconciled with the UM. As of JULES v3.1, a single code repository is used for both standalone JULES and JULES in the UM.

Further information can be found on the JULES website: http://jules.jchmr.org/.


.. toctree::
   :maxdepth: 1
   :numbered:
   
   release_notes/contents
   overview/intro
   building-and-running/intro
   input/overview
   output
   namelists/contents
   examples
   code/contents
   output-variables

