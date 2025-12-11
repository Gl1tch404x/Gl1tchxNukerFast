import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

PURPLE = Fore.MAGENTA

def display_logo():
    logo = f"""
{PURPLE}██████╗ {PURPLE} ██╗ {PURPLE}     ██╗{PURPLE}████████╗ {PURPLE}██████╗{PURPLE}██╗  ██╗{PURPLE}███████╗{PURPLE}██████╗ {PURPLE}
██╔════╝ {PURPLE}██║ {PURPLE}     ██║{PURPLE}╚══██╔══╝{PURPLE}██╔════╝{PURPLE}██║  ██║{PURPLE}██╔════╝{PURPLE}██╔══██╗{PURPLE}
██║  ███╗{PURPLE}██║ {PURPLE}     ██║{PURPLE}   ██║   {PURPLE}██║     {PURPLE}███████║{PURPLE}█████╗  {PURPLE}██║  ██║{PURPLE}
██║   ██║{PURPLE}██║ {PURPLE}     ██║{PURPLE}   ██║   {PURPLE}██║     {PURPLE}██╔══██║{PURPLE}██╔══╝  {PURPLE}██║  ██║{PURPLE}
╚██████╔╝{PURPLE}███████╗{PURPLE} ██║{PURPLE}   ██║   {PURPLE}╚██████╗{PURPLE}██║  ██║{PURPLE}███████╗{PURPLE}██████╔╝{PURPLE}
 ╚═════╝ {PURPLE}╚══════╝{PURPLE} ╚═╝{PURPLE}   ╚═╝    {PURPLE}╚═════╝{PURPLE}╚═╝  ╚═╝{PURPLE}╚══════╝{PURPLE}╚═════╝ {PURPLE}
                                                            
████████╗ {PURPLE}██████╗  {PURPLE}██████╗ {PURPLE}██╗     {PURPLE}███████╗{PURPLE}                  
╚══██╔══╝{PURPLE}██╔═══██╗{PURPLE}██╔═══██╗{PURPLE}██║     {PURPLE}██╔════╝{PURPLE}                  
   ██║   {PURPLE}██║   ██║{PURPLE}██║   ██║{PURPLE}██║     {PURPLE}███████╗{PURPLE}                  
   ██║   {PURPLE}██║   ██║{PURPLE}██║   ██║{PURPLE}██║     {PURPLE}╚════██║{PURPLE}                  
   ██║   {PURPLE}╚██████╔╝{PURPLE}╚██████╔╝{PURPLE}███████╗{PURPLE}███████║{PURPLE}                  
   ╚═╝    {PURPLE}╚═════╝  {PURPLE}╚═════╝ {PURPLE}╚══════╝{PURPLE}╚══════╝{PURPLE}                  

                                                                                       
{Fore.MAGENTA}Creator: {Fore.MAGENTA}Glitched Tools{Style.RESET_ALL}
{Fore.MAGENTA}Glitched Tools Paid Discord Server Nuking Tool{Style.RESET_ALL}
"""
    print(logo)
