hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r=float(rate)
if(h>40):
    print 40*r+(h-40)*1.5*r
else:
    print h*r