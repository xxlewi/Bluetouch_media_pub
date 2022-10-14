version = "1.0.1"

slovnik = {
    "power_state" : { 
        "message_get" : {
            "get": "050100191D",
            "report_on": "06010119021d", # pozor změnila se tam skupina z 00 na 01 - možná to budu parsovat
            "report_off": "06010119011e"
        },
        "message_set" : {
            "turn_on" : "06010018021D",
            "turn_off": "06010018011E"
        }
    },
    "power_saving_mode" : {
        "message_get" : {
            "get": "050100D3D7",
            "mode_1": "060101d304d1",
            "mode_2": "060101d305d0",
            "mode_3": "060101d306d3",
            "mode_4": "060101d307d2"
        },
        "message_set" : {
            "mode_1": "060101d204d0",
            "mode_2": "060101d205d1",
            "mode_3": "060101d206d2",
            "mode_4": "060101d207d3"
            
        }
    }    
}

# for x in slovnik["power_saving_mode"]["message_set"]:
#     print(x) #tohle vyhodí klíče
#     print(slovnik["power_saving_mode"]["message_set"][x]) #tohle value<