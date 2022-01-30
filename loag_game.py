import pickle

story = {
    1: {
      'Text': [
            "Olha só... não é que você realmente voltou?",
            "Não esperava te encontrar com vida depois de todo o caos que causou na capital",
            "... Bem, se você veio me ver acho que só pode significar uma coisa. Quer realmente esse destino?"
        ],
      'Options': [
          ("Não tem outro jeito, essa é a minha única chance de fugir", 2),
          ("Sim, não posso deixar tudo acabar assim! Preciso tentar mais uma vez ", 3)
        ]
    },
    2: {    
        'Text': [
            "Pretende fugir como uma criança assustada?",
            "Incrível como coragem e caráter vem de berço... Mas tudo bem, faço isso apenas pela minha dívida com Helena",
            "Bem... como foi acordado com ela... Você voltará para onde tudo começou",
            "No dia que a conheceu, exatos 60 dias atrás." ,
            "Terá um novo nome e pronome, começará sua vida do zero ... Como tanto deseja.",
            "Mas não se deixe enganar, o seu destino continua o mesmo! Você continua sendo a pessoa que colocou tudo a perder!",
            "e eu não pretendo ajudar em nada além do que concordei com Helena.",
            "Pra mim você continua sendo a mesma criança assustada e egoísta que sempre foi.",
            "Contudo, se ao final dos 60 dias o seu destino tiver mudado, você será recompensado com um desejo",
            "E apenas um desejo... faça com que o sacrifício de Helena não tenha sido em vão"
        ],
        'Options': [
          (" ", 4),
          (" ", 5)
        ]
    },
    3: {
        'Text': [
            "Tentar mais uma vez? Não acha que causou dor o suficiente nesse mundo? Vai realmente fugir das consequências de suas ações?",
            "Incrível como coragem e caráter vem de berço... Mas tudo bem, faço isso apenas pela minha dívida com Helena",
            "Bem... como foi acordado com ela... Você voltará para onde tudo começou",
            "No dia que a conheceu, exatos 60 dias atrás." ,
            "Terá um novo nome e pronome, começará sua vida do zero ... Como tanto deseja.",
            "Mas não se deixe enganar, o seu destino continua o mesmo! Você continua sendo a pessoa que colocou tudo a perder!",
            "e eu não pretendo ajudar em nada além do que concordei com Helena.",
            "Pra mim você continua sendo a mesma criança assustada e egoísta que sempre foi.",
            "Contudo, se ao final dos 60 dias o seu destino tiver mudado, você será recompensado com um desejo",
            "E apenas um desejo... faça com que o sacrifício de Helena não tenha sido em vão"
        ],
        'Options': [
          (" ", 4),
          (" ", 5)
        ]
    },
    4: {
      'Text': [
            " ",
            " "
        ],
      'Options': []
    },
    5: {
      'Text': [
            " ",
            " "
        ],
      'Options': []
    }
}

with open('chapter1.ch', 'wb') as chapter:
  pickle.dump(story, chapter)