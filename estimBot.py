print("EstimBot V 0.1 \n")

rep = int(input("number of zones....\n"))

def normalCalc():
    xm = float(input("Enter the lenght....\n"))
    ym = float(input("Enter the height....\n"))
    format_X = float(input("Size x....\n"))
    format_y = float(input("Size y....\n"))
    unit = input("Enter the Unit....\n")
    area = round(xm * ym,2)
    full_tile = round(xm / format_X,0) * round(ym / format_y,0)
    print("The area is {0} {1} and need {2} tiles\n".format(area, unit, full_tile))

def zoneCall(x):
    for n in range(x):
        print("zone {0}".format(n+1))
        normalCalc()
    print("Done")

zoneCall(rep)
