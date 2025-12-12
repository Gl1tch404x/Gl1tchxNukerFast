import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

PURPLE = Fore.MAGENTA

def display_logo():
    logo = f"""
        {PURPLE}
  ________.__  ____  __         .__           ___________           .__          
 /  _____/|  |/_   |/  |_  ____ |  |__ ___  __\__    ___/___   ____ |  |   ______
/   \  ___|  | |   \   __\/ ___\|  |  \\  \/  / |    | /  _ \ /  _ \|  |  /  ___/
\    \_\  \  |_|   ||  | \  \___|   Y  \>    <  |    |(  <_> |  <_> )  |__\___ \ 
 \______  /____/___||__|  \___  >___|  /__/\_ \ |____| \____/ \____/|____/____  >
        \/                    \/     \/      \/                               \/          
         {PURPLE}               
                                                                          
{Fore.MAGENTA}Creator: {Fore.MAGENTA}Glitched Tools{Style.RESET_ALL}
{Fore.MAGENTA}Glitched Tools Discord Server Nuking Tool{Style.RESET_ALL}
"""
    print(logo)
