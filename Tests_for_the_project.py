#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

dados=pd.read_csv("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/N/00ae19b2-33b1-443e-88c6-aad3826a2c9b/257b1c80-203b-4cf0-9841-5a1242299270.FPKM.txt",sep="\t",header=None)
dados.columns=["Código do gene","Expressão do gene"]


# In[3]:


dados.head()


# In[4]:


import pandas as pd
dados=pd.read_csv("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/N/00ae19b2-33b1-443e-88c6-aad3826a2c9b/257b1c80-203b-4cf0-9841-5a1242299270.FPKM.txt",sep="\t",header=None)
dados.columns=["Código do gene","Expressão do gene"]
dataf=pd.DataFrame(dados)


# In[5]:


print(dataf)


# In[6]:


dataf.shape


# In[7]:


dataf.describe()


# In[8]:


p=dataf.describe()
print(p)


# In[9]:


dataf["Expressão do gene"]


# In[16]:


f=dataf.loc[dataf["Código do gene"]=="ENSG00000173039.17"]
print(f)
"""import pandas as pd

def Busca(dataframe,coluna,gene):
    novo_gene=None
    tamanho=len(dataframe)
    for i in range(tamanho):
        encontra=dataframe[coluna][i].find(gene)
        if(encontra!=-1):
            novo_gene=dataframe[coluna][i]
    return novo_gene

dados=pd.read_csv("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/N/00ae19b2-33b1-443e-88c6-aad3826a2c9b/257b1c80-203b-4cf0-9841-5a1242299270.FPKM.txt",sep="\t",header=None)
dados.columns=["Código do gene","Expressão do gene"]
dataf=pd.DataFrame(dados)

fabio=Busca(dataf, "Código do gene", "ENSG00000173039")
print(fabio)"""


# In[17]:


fabio=dataf.loc[0:100]


# In[18]:


print(fabio)


# In[19]:


novo=fabio.loc[fabio["Expressão do gene"]>=1]


# In[20]:


print(novo)


# In[21]:


dataf["Código do gene"].value_counts()


# In[22]:


import matplotlib.pyplot as plt


# In[23]:


dataf.hist(column="Expressão do gene",bins=50)
plt.show()


# In[24]:


fabio.describe()


# In[25]:


oi=dataf.loc[dataf["Expressão do gene"]>1000]


# In[26]:


oi.hist(column="Expressão do gene", bins=30,alpha=.6)#, height=None)
plt.ylim(0,100)
plt.xlim()
plt.show()


# In[27]:


oi.shape


# In[28]:


dataf.shape


# In[29]:


gene=pd.read_table("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/gdc_sample_sheet.2019-07-24.tsv")


# In[30]:


gene.head()


# In[31]:


fabio=input("Digite um nome:")


# In[32]:


tam=len(dataf)


# In[33]:


print(tam)


# In[34]:


l=[]
l.append(dataf["Código do gene"][0])


# In[35]:


print(l)


# In[36]:


dicionario={"fabio":4,"ana":5}


# In[37]:


chave=dicionario.keys()
print(chave)


# In[38]:


print(dicionario)


# In[39]:


for i in chave:
    print(i)


# In[40]:


dad=dataf.loc[1:6]


# In[41]:


print(dad)


# In[42]:


dad.loc[-1]=["oi",2.333]
dad.index=dad.index+1
dad=dad.sort_index()


# In[43]:


print(dad)


# In[44]:


genes=pd.read_csv("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/transcripts-Summary-Homo_sapiens_Gene_Splice_ENSG00000173039.csv")
gene=pd.DataFrame(genes)


# In[45]:


gene.head()


# In[46]:


clinico=pd.read_table("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/clinical.tsv")
clinic=pd.DataFrame(clinico)


# In[47]:


clinic.head()


# In[48]:


clinic.describe()


# In[49]:


tabelas=pd.read_table("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/gdc_sample_sheet.2019-07-24.tsv")
tabela=pd.DataFrame(tabelas)


# In[50]:


tabela.head()


# In[51]:


tabela.describe()


# In[52]:


interesse=pd.read_excel("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/Lista_de_genes_de_interesse.xlsx")
interes=pd.DataFrame(interesse)


# In[53]:


interes.head()


# In[54]:


interes.describe()


# In[55]:


tam=len(interes)
tamh=len(dataf)
for i in range(tam):
    for j in range(tamh):
        if((interes["Ensembl"][i])==(dataf["Código do gene"][j][0:15])):
            variavel=dataf.loc[dataf["Código do gene"]==dataf["Código do gene"][j]]
            print(variavel)
            


# In[56]:


f=dataf["Código do gene"][0][0:15]
print(f)


# In[57]:


g=interes["Ensembl"][0]
print(g)


# In[58]:


tipo=tabela.loc[tabela["Sample ID"]=="TCGA-E9-A1RF-11A"]
print(tipo)


# In[59]:


procura=dataf["Código do gene"][0].find("Fabio")
print(procura)


# In[60]:


guardar=dataf.loc[dataf["Código do gene"]=="Fabio"]
t=len(guardar)
print(guardar)
print(t)


# In[61]:


guardar=dataf.loc[dataf["Código do gene"]=="ENSG00000173039.17"]
t=len(guardar)
print(guardar)
print(t)


# In[62]:


for i in range(10):
    for j in range (1164):
        print(j)


# In[63]:


dici={"Fabio":1}
datas=pd.DataFrame(dici)
print(datas)
datas.describe()


# In[ ]:


b=tabelas.loc[tabelas["File Name"]=="d8f60cfe-3faa-406f-8ed6-2bb201dc36f4.FPKM.txt.gz"]
print(b)


# In[ ]:


import matplotlib.pyplot as plt
help(plt.hist)


# In[ ]:


plt.hist(range(0, 10))

"""scale_factor = 5

xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()

plt.xlim(xmin * scale_factor, xmax * scale_factor)
plt.ylim(ymin * scale_factor, ymax * scale_factor)"""
plt.xlim(0,60)
plt.ylim(0,60)
plt.show()


# In[6]:


import matplotlib.pyplot as plt
a =(3)**(1/2)
b = [-1*a, a]
c = [0,0]
plt.plot(b, c, 'g-o')
plt.show()
plt.close()


# In[ ]:





# In[ ]:




