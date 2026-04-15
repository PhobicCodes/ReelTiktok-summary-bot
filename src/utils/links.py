""" Utilities for extracting and classifying links from messages."""

from __future__ import annotations
import re

URL_PATTERN = re.compile(r"https?://\S+")

def extract_urls(text: str) -> list[str]:
    """Return all URLS found in a message"""
    return URL_PATTERN.findall(text)

def get_supported_platform(url: str) -> str | None:
    """Return the supported platform name for a url, or None if not supported"""
    lowered_url = url.lower()
    if "tiktok.com" in lowered_url:
        return "tiktok"
    
    if "instagram.com/reel/" in lowered_url:
        return "instagram_reel"
    
    return None