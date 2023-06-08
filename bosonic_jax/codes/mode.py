"""
Generic Bosonic Mode Class
"""

from typing import Tuple

from bosonic_jax.codes.base import BosonicQubit
import jaxquantum as jqt

from jax.config import config
import jax.numpy as jnp

config.update("jax_enable_x64", True)


class BosonicMode(BosonicQubit):
    """
    FockQubit
    """

    def _params_validation(self):
        super()._params_validation()

    def _get_basis_z(self) -> Tuple[jnp.ndarray, jnp.ndarray]:
        """
        Construct basis states |+-x>, |+-y>, |+-z>
        """
        N = int(self.params["N"])
        plus_z = jqt.basis(N, 0)
        minus_z = jqt.basis(N, 1)
        return plus_z, minus_z
