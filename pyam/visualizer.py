import pandas as pd

import pycollocation


class Visualizer(pycollocation.Visualizer):
    """Class for visualizing various functions of the solution to the model."""

    __complementarities = ['Fxy', 'Fxl', 'Fxr', 'Fyl', 'Fyr', 'Flr']

    __partials = ['F', 'Fx', 'Fy', 'Fl', 'Fr']

    __solution = None

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
        if self.__solution is None:
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

            self.__solution = tmp

        return self.__solution

    @property
    def _soln_with_theta_frequency(self):
        """Solution including the density for theta."""
        tmp_df = self.solution.sort('theta', ascending=True, inplace=False)
        tmp_df['theta_frequency'] = self.solver.problem.input1.evaluate_pdf(tmp_df.index.values) / tmp_df.theta
        return tmp_df

    @property
    def factor_payment_1_cdf(self):
        """
        Cumulative distribution function (cdf) for factor payments to input 1.

        :getter: Return the current cdf.
        :type: pandas.Series

        """
        return self.compute_cdf(self.factor_payment_1_pdf)

    @property
    def factor_payment_1_pdf(self):
        """
        Probability density function (pdf) for factor payments to input 1.

        :getter: Return the current pdf.
        :type: pandas.Series

        """
        tmp_df = self._soln_with_theta_frequency.sort('factor_payment_1',
                                                      ascending=True,
                                                      inplace=False)
        # frequency measured in number of units of input 1!
        frequency = tmp_df.theta.values * tmp_df.theta_frequency.values
        value = tmp_df.factor_payment_1.values
        return pd.Series(frequency, index=value)

    @property
    def factor_payment_1_sf(self):
        """
        Survival function (sf) for factor payments to input 1.

        :getter: Return the current sf.
        :type: pandas.Series

        """
        return self.compute_sf(self.factor_payment_1_cdf)

    @property
    def factor_payment_2_cdf(self):
        """
        Cumulative distribution function (cdf) for factor payments to input 2.

        :getter: Return the current cdf.
        :type: pandas.Series

        """
        return self.compute_cdf(self.factor_payment_2_pdf)

    @property
    def factor_payment_2_pdf(self):
        """
        Probability density function (pdf) for factor payments to input 2.

        :getter: Return the current pdf.
        :type: pandas.Series

        """
        tmp_df = self._soln_with_theta_frequency.sort('factor_payment_2',
                                                      ascending=True,
                                                      inplace=False)
        frequency = tmp_df.theta_frequency.values
        value = tmp_df.factor_payment_2.values
        return pd.Series(frequency, index=value)

    @property
    def factor_payment_2_sf(self):
        """
        Survival function (sf) for factor payments to input 2.

        :getter: Return the current sf.
        :type: pandas.Series

        """
        return self.compute_sf(self.factor_payment_2_cdf)

    @property
    def theta_cdf(self):
        """
        Cumulative distribution function (cdf) for theta.

        :getter: Return the current cdf.
        :type: pandas.Series

        """
        return self.compute_cdf(self.theta_pdf)

    @property
    def theta_pdf(self):
        """
        Probability density function (pdf) for theta.

        :getter: Return the current pdf.
        :type: pandas.Series

        """
        tmp_df = self._soln_with_theta_frequency
        frequency = tmp_df.theta_frequency.values
        value = tmp_df.theta.values
        return pd.Series(frequency, index=value)

    @property
    def theta_sf(self):
        """
        Survival function (sf) for theta.

        :getter: Return the current sf.
        :type: pandas.Series

        """
        return self.compute_sf(self.theta_cdf)

    @staticmethod
    def compute_cdf(pdf):
        """Compute the cdf given a pdf."""
        cdf = pdf.cumsum() / pdf.sum()
        return cdf

    @staticmethod
    def compute_sf(cdf):
        """Compute the sf given the cdf."""
        sf = 1 - cdf
        return sf
