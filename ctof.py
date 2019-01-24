#CSIS 1400
#Celcius to Farenheight
#Lukas Simonson

def main():
    #Usr Instructions
    print("This converts cel to far")
    print("You will enter cel and I")
    print("will respond with far")
    
    #input
    strcel = input("Degrees in cel ->")
    
    #Conversion
    fltcel = float(strcel)
    fltfar = ctof(fltcel)
    
    #Output
    print("The temp in far is", fltfar)
    
    if fltfar >= 100:
        print("Too hot")
    else:
        print("Too cold")

def ctof(fltcel):
    return (fltcel *(9/5)) + 32
    
main()