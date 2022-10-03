import numpy as np
import pandas as pd
import netCDF4

## DATA PROCESSING

def readFile(filePath):
  '''
  Reads a netCDF Vectrino file and returns its contents as two pandas
  dataframes
  '''
  f = netCDF4.Dataset(filePath)
  
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
