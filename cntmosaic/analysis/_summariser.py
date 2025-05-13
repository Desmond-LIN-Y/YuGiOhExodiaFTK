import numpy as np
import jax

class ModelSummariserMCMC:
    '''
    Basic Model implementation only
    '''
    pass
        
    def summarise_rate(self, probs: tuple=(0.025, 0.5, 0.975)):
        """Summarise the posterior contact rate
        
        Parameters
        ----------
        probs : tuple
            The quantiles to compute
        
        Returns
        -------
        dict
            A dictionary containing the quantiles of the posterior contact rate
        """
        pass
        
    def summarise_cint(self, probs: tuple=(0.025, 0.5, 0.975)):
        """Summarise the posterior contact intensity
        
        Parameters
        ----------
        probs : tuple
            The quantiles to compute
        
        Returns
        -------
        dict
            A dictionary containing the quantiles of the posterior contact intensity
        """
        pass
            
    def summarise_mcint(self, probs: tuple=(0.025, 0.5, 0.975)):
        """Summarise the posterior marginal contact intensity
        
        Parameters
        ----------
        probs : tuple
            The quantiles to compute
        
        Returns
        -------
        dict
            A dictionary containing the quantiles of the posterior marginal contact intensity
        """
        pass


class ModelSummariserSVI:
    def __init__(self, model):
        pass
        
    def get_post_predictive(self):
        """
        Get the posterior predictive distribution of the model.
        This is a wrapper around the model's posterior_predictive_svi method.
        It uses the model's guide to sample from the posterior predictive distribution.
        The guide is a variational approximation to the posterior distribution.
        """
        pass
    
    def get_post_predictive_cint(self):
        pass
        
    def summarise_rate(self, probs: tuple = (0.025, 0.5, 0.975)):
        """
        Summarise the rate parameter of the model.
        This is a wrapper around the model's summarise_rate method.
        It uses the model's posterior predictive distribution to compute the summary statistics.
        """
        pass

    def summarise_cint(self, probs: tuple = (0.025, 0.5, 0.975)):
        """
        Summarise the contact intensity matrix of the model.
        It uses the model's posterior predictive distribution to compute the summary statistics.
        """
        pass

    def summarise_mcint(self, probs: tuple = (0.025, 0.5, 0.975)):
        """
        Summarise the marginal contact intensity of the model.
        It uses the model's posterior predictive distribution to compute the summary statistics.
        """
        pass

class ModelSummariserSocialMix:
  def __init__(self, sm):
    self.sm = sm
    
  def summarise_rate(self, probs: tuple = (0.025, 0.5, 0.975)):
    """
    Summarise the contact rate matrix.
    """
    pass
      
  def summarise_cint(self, probs: tuple = (0.025, 0.5, 0.975)):
    """
    Summarise the contact intensity matrix.
    """
    pass
      
  def summarise_mcint(self, probs: tuple = (0.025, 0.5, 0.975)):
    """
    Summarise the marginal contact intensity of the model.
    """
    pass