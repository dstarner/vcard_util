"""Objects that allow abstracting and operating against VCard resources easily."""
from dataclasses import dataclass


@dataclass
class VCardProperty:
    """Represents a line in a VCard definition containing information."""

    pass


@dataclass
class VCard:
    """Represents a single VCard and a block of parsed properties."""

    pass

@dataclass
class VCardList:
    """Represents a list of VCards and their parsed properties."""

    pass
