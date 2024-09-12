import numpy as np
import skfuzzy as fuzz
from variavel_fuzzy import VariavelFuzzy
from regra_fuzzy import RegraFuzzy
from sistema_fuzzy import SistemaFuzzy

# Definir as variáveis fuzzy

# Variável histórico de crédito
historico_credito = VariavelFuzzy('historico_credito', np.arange(0, 11, 1), {
    'ruim': fuzz.trimf(np.arange(0, 11, 1), [0, 0, 3]),
    'regular': fuzz.trimf(np.arange(0, 11, 1), [2, 5, 8]),
    'bom': fuzz.trimf(np.arange(0, 11, 1), [6, 8, 10]),
    'excelente': fuzz.trimf(np.arange(0, 11, 1), [8, 10, 10])
})

# Variável renda mensal
renda_mensal = VariavelFuzzy('renda_mensal', np.arange(0, 11, 1), {
    'baixa': fuzz.trimf(np.arange(0, 11, 1), [0, 0, 4]),
    'media': fuzz.trimf(np.arange(0, 11, 1), [3, 5, 7]),
    'alta': fuzz.trimf(np.arange(0, 11, 1), [6, 10, 10])
})

# Variável dívida atual
divida_atual = VariavelFuzzy('divida_atual', np.arange(0, 11, 1), {
    'baixa': fuzz.trimf(np.arange(0, 11, 1), [0, 0, 3]),
    'moderada': fuzz.trimf(np.arange(0, 11, 1), [2, 5, 8]),
    'alta': fuzz.trimf(np.arange(0, 11, 1), [6, 10, 10])
})

# Variável risco (consequente)
risco = VariavelFuzzy('risco', np.arange(0, 11, 1), {
    'baixo': fuzz.trimf(np.arange(0, 11, 1), [0, 0, 4]),
    'medio': fuzz.trimf(np.arange(0, 11, 1), [3, 5, 7]),
    'alto': fuzz.trimf(np.arange(0, 11, 1), [6, 10, 10])
}, tipo='consequente')

# Definir as regras fuzzy
regras = [
    RegraFuzzy(historico_credito.variavel['excelente'] & divida_atual.variavel['baixa'], risco.variavel['baixo']),
    RegraFuzzy(historico_credito.variavel['ruim'] & divida_atual.variavel['alta'], risco.variavel['alto']),
    RegraFuzzy(historico_credito.variavel['bom'] & renda_mensal.variavel['media'] & divida_atual.variavel['moderada'], risco.variavel['medio']),
    RegraFuzzy(historico_credito.variavel['regular'] & divida_atual.variavel['moderada'], risco.variavel['medio']),
    RegraFuzzy(historico_credito.variavel['regular'] & divida_atual.variavel['alta'], risco.variavel['alto'])
]

# Criar o sistema fuzzy
sistema_fuzzy = SistemaFuzzy(
    variaveis={
        'historico_credito': historico_credito,
        'renda_mensal': renda_mensal,
        'divida_atual': divida_atual,
        'risco': risco
    },
    regras=regras
)

# Definir as entradas para o sistema
entradas = {
    'historico_credito': 7,  # exemplo
    'renda_mensal': 6,       # exemplo
    'divida_atual': 4        # exemplo
}

# Calcular o risco com base nas entradas fornecidas
resultado = sistema_fuzzy.calcular(entradas)

# Exibir o risco calculado
print(f"Risco calculado: {resultado:.2f}")

# Visualizar as funções de pertinência
sistema_fuzzy.visualizar_variaveis()
