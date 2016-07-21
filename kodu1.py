sümbolid={}
def sümbolite_sagedus(sõne):
    arv=1
    n=0
    for sümbol in sõne:
        if sümbol not in sümbolid:
            sümbolid[sümbol]=sõne.count(sümbol)
       
    return sümbolid

hulk=set()
def erinevad_sümbolid(sõne):
    for sümbol in sõne:
        hulk.add(sümbol)
    return hulk

print(sümbolite_sagedus("Tere maailm!"))
print(erinevad_sümbolid("maailm"))