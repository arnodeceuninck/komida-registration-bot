from discord.ext import commands
from main import session, User
from request import register_tracking

TOKEN = "ENTER YOUR DISCORD BOT TOKEN HERE"

bot = commands.Bot(command_prefix='-')


@bot.command(pass_context=True)
async def register(ctx):
    user = get_user(ctx)
    if not user.phone_number or not user.name or not user.email:
        await ctx.send(f"Your account is not complete. "
                       f"Please provide your info (you can also send the bot this as DM) and try again.\n"
                       f"-name <firstname> <lastname>\n"
                       f"-phone <phone_number>\n"
                       f"-mail <your_email>\n")
        return
    response = register_tracking(user)
    msg = response.json()["message"]
    await ctx.send(f"Reply: {msg}")


def get_user(ctx):
    discord_id = get_discord_id(ctx)
    user = session.query(User).filter_by(discord_id=discord_id).first()
    if not user:
        user = new_user(ctx)
    return user


def get_discord_id(ctx):
    return ctx.message.author.id


def new_user(ctx):
    user = User(discord_id=get_discord_id(ctx))
    session.add(user)
    session.commit()
    return user


@bot.command(pass_context=True)
async def name(ctx, *, text):
    user = get_user(ctx)
    user.name = text
    session.commit()
    await ctx.message.reply(f"Name set to {user.name}")


@bot.command(pass_context=True)
async def phone(ctx, *, text):
    user = get_user(ctx)
    user.phone_number = text
    session.commit()
    await ctx.message.reply(f"Phone number set to {user.phone_number}")


@bot.command(pass_context=True)
async def mail(ctx, *, text):
    user = get_user(ctx)
    user.email = text
    session.commit()
    await ctx.message.reply(f"Mail set to {user.email}")


@bot.command(pass_context=True)
async def info(ctx):
    user = get_user(ctx)
    await ctx.message.reply(f"Name: {user.name}\n"
                            f"Mail: {user.email}\n"
                            f"Phone: {user.phone_number}")


bot.run(TOKEN)
