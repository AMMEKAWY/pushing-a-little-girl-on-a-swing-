#--------importing modules-------------

import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------
#-------defining quantities-------------
#---------------------------------------

b=5.05                  #damping coeff.
m=40                    #little girl's mass
l=2                     #swing length
g=9.81                  #earth's gravitational acc.

uo=np.pi/6              #initial angle
u=[uo]                  #angle's list    
to=0                    #initial time
t=[to]                  #time list
tf=100                  #final time in seconds (when to stop)
h=(tf-to)/(100000)      #time step
wo=0                    #initial angular velocity
w=[wo]                  #angular velocity list
i=0                     #counter

#------------------------------------------
#-------if we didn't push the girl---------
#------(damped harmonic oscillator)--------
#---------Using Euler's method-------------
#------------------------------------------

while round(t[-1],1)!=tf:

    w.append(w[i]-((g/l)*np.sin(u[i])+(b/(m*l))*w[i])*h)
    u.append(u[i]+h*w[i])
    t.append(t[i]+h)
    i+=1

plt.plot(t,u)           #plotting the first curve
    
#------------------------------------------
#-if we are pushing the girl periodically--
#------(damped harmonic oscillator)--------
#---------Using Euler's method-------------
#------------------------------------------


#---------Re-defining quantities-----------

u=[uo]                  #angle list
to=0                    #initial time
t=[to]                  #time step
F=[0]                   #force list
h=(tf-to)/(100000)      #time step
wo=0                    #initial angular velocity 
w2=[wo]                 #the angular velocity for the second case
i=0                     #counter
angular=[]              #angular velocity limit list at
                        #t-->the first time period+epsilon (under no force)    


while round(t[i],1)!=tf:

    u.append(u[i]+h*w2[i])
    
    if i>=0 and i<50:   # we won't push at the very first swing
        F.append(0)     #at the first time she will move under
                        #the force of her weight
    else:

        #peak finding algorithm
        #we will push her only when she gets back
        
        if round((u[i]-u[i-1])/h,2)==0:
            if round((u[i+1]-2*u[i]+u[i-1])/h**2,2)<0:
                if u[i]<u[0]:
                    angular.append(w[i]) 
                    kk=round(2*(np.cos(u[i])-np.cos(u[0]))/np.sqrt((angular[0])**2),3) #multiplier
                    F.append(kk*m*g)    #the magnitude of the force
                else:
                    F.append(0)
            else:
                F.append(0)

        else:
            F.append(0)
    w2.append(w2[i]-((g/l)*np.sin(u[i])+(b/(m*l))*w2[i]+F[i]/(m*l))*h)
    t.append(t[i]+h)
    i+=1

#------------------------------------------
#------------scaling the force-------------
#------------------------------------------


i=0                 #counter
H=[]                #scaled-force list
while i != len(F):
    H.append(F[i]/(kk*m*g*10))
    i+=1



#------------------------------------------
#---------plotting the results-------------
#------------------------------------------

plt.plot(t,u)
plt.plot(t,H)
plt.xlabel("time (sec.)")
plt.ylabel("theta (rad)")
plt.grid()
plt.legend(['theta under no force','theta under force', 'scaled-force '], loc='upper right')

plt.show()
