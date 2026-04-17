import pandas as pd
import numpy as np
import statsmodels.api as sm

class PrescriptiveEngine:
    def __init__(self, df_camp, df_crea):
        self.df_camp = df_camp.copy()
        self.df_crea = df_crea.copy()

    def apply_stop_start_continue(self):
        """
        Aplica lógica booleana baseada em quartis para prescrever ações de mídia e criação.
        """
        # --- Lógica para Campanhas ---
        top_roas = self.df_camp['ROAS'].quantile(0.75)
        low_roas = self.df_camp['ROAS'].quantile(0.25)
        avg_cpa = self.df_camp['CPA'].mean()

        def classify_camp(row):
            if row['ROAS'] >= top_roas and row['Investimento_BRL'] < self.df_camp['Investimento_BRL'].median():
                return 'START/SCALE (Under-invested Alpha)'
            elif row['ROAS'] <= low_roas and row['CPA'] > avg_cpa:
                return 'STOP/ABANDON (Inefficient)'
            elif row['ROAS'] > self.df_camp['ROAS'].median():
                return 'CONTINUE/OPTIMIZE'
            else:
                return 'MONITOR/PIVOT'

        self.df_camp['prescriptive_action'] = self.df_camp.apply(classify_camp, axis=1)

        # --- Lógica para Criativos ---
        high_hook = self.df_crea['Hook_Rate_Pct'].quantile(0.75)
        high_fatigue = 60 # Threshold padrão de mercado para fadiga

        def classify_crea(row):
            if row['Fatigue_Score'] > high_fatigue:
                return 'STOP/REPLACE (Ad Fatigue)'
            elif row['Hook_Rate_Pct'] >= high_hook and row['ROAS'] >= self.df_crea['ROAS'].median():
                return 'START/PRODUCE_SIMILAR (Winning DNA)'
            elif row['ROAS'] < low_roas:
                return 'STOP/RE-EVALUATE'
            else:
                return 'CONTINUE/TEST_VARIANTS'

        self.df_crea['creative_action'] = self.df_crea.apply(classify_crea, axis=1)
        
        return self.df_camp, self.df_crea

    def get_feature_importance(self, target='ROAS'):
        """
        Identifica quais atributos de criativo têm correlação estatística com o sucesso.
        """
        # Seleção de colunas categóricas para análise de DNA
        features = ['Estilo_Headline', 'Paleta_Cores', 'Presenca_Pessoa', 'Tipo_Criativo']
        df_model = pd.get_dummies(self.df_crea[features], drop_first=True)
        
        X = sm.add_constant(df_model.astype(float))
        y = self.df_crea[target]
        
        model = sm.OLS(y, X).fit()
        return model.summary()

    def get_cmo_summary(self, df_camp_processed, df_crea_processed):
        """
        Gera um report executivo simplificado.
        """
        summary = {
            "Campaign Actions": df_camp_processed['prescriptive_action'].value_counts().to_dict(),
            "Creative Actions": df_crea_processed['creative_action'].value_counts().to_dict()
        }
        return summary
