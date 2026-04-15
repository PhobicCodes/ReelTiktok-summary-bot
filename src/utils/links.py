"""Utilities for extracting and classifying links from messages."""

import re

URL_PATTERN = re.compile(r"https?://\S+")
TRAILING_PUNCTUATION = ".,!?:;)\"]"


def clean_url(url):
    """Remove common trailing punctuation from a detected URL."""
    return url.rstrip(TRAILING_PUNCTUATION)


def extract_urls(text):
    """Return all cleaned URLs found in a message."""
    raw_urls = URL_PATTERN.findall(text)
    return [clean_url(url) for url in raw_urls]


def get_supported_platform(url):
    """Return the supported platform name for a URL, or None if unsupported."""
    lowered_url = url.lower()

    if "tiktok.com" in lowered_url or "vt.tiktok.com" in lowered_url:
        return "tiktok"

    if "instagram.com/reel/" in lowered_url or "instagram.com/reels/" in lowered_url:
        return "instagram_reel"

    return None