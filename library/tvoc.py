def get_TVOC_condition(TVOC):

    if 2200 < TVOC < 5500:
        print ("Unhealthy")

    elif 660 < TVOC < 2200 :
        print ("Poor")

    elif 220 < TVOC < 660 :
        print ("Moderate")

    elif 65 < TVOC < 220 :
        print ("Good")

    elif 0 < TVOC < 65 :
        print ("Excellent")
