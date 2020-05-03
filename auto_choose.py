from rules import *
import pandas as pd

class auto_choose:
    
    def __init__(self, df):
        
        self.df = df
        self.sample = 1.0
        
        self.types = pd.read_json('types.json')
        self.df_sample = self.df.sample(frac=self.sample)
        
        self.possibilidades={}
        
    def auto_choose(self):
        for ind1, row1 in self.types.iterrows():
            aux=[]
            aux2=[]

            #Se o tipo tiver apenas uma regra, beleza...
            try:
                rule = pd.DataFrame(row1['Types'],index=[0])

            #Senão faz a leitura para 2+ regras
            except:
                rule = pd.DataFrame(row1['Types'])

            #Para cada regra do tipo
            for ind2, row2 in rule.iterrows():
                results = self.df_sample.applymap(eval(row2['rules']))

                #Verifico a efetividade da regra para cada coluna individualmente
                for coluna in self.df_sample.columns:
                    prop_acerto = (results[results[coluna]==row2['result_rules']].shape[0])/results.shape[0]
                    if(prop_acerto >= row2['min_rules']):
                        aux.append(coluna)

            #Se todas as regras foram aceitas
            qtd_regras = rule.shape[0]
            for coluna in self.df_sample.columns:
                aux2 = [l for l in aux if l == coluna]

                if(len(aux2) == qtd_regras):
                    dic={coluna:row2['name']}
                    self.possibilidades.update(dic)
                    
    def auto_wrangler(self) -> pd.DataFrame:
        pass
    