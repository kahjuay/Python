text = "X-DSPAM-Confidence:    0.8475";
intPos = text.find(":")
fltNum = float(text[intPos+1:])
print (fltNum)