# This is example code for the BK Precision 5335B Power Meter
# A programming manual for the BK Precision 5335B can be found at:
# https://bkpmedia.s3.amazonaws.com/downloads/programming_manuals/en-us/5335B_programming_manual.pdf


import visa
import time
    
manager = visa.ResourceManager()
print("This Script is made for the BK5335B Power Meter")
manager = visa.ResourceManager()
li = manager.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which Device?: ")
Power_Meter = manager.open_resource(li[int(choice)]) #creates an alias (variable) for the VISA resource name of a device
# we do this so we don't have to call that constantly. This is unique to a unit and changes depending on USB port used and serial number of a unit. 
# This will automatically detect connected devices and allows you to select the one you want to run the script on.



# Since this is a measurement device, many of the commands are simply measurement commands and are very similar!




#####_________________________Initialize_________________________#####
print("Initializing Test Script...")
print("\n")
print("\n")


Power_Meter.write("System:REM")         # Sets System to Remote Mode 
#Power_Meter.write("System:BEEP:imm")    # Test BEEP!
Power_Meter.write("System:CLE")         # Clears Errors
Power_Meter.write("CALC:int on")        # Sets integration mode to on 
Power_Meter.write("int:star")           # Starts Integration

Power_Meter.write("calc:harm on")       # Sets Harmonic Calculation to on

Power_Meter.write("calc:scope off")     # turns off oscilloscope
Power_Meter.write("Calc:hold off")      # turns hold mode off

Power_Meter.write("INR ON")             # Turns on inrush measurement
Power_Meter.write("INr:TRIG:Curr 0.01") # sets the current trigger level for the inrush current measurement to 0.01A

time.sleep(1)   # Time delay in seconds

 

#####_________________________Reading Voltage and Current Measurements_________________________#####
print("Current Measurements: ")
print("\n")

print("AC Reading:", end =' ')
Power_Meter.write("Fetch:curr:AC?")     # To read values we use either the fetch or measure command.
print(Power_Meter.read())               # Notice the case doesn't matter and we can either use the short or long form.
                                        # All of these commands work the same for the voltage, using the VOLTage command.
print("DC Reading:", end =' ')
Power_Meter.write("Fetch:current:DC?")
print(Power_Meter.read())

print("Crest Factor:", end =' ')
Power_Meter.write("Fetch:CURRent:CFAC?")
print(Power_Meter.read())

print("RMS:", end =' ')
Power_Meter.write("Fetch:CuRr:RMS?")
print(Power_Meter.read())

print("RMN:", end =' ')
Power_Meter.write("FetC:current:rmn?")
print(Power_Meter.read())

print("Mean:", end =' ')
Power_Meter.write("measure:current:mn?")
print(Power_Meter.read())

print("Inrush:", end =' ')
Power_Meter.write("MEAS:current:INr?")
print(Power_Meter.read())

print("Max:", end =' ')
Power_Meter.write("mEaS:cUrR:mAxP?")
print(Power_Meter.read())

print("Min:", end =' ')
Power_Meter.write("Fetch:current:MINpk?")
print(Power_Meter.read())

print("Peak-to-Peak:", end =' ')
Power_Meter.write("Fetch:current:PPEAK?")
print(Power_Meter.read())
print("\n")
print("\n")

#####_________________________Reading Power Measurements_________________________#####

print("Power Measurements: ")
print("\n")


print("Active:", end =' ')
Power_Meter.write("fetc:pow:act?")
print(Power_Meter.read())

print("Apparent:", end =' ')
Power_Meter.write("fetc:pow:app?")
print(Power_Meter.read())

print("Reactive:", end =' ')
Power_Meter.write("meas:pow:reac?")
print(Power_Meter.read())

print("Power Factor:", end =' ')
Power_Meter.write("measure:power:pfactor?")
print(Power_Meter.read())

print("Phase:", end =' ')
Power_Meter.write("Fetch:power:phase?")
print(Power_Meter.read())                           # We use similar commands for measure frequency and energy measurements

print("\n")
print("\n")

#####_________________________Harmonics_________________________#####

# Some Random Harmonic Measurements
print("Some Harmonic Measurements: ")
print("\n")

print("Current - Total Harmonic Distortion:", end ='\n')
Power_Meter.write("fetc:harm:curr:thd?")
print(Power_Meter.read())

print("Total Harmonic Voltage:", end =' ')
Power_Meter.write("meas:harm:volt:thar?")
print(Power_Meter.read())

print("Apparent Power Harmonic:", end ='\n')
Power_Meter.write("Fetch:Harm:POWER:APP?")
print(Power_Meter.read())

print("\n")
print("\n")

# Changing Harmonic Settings
print("Some Harmonic Settings: ")
print("\n")

Power_Meter.write("Harm:seq ODD")
print("Harmonic Sequence is", end =' ')
Power_Meter.write("Harm:seq?")
print(Power_Meter.read())

Power_Meter.write("harmonic:THD THDR ")                            
print("Formula for Total Harmonic Distortion is", end =' ') 
Power_Meter.write("Harm:thd?")
print(Power_Meter.read())

Power_Meter.write("harm:PLLS off")
print("Phase Locked Loop Source is", end =' ')
Power_Meter.write("Harm:plls?")
print(Power_Meter.read())

print("\n")
print("\n")






#####_________________________END_________________________#####

Power_Meter.write("int:stop")       # Stops Integration 
Power_Meter.write("calc:int off")   # Turns Integration off
Power_Meter.write("calc:int:cle")   # Clears Integration
Power_Meter.write("System:LOC")     # Sets Control Mode to Local

Power_Meter.write("System:err?")
print(Power_Meter.read())               # Queries error code (0 is none)

print("Goodbye")