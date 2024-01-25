from enum import Enum
import random  
import numpy as np

event= Enum('event',['TtoH','HtoR','RtoD','DtoR','RtoT'])


def compute_possible_events(X):
    possible_events=[]
    if X[0]>0: # T
        possible_events.append(event.TtoH)
    if X[1]>0: # H
        possible_events.append(event.HtoR)
    if X[2]>0: # R
        possible_events.append(event.RtoD)
        possible_events.append(event.RtoT)
    if X[3]>0: # D 
        possible_events.append(event.DtoR)
    return possible_events
    # dans tous les cas un nouveau truc peut arriver dans http 
    # possible_events.append(event.http)
    #match ev:
     #   case event.http:
      #      possible_events.append(event.proc)
       # case event.proc:
        #    possible_events.append(event.database)
         #   possible_events.append(event.out)
       # case event.database:
        #    possible_events.append(event.proc)
        #case _:
         #   pass
    #return possible_events
        

# event= Enum('event',['TtoH','HtoR','RtoD','DtoR','RtoT'])

def rate(S,X,lh, uh, ur, ud, C, p): # pas fini
    res=S

    #  ∆X = λH + μH 1(XH > 0) + min(XR, C)μR + μD · 1(XD > 0)
    for rate in res:
        match rate:    
            case event.TtoH:
                rate=lh
            case event.HtoR:
                rate=uh
            case event.RtoD:
                rate=min(C*ur,X[2]*ur)
            case event.DtoR:
                rate=ud
            case event.RtoT:
                pass 

def indic(x):
    return 1 if x else 0
                



def compute_one_thread(lh, uh, ur, ud, C, p):
    # initialisation 
    N=1
    #  T0 H1 R2 D3 
    X=[N,0,0,0]
    #et=[1,0,0,0]
    #eh=[0,1,0,0]
    #er=[0,0,1,0]
    #ed=[0,0,0,1]
    k=0 # when T is empty to calculate possibility of rejection 
    A=[0,0,0,0]
    tau=1000
    #events=[event.rien]

     #  ∆X = λH + μH 1(XH > 0) + min(XR, C)μR + μD · 1(XD > 0)
   
    # simulation 
    for n in range(1,tau):
        u=random.uniform(0.0,1.0)
        max_rate=lh*indic(X[0]>0) + uh*indic(X[1]>0) + min(X[2],C)*ur + ud*indic(X[3])
        proba_TtoH=lh*indic(X[0]>0)/max_rate
        proba_HtoR=uh*indic(X[1]>0)/max_rate
        proba_RtoD=(1-p)*ur*min(X[2],C)/max_rate
        proba_RtoT=p*ur*min(X[2],C)/max_rate
        proba_DtoR=ud*indic(X[3]>0)/max_rate
        
        print("tour {}".format(n))
        print("max_rate: {}".format(max_rate))
        print("probas:")
        print(proba_TtoH)
        print(proba_HtoR)
        print(proba_RtoD)
        print(proba_RtoT)
        print(proba_DtoR)
        print("sum probas: {}".format(proba_DtoR+proba_HtoR+proba_RtoD+proba_RtoT+proba_TtoH))

        #  T0 H1 R2 D3 
        # X=[N,0,0,0]
        #S=compute_possible_events(X)
        if u <= proba_TtoH:
            # X=X+eh-et
            X[1]+=1
            X[0]-=1
        elif proba_TtoH <= u <= proba_HtoR+proba_TtoH:
            # X=X+er-eh
            X[2]+=1
            X[1]-=1
        elif proba_HtoR+proba_TtoH <= u <= proba_HtoR+proba_TtoH+proba_RtoD:
            # X=X+ed-er
            X[3]+=1
            X[2]-=1
        elif proba_HtoR+proba_TtoH+proba_RtoD <= u <= proba_HtoR+proba_TtoH+proba_RtoD+proba_RtoT:
            # X=X+et-er
            X[0]+=1
            X[2]-=1
        elif proba_HtoR+proba_TtoH+proba_RtoD+proba_RtoT <= u <= proba_HtoR+proba_TtoH+proba_RtoD+proba_RtoT+proba_DtoR:
            # X=X+er-ed
            X[2]+=1
            X[3]-=1
        else:
            print("gros soucis" + str(u))
            exit()
        
        # performances measures 
        k+=indic(X[0]==0)


    p_rejec=k/tau 
    cust_numb=
    return (X,p_rejec,# performance measures with N = 1 


X=compute_one_thread(1,1,1,1,1,0.9)
print(X)