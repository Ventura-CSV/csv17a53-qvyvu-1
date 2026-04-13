from __future__ import annotations 


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===
    # Your code here
    if len(set(mapping.values())) == len(mapping):
        return None
    pairs = ()
    for first_x, first_y in mapping.items():
        for second_x, second_y in mapping.items():
            if first_y == second_y and first_x != second_x:
                pairs += ((first_x, second_x))
    return pairs if pairs else None
    # === END TODO ===


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===


def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===
