"""Tests for foundational SEFI stability placeholders."""

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
