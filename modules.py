import autoalert


def m1(ht,at,hs,ass,hp,ap,ha,aa,cl,per):
    if "1" in per:
        #8-11
        min=int(cl.split(":")[0])
        if min>=8 and min<12:
            if hs<-8.5 and hp>ap and ha>aa:
                autoalert.text()
            elif ass<-8.5 and ap>hp and aa>ha:
                autoalert.text()
    print("hi")

