#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Projeto de Laboratório

import os
from os import mkdir
import zipfile
import gzip
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


#import random
#from random import gauss
#from os import makedirs
#import numpy as np
#import math

def Busca(dataframe,coluna,gene):
    novo_gene=None
    tamanho=len(dataframe)
    for i in range(tamanho):
        encontra=dataframe[coluna][i].find(gene)
        if(encontra!=-1):
            novo_gene=dataframe[coluna][i]
    return novo_gene

class Projeto_Laboratorio:
    def __init__(self,diretorio,subtipos,amostras):
        self.diretorio=diretorio
        self.subtipos=subtipos
        self.amostra=amostras
        self.amostras=None
        self.paciente=""
        self.lista=[]
        self.lista_paciente=[]
        self.dicionario=0
        self.lista_subtipo=[]
        self.gene=""
        #self.lista_grafico=[]
        
        

    def Extrai_zip(self):
        for subdir,dirs,files in os.walk(self.diretorio):
            for file in files:
                if(file[-3:]=="zip"):
                    arq=zipfile.ZipFile(self.diretorio+"/"+self.arquivo)
                    arq.extractall(self.diretorio)
                    arq.close()

    def Extrair_gz(self):

        for subdir,dirs,files in os.walk(self.diretorio):
            #print(dirs)
            #print(subdir)
            tam=len(files)
            #diretorio=dirs
            for file in files:
                #print(file)
                if(tam>1)and(file[-8:]=="FPKM.txt"):
                    self.lista.append(subdir+"/"+file)
                    self.lista_paciente.append(file)
                if(tam==1)and(file[-2:]=="gz"):
                    arq=gzip.open(subdir+"/"+file,"rb")
                    ler=arq.read()
                    arq.close()
                    arq2=open(subdir+"/"+file[:-3],"wb")
                    arq2.write(ler)
                    #shutil.copyfileobj(arq,arq2)
                    arq2.close()
                    self.lista.append(subdir+"/"+file)
                    self.lista_paciente.append(file)
        self.dicionario=dict(zip(self.lista_paciente,self.lista))
        #print(self.lista_paciente)
        return self.dicionario
                    
    def Dados(self):
        self.paciente=input("Digite o código do paciente:")
        self.paciente=self.paciente+".txt"
        dados=pd.read_csv(self.dicionario[self.paciente],sep="\t",header=None)
        dados.columns=["Codigo do gene","Expressao do gene"]
        dataf=pd.DataFrame(dados)
        dataf.describe()
        opcao=input("""Digite o código do gene desejado para se visualizar sua expressão, ou "sair" para encerrar a busca:""")
        
        while(opcao!="sair"):
            
            busca=Busca(dataf,"Codigo do gene",opcao)
            
            expressao_gene=dataf.loc[dataf["Codigo do gene"]==busca]
            print(expressao_gene)
                
            opcao=input("""Digite o código do gene desejado para se visualizar sua expressão, ou "sair" para encerrar a busca:""")

        
    
    def Graficos(self,gene=None,nome=None):
        self.lista_subtipo=[]
        if(gene!=None):
            self.gene=gene
        else:
            self.gene=input("Digite o código da molécula que será analisada:")
        
        for subdir,dirs,files in os.walk(self.subtipos):
            for file in files:
                if(file[-4:]=="xlsx"):
                    self.lista_subtipo.append(file)
        #print(self.lista_subtipo)
        amostra=pd.read_table(self.amostra)
        self.amostras=pd.DataFrame(amostra)
        #print(amostras)
        tamanho=len(self.amostras)
        for i in self.lista_subtipo:
            subtipo=pd.read_excel(self.subtipos+"/"+i)
            subtipos=pd.DataFrame(subtipo)
            #print(subtipos)
            dataframe=pd.DataFrame()#columns=[gene]
            dataframes=pd.DataFrame()
            nv_diretorio="C:/Users/Fabio/Pictures/Imagens_Projeto_Laboratorio/Teste/"
            sinal1=False
            sinal2=False
            if(nome!=None):
                sinal2=os.path.isdir(nv_diretorio+nome)
                nv_diretorio=nv_diretorio+nome
            else:
                sinal1=os.path.isdir(nv_diretorio+self.gene)
                nv_diretorio=nv_diretorio+self.gene
                
            if(nome==None)and(sinal1==False):
                os.mkdir(nv_diretorio)
            elif(nome!=None)and(sinal2==False):
                os.mkdir(nv_diretorio)
            
            for j in range(tamanho):
                tipo=subtipos.loc[subtipos["Sample ID"]==self.amostras["Sample ID"][j]]
                
                tamanho_tipo=len(tipo)
                if(tamanho_tipo==1)and((self.amostras["File Name"][j][:-3] in self.dicionario)==True):
                    #print(tipo)
                    
                    dado=pd.read_csv(self.dicionario[self.amostras["File Name"][j][:-3]],sep="\t",header=None)
                    dado.columns=["Codigo do gene","Expressao do gene"]
                    df=pd.DataFrame(dado)
                    
                    busca=Busca(df,"Codigo do gene",self.gene)
                    expressao=df.loc[dado["Codigo do gene"]==busca]
                    
                    nome_grupo=i[:-5]#+" - "+busca
                    nome_novo=nome_grupo.replace("_"," ")
                    dtf=pd.DataFrame(expressao["Expressao do gene"])
                    dtf.columns=["Expressao do gene"]
                    dataframe=dataframe.append(dtf)
                    
                    dtfs=pd.DataFrame(data=[self.amostras["Sample ID"][j]],columns=["Codigo do paciente"])
                    dataframes=dataframes.append(dtfs)
            
            local=nv_diretorio+"/"+nome_grupo
            sinal3=os.path.isdir(local)
            if(sinal3==False):
                os.mkdir(local)
            
            x=dataframes.to_dict("list")
            #print(x)
            y=dataframe.to_dict("list")
            #print(y)
            x.update(y)
            #print(x)
            
            novo_df=pd.DataFrame(x)
            
            print(" ")
            print(nome_novo)
            print(" ")

            descricao=dataframe.describe()
            print(descricao)
            
            media=descricao["Expressao do gene"]["mean"]
            sigma=descricao["Expressao do gene"]["std"]
            
            plt.style.use("ggplot")
            plt.figure(figsize=(15,10))
            plt.hist(y["Expressao do gene"],bins=30,ec="k",alpha=.6,color="royalblue")
            if(nome==None):
                plt.title(nome_novo+" - Histograma - "+self.gene)
            else:
                plt.title(nome_novo+" - Histograma - "+nome)
            plt.xlabel("""Expressão do gene 
            
            µ= %f
            σ= %f"""%(media,sigma))
            plt.ylabel("Número de amostras")
            plt.ylim(0,90)
            plt.savefig(local+"/"+nome_grupo+" - Histograma.png",format="png")
            plt.show()
            plt.close()
            
            gaussiana=[]
            for e in y["Expressao do gene"]:
                z=(e-media)/sigma
                gaussiana.append(z)
            
            plt.style.use("ggplot")
            plt.figure(figsize=(15,10))
            plt.hist(gaussiana,bins=30,ec="k",alpha=.6,color="blue")
            if(nome==None):
                plt.title(nome_novo+" - "+self.gene)
            else:
                plt.title(nome_novo+" - "+nome)
            plt.xlabel("""Expressão normalizada do gene
            
            µ= %f
            σ= %f"""%(media,sigma))
            plt.ylabel("Número de amostras")
            plt.ylim(0,90)
            plt.savefig(local+"/"+nome_grupo+" - Histograma (Gaussiana padronizada).png",format="png")
            plt.show()
            plt.close()
            
            fig=px.scatter(novo_df,x="Codigo do paciente",y="Expressao do gene",log_x=False,width=1000)
            fig.update_traces(marker=dict(size=8,line=dict(width=1)),selector=dict(mode="markers"))
            if(nome==None):
                fig.update_layout(title=nome_novo+" - Dispersao - "+self.gene)
            else:
                fig.update_layout(title=nome_novo+" - Dispersao - "+nome)
            fig.update_xaxes(title="Código da amostra")
            fig.update_yaxes(title="Expressão do gene")
            fig.show()
            
            if not os.path.exists("C:/Users/Fabio/Pictures"):
                os.mkdir("C:/Users/Fabio/Pictures")
            fig.write_image(local+"/"+nome_grupo+" - Dispersao.png")
            fig.write_html(local+"/"+nome_grupo+" - Dispersao.html")
            
            """x=dataframes["Sample ID"]
            y=dataframes[nome_coluna]
            plt.scatter(x,y)
            plt.show()"""
            
            """gaussiana=[gauss(media,sigma) for i in y["Expressao do gene"]]
            #plt.figure(figsize=(10,20))
            plt.hist(gaussiana,bins=20)
            plt.title(nome_grupo+" - Histograma (Gaussiana) - NFKB3")
            plt.xlabel("Media")
            plt.ylabel("Probabilidade")
            plt.savefig("C:/Users/Fabio/Pictures/Imagens_Projeto_Laboratorio/"+nome_grupo+" - Histograma (Gaussiana).png",format="png")
            plt.show()"""


# In[6]:


#Programa principal

diretorio="C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/Data/1.mRNA/gdc_download"
subtipos="C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/Subtipos_de_Tumor"
amostras="C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/gdc_sample_sheet.2019-07-24.tsv"

projeto=Projeto_Laboratorio(diretorio,subtipos,amostras)
projeto.Extrai_zip()
projeto.Extrair_gz()

opcao=input("""
Digite umas das opções abaixo:

1 - Se deseja produzir os gráficos de um único gene;
2 - Se deseja produzir gráficos de um conjunto de genes;
3 - Se só deseja visualizar os genes ou um gene de um paciente especifico.

Opcão:
""")

if(opcao=="3"):
    projeto.Dados()
elif(opcao=="1"):
    projeto.Graficos()
elif(opcao=="2"):
    interesse=pd.read_excel("C:/Users/Fabio/Documents/Estudo_Projeto_de_Laboratório/Projeto/Novo/Nova/Lista_de_genes_de_interesse_incompleto.xlsx")
    interes=pd.DataFrame(interesse)
    tam=len(interes)
    for i in range(tam):
        nome=interes["Gene Synonyms"][i].split(",")
        projeto.Graficos(interes["Ensembl"][i],nome[0])


# In[ ]:





# In[ ]:




