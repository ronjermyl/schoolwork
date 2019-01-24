#CSIS 1400
#Lukas Simonson
#Using Crickets as a Thermometor
def main():
    #Usr Instructions
    print("===================================================")
    print("Hey Dipper, I'll calculate the temperature for you.")
    print("Using your stopwatch, count how many times the")
    print("cricket chirps in 13 seconds.")

    
    #Usr input
    chirps = input("How many chirps did you count?")
    
    #Float Conversion
    fltChirps = float(chirps)
    
    #Temp math
    temp = (fltChirps + 40)
    
    #Compares the temp for output
    if temp < 55:
        print("It is too cold for Crickets")
    #elif temp > 125:
    #    print("It is too hot for Crickets")
    else:
        print("By My Calculations it is about", temp, "degrees")
    
    #Closer
    print("===================================================")
    
main()

