def pikima_sõna_pikkus(sõne):
    kirjavahemärkideta=sõne.strip('!.')
    kirjavahemärkideta=kirjavahemärkideta.replace(',','')
    sõnad=kirjavahemärkideta.split()
    
    pikim=0
    for sõna in sõnad:
        pikkus=len(sõna)
        
        if pikkus>pikim:
            pikim=pikkus

    return pikim
        
print(pikima_sõna_pikkus("Tere tulemast!"))
print(pikima_sõna_pikkus("Poesell, Jim, ei öelnud midagi."))