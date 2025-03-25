def check_month(ay):
    liste = []

    pazartesi = ay[::5]
    sali = ay[1::5]
    carsamba = ay[2::5]
    cuma = ay[4::5]


    # mother check
    if "m" in ay:
        m_off_day = ay.index("m")
        m_days = ay[m_off_day::5]
        if m_days.count("m")!=ay.count("m"):
            liste.append(1)



    # father check
    if "f" in ay:
        if ay.count("f")>2:
            liste.append(2)
        elif ay.index("f")!=len(ay)-1:
            if ay[ay.index("f")+1]=="f":
                if ay.index("f")%5!=4:
                    liste.append(2)



    # babysitter check -- always available

    # grandma check  
    if carsamba.count("g")>1:
        liste.append(4)



    # aunt1 check    
    top_a1 = sali.count("a1") + cuma.count("a1")
    if ay.count("a1")!=top_a1:
        liste.append(5)



    # aunt2 check
    metin= "".join(ay)
    if "a1a2" in metin:
        k = metin.count("a1a2")
        if ay[4]=="a1" and ay[5]=="a2":
            k -=1
        if ay[9]=="a1" and ay[10]=="a2":
            k-=1
        if ay[14]=="a1" and ay[15]=="a2":
            k-=1
        if len(ay)>20:
            if ay[19]=="a1" and ay[20]=="a2":
                k-=1
        if k>=1:
            liste.append(6)
            


    # n check
    top_n = pazartesi.count("n") + sali.count("n") + carsamba.count("n")
    if ay.count("n")!=top_n:
        liste.append(7)



    # liste check
    if len(liste)>0:
        #print(liste)
        return liste


    # unit calculation
    toplam = 0
    toplam += 10*ay.count("m")
    toplam += 20*ay.count("f")
    toplam += 50*ay.count("g")
    toplam += 32*ay.count("a1")
    toplam += 27*ay.count("a2")
    if ay.count("n")>1:
        def q(r,n):
            top = (1-r**(n+1))/(1-r)   
            top -= 1
            return int(top)
        toplam += q(5,ay.count("n")-1)
    # calculus dersinde yeni ogrendigimiz formul


    # babysitter unit hesapla
    
    #haftasonlari
    def g(i):
        ay.insert(i, "x")
        ay.insert(i+1, "x")
    g(5);g(12);g(19);g(26)

    top_b = ay.count("b")

    def f():
        if ay.count("b")>1:
            b_unit = 0
            ilk_b = ay.index("b")
            ikinci_b = ay.index("b", ilk_b+1)
            if ikinci_b-ilk_b<=3:
                b_unit += ikinci_b-ilk_b-1
            ay.remove("b")
            return b_unit
        else:
            return 0
    
    top_b += f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()+f()
    toplam += top_b*30
    
    #print(toplam)
    return toplam


"""M1 = ["g","m","f","a2","a1",
"b","n","n","g","a1",
"n","m","b","b","b",
"b","m","f","b","a2",
"a2"
]

check_month(M1)"""
