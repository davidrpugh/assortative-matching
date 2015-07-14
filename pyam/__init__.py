"""
Objects imported here will live in the `pyam` namespace

"""
__all__ = ["Input", "AssortativeMatchingModelLike", "AssortativeMatchingProblem"]

from . inputs import Input
from . model import 
from . problem import AssortativeMatchingProblem
from . orthogonal_polynomials import OrthogonalPolynomialSolver
from . visualizers import Visualizer

# Add Version Attribute
from pkg_resources import get_distribution

__version__ = get_distribution('pyCollocation').version
