import pytest

from creative_standards import get_format, list_formats, validate_asset


def test_2160x720_format_is_available():
    spec = get_format("display.2160x720")
    assert (spec["width"], spec["height"]) == (2160, 720)
    assert spec["aspect_ratio"] == "3:1"


def test_valid_asset_passes():
    result = validate_asset("display.2160x720", width=2160, height=720, file_type="png", file_bytes=500_000)
    assert result.valid is True
    assert result.errors == ()


def test_invalid_dimensions_and_type_fail():
    result = validate_asset("google.display.300x250", width=301, height=250, file_type="svg", file_bytes=10_000)
    assert result.valid is False
    assert len(result.errors) == 2


def test_channel_filtering():
    assert all(item["channel"] == "meta" for item in list_formats("meta"))


def test_unknown_format_rejected():
    with pytest.raises(KeyError):
        get_format("unknown")
