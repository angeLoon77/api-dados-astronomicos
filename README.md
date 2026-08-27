# Dados Astronômicos - Planetas

Programa em Python que consulta dados reais de planetas e outros corpos celestes via [Le Système Solaire API](https://api.le-systeme-solaire.net/), calcula a gravidade relativa em comparação com a Terra e exibe as informações no terminal.

## Funcionalidades

- Consulta de dados de planetas (e outros corpos, como o Sol e a Lua) por nome, com suporte a nomes em português (ex: "terra", "marte", "júpiter")
- Exibição de gravidade, massa, volume, raio equatorial, temperatura média e distância do Sol (em UA)
- Listagem de luas conhecidas do corpo celeste consultado
- Cálculo próprio da gravidade relativa à Terra, com base na massa e no raio do planeta, e comparação com o valor oficial da API (precisão em %)
- Loop contínuo de consulta, até o usuário optar por sair

## Tecnologias

- Python 3
- [requests](https://pypi.org/project/requests/) — chamadas HTTP para a API
- [python-dotenv](https://pypi.org/project/python-dotenv/) — carregamento de variáveis de ambiente

## Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/angeLoon77/api-dados-astronomicos.git
   cd api-dados-astronomicos
   ```
   
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1   # Windows (PowerShell)
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure sua chave de API:
   - Renomeie o arquivo `.env.example` para `.env`
   - Insira sua chave da API no campo `chave_api`

5. Rode o programa:
   ```bash
   python space_api.py
   ```

## Como usar

Digite o nome de um planeta (em português ou inglês) quando solicitado, e o programa exibirá seus dados. Digite `sair` para encerrar o programa.

```
Digite O planeta Desejado ('sair' para fechar o programa): marte
💡 Dica: Convertendo 'marte' para o termo em inglês da API: 'mars'
**************************************************
Nome do Astro: Mars
Gravidade do Astro 'Mars' é: 3.71m/s²
...
```

## Estrutura do projeto

```
├── nome_do_arquivo.py   # Classe Planet + lógica de consulta e cálculo
├── .env.example          # Modelo de variáveis de ambiente (sem valores reais)
└── requirements.txt
```

## Limitações conhecidas / melhorias futuras

- Interface via terminal apenas — sem interface gráfica
- Nomes de planetas fora da lista de tradução pt-BR (`planetas_ptbr`) precisam ser digitados em inglês
- Ideia original era integrar este projeto com meu projeto de [simulação de gravidade](https://github.com/angeLoon77/simulacao-gravidade-ursina) (usando os dados reais dos planetas para simular órbitas), mas os dois projetos foram mantidos separados por enquanto

## Sobre o projeto

Este é um projeto pessoal de aprendizado, feito para praticar consumo de APIs externas, orientação a objetos e cálculos físicos em Python.
