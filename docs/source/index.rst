cntmosaic Documentation
=======================
What is Contact Mosaic?
-----------------------
Contact Mosaic (``cntmosaic``) is a Python package for analysing social contact patterns from 
social contact data. It provides a set of tools to process, analyse, simulate, and visualise social contact data.
It also provides a set of models to infer social contact matrices from real world social contact data.
The models in ``cntmosaic`` are implemented using the probabilistic programming language `Numpyro <https://num.pyro.ai/en/stable/index.html>`_ which allows for
both Hamiltonian Monte Carlo (HMC) based full Bayesian inference and fast stochastic variational inference (SVI).

.. toctree::
   :maxdepth: 2
   :caption: Package Modules:
   
   modules/analysis
   modules/dataloader
   modules/vis
   modules/utils
   modules/tutorial
   modules/models

Indices and Tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`