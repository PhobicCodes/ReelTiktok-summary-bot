"""Application entry point for the Reel Summary Bot."""

from __future__ import annotations

from bot import create_client
from config import get_token


def main() -> None:
    """Start the Discord bot."""
    client = create_client()
    client.run(get_token())


if __name__ == "__main__":
    main()