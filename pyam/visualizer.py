import pandas as pd

import pycollocation


class Visualizer(pycollocation.Visualizer):
    """Class for visualizing various functions of the solution to the model."""

    __complementarities = ['Fxy', 'Fxl', 'Fxr', 'Fyl', 'Fyr', 'Flr']

    __partials = ['F', 'Fx', 'Fy', 'Fl', 'Fr']

    @property
    def _complementarities(self):
        """Dictionary mapping a complementarity to a callable function."""
        tmp = {}
        for complementarity in self.__complementarities:
            expr = eval("self.solver.problem." + complementarity)
            tmp[complementarity] = self.solver.problem._lambdify_factory(expr.subs(self.solver.problem._subs))

        return tmp

    @property
    def _factor_payments(self):
        """Dictionary mapping a factor payment to a callable function."""
        tmp = {}
        for payment in ["factor_payment_1", "factor_payment_2"]:
            expr = eval("self.solver.problem." + payment)
            tmp[payment] = self.solver.problem._lambdify_factory(expr)

        return tmp

    @property
    def _partials(self):
        """Dictionary mapping a partial derivative to a callable function."""
        tmp = {}
        for partial in self.__partials:
            expr = eval("self.solver.problem." + partial)
            tmp[partial] = self.solver.problem._lambdify_factory(expr.subs(self.solver.problem._subs))

        return tmp

    @property
    def _solution(self):
        """Return the solution stored as a dict of NumPy arrays."""
        tmp = super(Visualizer, self)._solution

        # list of tuples!
        derivatives = (self._complementarities.items() + self._partials.items() +
                       self._factor_payments.items())

        for derivative, function in derivatives:
            values = function(self.interpolation_knots,
                              tmp['mu'].values,
                              tmp['theta'].values,
                              *self.solver.problem.params.values())
            tmp[derivative] = pd.Series(values, index=self.interpolation_knots)

        return tmp
