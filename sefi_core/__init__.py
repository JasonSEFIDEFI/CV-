"""Core SEFI simulation interfaces for geometric stability analysis."""

from .stability import (
    DisplacementMetrics,
    StabilitySurface,
    WarpResidualSummary,
    analyze_warp_residual_geometry,
    evaluate_geometric_stabilizers,
    evaluate_non_intersection_tolerance,
    initialize_stability_surface,
    is_metric_compatible_affine_connection,
    track_syndrome_vector_displacement,
)

__all__ = [
    "DisplacementMetrics",
    "StabilitySurface",
    "WarpResidualSummary",
    "analyze_warp_residual_geometry",
    "evaluate_geometric_stabilizers",
    "initialize_stability_surface",
    "evaluate_non_intersection_tolerance",
    "is_metric_compatible_affine_connection",
    "track_syndrome_vector_displacement",
]
