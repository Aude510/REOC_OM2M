import random  
import numpy as np


# fonction indicatrice 
def indic(x):
    return 1 if x else 0
                



def compute_N_thread(lh, uh, ur, ud, C, p,N):

    print("Computing with lamdba_h {}, mu_h {}, mu_r {},mu_d {}, C {}, p {} and N {}".format(lh, uh, ur, ud, C, p, N))
    # initialisation 
    #  T0 H1 R2 D3 
    X=[N,0,0,0]
    tours=100000
 
    temps_total=0
    # performance measures 
    k=0 # when T is empty to compute possibility of rejection 
    customers=[0,0,0,0] # to compute mean number of customers 
    requests=[0,0,0,0] # to compute throughput 
   
 
    # simulation 
    for _ in range(1,tours):
        u=random.uniform(0.0,1.0)
        max_rate=lh*indic(X[0]>0) + uh*indic(X[1]>0) + min(X[2],C)*ur + ud*indic(X[3])
        duree=np.random.exponential(1/max_rate)
        temps_total+=duree
        proba_TtoH=lh*indic(X[0]>0)/max_rate
        proba_HtoR=uh*indic(X[1]>0)/max_rate
        proba_RtoD=(1-p)*ur*min(X[2],C)/max_rate
        proba_RtoT=p*ur*min(X[2],C)/max_rate
        proba_DtoR=ud*indic(X[3]>0)/max_rate
        
        # performances measures 
        k+=indic(X[0]==0)*duree # pondérer par durée en réseau ouvert 
        customers=[nb+x*duree for nb,x in zip(customers,X)] 

        
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
        

    p_rejec=k/temps_total 
    cust_nb=[nb/temps_total for nb in customers]
    throughput=[nb/temps_total for nb in requests]
    sojourns=[c/r if r!= 0 else 0 for c,r in zip(cust_nb,throughput)]
    (sojourn_h,sojourn_r,sojourn_d)=tuple(sojourns[1:])
    sojourn_r_d=(sojourn_r+(1-p)*sojourn_d)/p
    mean_sojourn=sojourn_h+sojourn_r_d
    return (p_rejec,cust_nb,throughput,mean_sojourn,sojourns) 


def part2():
    lh=1
    uh=10
    ur=1
    ud=10
    C=5
    p=0.5
    N=15

    (p_rejec,cust_nb,_,mean_sojourn,_)=compute_N_thread(lh,uh,ur,ud,C,p,N)


    print("Probability of rejection: {}".format(p_rejec))
    print("Average number of requests: {}".format(cust_nb))
    print("Mean sojourn time : {}".format(mean_sojourn))

    print("\n")
    print("-----------------------------------------------------------------------------------------\n")

    lh=1
    uh=10
    ur=1
    ud=10
    C=5
    p=0.22
    N=15

    (p_rejec,cust_nb,_,mean_sojourn,_)=compute_N_thread(lh,uh,ur,ud,C,p,N)


    print("Probability of rejection: {}".format(p_rejec))
    print("Average number of requests: {}".format(cust_nb))
    print("Mean sojourn time : {}".format(mean_sojourn))

    print("\n")
    print("-----------------------------------------------------------------------------------------\n")

    lh=1
    uh=10
    ur=1
    ud=10
    C=5
    p=0.5
    N=30

    (p_rejec,cust_nb,_,mean_sojourn,_)=compute_N_thread(lh,uh,ur,ud,C,p,N)


    print("Probability of rejection: {}".format(p_rejec))
    print("Average number of requests: {}".format(cust_nb))
    print("Mean sojourn time : {}".format(mean_sojourn))

    print("\n")
    print("-----------------------------------------------------------------------------------------\n")

    lh=1
    uh=10
    ur=1
    ud=10
    C=5
    p=0.22
    N=30

    (p_rejec,cust_nb,_,mean_sojourn,_)=compute_N_thread(lh,uh,ur,ud,C,p,N)


    print("Probability of rejection: {}".format(p_rejec))
    print("Average number of requests: {}".format(cust_nb))
    print("Mean sojourn time : {}".format(mean_sojourn))

    print("\n")
    print("-----------------------------------------------------------------------------------------\n")



def part1():
    lh=2
    uh=1
    ur=1
    ud=1
    C=1
    p=1
    N=1

    (p_rejec,_,_,mean_sojourn,_)=compute_N_thread(lh,uh,ur,ud,C,p,N)


    print("Probability of rejection: {}".format(p_rejec))
    print("Mean sojourn time : {}".format(mean_sojourn))

    print("\n")
    print("-----------------------------------------------------------------------------------------\n")



print("\n")
print("-----------------------------------------------------------------------------------------\n")

part1()
