son_clave = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0] #The 7th repreentation from Toussaint
clave_rumba =(1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0)
clave_bossa_nova = (1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0)
clave_son =     (1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0)
claves = [son_clave,clave_rumba,clave_bossa_nova,clave_son]

for son in claves: print(PEuclid(5,16)-P[son])

Root.default = -2
print(son_clave)
Clock.bpm = 180
Clock.clear()
Clock.start()

def beat2dur(beat):
    durs = []
    current=1 #funk/hack, we start on a 1
    for e in beat:
        if 0==e:
            current+=1
        else:
            durs.append(current)
            current = 1
    durs.append(current)
    return durs[1:]# so dirty

def b2(rhythm, s1,s2):
    return ''.join([s1 if r ==0 else s2 for r in rhythm])
    
Root.default = -2
print(son_clave)
son = son_clave # Play diff to son_clave
def b2(rhythm, s1,s2):
    return ''.join([s1 if r ==0 else s2 for r in rhythm])
son_durs = P[beat2dur(son)]
r=rest()
p5 >> play(P[b2(son,"p ",'iat') ], pan=(1,-1), dur=1, amp=0.5)
p4 >> play(P[b2(son,"-s",'g(wy)hhh') ], pan=(-1,1), dur=1, amp=0.5)
b1 >> bass(P[0,r,[r,2,3,r],4,7],dur=beat2dur(son),pan=(1,-1),amp=0.5)
s1 >> swell([0],dur=16)

