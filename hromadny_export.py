version = "1.0.0"
from pexpect import pxssh
import time


seznam_objektu = []
cesta_importovaneho_souboru = 'oc_haje.csv'
seznam_ip = []


class Import():
    def __init__(self, ip_adresa_player, ip_adresa_tv, player_name, lokace, poznamka, cas_1, prikaz_1, cas_2, prikaz_2, cas_3, prikaz_3, cas_4, prikaz_4, cas_5, prikaz_5):
        self.ip_adresa_player = ip_adresa_player.strip()
        self.ip_adresa_tv = ip_adresa_tv.strip()
        self.player_name = player_name.strip()
        self.lokace = lokace.strip()
        self.poznamka = poznamka.strip()
        self.cas_1 = cas_1.strip()
        self.prikaz_1 = prikaz_1.strip()
        self.cas_2 = cas_2.strip()
        self.prikaz_2 = prikaz_2.strip()
        self.cas_3 = cas_3.strip()
        self.prikaz_3 = prikaz_3.strip()
        self.cas_4 = cas_4.strip()
        self.prikaz_4 = prikaz_4.strip()
        self.cas_5 = cas_5.strip()
        self.prikaz_5 = prikaz_5.strip()
        self.cesta_k_programu = " /usr/bin/python3 /home/pi/dsmedia_remote/main.py "
        self.cmd_1 = '"' + self.cas_1 + self.cesta_k_programu + self.prikaz_1 + '"'
        self.cmd_2 = '"' + self.cas_2 + self.cesta_k_programu + self.prikaz_2 + '"'
        self.cmd_3 = '"' + self.cas_3 + self.cesta_k_programu + self.prikaz_3 + '"'
        self.cmd_4 = '"' + self.cas_4 + self.cesta_k_programu + self.prikaz_4 + '"'
        self.cmd_5 = '"' + self.cas_5 + self.cesta_k_programu + self.prikaz_5 + '"'

        # self.prikaz_list = [self.prikaz_1, self.prikaz_2, self.prikaz_3, self.prikaz_4, self.prikaz_5]

### Import dokumentu ###
with open(cesta_importovaneho_souboru) as csv: # importuje soubor
    print(csv.readline()) # přečte a ignoruje první řádek
    for x in csv.readlines(): # přečte postupně řádky
        data = x.split(";") # udělá u toho list a rozdělí ho
        objekt = Import(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9],
                        data[10], data[11], data[12], data[13], data[14]) # naplní objekt daty ze souboru
        seznam_objektu.append(objekt) # uloží objekt do seznamu

#Projde všechny IP adresy a uloží je do seznamu
for x in seznam_objektu:
    seznam_ip.append(x.ip_adresa_player)


for x in seznam_objektu:
    # print(f"{x.ip_adresa_player}\n{x.cmd_1}\n{x.cmd_2}\n{x.cmd_3}\n{x.cmd_4}\n{x.cmd_5}")

    s = pxssh.pxssh()
    if not s.login(x.ip_adresa_player, 'pi', 'pi'):
        print(f"SSH session failed on login {x.ip_adresa_player} - {x.player_name} - {x.lokace} - {x.poznamka}")
        print(str(s))
    else:
        print(f"SSH session login successful {x.ip_adresa_player} - {x.player_name} - {x.lokace} - {x.poznamka}")
        ### CMD ###
        # s.sendline("git clone https://github.com/xxlewi/dsmedia_remote.git") # ok funguje

        # write out current crontab
        s.sendline("crontab -r")
        s.sendline("crontab -l > mycron")
        if x.prikaz_1 == "" or x.cas_1 == "":
            pass
        else:
            s.sendline(f'echo {x.cmd_1} >> mycron')

        if x.prikaz_2 == "" or x.cas_2 == "":
            pass
        else:
            s.sendline(f'echo {x.cmd_2} >> mycron')

        if x.prikaz_3 == "" or x.cas_3 == "":
            pass
        else:
            s.sendline(f'echo {x.cmd_3} >> mycron')

        if x.prikaz_4 == "" or x.cas_4 == "":
            pass
        else:
            s.sendline(f'echo {x.cmd_4} >> mycron')

        if x.prikaz_5 == "" or x.cas_5 == "":
            pass
        else:
            s.sendline(f'echo {x.cmd_5} >> mycron')
        # print(cron)
        # install new cron file
        s.sendline("crontab mycron")
        s.sendline("cat crontab -l")
        s.sendline("rm mycron")

        # s.prompt()         # match the prompt
        # print(s.before)     # print everything before the prompt.
        s.logout()