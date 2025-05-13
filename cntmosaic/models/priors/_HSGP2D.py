import numpy as np
from numpy.typing import NDArray
import jax.numpy as jnp

import numpyro
from numpyro import distributions as dist
from numpyro.contrib.hsgp.laplacian import eigenfunctions
from numpyro.contrib.hsgp.spectral_densities import diag_spectral_density_matern

from ._Prior2D import Prior2D

from .._utils import (
    age_age_grid,
    diff_age_age_grid,
    lower_tri_indices,
    symmetrize_from_lower_tri
)

from .._math import (
    inverse_alr,
    inverse_clr,
    inverse_ilr,
)

class HSGP2D(Prior2D):
    """Class for sampling from a 2 dimensional Hilbert space approximate Gaussian process (HSGP).
    
    Parameters
    ----------
    C: int | list[float], default=[1.5, 1.5]
		The boundary condition of the approximation.
    M: int | list[int], default=[30, 30]
		The number of eigenfunctions to use.
    grid_type: str, default='age-age'
        The type of grid to use. Options are 'age-age' and 'diff-age'.
    loc: float, default=0
        The mean or mean function of the HSGP.
    event_dim: int, default=1
        The number of dimensions of the event.
    transform: str | None, default=None
        The transformation to apply to the HSGP. Options are 'alr', 'clr', and 'ilr'.
    symmetric: bool, default=False
		Whether the sampled matrix should be symmetric.
    """
    def __init__(self,
                 C: float | list[float] = [1.5, 1.5],
                 M: int | list[int] = [30, 30],
                 grid_type: str='age-age',
                 loc: float=0,
                 event_dim: int=1,
                 transform: str | None=None,
                 symmetric: bool=False):
        super().__init__(grid_type, loc, event_dim, transform)
        self.C = C
        self.M = M
        self.symmetric = symmetric

    def set_age_bounds(self, min_age: int, max_age: int):
        pass
    
    def _set_grid(self):
        pass
    def _make_eigenfunctions(self):
        pass
  
    def sample(self, alpha, rho):
        """Sample from the HSGP."""
        raise NotImplementedError