import requests
from dotenv import load_dotenv
import os
import unicodedata

def configure():
    load_dotenv()

load_dotenv()

base_url =  "https://api.le-systeme-solaire.net/rest"
headers = {"Authorization": f"Bearer {os.getenv('chave_api')}"}


class Planet:
    def __init__(self,data):
        self.nome = data["englishName"]
        self.gravidade = data["gravity"]
        self.raio = data["equaRadius"]
        self.tipo = data["bodyType"]
        self.luas = data.get("moons") or []

        dados_massa = data["mass"]
        self.massa = (dados_massa["massValue"] * (10 ** dados_massa["massExponent"]))
        dados_volume = data["vol"]
        self.volume = (dados_volume["volValue"] * (10 ** dados_volume["volExponent"]))

    def show_info(self):
            print("*" * 50)
            print(f"Nome do Astro: {self.nome}")
            print(f"Gravidade do Astro é: {self.gravidade:.2f}m/s²")
            print(f"A Massa do Astro é de: {self.massa:.3e}kg")
            print(f"O Volume do Astro é de: {self.volume:.3e}km³")
            print(f"O Raio Equatorial do Astro é de: {self.raio:.2f}km")
            print(f"O Astro é um(a): {self.tipo}")

            if self.luas:
             print(f"\nLuas de {self.nome}: ")

             for lua in self.luas:               
                print(f"- {lua['moon']}")
            else:
                print(f"\n{self.nome} não possui luas cadastradas")

            print("*" * 50)

    def calculo_gravidade_relativa(self):
        # Formula precisa da razão entre massa e raio
        # g_p = g_t * (M_p / M_t) * (R_t / R_p)^2

        MASSA_TERRA = 5.972e+24  
        RAIO_TERRA = 6378.0      
        GRAVIDADE_TERRA = 9.81

        razao_massa = self.massa / MASSA_TERRA
        razao_raio = RAIO_TERRA / self.raio

        g_calculada_ms2 = GRAVIDADE_TERRA * razao_massa * (razao_raio ** 2)
        g_calculada_Gs = (self.massa / MASSA_TERRA) * ((RAIO_TERRA / self.raio) ** 2)
        return g_calculada_ms2, g_calculada_Gs

def get_planet(name):
    url = (f"{base_url}/bodies/{name}")

    try:
        resposta = requests.get(url, 
                            headers=headers,
                            timeout=10)

        resposta.raise_for_status()
        return resposta.json()
    
    except requests.exceptions.RequestException as erro:
        (f"Falha ao Acessar Dados Astronômicos {erro}")
        return None

print("*" * 50)
print("BEM VINDO! NESSE PROGRAMA VOCÊ VAI OBTER DADOS ASTRONÔMICOS!")
print("*" * 50)
    
while True:
    planeta_escolhido = input("\nDigite O planeta Desejado ('sair' para fechar o programa): ").strip().lower()
    if planeta_escolhido == 'sair':
        print("\nAté Mais Parceiro! 🥏")
        break
    
    planetas_ptbr = {"terra": "earth", "marte": "mars", "vênus": "venus", "júpiter": "jupiter", "mercurio": "mercury", "saturno": "saturn","urano": "uranus","netuno": "neptune", "plutão": "pluto", "sol": "sun", "lua": "moon"}
    if planeta_escolhido in planetas_ptbr:
        print(f"💡 Dica: Convertendo '{planeta_escolhido}' para o termo em inglês da API: '{planetas_ptbr[planeta_escolhido]}'")
        planeta_escolhido = planetas_ptbr[planeta_escolhido]

    dados = get_planet(planeta_escolhido)

    if dados is not None:
        planeta = Planet(dados)
        g_ms2, g_gs = planeta.calculo_gravidade_relativa()
        if planeta.gravidade == 0:
            planeta.gravidade = g_ms2
        planeta.show_info()
        diferença_percentual = abs((g_ms2 - planeta.gravidade) / planeta.gravidade) * 100
        precisao = 100 - diferença_percentual

        print("-" * 50)
        print(f"-> Gravidade Calculada (Base = 🌏) é de: {g_ms2:.2f}m/s²")
        print(f"-> Força Gravitacional (Base = 🌏) é de: {g_gs:.2f}Gs")
        print(f"-> A Precisão do Calculo Gravitacional é de: {precisao:.2f}%")
        print("-" * 50)
    else:
        print(f"❌ ERRO: Não foi Possivel Encontrar o Planeta {planeta_escolhido}. Certifique-se de Digitar O Nome Correto!")

