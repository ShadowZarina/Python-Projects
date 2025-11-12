import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Your Token Here') # Replace with your own token

# TO - DO LIST
'''
import discord
from discord.ext import commands, tasks
import datetime
import os # To load your bot token from an environment variable

# --- Configuration ---
# You need to enable Message Content and Member Intents in your bot's settings
# on the Discord Developer Portal.
# 'all' is often used for simplicity in early development, but for production,
# it's best to only request the intents you need.
intents = discord.Intents.all() 
# You can adjust the command prefix (e.g., '!')
bot = commands.Bot(command_prefix='!', intents=intents)

# --- Events ---

@bot.event
async def on_ready():
    """Confirms the bot is logged in and ready."""
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    # Start the scheduled task loop when the bot is ready
    # You would typically have a single scheduling loop or separate loops for different checks
    # daily_check_for_schedule.start() 
    try:
        # Syncing global slash commands (optional, but good practice)
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# --- Utility Functions (for scheduling and announcements) ---

def get_students_role(guild: discord.Guild) -> discord.Role | None:
    """Finds the 'Students' role in a given guild."""
    # NOTE: Role name must match exactly.
    return discord.utils.get(guild.roles, name="Students")

async def announce_to_students(guild: discord.Guild, message: str, channel_id: int):
    """Pings the Students role and sends an announcement to a specific channel."""
    role = get_students_role(guild)
    channel = guild.get_channel(channel_id)
    
    if role and channel:
        # Pings the role to notify all members with it, then sends the message
        await channel.send(f"{role.mention} **ANNOUNCEMENT:** {message}")
        print(f"Announcement sent to channel {channel_id} in {guild.name}")
    else:
        print(f"Could not find 'Students' role or channel {channel_id} in {guild.name}")

# --- Commands (for manual announcement/scheduling setup) ---

@bot.command(name='announce')
@commands.has_permissions(administrator=True) # Restrict to admins
async def announce_command(ctx, channel_id: int, *, message: str):
    """
    Manual command to trigger an announcement.
    Usage: !announce <channel_id> <Your announcement message>
    """
    await announce_to_students(ctx.guild, message, channel_id)
    await ctx.send("Announcement dispatched!")

# @bot.tree.command(name="setschedule", description="Set an exam/meeting schedule.")
# async def set_schedule_slash(interaction: discord.Interaction, type: str, date: str, time: str, details: str):
#     # This function would involve parsing the date/time, saving it to a file/database,
#     # and then creating an event or using the tasks loop to check for the time.
#     # For this example, we'll keep it simple:
#     response = f"Schedule saved: **{type.upper()}** on {date} at {time} for: {details}"
#     await interaction.response.send_message(response)


# --- Scheduling Loop (for automated reminders) ---

@tasks.loop(time=datetime.time(hour=9, minute=0, tzinfo=datetime.timezone.utc))
async def daily_check_for_schedule():
    """A loop that runs every day at 9:00 AM UTC to check for announcements/deadlines."""
    # You will need to determine a target announcement channel ID
    ANNOUNCEMENT_CHANNEL_ID = 123456789012345678 # <<< REPLACE with your actual channel ID
    
    # In a real bot, you would load data from a database or file here.
    # Example: Check for tomorrow's assignments
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    # This is a very basic placeholder for demonstration.
    # A real implementation would have persistent storage and complex logic.
    if tomorrow == "2025-11-13": # Hypothetical example date
        announcement_message = f"REMINDER: Assignment 3 is due **tomorrow**, {tomorrow}!"
        for guild in bot.guilds:
            await announce_to_students(guild, announcement_message, ANNOUNCEMENT_CHANNEL_ID)

# --- Run the Bot ---

if __name__ == '__main__':
    # It is best practice to load the token from an environment variable for security
    BOT_TOKEN = os.getenv('DISCORD_TOKEN') 
    if BOT_TOKEN is None:
        # Fallback for testing, but seriously, use a .env file or env variable
        print("!! WARNING: DISCORD_TOKEN environment variable not set. Using placeholder.")
        # Replace 'YOUR_BOT_TOKEN' with your actual token for a quick test
        # but remove it before sharing!
        BOT_TOKEN = 'YOUR_BOT_TOKEN' 
        
    bot.run(BOT_TOKEN)
'''
