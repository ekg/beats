son_clave = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0] #The 7th repreentation from Toussaint
clave_rumba =(1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0)
clave_bossa_nova = (1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0)
clave_son =     (1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0)

Clock.bpm=121
x0 >> play(P["x-o"]*son_clave)
x2 >> blip(P[0,1.5]-8,amp=son_clave, delay=0.5)
x1 >> play(P["-"]*son_clave)
d1 >> play(P["V-o-"], sample=7)

print(SynthDefs)
Clock.clear()
