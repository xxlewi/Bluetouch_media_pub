version = "0.0.1"
from pexpect import pxssh
from slovnik import philips

class Program():
    def __init__(self, ip_player, ip_tv, player_name, lokace, poznamka, cas_1, prikaz_1, cas_2, prikaz_2, cas_3, prikaz_3, cas_4, prikaz_4, cas_5, prikaz_5):
        self.ip_player = ip_player.strip()
        self.ip_tv = ip_tv.strip()
        self.cesta_k_programu = " /usr/bin/python3 /home/pi/dsmedia_remote/main.py "
        # self.cmd_1 = '"' + self.cas_1 + self.cesta_k_programu + self.prikaz_1 + '"'

    def prikaz_do_rpi(self):
        s = pxssh.pxssh()
        if not s.login(self.ip_player, 'pi', 'pi'):
            print(f"SSH session failed on login {self.ip_player}")
            print(str(s))
        else:
            print(f"SSH session login successful {self.ip_player}")
            ### CMD ###
            # s.sendline("git clone https://github.com/xxlewi/dsmedia_remote.git") # stáhne repozitář
            # s.prompt()         # match the prompt
            # print(s.before)     # print everything before the prompt.
            s.logout()
    
    # def prikaz(self, cmd_p):
    #     stream = f"echo '{cmd_p}'|xxd -r -p|nc -w 1 {self.ip_tv} 5000|xxd -ps"
    #     return stream
            
    # def prikaz_do_tv(self, prikaz):
        
        