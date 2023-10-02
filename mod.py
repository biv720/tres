import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban a member from the server."""
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned for {reason}.')

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        """Mute a member."""
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            await ctx.send("Muted role not found. Please create a 'Muted' role.")
            return

        await member.add_roles(muted_role)
        await ctx.send(f'{member.mention} has been muted.')

def setup(bot):
    bot.add_cog(Mod(bot))
