import socket  
import termcolor  
import time  
import sys  
import os  
  
def clear_screen():  
    os.system('cls' if os.name == 'nt' else 'clear')  
  
def loading_animation(message, duration=2):  
    try:  
        for i in range(duration * 10):  
            sys.stdout.write(f"\r{message}" + "." * (i % 4))  
            sys.stdout.flush()  
            time.sleep(0.1)  
    except KeyboardInterrupt:  
        sys.stdout.write("\r\n[!] Scan Interrupted by User. Mr.Tame will sleep again...\n")  
        sys.exit(0)  
    print("\n")  
  
skull_ascii = """  
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⠴⠶⠶⠶⠶⠶⠶⠶⠶⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⢀⣤⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠶⣤⡀⠀⠀⠀⠀⠀  
⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⡄⠀⠀⠀  
⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀  
⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀  
⣿⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⢹⡄  
⡏⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇  
⣿⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⢸⡇  
⢹⡆⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⣾⠀  
⠈⢷⡀⢸⡇⠀⢀⣠⣤⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⢀⣠⣶⣶⣶⣶⣤⣄⠀⠀⣿⠀⣼⠃⠀  
⠀⠈⢷⣼⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⡾⠃⠀⠀  
⠀⠀⠈⣿⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠃⠀⢸⡇⠀⠀⠀  
⠀⠀⠀⣿⠀⠀⠘⢿⣿⣿⣿⣿⡿⠃⠀⢠⠀⣄⠀⠀⠙⢿⣿⣿⣿⡿⠏⠀⠀⢘⡇⠀⠀⠀  
⠀⠀⠀⢻⡄⠀⠀⠀⠈⠉⠉⠀⠀⠀⣴⣿⠀⣿⣷⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢸⡇⠀⠀⠀  
⠀⠀⠀⠈⠻⣄⡀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠘⣟⠳⣦⡀⠀⠀⠀⠸⣿⡿⠀⢻⣿⡟⠀⠀⠀⠀⣤⡾⢻⡏⠁⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠀⢻⡄⢻⠻⣆⠀⠀⠀⠈⠀⠀⠀⠈⠀⠀⠀⢀⡾⢻⠁⢸⠁⠀⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠀⢸⡇⠀⡆⢹⠒⡦⢤⠤⡤⢤⢤⡤⣤⠤⡔⡿⢁⡇⠀⡿⠀⠀⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠀⠘⡇⠀⢣⢸⠦⣧⣼⣀⡇⢸⢀⣇⣸⣠⡷⢇⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⠺⣄⣇⢸⠉⡏⢹⠉⡏⢹⢀⣧⠾⠋⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠈⠉⠙⠓⠚⠚⠋⠉⠁⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠶⠦⣤⣤⣤⡤⠶⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
"""  
  
mrtame_ascii = """  
  
 ███▄ ▄███▓ ██▀███          ▄▄▄█████▓ ▄▄▄       ███▄ ▄███▓▓█████   
▓██▒▀█▀ ██▒▓██ ▒ ██▒        ▓  ██▒ ▓▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀   
▓██    ▓██░▓██ ░▄█ ▒        ▒ ▓██░ ▒░▒██  ▀█▄  ▓██    ▓██░▒███     
▒██    ▒██ ▒██▀▀█▄          ░ ▓██▓ ░ ░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   
▒██▒   ░██▒░██▓ ▒██▒ ██▓      ▒██▒ ░  ▓█   ▓██▒▒██▒   ░██▒░▒████▒  
░ ▒░   ░  ░░ ▒▓ ░▒▓░ ▒▓▒      ▒ ░░    ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░  
░  ░      ░  ░▒ ░ ▒░ ░▒         ░      ▒   ▒▒ ░░  ░      ░ ░ ░  ░  
░      ░     ░░   ░  ░        ░        ░   ▒   ░      ░      ░     
       ░      ░       ░                    ░  ░       ░      ░  ░  
                      ░                                                                                                    
~ created by @andreihansel (tameSec)  
"""  
  
def display_startup():  
    clear_screen()  
      
    print(termcolor.colored(mrtame_ascii, 'red'))  
    loading_animation(termcolor.colored("WAKING UP MR.TAME"))  
    print(termcolor.colored(skull_ascii, 'yellow'))  
    time.sleep(1)  
    print(termcolor.colored("\nMR.TAME 1.0 // I AM MR.TAME, YOUR VIRTUAL HARBINGER. WHO SHALL WE PWN TODAY?\n", 'yellow'))  
  
def scan(ip, ports):  
    print('\n' + termcolor.colored(f"Starting Scan For {ip}", 'green'))  
    open_ports = []  
    for port in range(1, ports + 1):  
        if hunt_elf(ip, port):  
            open_ports.append(port)  
  
    if not open_ports:  
        print(termcolor.colored(f"Oops, there are no ports open at {ip}", 'red'))  
  
def hunt_elf(ip, port):  
    try:  
        stockings = socket.socket()  
        stockings.settimeout(0.5)  
        stockings.connect((ip, port))  
        print(termcolor.colored(f"[+] OPEN //Port {port}", 'green'))  
        stockings.close()  
        return True  
    except:  
        return False  
  
def display_menu():  
    print(termcolor.colored("\n[1] Port Scanner", 'cyan'))  
    print(termcolor.colored("[2] Coming Soon", 'cyan'))  
    print(termcolor.colored("[3] Coming Soon", 'cyan'))  
    print(termcolor.colored("[4] Exit", 'cyan'))  
  
def main():  
    display_startup()  
    display_menu()  
  
    while True:  
        choice = input(termcolor.colored("\n[*] Enter your choice: ", 'cyan'))  
  
        if choice == '1':
            
            print(termcolor.colored("\n=== PORT SCANNER V1.0 ===", 'red'))
            targets = input(termcolor.colored("[*] Enter Target(s) to Scan (split by ,): ", 'cyan'))  
            ports = int(input(termcolor.colored("[*] Enter Number of Ports to Scan: ", 'cyan')))  
  
            if ',' in targets:  
                print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))  
                for target in targets.split(','):  
                    scan(target.strip(), ports)  
            else:  
                scan(targets.strip(), ports)  
  
            print(termcolor.colored("\nScan Complete!", 'yellow'))  
            display_menu()  
  
        elif choice == '2' or choice == '3':  
            print(termcolor.colored("\nComing Soon!", 'yellow'))  
            display_menu()  
  
        elif choice == '4':  
            print(termcolor.colored("\nExiting...", 'yellow'))  
            break  
  
        else:  
            print(termcolor.colored("\nInvalid choice. Please try again.", 'red'))  
            display_menu()  
  
if __name__ == "__main__":  
    try:  
        main()  
    except KeyboardInterrupt:  
        print(termcolor.colored("\n[!] Scan Interrupted by User. Exiting...", 'red'))  
