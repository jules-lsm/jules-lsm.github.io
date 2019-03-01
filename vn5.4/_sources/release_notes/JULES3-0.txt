JULES version 3.0 Release Notes
===============================


The major change in version 3.0 is the introduction of the IMOGEN impacts tool. IMOGEN is a system where JULES is gridded on to surface land points, and is forced with an emulation of climate change using "pattern-scaling" calibrated against the Hadley Centre GCM. This climate change impacts system has the advantage that:

* The pattern-scaling allows estimates of climate change for a broad range of emissions scenarios.
* New process understanding can be tested for its global implications.
* New process understanding can also be checked for stability before full inclusion in a GCM.
* By adding climate change anomalies to datasets such as the CRU dataset, then GCM biases can be removed.
  
It must be recognised that the system is "off-line", and so if major changes to the land surface occur there might be local and regional feedbacks that can only be predicted using a fully coupled GCM. Hence IMOGEN doesn't replace GCMs, but it does give a very powerful first-look as to potential land surface changes in an anthropogenically forced varying climate. This was accomplished with help from Mark Lomas at the University of Sheffield and Chris Huntingford at CEH.

There are also several small bug fixes:

* A fix effecting fluxes in `sf_stom` from Lina Mercado at CEH. This bug fix was announced on the mailing list.
* Small fixes for potential evaporation and canopy snow depth from the UM.
* A small issue with some memory not being deallocated at the end of a run.
