version = "1.0.3"
from pexpect import pxssh

class Prikazy():
    def __init__(self, player_name, ip_adresa_player, tv_name, ip_adresa_tv, lokace, poznamka, 
                 cas_1, prikaz_1, cas_2, prikaz_2, cas_3, prikaz_3, cas_4, prikaz_4, cas_5, prikaz_5, cas_6, prikaz_6, cas_7, prikaz_7, cas_8, prikaz_8, cas_9, prikaz_9, cas_10,
                 prikaz_10, cas_11, prikaz_11, cas_12, prikaz_12, cas_13, prikaz_13, cas_14, prikaz_14, cas_15, prikaz_15, cas_16,
                 prikaz_16, cas_17, prikaz_17, cas_18, prikaz_18, cas_19, prikaz_19, cas_20, prikaz_20):

        self.player_name = player_name.strip()        
        self.ip_adresa_player = ip_adresa_player.strip()
        self.tv_name = tv_name.strip()
        self.ip_adresa_tv = ip_adresa_tv.strip()
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
        self.cas_6 = cas_6.strip()
        self.prikaz_6 = prikaz_6.strip()
        self.cas_7 = cas_7.strip()
        self.prikaz_7 = prikaz_7.strip()
        self.cas_8 = cas_8.strip()
        self.prikaz_8 = prikaz_8.strip()
        self.cas_9 = cas_9.strip()
        self.prikaz_9 = prikaz_9.strip()
        self.cas_10 = cas_10.strip()
        self.prikaz_10 = prikaz_10.strip()
        self.cas_11 = cas_11.strip()
        self.prikaz_11 = prikaz_11.strip()
        self.cas_12 = cas_12.strip()
        self.prikaz_12 = prikaz_12.strip()
        self.cas_13 = cas_13.strip()
        self.prikaz_13 = prikaz_13.strip()
        self.cas_14 = cas_14.strip()
        self.prikaz_14 = prikaz_14.strip()
        self.cas_15 = cas_15.strip()
        self.prikaz_15 = prikaz_15.strip()      
        self.cas_16 = cas_16.strip()
        self.prikaz_16 = prikaz_16.strip()
        self.cas_17 = cas_17.strip()
        self.prikaz_17 = prikaz_17.strip()
        self.cas_18 = cas_18.strip()
        self.prikaz_18 = prikaz_18.strip()
        self.cas_19 = cas_19.strip()
        self.prikaz_19 = prikaz_19.strip()
        self.cas_20 = cas_20.strip()
        self.prikaz_20 = prikaz_20.strip()

        # Cesta k repozitari
        self.cesta_k_programu = " /usr/bin/python3 /home/pi/Bluetouch_media_pub/main.py "
        # CMD line
        self.cmd_1 = '"' + self.cas_1 + self.cesta_k_programu + self.prikaz_1 + '"'
        self.cmd_2 = '"' + self.cas_2 + self.cesta_k_programu + self.prikaz_2 + '"'
        self.cmd_3 = '"' + self.cas_3 + self.cesta_k_programu + self.prikaz_3 + '"'
        self.cmd_4 = '"' + self.cas_4 + self.cesta_k_programu + self.prikaz_4 + '"'
        self.cmd_5 = '"' + self.cas_5 + self.cesta_k_programu + self.prikaz_5 + '"'
        self.cmd_6 = '"' + self.cas_6 + self.cesta_k_programu + self.prikaz_6 + '"'
        self.cmd_7 = '"' + self.cas_7 + self.cesta_k_programu + self.prikaz_7 + '"'
        self.cmd_8 = '"' + self.cas_8 + self.cesta_k_programu + self.prikaz_8 + '"'
        self.cmd_9 = '"' + self.cas_9 + self.cesta_k_programu + self.prikaz_9 + '"'
        self.cmd_10 = '"' + self.cas_10 + self.cesta_k_programu + self.prikaz_10 + '"'
        self.cmd_11 = '"' + self.cas_11 + self.cesta_k_programu + self.prikaz_11 + '"'
        self.cmd_12 = '"' + self.cas_12 + self.cesta_k_programu + self.prikaz_12 + '"'
        self.cmd_13 = '"' + self.cas_13 + self.cesta_k_programu + self.prikaz_13 + '"'
        self.cmd_14 = '"' + self.cas_14 + self.cesta_k_programu + self.prikaz_14 + '"'
        self.cmd_15 = '"' + self.cas_15 + self.cesta_k_programu + self.prikaz_15 + '"'
        self.cmd_16 = '"' + self.cas_16 + self.cesta_k_programu + self.prikaz_16 + '"'
        self.cmd_17 = '"' + self.cas_17 + self.cesta_k_programu + self.prikaz_17 + '"'
        self.cmd_18 = '"' + self.cas_18 + self.cesta_k_programu + self.prikaz_18 + '"'
        self.cmd_19 = '"' + self.cas_19 + self.cesta_k_programu + self.prikaz_19 + '"'
        self.cmd_20 = '"' + self.cas_20 + self.cesta_k_programu + self.prikaz_20 + '"'
            
class Program():
    def __init__(self, cesta):
        # Seznamy
        self.cesta_importovaneho_souboru = cesta
        self.seznam_objektu = []
        # Spoustim
        self.import_dokumentu()
        self.nastaveni_crontabu()

    def import_dokumentu(self):
        ### Import dokumentu ###
        with open(self.cesta_importovaneho_souboru) as csv: # importuje soubor
            print(csv.readline()) # přečte a ignoruje první řádek
            for x in csv.readlines(): # přečte postupně řádky
                data = x.split(";") # udělá u toho list a rozdělí ho
                
                objekt = Prikazy(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9],
                                data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19],
                                data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28], data[29],
                                data[30], data[31], data[32], data[33], data[34], data[35], data[36], data[37], data[38], data[39],
                                data[40], data[41], data[42], data[43], data[44], data[45],) 
                
                # naplní objekt daty ze souboru
                self.seznam_objektu.append(objekt) # uloží objekt do seznamu



    def nastaveni_crontabu(self):
        
        with open("ok_report.csv", mode="w") as textak:
            textak.write("Player_name;IP_address_player;TV_name;IP_address_tv;Location;Note;Time_1;Command_1;Time_2;Command_2;Time_3;Command_3;Time_4;Command_4;Time_5;Command_5;Time_6;Command_6;Time_7;Command_7;Time_8;Command_8;Time_9;Command_9;Time_10;Command_10;Time_11;Command_11;Time_12;Command_12;Time_13;Command_13;Time_14;Command_14;Time_15;Command_15;Time_16;Command_16;Time_17;Command_17;Time_18;Command_18;Time_19;Command_19;Time_20;Command_20;\n")
        textak.close
        
        with open("err_report.csv", mode="w") as textak:
            textak.write("Player_name;IP_address_player;TV_name;IP_address_tv;Location;Note;Time_1;Command_1;Time_2;Command_2;Time_3;Command_3;Time_4;Command_4;Time_5;Command_5;Time_6;Command_6;Time_7;Command_7;Time_8;Command_8;Time_9;Command_9;Time_10;Command_10;Time_11;Command_11;Time_12;Command_12;Time_13;Command_13;Time_14;Command_14;Time_15;Command_15;Time_16;Command_16;Time_17;Command_17;Time_18;Command_18;Time_19;Command_19;Time_20;Command_20;\n")
        textak.close

        for x in self.seznam_objektu:
            if x.ip_adresa_player == "":
                pass
            else:
                
                try:
                    # print(f"{x.ip_adresa_player}\n{x.cmd_1}\n{x.cmd_2}\n{x.cmd_3}\n{x.cmd_4}\n{x.cmd_5}")
                    s = pxssh.pxssh()
                    # if not s.login(x.ip_adresa_player, 'pi', 'pi'):
                    s.login(x.ip_adresa_player, 'pi', 'pi', sync_multiplier=3)
                                        # s.login(x.ip_adresa_player, 'debug', ssh_key='signagelab.key', sync_multiplier=3)
                        # print(f"SSH session failed on login {x.ip_adresa_player} - {x.player_name} - {x.lokace} - {x.poznamka}")
                        # print(str(s))
                    # else:
                    print(f"SSH session login successful {x.ip_adresa_player} - {x.player_name} - {x.lokace} - {x.poznamka}")
                    ### CMD ###
                    
                    # # Toto je jen pro Signagelab
                    # s.sendline("sudo bash")
                    # # / Toto je jen pro Signagelab
                    
                    s.sendline("git clone https://github.com/xxlewi/Bluetouch_media_pub.git") # ok funguje

                    # write out current crontab
                    s.sendline("crontab -r")
                    s.sendline("crontab -l > mycron")
                    
                                    
                    if (x.prikaz_1 == "" or x.prikaz_1 == "-")  or (x.cas_1 == "" or x.cas_1 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_1} >> mycron')

                    if (x.prikaz_2 == "" or x.prikaz_2 == "-")  or (x.cas_2 == "" or x.cas_2 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_2} >> mycron')

                    if (x.prikaz_3 == "" or x.prikaz_3 == "-")  or (x.cas_3 == "" or x.cas_3 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_3} >> mycron')

                    if (x.prikaz_4 == "" or x.prikaz_4 == "-")  or (x.cas_4 == "" or x.cas_4 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_4} >> mycron')

                    if (x.prikaz_5 == "" or x.prikaz_5 == "-")  or (x.cas_5 == "" or x.cas_5 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_5} >> mycron')
                        
                    if (x.prikaz_6 == "" or x.prikaz_6 == "-")  or (x.cas_6 == "" or x.cas_6 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_6} >> mycron')

                    if (x.prikaz_7 == "" or x.prikaz_7 == "-")  or (x.cas_7 == "" or x.cas_7 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_7} >> mycron')

                    if (x.prikaz_8 == "" or x.prikaz_8 == "-")  or (x.cas_8 == "" or x.cas_8 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_8} >> mycron')

                    if (x.prikaz_9 == "" or x.prikaz_9 == "-")  or (x.cas_9 == "" or x.cas_9 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_9} >> mycron')

                    if (x.prikaz_10 == "" or x.prikaz_10 == "-")  or (x.cas_10 == "" or x.cas_10 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_10} >> mycron')
                        
                    if (x.prikaz_11 == "" or x.prikaz_11 == "-")  or (x.cas_11 == "" or x.cas_11 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_11} >> mycron')

                    if (x.prikaz_12 == "" or x.prikaz_12 == "-")  or (x.cas_12 == "" or x.cas_12 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_12} >> mycron')

                    if (x.prikaz_13 == "" or x.prikaz_13 == "-")  or (x.cas_13 == "" or x.cas_13 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_13} >> mycron')

                    if (x.prikaz_14 == "" or x.prikaz_14 == "-")  or (x.cas_14 == "" or x.cas_14 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_14} >> mycron')

                    if (x.prikaz_15 == "" or x.prikaz_15 == "-")  or (x.cas_15 == "" or x.cas_15 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_15} >> mycron')
                        
                    if (x.prikaz_16 == "" or x.prikaz_16 == "-")  or (x.cas_16 == "" or x.cas_16 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_16} >> mycron')

                    if (x.prikaz_17 == "" or x.prikaz_17 == "-")  or (x.cas_17 == "" or x.cas_17 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_17} >> mycron')

                    if (x.prikaz_18 == "" or x.prikaz_18 == "-")  or (x.cas_18 == "" or x.cas_18 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_18} >> mycron')

                    if (x.prikaz_19 == "" or x.prikaz_19 == "-")  or (x.cas_19 == "" or x.cas_19 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_19} >> mycron')

                    if (x.prikaz_20 == "" or x.prikaz_20 == "-")  or (x.cas_20 == "" or x.cas_20 == "-"):
                        pass
                    else:
                        s.sendline(f'echo {x.cmd_20} >> mycron')
                    
                    
                    # print(cron)
                    # install new cron file
                    
                    s.sendline("crontab mycron")
                    s.sendline("cat crontab -l")
                    s.sendline("rm mycron")
                    
                                ###### /CMD ########
            
                    #zapsání do souboru

                    with open("ok_report.csv", mode="a+") as textak:
                        # textak.write(f"Player_name;IP_address_player;TV_name;IP_address_tv;Location;Note;Time_1;Command_1;Time_2;Command_2;Time_3;Command_3;Time_4;Command_4;Time_5;Command_5;Time_6;Command_6;Time_7;Command_7;Time_8;Command_8;Time_9;Command_9;Time_10;Command_10;Time_11;Command_11;Time_12;Command_12;Time_13;Command_13;Time_14;Command_14;Time_15;Command_15;Time_16;Command_16;Time_17;Command_17;Time_18;Command_18;Time_19;Command_19;Time_20;Command_20;\n")
                        textak.write(f"{x.player_name};{x.ip_adresa_player};{x.tv_name};{x.ip_adresa_tv};{x.lokace};{x.poznamka};{x.cas_1};{x.prikaz_1};{x.cas_2};{x.prikaz_2};{x.cas_3};{x.prikaz_3};{x.cas_4};{x.prikaz_4};{x.cas_5};{x.prikaz_5};{x.cas_6};{x.prikaz_6};{x.cas_7};{x.prikaz_7};{x.cas_8};{x.prikaz_8};{x.cas_9};{x.prikaz_9};{x.cas_10};{x.prikaz_10};{x.cas_11};{x.prikaz_11};{x.cas_12};{x.prikaz_12};{x.cas_13};{x.prikaz_13};{x.cas_14};{x.prikaz_14};{x.cas_15};{x.prikaz_15};{x.cas_16};{x.prikaz_16};{x.cas_17};{x.prikaz_17};{x.cas_18};{x.prikaz_18};{x.cas_19};{x.prikaz_19};{x.cas_20};{x.prikaz_20};\n")         
                    textak.close

                    # s.prompt()         # match the prompt
                    # print(s.before)     # print everything before the prompt.
                    s.logout()
                    
                except pxssh.ExceptionPxssh as e:
                    print("pxssh failed on login.")
                    print(e)    
                    print(f"SSH session failed on login {x.ip_adresa_player}")
                    

                    with open("err_report.csv", mode="a+") as textak:
                        # textak.write(f"Player_name;IP_address_player;TV_name;IP_address_tv;Location;Note;Time_1;Command_1;Time_2;Command_2;Time_3;Command_3;Time_4;Command_4;Time_5;Command_5;Time_6;Command_6;Time_7;Command_7;Time_8;Command_8;Time_9;Command_9;Time_10;Command_10;Time_11;Command_11;Time_12;Command_12;Time_13;Command_13;Time_14;Command_14;Time_15;Command_15;Time_16;Command_16;Time_17;Command_17;Time_18;Command_18;Time_19;Command_19;Time_20;Command_20;\n")
                        textak.write(f"{x.player_name};{x.ip_adresa_player};{x.tv_name};{x.ip_adresa_tv};{x.lokace};{x.poznamka};{x.cas_1};{x.prikaz_1};{x.cas_2};{x.prikaz_2};{x.cas_3};{x.prikaz_3};{x.cas_4};{x.prikaz_4};{x.cas_5};{x.prikaz_5};{x.cas_6};{x.prikaz_6};{x.cas_7};{x.prikaz_7};{x.cas_8};{x.prikaz_8};{x.cas_9};{x.prikaz_9};{x.cas_10};{x.prikaz_10};{x.cas_11};{x.prikaz_11};{x.cas_12};{x.prikaz_12};{x.cas_13};{x.prikaz_13};{x.cas_14};{x.prikaz_14};{x.cas_15};{x.prikaz_15};{x.cas_16};{x.prikaz_16};{x.cas_17};{x.prikaz_17};{x.cas_18};{x.prikaz_18};{x.cas_19};{x.prikaz_19};{x.cas_20};{x.prikaz_20};\n")         
                    textak.close
                
    
    def auktualizace_rpi(self):
        for x in self.seznam_objektu:
            try:
                s = pxssh.pxssh()
                s.login(x.ip_adresa_player, 'pi', 'pi', sync_multiplier=3)
                # auto_prompt_reset=False            
        
                print(f"SSH session login successful {x.ip_adresa_player}")
                ### CMD ###
                
                # # vytvoření souboru
            
                s.sendline("cd /home/pi")
                s.sendline("echo 'sudo apt-get -y update' > update.sh")
                s.sendline("echo 'sleep 3' >> update.sh")
                s.sendline("echo 'sudo apt-get -y upgrade' >> update.sh")
                s.sendline("echo 'sleep 3' >> update.sh")
                s.sendline("echo 'sudo apt autoremove -y' >> update.sh")
                s.sendline("echo 'sleep 3' >> update.sh")
                s.sendline("echo 'sudo apt-get autoclean -y' >> update.sh") 
                s.sendline("echo 'sleep 3' >> update.sh")
                s.sendline("echo 'sudo reboot' >> update.sh")
                # # sudo apt update && sudo apt full-upgrade
                
                # #nastavení oprávnění
                s.sendline("sudo chmod +x aktualizace.sh")
                
                # spuštění příkazu a detach
                s.sendline("./aktualizace.sh & disown")
                
                

                ###### /CMD ########
                
                #zapsání do souboru

                with open("report.csv", mode="a+") as textak:
                    textak.write(f"{x.ip_adresa_player}; Ok;\n")
                textak.close


                # s.prompt()         # match the prompt
                # print(s.before)     # print everything before the prompt.
                s.logout()
                
                
            except pxssh.ExceptionPxssh as e:
                print("pxssh failed on login.")
                print(e)    
                print(f"SSH session failed on login {x.ip_adresa_player}")
                

                with open("report.csv", mode="a+") as textak:
                    textak.write(f"{x.ip_adresa_player}; Chyba;\n")
                textak.close
        
            
                    
    
################### PROGRAM ####################     
    
soubor = "import_moje.scv.csv"       
program = Program(soubor)