import pandas as pd

class charge_controller():
    def __init__(self, cc_voltage, cc_current):
        self.voltage = cc_voltage
        self.current = cc_current
        
class inverter():
    pass

class battery():
    def __init__(self, batt_voltage, batt_type, batt_size, batt_peukert):
        self.voltage = batt_voltage
        self.type = batt_type
        self.size = batt_size
        self.peukert = batt_peukert

class solar_panel():
    def __init__(self, sp_voc, sp_isc, sp_vmp, sp_imp, sp_wattage):
        self.wattage = sp_wattage

class generator():
    pass

if __name__ == "__main__":

    #Create a charge controller object
    cc_voltage = 75
    cc_current = 15

    cc1 = charge_controller(cc_voltage, cc_current)

    #Create a battery object
    batt_voltage = 12  #V
    batt_type = "LFP"
    batt_size = 60     #Ah
    batt_peukert = 1.05

    batt1 = battery(batt_voltage, batt_type, batt_size,batt_peukert)

    #Create a solar panel object
    sp_voc = 0
    sp_isc = 0
    sp_vmp = 0
    sp_imp = 0
    sp_wattage = 320

    sp1 = solar_panel(sp_voc, sp_isc, sp_vmp, sp_imp, sp_wattage)

    #load the solar insolation data

    insolation_df = pd.read_csv("manila_8760.csv", index_col=0)

    print insolation_df

    #Load the load profiles

    loads_df = pd.read_csv("load_profiles.csv")
    loads_df['day'] = 0

    print loads_df

    #Create as base dataframe with insolation and load data only
    #
    #First, ascertain the type of load profile
    #Allowable types are 24hr (daily), 168hr (weekly), or 8760hr (annual).
    #Reject any other types and crash out for now

    loads_df_length = 24 #Fucking just assume it's daily for now... add this functionality later

    print loads_df_length

    if loads_df_length == 24:

        i = 0
        while i < 365:

            if i == 0: loads_8760_df = loads_df
            else:
                loads_df['day'] = i
                loads_8760_df = loads_8760_df.join(loads_df)
            i += 1


        #loads_8760_df.set_index('day', inplace=True)

    print loads_8760_df

    #Now merge the solar insolation df

    #calculations_df = 



    