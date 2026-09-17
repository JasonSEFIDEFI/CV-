"""Tests for foundational SEFI stability placeholders."""

import pytest

from sefi_core.stability import (
    evaluate_non_intersection_tolerance,
    is_metric_compatible_affine_connection,
)


def test_metric_compatible_affine_connection_within_tolerance() -> None:
    """Metric compatibility should pass when covariant gradients are tiny."""

    gradient = [1e-11, -5e-10, 2e-10]
    assert is_metric_compatible_affine_connection(gradient, tolerance=1e-9)


def test_metric_compatible_affine_connection_outside_tolerance() -> None:
    """Metric compatibility should fail when any component exceeds tolerance."""

    gradient = [1e-11, 2e-8, -3e-10]
    assert not is_metric_compatible_affine_connection(gradient, tolerance=1e-9)


def test_non_intersection_tolerance_logic() -> None:
    """Non-intersection should match the defined stability tolerance bounds."""

    assert evaluate_non_intersection_tolerance(0.05, stability_tolerance=0.1)
    assert not evaluate_non_intersection_tolerance(0.12, stability_tolerance=0.1)


def test_non_intersection_negative_displacement_rejected() -> None:
    """Negative displacement should be rejected as an invalid magnitude."""

    with pytest.raises(ValueError, match="displacement must be non-negative"):
        evaluate_non_intersection_tolerance(-0.01, stability_tolerance=0.1)


def test_negative_tolerance_rejected_for_stability_predicates() -> None:
    """Negative tolerance values should be rejected by both predicates."""

    with pytest.raises(ValueError, match="tolerance must be non-negative"):
        is_metric_compatible_affine_connection([0.0], tolerance=-1e-9)

    with pytest.raises(ValueError, match="stability_tolerance must be non-negative"):
        evaluate_non_intersection_tolerance(0.01, stability_tolerance=-0.1)
