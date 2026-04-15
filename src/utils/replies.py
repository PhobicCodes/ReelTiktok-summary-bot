"""Utilities for building bot reply messages."""


def build_detection_reply(platform, link):
    """Build the reply text for a detected platform and link."""
    if platform == "tiktok":
        return f"TikTok link detected.\nLink: {link}"

    if platform == "instagram_reel":
        return f"Instagram Reel detected.\nLink: {link}"

    return None