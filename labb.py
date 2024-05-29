import time
def prefix(num, enhet):
    prefix = ["","milli","micro","nano","pico"]
    for i in range(len(prefix)):
        if num*(1000**(i))>= 1:
            response = str(num*(1000**(i)))+" "+prefix[i]+ enhet
            return response
L = float(input(f"Ange distansen i meter mellan mätinstrumentet och den roterande spegeln: \n"))
d = float(input(f"Ange distansen i meter mellan den roterande spegeln och den sväriska spegeln: \n"))
w = float(input(f"Ange varvtalen i varv per sekund: \n"))
r = (4*3.14 * w * d / 299792458)
u = r*2
h = L * u
c = 8 * 3.14 * w * d * L/h
print("Med dessa mätvärden skulle det visas två punkter på mätinstrumentet med",prefix(h,"meter"), "mellanrum")
time.sleep(3)
print("och ljusets hastighet skulle kalkyleras till",c,"m/s")