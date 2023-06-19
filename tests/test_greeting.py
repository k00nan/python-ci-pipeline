import pytest

from python_ci_pipeline.greeting import greeting


# this decorator allows that all assert statements in a test are executed,
# even if the first one were to fail
@pytest.mark.parametrize(
    "name, expected_result",
    [
        ("Amela", "Hallo, Amela!"),
        ("damir", "Hallo, damir!"),
        ("2", "Hallo, 2!"),
        ("", "Hallo, kenan!"),
    ],
)
def test_greeting(name: str, expected_result: str) -> None:
    actual_result = greeting(name)
    assert (
        actual_result == expected_result
    ), f"Expected different result. Expected '{expected_result}', got '{actual_result}' instead."
