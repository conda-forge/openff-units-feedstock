"""Test some basic behavior of the public classes."""

from pint import __version__ as pint_version
from openff.units import __version__ as openff_units_version
from openff.units import Quantity, Unit, unit
from openff.units.elements import MASSES, NUMBERS, SYMBOLS
from openff.units.openmm import to_openmm, from_openmm


assert openff_units_version != "0.0.0", "Version handling mangled!"

print(f"Testing with {pint_version=} and {openff_units_version=}")

[1, 2, 3] * unit.kilojoule_per_mole
1.5 * Unit("nanometer")

assert unit.Quantity("0.0") == 0.0 * unit.dimensionless
assert unit.Quantity("1 nanometer") == Quantity("1 nanometer")

assert MASSES[1].m_as(unit.dalton) == 1.007947
assert NUMBERS["Hg"] == 80
assert SYMBOLS[79] == "Au"

assert from_openmm(to_openmm(Quantity("2.0 angstrom"))).m_as("angstrom") == 2.0

print(
    "Tests appear to have passed!"
    f"\n{(0.5 * unit.kilojoule_per_mole)=},"
    f"\n{([4, 4, 4] * unit.nanometer)=},"
    f"\n{SYMBOLS[79]=}",
)
