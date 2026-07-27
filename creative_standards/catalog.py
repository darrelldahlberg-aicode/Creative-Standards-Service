"""Versioned, platform-neutral creative format catalog."""

FORMATS = {
    "display.2160x720": {
        "version": "1.0",
        "channel": "display",
        "width": 2160,
        "height": 720,
        "aspect_ratio": "3:1",
        "file_types": ["png", "jpg", "webp"],
        "max_file_bytes": 10_000_000,
        "safe_area": {"top": 36, "right": 72, "bottom": 36, "left": 72},
        "guidance": ["Keep primary text inside the safe area", "Use one dominant offer", "Maintain strong left-to-right hierarchy"],
    },
    "meta.feed.square": {
        "version": "1.0", "channel": "meta", "width": 1080, "height": 1080,
        "aspect_ratio": "1:1", "file_types": ["png", "jpg", "webp"],
        "max_file_bytes": 30_000_000, "safe_area": {"top": 54, "right": 54, "bottom": 54, "left": 54},
    },
    "meta.story.vertical": {
        "version": "1.0", "channel": "meta", "width": 1080, "height": 1920,
        "aspect_ratio": "9:16", "file_types": ["png", "jpg", "webp", "mp4"],
        "max_file_bytes": 30_000_000, "safe_area": {"top": 250, "right": 60, "bottom": 250, "left": 60},
    },
    "google.display.300x250": {
        "version": "1.0", "channel": "google-display", "width": 300, "height": 250,
        "aspect_ratio": "6:5", "file_types": ["png", "jpg", "gif"],
        "max_file_bytes": 150_000, "safe_area": {"top": 10, "right": 10, "bottom": 10, "left": 10},
    },
    "google.display.728x90": {
        "version": "1.0", "channel": "google-display", "width": 728, "height": 90,
        "aspect_ratio": "364:45", "file_types": ["png", "jpg", "gif"],
        "max_file_bytes": 150_000, "safe_area": {"top": 6, "right": 10, "bottom": 6, "left": 10},
    },
    "tiktok.video.vertical": {
        "version": "1.0", "channel": "tiktok", "width": 1080, "height": 1920,
        "aspect_ratio": "9:16", "file_types": ["mp4", "mov"],
        "max_file_bytes": 500_000_000, "safe_area": {"top": 180, "right": 140, "bottom": 320, "left": 60},
    },
    "email.hero.1200x600": {
        "version": "1.0", "channel": "email", "width": 1200, "height": 600,
        "aspect_ratio": "2:1", "file_types": ["png", "jpg", "webp"],
        "max_file_bytes": 1_000_000, "safe_area": {"top": 30, "right": 40, "bottom": 30, "left": 40},
    },
}


def get_format(format_id: str) -> dict:
    try:
        return dict(FORMATS[format_id])
    except KeyError as exc:
        raise KeyError(f"Unknown creative format: {format_id}") from exc


def list_formats(channel: str | None = None) -> list[dict]:
    return [dict({"id": key}, **value) for key, value in FORMATS.items() if channel is None or value["channel"] == channel]
