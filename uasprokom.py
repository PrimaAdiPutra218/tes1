#Import semua modul yang diperlukan 
import json
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import streamlit as st
#-------------------------------------------

#Open file 
f = open("kode_negara_lengkap.json") 
file_json = json.load(f)
df_csv = pd.read_csv("produksi_minyak_mentah.csv")
df_json = pd.DataFrame.from_dict(file_json, orient = 'columns')
#--------------------------------------------------------------

#====================  SOAL NOMOR 1 ====================== 
#Menghilangkan data yang tidak termasuk negara (Organisasi)
list1 = []
for i in list (df_csv['kode_negara']):
    if i not in list(df_json['alpha-3']):
        list1.append(i)

for i in list1: 
    df_csv = df_csv[df_csv.kode_negara !=i]
#----------------------------------------------------------

"""nama_negara = []
for i in range (len(df_csv)):
    for j in range (len(df_json)):
        if list (df_csv['kode_negara'])[i] == list(df_json['alpha-3'])[j]:
            nama_negara.append(list(df_json['name'])[j])"""

#input nama negara dari user 
N = st.text_input("Masukkan nama negara: ")
#----------------------------------

#membuat grafik produksi negara terhadap waktu 
df1 = df_csv.loc[df_csv['kode_negara']==N]

graph1 = plt.subplot()
df1.plot(x='tahun', y='produksi')
graph1 = plt.show()
st.pyplot(graph1)
#---------------------------------------------








#2
T = int(input("Masukkan tahun: "))
B1 = int(input("Masukkan banyak negara: "))

df2 = df_csv.loc[df_csv['tahun'] == T]
df2 = df2.sort_values(by=['produksi'], ascending = False)
df2 = df2[:B1]

df2.plot.bar(x = 'kode_negara', y = 'produksi')
plt.show()



#3
list2 = []
kumulatif = []

B2 = int(input("Masukkan banyak negara: "))
for i in list(df_csv['kode_negara']):
    if i not in list2: 
        list2.append(i)

for i in list2:
    a = df_csv.loc[df_csv['kode_negara'] == i, 'produksi'].sum()
    kumulatif.append(a)

dfkumulatif = pd.DataFrame(list(zip(list2, kumulatif)), columns = ['kode_negara', 'kumulatif'])
dfkumulatif = dfkumulatif.sort_values(by = ['kumulatif'], ascending = False)
dfkumulatif = dfkumulatif [:B2]

dfkumulatif.plot.bar ( x = 'kode_negara', y = 'kumulatif')
plt.show()


#4
#bagian 1 
jumlah_produksi = df2[:1].iloc[0]['produksi']
kode_negara = df2[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range (len(df_json)):
    if list(df_json['alpha-3'])[i] == kode_negara:
        nama_negara = list(df_json['name'])[i]
        region_negara = list(df_json['region'])[i]
        subregion_negara = list(df_json['sub-region'])[i]

print ("Negara dengan jumlah produksi minyak terbesar pada tahun {}".format(T))
print ("{} \n{} \n{} \n{} \n{}".format(jumlah_produksi, kode_negara, nama_negara,  region_negara, subregion_negara))

#Bagian 2
dfterkecil = df2[df2.produksi != 0]
dfterkecil = dfterkecil.sort_values(by = ['produksi'], ascending = True )

jumlah_produksi = dfterkecil[:1].iloc[0]['produksi']
kode_negara = dfterkecil[:1].iloc[0]['kode_negara']
nama_negara = ""
region_negara = ""
subregion_negara = ""

for i in range(len(df_json)):
    if list(df_json['alpha-3'])[i] == kode_negara:
        nama_negara = list(df_json['name'])[i]
        region_negara = list(df_json['region'])[i]
        subregion_negara = list(df_json['sub-region'])[i]

print("Negara dengan jumlah produksi minyak terkecil pada tahun {}".format(T))
print ("{} \n{} \n{} \n{} \n{}".format(jumlah_produksi, kode_negara, nama_negara,  region_negara, subregion_negara))

#Bagian 3
dfproduksinol = df2[df2.produksi == 0]
listnegaranol = []
listregionnol = []
listsubregionnol = []

for i in range (len(dfproduksinol)):
    for j in range (len(df_json)):
        if list (dfproduksinol['kode_negara'])[i] == list(df_json['alpha-3'])[j]:
            listnegaranol.apppend(list(df_json['name'])[j])
            listregionnol.append(list(df_json['region'])[j])
            listsubregionnol.append(list(df_json['sub-region'])[j])

dfproduksinol['negara'] = listnegaranol
dfproduksinol['region'] = listregionnol
dfproduksinol['sub-region'] = listsubregionnol

dfkumulatifnol = dfkumulatif[dfkumulatif.kumulatif == 0]
listnegarakumulatifnol = []
listregionkumulatifnol = []
listsubregionkumulatifnol = []

for i in range(len(dfkumulatifnol)):
    for j in range(len(df_json)):
        if list (dfkumulatifnol['kode_negara'])[i] == list(df_json['alpha-3'])[j]:
            listnegarakumulatifnol.append(list(df_json['name'])[j])
            listregionkumulatifnol.append(list(df_json['region'])[j])
            listsubregionkumulatifnol.append(list(df_json['sub-region'])[j])

dfkumulatifnol['negara'] = listnegarakumulatifnol
dfkumulatifnol['region'] = listregionkumulatifnol
dfkumulatifnol['sub-region'] = listsubregionkumulatifnol

print(dfproduksinol)
print(dfkumulatifnol)


