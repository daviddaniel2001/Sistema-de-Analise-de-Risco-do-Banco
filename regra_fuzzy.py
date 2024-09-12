from skfuzzy import control as ctrl

class RegraFuzzy:
    def __init__(self, antecedentes, consequente):
        """
        Define uma regra fuzzy.
        
        antecedentes: Condição ou combinação de variáveis fuzzy e seus termos (e.g., variavel['termo']).
        consequente: Variável fuzzy de saída e seu termo (e.g., variavel['termo']).
        """
        # Criar a regra fuzzy com os antecedentes e o consequente
        self.regra = ctrl.Rule(antecedentes, consequente)
