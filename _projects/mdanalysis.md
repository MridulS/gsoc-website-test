---
desc: "Analyize Molecular Dynamics Simulations"
markdown: mdanalysis.md
name: "MDAnalysis"
ideaslist: "https://www.mdanalysis.org/ideas"
logo_url: "https://www.mdanalysis.org/public/mdanalysis-logo_square.png"
organization_url: "https://mdanalysis.org"
email: "https://groups.google.com/forum/#!forum/mdnalysis-devel"
contributing: "https://github.com/MDAnalysis/mdanalysis/wiki/Guide-for-Developers"
status: "affiliated"
tags:
  - Python
  - Biology
  - Physics
  - Chemistry
  - Cython
---

MDAnalysis is an object-oriented Python library to analyze trajectories from
molecular dynamics (MD) simulations in many popular formats. It can write most
of these formats, too, together with atom selections suitable for visualization
or native analysis tools.

MDAnalysis allows one to read particle-based trajectories (including individual
coordinate frames such as biomolecules in the PDB format) and access the atomic
coordinates through NumPy arrays. This provides a flexible and relatively fast
framework for complex analysis tasks. In addition, powerful atom selection
commands are implemented. Trajectories can also be manipulated (for instance,
fit to a reference structure) and written out. The basic example demonstrates
some of these features.
