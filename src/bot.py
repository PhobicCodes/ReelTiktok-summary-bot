"""Discord client setup and event handlers."""

import discord

from utils.links import extract_urls, get_supported_platform
from utils.replies import build_detection_reply


def find_first_supported_link(links):
    """Return the first supported (platform, link) pair, or None."""
    for link in links:
        platform = get_supported_platform(link)
        if platform:
            return platform, link

    return None




def create_client():
    """Create and configure the Discord client."""
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user} (ID: {client.user.id})")
        print("Bot is online.")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        links = extract_urls(message.content)
        if not links:
            return

        result = find_first_supported_link(links)
        if not result:
            return

        platform, link = result

        reply = build_detection_reply(platform, link)
        if not reply:
            return

        await message.channel.send(reply)

    return client