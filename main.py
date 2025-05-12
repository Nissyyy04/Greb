import os
from colorama import Fore, Style
import art, fade
import asyncio
import msvcrt
import shared
import app

async def cls(): os.system('cls' if os.name == 'nt' else 'clear')
async def banner(text="Greb"): print(fade.purplepink(art.text2art(text, font='amcslash')))
async def redbanner(text="Greb"): print(fade.fire(art.text2art(text, font='amcslash')))


async def main():
    await cls()
    
    menuOptions = [
        "Change Discord Webhook",
        "Change Redirect URL",
        "Start Greb Logger",
        "Exit"
    ]
    
    selectedOption = 0
    
    await cls()
    await banner()

    for i in range(len(menuOptions)):
        if i == selectedOption:
            print(f"{Fore.MAGENTA}>> {Fore.LIGHTMAGENTA_EX}{menuOptions[i]}{Fore.MAGENTA} <<{Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTBLUE_EX}   {menuOptions[i]}{Style.RESET_ALL}")
    
    while True:
  
        ch = ord(msvcrt.getch())
        
        if ch == 27:
            await cls()
            await redbanner("Exiting...")
            
            quit()
        elif ch == 80:
            if selectedOption < len(menuOptions)-1: selectedOption+=1
            else: continue
        elif ch == 72:
            if selectedOption > 0: selectedOption-=1
            else: continue
        elif ch == 13:
            if selectedOption == 0:
                await cls()
                await banner("Webhook")
                
                new_whook = input(f"{Fore.LIGHTMAGENTA_EX}Enter new Discord Webhook URL{Fore.MAGENTA}: {Fore.CYAN}")
                shared.config.set("webhook", new_whook)
                shared.discord_webhook = new_whook
                
                print()
                print(f"{Fore.LIGHTGREEN_EX}Discord Webhook set to {Fore.CYAN}{new_whook}{Style.RESET_ALL}")
                for i in range(3, 0, -1):
                    print(f"{Fore.LIGHTGREEN_EX}Continuing in {Fore.CYAN}{i}{Fore.LIGHTGREEN_EX} seconds...", end="\r")
                    await asyncio.sleep(1)
                
            elif selectedOption == 1:
                await cls()
                await banner("Redirect  URL")
                new_redirect_url = input(f"{Fore.LIGHTMAGENTA_EX}Enter new Redirect URL{Fore.MAGENTA}: {Fore.CYAN}")
                shared.config.set("redirect_url", new_redirect_url)
                shared.redirect_url = new_redirect_url
                
                print()
                print(f"{Fore.LIGHTGREEN_EX}Redirect URL set to {Fore.CYAN}{new_redirect_url}{Style.RESET_ALL}")
                for i in range(3, 0, -1):
                    print(f"{Fore.LIGHTGREEN_EX}Continuing in {Fore.CYAN}{i}{Fore.LIGHTGREEN_EX} seconds...", end="\r")
                    await asyncio.sleep(1)
            
            elif selectedOption == 2:
                await cls()
                await banner("Greb")
                
                app.run()
                
            elif selectedOption == 3:
                await cls()
                await redbanner("Exiting...")
                quit()
        else: continue
        
        await cls()
        await banner()
    
        for i in range(len(menuOptions)):
            if i == selectedOption:
                print(f"{Fore.MAGENTA}>> {Fore.LIGHTMAGENTA_EX}{menuOptions[i]}{Fore.MAGENTA} <<{Style.RESET_ALL}")
            else:
                print(f"{Fore.LIGHTBLUE_EX}   {menuOptions[i]}{Style.RESET_ALL}")
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()