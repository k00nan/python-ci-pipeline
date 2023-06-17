import pytest
from python_ci_pipeline.moin import moin

@pytest.mark.parametrize(
    "expected_result",
    [('moin')],
)
def test_moin(expected_result: str) -> None:
    actual_result = moin()
    assert(
        actual_result == expected_result
    ), f"Expected different result. Expected '{expected_result}', got '{actual_result}' instead."
