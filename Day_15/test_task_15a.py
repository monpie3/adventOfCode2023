from task_15a import hash_algorithm

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("HASH", 52),
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47),
        ("qp-", 14),
        ("pc=4", 180),
        ("ot=9", 9),
        ("ab=5", 197),
        ("pc-", 48),
        ("pc=6", 214),
        ("ot=7", 231),
    ],
)
def test_hash_algorithm(test_input, expected):
    assert hash_algorithm(test_input) == expected
