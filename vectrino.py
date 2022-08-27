import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import netCDF4
import pickle

## DATA PROCESSING

def readFile(filePath):
  '''
  Reads a netCDF Vectrino file and returns its contents as two pandas
  dataframes
  '''
  f = netCDF4.Dataset(filePath,memory=)
  
  # Organize profiles in a single pandas dataframe
  data = f['Data']['Profiles']
  shapeTime = data['time'].shape
  prof = pd.DataFrame({k:np.array(data[k]) \
                     for k in list(data.variables.keys()) \
                     if data[k].shape == shapeTime})
  
  # Organize bottom check in a separate pandas dataframe
  data = f['Data']['BottomCheck']
  shapeTime = data['time'].shape
  bott = pd.DataFrame({k:np.array(data[k]) \
                     for k in list(data.variables.keys()) \
                     if data[k].shape == shapeTime})
  
  f.close()
  
  return prof,bott

def processVelProfile(profiles):
  '''
  Organizes netCDF4 velocity file into pandas dataframe
  '''
  keys = {"OG" : ['VelocityX','VelocityY','VelocityZ2'],\
          "vel" : ['u','v','w']}
  
  ## Extract only velocity information
  vels = profiles[['time']+keys['OG']].copy()
  #vels['time'] -=  vels['time'][0]
  t = vels['time']
  vels.set_index('time', inplace = True)  
  vels.rename(columns = {k:v for k,v in zip(keys['OG'],keys['vel'])}, inplace = True)

  return vels,keys

def calculatePrimes(vels):
  '''
  Calculates velocity perturbations
  '''
  keys = {"OG" : ['VelocityX','VelocityY','VelocityZ1'],\
          "vel" : ['u','v','w']}
    
  ## Store mean velocities
  avgt = {k.upper():vels[k].mean() for k in keys['vel']}
  
  ## Calculate perturbations (u'_j)
  keys["vprime"] = [f"{k}'" for k in keys["vel"]]
  for k,p in zip(keys["vel"],keys["vprime"]):
    vels[p] = vels[k] - avgt[k.upper()]
    
  ## Calculate Reynolds tensor (u'_i u'_j)
  keys["ortho"] = [f"{k}'{k}'" for k in keys["vel"]]
  for k,p in zip(keys["vprime"],keys["ortho"]):
      vels[p] = vels[k] * vels[k]
  
  keys["vprimeaux"] = keys["vprime"][-1:] + keys["vprime"][:-1]
  keys["shear"] = [f"{u}{v}" for u,v in zip(keys["vprime"],keys["vprimeaux"])]
  for k,p1,p2 in zip(keys["shear"],keys["vprime"],keys["vprimeaux"]):
    vels[k] = vels[p1] * vels[p2]
  
  del keys["vprimeaux"]
  
  return vels,keys

def processBottom(bottoms,probeDist=0.05):
  '''
  Organizes netCDF4 bottom file into pandas dataframe
  '''
  ## Extract only distance information
  bots = bottoms[['time','BottomDistance']].copy()
  bots.set_index('time', inplace = True)  
  bots.rename(columns = {'BottomDistance':'depth'}, inplace = True)
  bots['depth'] = bots['depth'] - probeDist
  return bots

def maskSeries(vels,zscore=3.0):
  '''
  mask values with a z-score greater that stdevs
  '''
  for k in vels.keys():
    mask = np.abs(vels[[k]]-vels[[k]].mean()) > (zscore*vels[[k]].std())
    vels[[k]] = vels[[k]].mask(mask)
  return vels

def pickleVelsAndBots(file,mask=True):
  '''
  Runs all the processing and pickling in one step
  '''
  prof,bott = readFile(file)
  bots = processBottom(bott,probeDist=0.05)
  vels,keys = processVelProfile(prof)
  if mask: vels = maskSeries(vels)
  vels,keys = calculatePrimes(vels)
  
  vels.to_pickle(file.replace(".nc",".pklv"))
  bots.to_pickle(file.replace(".nc",".pklb"))
  return None

#### PLOTS

def plotVelocityOverTime(vels,keys):
  THREE_COLORS = ['#1b9e77','#d95f02','#7570b3']
  avgt = {k.upper():vels[k].mean() for k in keys['vel']}

  fig,axs = plt.subplots(3,2,sharex='col',sharey=True,facecolor='w',\
                         figsize=[8,8],gridspec_kw={'hspace':0,'wspace':0.05,'width_ratios':[2,1]})

  for i,k in enumerate(keys["vel"]):
    K = k.upper()
    axs[i,0].plot(vels.index,vels[k],lw=0.2,c=THREE_COLORS[i],alpha=0.85,label=f"${k}(t)$")
    axs[i,0].axhline(y=avgt[K],lw=0.8,c='k',\
                   label="${:}$ = {:.3f}".format(K,avgt[K]))
    axs[i,0].legend(loc='best',ncol=2)
    axs[i,0].yaxis.set_major_locator(MaxNLocator(5)) 

    axs[i,1].hist(vels[k],bins='sqrt',histtype='step',\
          density=True,lw=2,color=THREE_COLORS[i],orientation='horizontal')
    axs[i,1].set(xscale='log')
  
  axs[-1,0].set(xlabel='Time [s]')
  axs[-1,1].set(xlabel='Freq. [-]')
  
  fig.supylabel('Velocity [m/s]',x=0.05,fontweight ="medium",ha="center",fontsize=12)
  plt.show()
  return None

def plotBottomsOverTime(bots):
  meanDepth = bots['depth'].mean()
  fig,axs = plt.subplots(1,1,facecolor='w',\
                         figsize=[6,4],gridspec_kw={'hspace':0})
  axs.plot(bots.index,bots['depth'],lw=1,c='brown',alpha=0.8,marker='.',ms=10)
  axs.axhline(y=meanDepth,lw=0.8,c='k',label="Mean: {:.2f} m".format(meanDepth))
  axs.legend()
  axs.set(ylim=[0,0.20],ylabel='Bottom Distance [m]',xlabel='Time [s]')
  plt.show()
  return None

def plotVPrimeOverTime(vels,keys):
  THREE_COLORS = ['#66c2a5','#fc8d62','#8da0cb']
  fig,axs = plt.subplots(3,2,sharex='col',sharey=True,facecolor='w',\
                         figsize=[8,8],gridspec_kw={'hspace':0,'wspace':0.05,'width_ratios':[2,1]})

  for i,k in enumerate(keys["vprime"]):
    axs[i,0].plot(vels.index,vels[k],lw=0.2,c=THREE_COLORS[i],alpha=0.9,label=f"${k}(t)$")
    axs[i,0].axhline(y=0.0,lw=0.8,c='k')
    axs[i,0].legend(loc='lower right')
    axs[i,0].yaxis.set_major_locator(MaxNLocator(5)) 

    axs[i,1].hist(vels[k],bins='sqrt',histtype='step',\
          density=True,lw=2,color=THREE_COLORS[i],orientation='horizontal')
    axs[i,1].set(xscale='log')

  axs[-1,0].set(xlabel='Time [s]')
  axs[-1,1].set(xlabel='Freq. [-]')
  
  fig.supylabel('Velocity perturbations [m/s]',x=0.05,fontweight ="medium",ha="center",fontsize=12)
  plt.show()
  return None
  
def plotReynoldsOverTime(vels,keys):
  SIX_COLORS = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c']
  fig,axs = plt.subplots(3,2,sharex=True,sharey=True,facecolor='w',\
                       figsize=[8,8],gridspec_kw={'hspace':0,'wspace':0})

  for i,k in enumerate(keys["ortho"]):
    axs[i,0].plot(vels.index,vels[k],lw=0.2,c=SIX_COLORS[i],alpha=1,label=f"${k}$")
    axs[i,0].axhline(y=vels[k].mean(),lw=0.8,c='k',ls='dashed',\
                     label=fr"$\widebar{{{k}}}=$" + "{:.1E} m²/s²".format(vels[k].mean()))
    axs[i,0].legend()
    axs[i,0].yaxis.set_major_locator(MaxNLocator(4))

  for i,k in enumerate(keys["shear"]):
    axs[i,1].plot(vels.index,vels[k],lw=0.2,c=SIX_COLORS[i+3],alpha=1,label=f"${k}$")
    axs[i,1].axhline(y=vels[k].mean(),lw=0.8,c='k',ls='dashed',\
                     label=fr"$\widebar{{{k}}}=$" + "{:.1E} m²/s²".format(vels[k].mean()))
    axs[i,1].legend()
     
  fig.supylabel("Reynolds' stresses [m$^2$/s$^2$]",x=0.05,fontweight ="medium",ha="center",fontsize=12)
  fig.supxlabel("Time [s]",y=0.05,fontweight ="medium",va="top",fontsize=12)

  plt.show()
  return None


## CONCEPTS

def logLaw(depth,width,slope,g=9.81,nu=1.0E-6):
  kappa = 0.41
  Bfact = 5.00
  
  y = np.geomspace(depth*1.0E-5,depth,200)
  area  = width * depth
  perim = width + (2*depth)
  radHy = area / perim
  
  ustar = np.sqrt(g*slope*radHy)
  
  
  u  = (ustar/kappa * np.log(y*ustar/nu)) + (Bfact*ustar)
  
  return (y,u)

def main():
  return 0

if __name__ == 'main':
  main()