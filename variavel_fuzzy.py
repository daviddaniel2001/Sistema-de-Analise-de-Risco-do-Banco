import skfuzzy as fuzz
from skfuzzy import control as ctrl

class VariavelFuzzy:
    def __init__(self, nome, universo, termos, tipo='antecedente'):
        """
        nome: Nome da variável fuzzy (por exemplo, 'histórico de crédito')
        universo: Intervalo de valores da variável
        termos: Dicionário com termos e funções de pertinência
        tipo: 'antecedente' ou 'consequente'
        """
        if tipo == 'antecedente':
            self.variavel = ctrl.Antecedent(universo, nome)
        else:
            self.variavel = ctrl.Consequent(universo, nome)

        # Definir as funções de pertinência para cada termo
        for termo, funcao in termos.items():
            self.variavel[termo] = funcao

    def visualizar(self):
        """Visualiza a função de pertinência da variável fuzzy."""
        self.variavel.view()
