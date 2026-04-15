"""Discord client setup and event handlers."""

from __future__ import annotations

import discord

from utils.links import extract_urls, get_supported_platform


def create_client() -> discord.Client:
    """Create and configure the Discord client."""
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready() -> None:
        print(f"Logged in as {client.user} (ID: {client.user.id})")
        print("Bot is online.")

    @client.event
    async def on_message(message: discord.Message) -> None:
        if message.author == client.user:
            return

        links = extract_urls(message.content)
        if not links:
            return
        
        for link in links:
            platform = get_supported_platform(link)
            
            if platform == "tiktok":
                await message.channel.send(f"TikTok link detected.")
                return 
            if platform == "instagram_reel":
                await message.channel.send(f"Instagram Reel detected.")
                return
                
            

    return client