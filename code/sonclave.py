son_clave = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0] #The 7th repreentation from Toussaint
clave_rumba =(1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0)
clave_bossa_nova = (1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0)
clave_son =     (1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0)

print(PEuclid(3,8)|PEuclid(2,5).rotate(-2)|[0,0,0])
print(son_clave)

def b2(rhythm, s1,s2):
    return ''.join([s1 if r ==0 else s2 for r in rhythm])

d1 >> play(P['V']*PEuclid(5,16))
p2 >> play(P[b2(son_clave," ",'p')],pan=(1,-1))
p3 >> play(P[b2(son_clave,"s",' ')],pan=(-1,1))

p4 >> play(P[b2(son_clave," ",' V')],pan=(1,-1))
p5 >> play(P[b2(son_clave," t",' ')],pan=(-1,1))

b1 >> dbass(P[1,1,2,0,1,0,2,1] , amp=son_clave, chop=2)

Root.default = -2

print(PEuclid(5,16))

print(son_clave)
Clock.bpm = 120
