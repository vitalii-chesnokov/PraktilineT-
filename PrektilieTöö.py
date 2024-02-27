#(2)
from pickle import FALSE, TRUE


def is_year_leap(arv:int)->bool:
    """ Funktsioon tagastab True, kui aasta in liigaasta või False, kui aasta on tavaline
    :param int aasta: kasutaja sisestab aasta number
    :rtype: bool
    """
    if aasta % 4 == 0:
        vastus=TRUE
    else:
        vastus=FALSE
    return vastus 

##(1) ARITHMETIC
#def arithmetic(arv1:float,arv2:flost,sumb:str)->any:
#    """ Funktsion tagastab aritmeetiliste tehtede tulemused
#    + - liitumine 
#    - -lahutamine
#    * - korrutamine
#    / -jagamine
#    :param float arv1: ujukomaarv mis sisestab kasutaja 
#    :param float arv2: ujukomaarv mis sisestab kasutaja
#    :param str sõne/tehe, mis sisestab kasutaja 

#    """
#    if sumb == "+":
#         vastus=arv1+arv2
#    elif sumb == "-":
#         vastus=arv1-arv2
#    elif sumb == "*":
#         vastus=arv1*arv2
#    elif sumb == "/":
#        if arv2==0:
#             vastus="DIV/0"
#        else:
#             vastus=arv1/arv2
#    else:
#         vastus="Tundmatu operatsioon"
#    return vastus