import numpy as np
import matplotlib.pyplot as plt

#__Parametros__##########################
#Nº de muestras de tiempo
N = 100
#Nº de muestras de frecuencia
M = 1024
#Frecuencia en Hertz
FS = 200
F1 = 80
F2 = 80.5
#########################################

#__Ejes__################################
fstep = FS/M                             
R = 2*M #rango                          
                                        
def flim(S):                            
    return int(S/2)*fstep               
def tlim(S):                            
    return int(S/2)/FS                    
                                        
t = np.linspace(-tlim(N), tlim(N-1), N)
f = np.linspace(-flim(R), flim(R-1), R) 
c = np.linspace(-1, 1, 200*R)
#########################################

#__Cajon__###############################
#Ancho del Cajon
ancho = 5

u = lambda x: np.piecewise(x,x>=0,[1,0])
u0 = u(t+int(ancho/2))                  
u1 = u((int(ancho-1)/2)-t)              
                                        
Cajon = u0*u1/ancho                     
#########################################

#__Seno__################################
f0 = 5/31                               
a0 = 1                                  
                                        
Seno = a0 * np.sin(2*np.pi*f0*t)        
#########################################

#__Coseno1__#############################
f1 = F1                               
a1 = 1                                  
                                        
Coseno1 = a1 * np.cos(2*np.pi*f1*t)      
#########################################

#__Coseno2__#############################
f2 = F2                               
a2 = 1                                  
                                        
Coseno2 = a2 * np.cos(2*np.pi*f2*t)      
#########################################

#__Unos__################################
Unos = [1]*N                            
#########################################

#__fft__#################################
def F(fun_t):                           
    fftR = abs(np.fft.fft(fun_t,n=M))/N   
    return np.concatenate((fftR,fftR))  
#########################################

#__Tren_de_deltas__######################
d = lambda z: np.piecewise(z,
                        abs(z%1)<=0.001,
                        [1,0])          
                                        
Del = (N-1)*d(c)                        
DelCos = d(c+f1)+d(c-f1)                
#########################################

#__SINC__################################
SINC = lambda w: np.sin(np.pi*N*w)/np.sin(np.pi*w)  
#########################################

#__TFCajon__#############################
FC = SINC(c)
#########################################

#__TFCos*Cajon__#########################
COSSINCS = 0
for i in range(2):
    COSSINCS += SINC(c-((5/31)+i*(21/31))) 
COSSINCS /= 2
#########################################

#__Ploteo__##############################
#Funcion a plotear
Fun = (Coseno1 + Coseno2)
#plt.plot(t, Fun, 'b-')
fig, ax = plt.subplots(2)               
ax[0].plot(t, Fun, 'bo')                
ax[1].plot(f, F(Fun), 'r-')          
#ax[1].plot(c, Del, 'b-')                
#ax[1].plot(c, abs(FC), 'g-')       
ax[0].set_xlabel(
    'Muestras (en el tiempo) [S]')          
ax[0].set_ylabel('Amplitud')            
ax[1].set_xlabel('Frecuencia')          
ax[1].set_ylabel('Amplitud')            
axLabels = np.linspace(-FS, FS, 81) 
#axLabels = np.linspace(-1, 1, 32+1)    
#axLabels = np.linspace(-1, 1, 2*M+1)    
ax[1].xaxis.set_ticks(axLabels)         
ax[0].grid()                            
ax[1].grid()
plt.ylabel('Amplitud')
plt.xlabel('Frecuencia [Hz]')
plt.grid()
plt.grid()
plt.xticks(rotation=90)                 
#plt.xlim(-1,1)
plt.tight_layout()                      
plt.subplots_adjust(
        left=0.053,
        bottom=0.085)
plt.show()                              
#########################################

