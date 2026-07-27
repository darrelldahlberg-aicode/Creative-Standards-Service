"""Deterministic creative-asset validation."""

from dataclasses import dataclass
from .catalog import get_format


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    format_id: str
    spec_version: str


def validate_asset(format_id: str, *, width: int, height: int, file_type: str, file_bytes: int, text_coverage: float | None = None) -> ValidationResult:
    spec = get_format(format_id)
    errors: list[str] = []
    warnings: list[str] = []
    normalized_type = file_type.lower().lstrip(".")
    if width != spec["width"] or height != spec["height"]:
        errors.append(f"dimensions must be {spec['width']}x{spec['height']}")
    if normalized_type not in spec["file_types"]:
        errors.append(f"file type must be one of: {', '.join(spec['file_types'])}")
    if file_bytes > spec["max_file_bytes"]:
        errors.append(f"file size exceeds {spec['max_file_bytes']} bytes")
    if file_bytes < 0:
        errors.append("file size cannot be negative")
    if text_coverage is not None:
        if not 0 <= text_coverage <= 1:
            errors.append("text_coverage must be between 0 and 1")
        elif text_coverage > 0.35:
            warnings.append("high text coverage may reduce readability and platform performance")
    return ValidationResult(not errors, tuple(errors), tuple(warnings), format_id, spec["version"])
