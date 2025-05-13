from numpy.typing import NDArray 
import pandas as pd
import numpy as np
import jax.numpy as jnp
import jax.random as jrd
import numpyro
from numpyro import distributions as dist
from cntmosaic.dataloader.restru_loaders import GeneralLoader, HyperParams
from dataclasses import dataclass

from ._BRC import BRC
from .priors import HSGP2D

    
class restr_BRCfine(BRC):
    """Bayesian Rate Consistency model with fine participant age, fine contact age inputs.

    Parameter
    ----------
    data: GeneralLoader
        Loaded GeneralLoader object
        
    References
	----------
	Shozen Dan et al., "Estimating fine age structure and time trends in 
	human contact patterns from coarse contact data: The Bayesian rate consistency model",
	PLoS Computational Biology. 2023
    """
    def __init__(self, data: GeneralLoader):
        pass
   
    def _set_default_params(self):
        """
        Initialize default model parameters for the contact intensity prior.

        This method sets reasonable default values for hyperparameters used in the 
        low-rank Gaussian Process (HSGP) approximation and the prior distributions 
        for model parameters. These values are chosen to provide a good starting 
        point for most use cases.

        Default Parameters
        ------------------
        M : list[int]
            Number of basis functions used for the HSGP approximation along each axis.
            Default is [30, 30].
        C : list[float]
            Boundary factors defining the domain limits of the Gaussian Process.
            Default is [1.5, 1.5].
        grid_type : str
            Type of grid used to model the contact dynamics. Can be 'age-age' or 'diff-age'.
            Use 'diff-age' if the dynamics are believed to depend primarily on the age difference.
            Default is 'age-age'.
        likelihood : str
            Likelihood model for observed contact counts. Default is 'negbin' (Negative Binomial).
            Available likelihood includes 'negbin', 'poisson'
        offset : array-like or None
            Optional additive offset to contact intensity. Should match the shape of the age grid.
            Default is None.

        Priors
        ------
        beta0 : Normal
            Prior for the baseline log-intensity parameter. Default is Normal(0, 10).
        alpha : InverseGamma
            Prior for the magnitude of the Gaussian Process. Default is InverseGamma(5, 5).
        rho : InverseGamma (expanded to 2D)
            Prior for the length scales of the Gaussian Process in each dimension.
            Default is InverseGamma(5, 5) expanded to shape [2].

        HSGP2D
        ------
        hsgp : HSGP2D
            A low-rank GP approximation initialized using the specified `M`, `C`, and `grid_type`.

        Notes
        -----
        These defaults are recommended for general use. However, all parameters and priors 
        can be modified after initialization as needed.
        """
        pass
        
    def model(self):
        """
        Define the probabilistic model for contact intensity estimation using a 
        low-rank Gaussian Process approximation (HSGP) within a Bayesian framework.

        This method is intended to be used with NumPyro for probabilistic inference. 
        It models contact counts using either a Poisson or Negative Binomial likelihood, 
        depending on the specified setting in `self.params.likelihood`.

        The latent log contact intensity is composed of:
        - A global intercept term `beta0`
        - A structured latent function `f` sampled from the HSGP prior
        - A log-contact matrix `log_P` representing expected structure in contact dynamics
        - An optional offset term applied multiplicatively on the rate scale

        Raises
        ------
        NotImplementedError
            If the `DataLoader.precompute()` step has not been completed or if 
            an unsupported likelihood is specified.

        Sampling Parameters
        -------------------
        beta0 : float
            Global intercept sampled from the prior specified in `params.prior['beta0']`.
        f : array
            Structured latent effect sampled from HSGP prior, depending on priors for `alpha` and `rho`.
        inv_disp : float, optional
            Inverse dispersion parameter for Negative Binomial likelihood. Sampled from Exponential(1).

        Deterministic Outputs
        ---------------------
        log_rate : array
            Sum of beta0 and latent GP term.
        log_cint : array
            Log contact intensity, adjusted with log_P and optional offset.

        Likelihood
        ----------
        Poisson:
            If `params.likelihood == 'poisson'`, observed contact counts `y` are modeled as:
                obs ~ Poisson(exp(log_cint + log_N))

        Negative Binomial:
            If `params.likelihood == 'negbin'`, the model uses:
                obs ~ NegativeBinomial2(mean=mu, concentration=inv_disp)

        Notes
        -----
        The precomputed data (`_precompute`) must include:
        - `y` : observed counts
        - `aid`, `bid` : indices into the contact matrix
        - `log_P`, `log_N` : known covariates or exposure matrices

        This model must be run within a NumPyro inference context (e.g., MCMC or SVI).
        """
        pass