def computepay(h,r):
    if(h<=40):
      return h*r
    else:
      return 40*r+(h-40)*1.5*r

hrs = raw_input("Enter Hours:")
rate= raw_input("Enter Rate:")

p = computepay(float(hrs),float(rate))
print p