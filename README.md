Sistema de Análise de Risco do Banco

Este projeto implementa um sistema de avaliação de risco para clientes de um banco utilizando lógica nebulosa (fuzzy logic) com a biblioteca Scikit-Fuzzy. O sistema avalia o risco com base em variáveis como histórico de crédito, renda mensal e dívida atual do cliente.

    Estrutura do Projeto:
        O projeto é organizado em várias classes e arquivos para manter o código modular e fácil de manter. As principais classes são:

        VariavelFuzzy: Define uma variável fuzzy com seu universo de discurso e funções de pertinência.

        RegraFuzzy: Define uma regra fuzzy que relaciona antecedentes (condições) a um consequente (resultado).

        SistemaFuzzy: Gerencia o sistema fuzzy, adiciona variáveis e regras, e realiza o cálculo do risco.

    Dependências:
        Para rodar este projeto, você precisa instalar as seguintes bibliotecas Python:

        numpy
        matplotlib
        scipy
        scikit-fuzzy
        Você pode instalar essas bibliotecas usando pip:

        pip install numpy matplortlib scipy scikit-fuzzy

        bash
        Copiar código
        pip install numpy matplotlib scipy scikit-fuzzy

    Arquivos:
        variavel_fuzzy.py
        Define a classe VariavelFuzzy que representa uma variável fuzzy, incluindo seu universo de discurso e funções de pertinência. Utiliza scikit-fuzzy para criar variáveis fuzzy e funções de pertinência.

        regra_fuzzy.py
        Define a classe RegraFuzzy que representa uma regra fuzzy. Cada regra relaciona os antecedentes (condições) ao consequente (resultado) usando operadores fuzzy.

        sistema_fuzzy.py
        Define a classe SistemaFuzzy que coordena as variáveis e regras fuzzy, realiza o cálculo do risco e exibe gráficos das variáveis.

        main.py
        O ponto de entrada do projeto. Configura as variáveis fuzzy, regras e o sistema fuzzy, realiza o cálculo do risco e exibe as visualizações.

    Como Rodar o Código:
        Configurar o Ambiente:
            Instale as dependências listadas acima.

        Executar o Código:
            python main.py

        Visualização: 
            O script exibirá gráficos das variáveis fuzzy e salvará as visualizações como arquivos PNG na pasta visualizacoes/.
