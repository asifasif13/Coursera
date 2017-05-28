score = raw_input("Enter Score: ")
sc = float(score)
if(sc>=0.0 and sc<=1.0):
    if(sc>=.9):
        print 'A'
    elif(sc>=.8):
        print 'B'
    elif sc>=.7:
        print 'C'
    elif sc>=.6:
        print 'D'
    else:
        print 'F'
else:
    print 'Out of range'