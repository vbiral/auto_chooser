import pandas as pd
import numpy as np
import re
import dateparser
import datetime

def verifica_cpf(cpf):
    #Valido o CPF
    d1=0
    d2=0
    i=0
    while i<10:
        d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
    if(int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0)):
        return 1
    return 0

def verifica_cnpj(cnpj):
    
    DIVISOR = 11

    CPF_WEIGHTS = ((10, 9, 8, 7, 6, 5, 4, 3, 2),
                  (11, 10, 9, 8, 7, 6, 5, 4, 3, 2))
    CNPJ_WEIGHTS = ((5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
                   (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2))

    first_part = cnpj[:12]
    second_part = cnpj[:13]
    first_digit = cnpj[12]
    second_digit = cnpj[13]

    #Calculo primeira parte do CNPJ
    sum = 0
    if len(first_part) == 9:
        weights = CPF_WEIGHTS[0]
    else:
        weights = CNPJ_WEIGHTS[0]

    for i in range(len(first_part)):
        sum = sum + int(first_part[i]) * weights[i]
    rest_division = sum % DIVISOR
    
    if rest_division < 2:
        primeiro_digito = '0'
    else:
        primeiro_digito = str(11 - rest_division)
    
    #Calculo segunda parte do CNPJ
    sum = 0
    if len(second_part) == 10:
        weights = CPF_WEIGHTS[1]
    else:
        weights = CNPJ_WEIGHTS[1]

    for i in range(len(second_part)):
        sum = sum + int(second_part[i]) * weights[i]
    rest_division = sum % DIVISOR
    
    if rest_division < 2:
        segundo_digito = '0'
    else:
        segundo_digito = str(11 - rest_division)

    if (first_digit == primeiro_digito and
        second_digit == segundo_digito):
        return 1
    return 0

def verifica_cpf_cnpj(cpf_cnpj):
    if(not isinstance(cpf_cnpj,str)):
        return -1
    
    cpf_cnpj = re.sub('[^0-9]', '', cpf_cnpj)
    
    if(cpf_cnpj==''):
        return -1
    
    #Elimino zeros a esquerda
    cpf_cnpj = int(cpf_cnpj)
    
    #Converto novamente para string
    cpf_cnpj = str(cpf_cnpj)
    
    if(len(cpf_cnpj)>14):
        return -1
    
    elif(len(cpf_cnpj) > 11):
        cpf_cnpj = cpf_cnpj.rjust(14,'0')
    
    elif(len(cpf_cnpj) < 11):
        cpf_cnpj = cpf_cnpj.rjust(11,'0')
        
    if(len(cpf_cnpj)==11):
        return verifica_cpf(cpf_cnpj)
    else:
        return verifica_cnpj(cpf_cnpj)

def verifica_email(email):
    if(not isinstance(email,str)):
        return -1
    
    pattern = '[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net|br|org|tv|uk)'
    if(re.search(pattern,email)):
        return 1
    return 0

def verifica_telefone_br(tel):
    if(not isinstance(tel,str)):
        return -1
    
    tel = re.sub('[^0-9]', '', tel)
    
    if(tel==''):
        return -1
    
    #Elimino zeros a esquerda
    tel = int(tel)
    
    #Converto novamente para string
    tel = str(tel)
    
    #Pego os dados do telefone
    if(len(tel) in [13,12]):
        ddi = tel[0:2]
        ddd = tel[2:4]
        nro = tel[4:]
    elif(len(tel) in [11,10]):
        ddi = '55'
        ddd = tel[0:2]
        nro = tel[2:]
    else:
        return 0
    
    if(ddi != '55'):
        return 0
    
    #Fixo
    if((len(nro)==8) and #Tamanho
       (nro[0] in ['2','3','4','5']) and #Primeiro Digito
       (int(ddd)>=10 and int(ddd)<=99) #DDD entre 10 e 99
      ):
        return 1
    
    #Celular
    elif((len(nro)==9) and #Tamanho
         (nro[0]=='9') and #Primeiro Digito
         (int(ddd)>=10 and int(ddd)<=99) #DDD entre 10 e 99
        ):
        return 1
    
    else:
        return 0
    
def verifica_cep_br(cep):
    if(not isinstance(cep,str)):
        return -1
    
    cep = re.sub('[^0-9]', '', cep)
    
    if(cep==''):
        return -1
    
    #Elimino zeros a esquerda
    cep = int(cep)
    
    #Converto novamente para string
    cep = str(cep)
    
    #Uma data pode ser compreendida como CEP, assim se o verifica_data der bom quer dizer
    #que era uma data em vez de CEP
    #TODO -> Refazer a regra de uma forma mais estruturada
    if(verifica_data(cep)==1):
        return 0
    
    if(len(cep) <= 8):
        cep = cep.rjust(8,'0')
    
    if(len(cep)>8):
        return 0
    #Não sei regras para verificar CEP
    return 1

def verifica_data(data):
    if(isinstance(data,datetime.datetime)):
        return 1
    
    if(not isinstance(data,str)):
        return -1
    
    data_corrigida = dateparser.parse(data)
    #O Dateparser consegue parsear até inteiros, então tem a chance de dar merda
    #TODO -> Refazer a regra de uma forma mais estruturada
        
    if(isinstance(data_corrigida, datetime.datetime)):
        if(data_corrigida.year > datetime.datetime.now().year):
            return 0
        elif(data_corrigida.year < 2010):
            return 0
        else:
            return 1
    else:
        return 0