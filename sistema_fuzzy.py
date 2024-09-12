from skfuzzy import control as ctrl

class SistemaFuzzy:
    def __init__(self, variaveis, regras):
        """
        Inicializa o sistema de controle fuzzy.

        variaveis: Dicionário de variáveis fuzzy (antecedentes e consequentes).
        regras: Lista de regras fuzzy.
        """
        self.variaveis = variaveis
        self.regras = regras

        # Criar o sistema de controle baseado nas regras
        self.sistema_controle = ctrl.ControlSystem([regra.regra for regra in self.regras])
        self.simulador = ctrl.ControlSystemSimulation(self.sistema_controle)

    def calcular(self, entradas):
        """
        Calcula o resultado fuzzy com base nas entradas fornecidas.

        entradas: Dicionário com os valores de entrada para cada variável fuzzy.
        """
        # Atribuir os valores de entrada
        for nome_variavel, valor in entradas.items():
            self.simulador.input[nome_variavel] = valor

        # Computar o resultado
        self.simulador.compute()

        # Retornar o resultado do consequente (risco)
        return self.simulador.output['risco']

    def visualizar_variaveis(self):
        """Visualiza as funções de pertinência de todas as variáveis fuzzy."""
        for variavel in self.variaveis.values():
            variavel.visualizar()
