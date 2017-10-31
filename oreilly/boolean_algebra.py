# -*- coding: utf-8 -*-
"""
Oreilly functions from
https://py.checkio.org/mission/boolean-algebra/
A mathematical function "boolean" that returns a boolean value
"""


def conjunction(bool_a: bool, bool_b: bool) -> bool:
    """
    mathematical logical value x ∧ y
    """
    return bool_a and bool_b


def disjunction(bool_a: bool, bool_b: bool) -> bool:
    """
    mathematical logical value x ∨ y
    """
    return bool_a or bool_b


def implication(bool_a: bool, bool_b: bool) -> bool:
    """
    mathematical logical value x→y (¬ x ∨ y)
    """
    return bool_a == bool_b or bool_b


def exclusive(bool_a: bool, bool_b: bool) -> bool:
    """
    mathematical logical value (x ∨ y)∧ ¬ (x ∧ y)
    """
    return bool_a != bool_b


def equivalence(bool_a: bool, bool_b: bool) -> bool:
    """
    mathematical logical value x ≡ y
    """
    return bool_a == bool_b


def boolean(bool_a: bool, bool_b: bool, operation: str) -> bool:
    """
    :param bool_a, bool_b: logical value 0 or 1
    :param operation:
    - "conjunction" denoted x ∧ y
    - "disjunction" denoted x ∨ y
    - "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y
    - "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y)
    - "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y)
     x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
    --------------------------------------
     0 | 0 |  0  |  0  |  1  |  0  |  1  |
     1 | 0 |  0  |  1  |  0  |  1  |  0  |
     0 | 1 |  0  |  1  |  1  |  1  |  0  |
     1 | 1 |  1  |  1  |  1  |  0  |  1  |
    --------------------------------------
    :return: logical value after operation: 0 or 1
    """
    function = [
        ["conjunction", conjunction(bool_a, bool_b)],
        ["disjunction", disjunction(bool_a, bool_b)],
        ["implication", implication(bool_a, bool_b)],
        ["exclusive", exclusive(bool_a, bool_b)],
        ["equivalence", equivalence(bool_a, bool_b)],
    ]
    return bool([fun[1] for fun in function if fun[0] == operation][0])
