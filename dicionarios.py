pokemon = [
    {
      "nome": "pikachu",
      "tipo": "eletrico",
      "geração": 1
    },
    {
        "nome": "cyndaquil",
        "tipo": "fogo",
        "geração": 2
    },
    {
        "nome": "mudkip",
        "tipo": "agua",
        "geração" : 3
    },
    {
        "nome": "turtwig",
        "tipo": "planta",
        "geração": 4
    },
    {
        "nome": "snivy",
        "tipo": "planta",
        "geração": 5
    },
    {
        "nome": "froakie",
        "tipo": "agua",
        "geração": 6
    },
    {
        "nome": "litten",
        "tipo": "fogo",
        "geração": 7
    },
    {
        "nome": "grookey",
        "tipo": "planta",
        "geração":8
    },
    {
        "nome": "quaxly",
        "tipo": "agua",
        "geração": 9
    }
]

soma_gens = 0
for pokemons in pokemon:
    soma_gens += pokemons["geração"]
print(soma_gens/len(pokemon))