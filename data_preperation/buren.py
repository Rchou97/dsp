# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
df_kadaster = pd.read_csv('amsterdam.csv') 
# Preview the first 5 lines of the loaded data 
df_kadaster.columns =['id','perceelid', 'perceeltype', 'huisnr', 'huisnr_bag_letter','huisnr_bag_toevoeging','bag_nummeraanduidingid','bag_adresseerbaarobjectid','lat','lon','rdx','rdy','oppervlakte','gebruiksdoel','reeksid']
df_kadaster.head()

straal = 20

df = df_kadaster.copy()
df

for j in df.iterrows():
    print(j)
    i = 0

    rdx_punt = j[10]
    rdy_punt = j[11]

    rdx_min = rdx_punt - straal
    rdx_max = rdx_punt + straal
    rdy_min = rdy_punt - straal 
    rdy_max = rdy_punt + straal

    rslt_df = df[(df['rdx'] > rdx_min) & 
               (df['rdx'] < rdx_max) &
              (df['rdy'] > rdy_min) &
              (df['rdy'] < rdy_max)]
    ##jel = ((df['rdx'] > rdx_min) & 
     ##           (df['rdx'] < rdx_max) & 
      ##          (df['rdy'] > rdy_min) &
       ##         (df['rdy'] < rdy_max)).sum()

    #print("Lat/lon: " + str(rdx_punt) + " / " + str(rdy_punt) + " == " + str(jel))
    jel = len(rslt_df.index)
    df.at['Buren', i] = jel
    i = i+1

df
df.to_csv('buren.csv')