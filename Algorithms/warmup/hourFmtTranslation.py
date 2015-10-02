[hh, mm, ssS] = "12:00:00AM".split(":")
ss = ssS[0:2]
ampm = ssS[2:len(ssS)]

if ampm == "PM":
    HH = (int(hh) + 12 - int(hh)/12 * 12)
else:
    HH = (int(hh) - int(hh)/12 * 12)
print ":".join(["{:02d}".format(HH), mm, ss])
