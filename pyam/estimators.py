import numpy as np
from scipy import optimize


class Estimator(object):
    """Class for estimating a model given some data."""

    def __init__(self, solver, data):
        self.solver = solver
        self.data = data

    def _objective(self, params, observed):
        domain = [self.solver.problem.input1.lower, self.solver.problem.input1.upper]
        initial_coefs = self.solver._coefs_array_to_dict(self.solver.result.x, self.solver.degrees)
        self.solver.solve(kind="Chebyshev",
                          coefs_dict=initial_coefs,
                          domain=domain,
                          method='hybr')
        return least_squares_objective(observed, predicted)

    @staticmethod
    def least_squares_objective(observed, predicted):
        residuals = observed - predicted
        return 0.5 * np.sum(residuals**2)

    def estimate(self, initial_params, **solver_opts):
        result = optimize.minimize(initial_params,
                                   self._objective,
                                   args=(self.data,),
                                   **solver_opts)
        return result
