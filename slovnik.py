
# ## = chybí checksum

slovnik = {
    "power_state" : { #4.1 dokumentace
        "message_get" : {
            "get": "050100191D",
            "report_on": "06010119021d", # pozor změnila se tam skupina z 00 na 01 - možná to budu parsovat
            "report_off": "06010119011e"
        },
        "message_set" : {
            "turn_on" : "06010018021D",
            "turn_off": "06010018011E"
        }
    }
}

# print(slovnik["Power_state"]["Message_get"]["Get"]) # Zavolám příkaz GET

# test = "0601001901##"

# #Projdu slovník a porovnám jestli není výsledek ve slovníku
# for x in slovnik["Power_state"]["Message_get"]:
#     if test in slovnik["Power_state"]["Message_get"][x]:
#         print(x)
#     else:
#         print("Chyba, výsledek nenalezen")

