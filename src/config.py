""" Configuration helpers for the Reel Tiktok Summary Bot"""

from __future__ import annotations

import os 

from dotenv import load_dotenv

load_dotenv()

def get_token() -> str:
    """Load the Discord token from environment variables."""
    token = os.getenv("DISCORD_TOKEN")

    if not token:
        raise ValueError(
            "DISCORD_TOKEN not found in environment variables. "
            "Please set it in the .env file."
        )

    return token    