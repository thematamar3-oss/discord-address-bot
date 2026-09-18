import os
import discord
from discord import app_commands
from dotenv import load_dotenv

# Načtení proměnných prostředí ze souboru .env (pro lokální testování)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class AddressBot(discord.Client):
    def __init__(self):
        # Nastavení intents pro správné fungování zpráv a DM
        intents = discord.Intents.default()
        intents.message_content = True
        intents.dm_messages = True
        
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Globální synchronizace příkazů
        await self.tree.sync()
        print("Příkazy bota byly úspěšně synchronizovány!")

bot = AddressBot()

@bot.event
async def on_ready():
    print(f"Přihlášen jako {bot.user} (ID: {bot.user.id})")
    print("Bot je plně připraven k použití na serveru i v DM!")

@bot.tree.command(name="address", description="Zobrazí platební adresy pro kryptoměny")
async def address(interaction: discord.Interaction):
    # Vytvoření estetického embed rámečku v tmavém stylu
    embed = discord.Embed(
        title="Send money here :)",
        color=discord.Color.from_rgb(30, 35, 40)
    )
    
    # Přidání polí s adresami v blocích kódu
    embed.add_field(
        name="1. Bitcoin (BTC)", 
        value="```bc1q3esetxuq39y2a7egpc7e4qh37lsg2qqgaz6pg```", 
        inline=False
    )
    embed.add_field(
        name="2. Litecoin (LTC)", 
        value="```LeYVQE3Ks6HjcxKwu5x14DTDqnuauh1hmi```", 
        inline=False
    )
    embed.add_field(
        name="3. Monero (XMR)", 
        value="```42tAUnUuYCHHnxAUWcwygGmeu3TifhaG1eFwtEugHYgaiCuvzMSrLFstmr9McsjdQzZoC9bheAD4XHstrKGjS44xkD86```", 
        inline=False
    )
    embed.add_field(
        name="4. Solana (SOL)", 
        value="```BUpPbvHdfQUCMUQBheyJdZYASdKsfwdvvFMtEFRpHHrz```", 
        inline=False
    )
    embed.add_field(
        name="5. Ethereum (ETH)", 
        value="```0x1591E8C9F0f5418c9458060aB84a0368739e2eb2```", 
        inline=False
    )

    # Odeslání odpovědi
    await interaction.response.send_message(embed=embed)

# Spuštění bota
if __name__ == "__main__":
    if not TOKEN:
        print("Chyba: Token nebyl nalezen! Zkontroluj nastavení na Renderu.")
    else:
        bot.run(TOKEN)
