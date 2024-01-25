import random  
import numpy as np


# fonction indicatrice 
def indic(x):
    return 1 if x else 0
                



def compute_one_thread(lh, uh, ur, ud, C, p):
    N=1
    print("Computing with lamdba_h {}, mu_h {}, mu_r {},mu_d {}, C {}, p {} and N {}".format(lh, uh, ur, ud, C, p, N))
    # initialisation 
    #  T0 H1 R2 D3 
    X=[N,0,0,0]
    tours=1000 
    tau=0
    # performance measures 
    k=0 # when T is empty to compute possibility of rejection 
    customers=[0,0,0,0] # to compute mean number of customers 
    requests=[0,0,0,0] # to compute throughput 
   
 
    # simulation 
    for _ in range(1,tours):
        u=random.uniform(0.0,1.0)
        max_rate=lh*indic(X[0]>0) + uh*indic(X[1]>0) + min(X[2],C)*ur + ud*indic(X[3])
        tau+=max_rate# np.random.exponential(max_rate)
        proba_TtoH=lh*indic(X[0]>0)/max_rate
        proba_HtoR=uh*indic(X[1]>0)/max_rate
        proba_RtoD=(1-p)*ur*min(X[2],C)/max_rate
        proba_RtoT=p*ur*min(X[2],C)/max_rate
        proba_DtoR=ud*indic(X[3]>0)/max_rate
        
        #print("sum probas: {}".format(proba_DtoR+proba_HtoR+proba_RtoD+proba_RtoT+proba_TtoH))

        #  T0 H1 R2 D3 
        if u <= proba_TtoH:
            # X=X+eh-et
            X[1]+=1
            X[0]-=1
            requests[1]+=1
        elif proba_TtoH <= u <= proba_HtoR+proba_TtoH:
            # X=X+er-eh
            X[2]+=1
            X[1]-=1
            requests[2]+=1
        elif proba_HtoR+proba_TtoH <= u <= proba_HtoR+proba_TtoH+proba_RtoD:
            # X=X+ed-er
            X[3]+=1
            X[2]-=1
            requests[3]+=1
        elif proba_HtoR+proba_TtoH+proba_RtoD <= u <= proba_HtoR+proba_TtoH+proba_RtoD+proba_RtoT:
            # X=X+et-er
            X[0]+=1
            X[2]-=1
            requests[0]+=1
        elif proba_HtoR+proba_TtoH+proba_RtoD+proba_RtoT <= u <= proba_HtoR+proba_TtoH+proba_RtoD+proba_RtoT+proba_DtoR:
            # X=X+er-ed
            X[2]+=1
            X[3]-=1
            requests[2]+=1
        else:
            print("gros soucis" + str(u))
            exit()
        
        # performances measures 
        k+=indic(X[0]==0)
        customers=np.add(customers,X)


    p_rejec=k/tau 
    cust_nb=[nb/tau for nb in customers]
    throughput=[nb/tau for nb in requests]
    return (p_rejec,cust_nb,throughput)# performance measures with N = 1 


(p_rejec,cust_nb,throughput)=compute_one_thread(lh=2,ud=1,uh=1,ur=1,C=1,p=1)
print("probabilité de refus : {}".format(p_rejec))
print("nombre de clients : {}, total : {}".format(cust_nb,sum(cust_nb)))
print("throughput : {}, total : {}".format(throughput,sum(throughput)))
