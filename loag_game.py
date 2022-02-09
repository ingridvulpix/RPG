import pickle

story = {
    1: {
      'Text': [
            "Olha só... não é que você realmente voltou?",
            "Não esperava te encontrar com vida depois de todo o caos que causou na capital",
            "... Bem, se você veio me ver acho que só pode significar uma coisa...",
            "Quer realmente esse destino?"
        ],
      'Options': [
          ("Não tenho outra escolha, é agora ou nunca", 2),
          ("Sim, não posso deixar tudo acabar assim! Preciso tentar mais uma vez ", 3)
        ]
    },
    2: {    
        'Text': [
            "Vindo de você e do seu desempenho ontem, creio que será nunca mesmo.",
            "Mas tudo bem, aparentemente você não foi derrotado o suficiente...",
            "Bem... seguiremos como foi acordado, você lembra das condições?"

        ],
        'Options': [
          ("Ah! Aquelas condições? Lembro sim, com certeza ....", 4),
          ("Então, talvez no calor do momento eu só tenha aceitado sem ouvir as condições, pode repetir?", 4)
        ]
    },
    3: {
        'Text': [
            "Aparentemente você não sofreu humilhação o suficiente!",
            "Mas tudo bem, seguiremos como foi acordado, você lembra das condições?"
        ],
        'Options': [
          ("Ah! Aquelas condições? Lembro sim, com certeza ....", 4),
          ("Então, talvez no calor do momento eu só tenha aceitado sem ouvir as condições, pode repetir?", 4)
        ]
    },
    4: {
      'Text': [
            "Hahahaha você não tem nem um pingo de vergonha na cara mesmo" ,
            "Como estou de bom humor, vou repetir o combinado! ",
            "Mas não venha depois chorar no meu ouvido se você não conseguir consertar as besteiras que fez",
            "Vamos lá, eu, como bruxo bondoso que sou, te concederei o que mais deseja!",
            "Mais uma chance! Será que dessa vez você acerta?",
            "Em troca você deverá abrir mão de seu nome e, consequentemente, seu passado",
            "Será como se a pessoa que você foi simplesmente nunca tivesse existido",
            "Mas te darei um nome e um pronome, assim você pode existir nessa nova realidade "
        ],
      'Options': [
        ("Então nem mesmo Helena se lembrará de mim?", 5)
      ]
    },
    5: {
      'Text': [
            "Sim, nem mesmo sua doce, e agora gelada, Helena ",
            "Voltarei o tempo em 60 dias, antes do estopim da guerra civil ... ",
            "Que você causou... francamente...",
            "Ae, a vida não é um morango! Não vou facilitar a história para você!",
            "Seria injusto se você voltasse isso tudo já sabendo as consequências das suas ações",
            "Você voltará sem passado e sem lembranças do futuro",
            "Essa nossa conversa será apenas um borrão para você"
        ],
      'Options': [
        ("Mas sem lembranças do que aconteceu, como eu posso fazer diferente?", 6)
      ]
    },
    6: {
    'Text': [
          "Incrível como isso não é problema meu hahahahaha Eu não gostaria de estar no seu lugar",
          ".......",
          "......",
          ".....",
          "Ta bom, TA BOM", 
          "Sem essa cara de cachorro que caiu da mudança! Eu vou te acompanhar nessa jornada",
          "Meio como um guia espiritual",
          "E você não saberá quem eu sou, eu só estarei te acompanhando em alguns momentos de sufoco",
          "MAS não é como se eu gostasse de você ou algo assim!",
          "Eu só quero garantir que ao final dos 60 dias você volte para mim!!",
          "Porque quando o prazo chegar e a magia se esgotar, você terá que fazer um sacrifício"
      ],
    'Options': [
      ("SACRIFÍCIO ????", 7)
    ]
    },
    7: {
    'Text': [
          "Ah, sim, sacrifício! Eu tinha te falado da última vez... lembra não?"
      ],
    'Options': [
      ("... não ...", 8)
    ]
    },
    8:{
    'Text': [
          "Você é muito burro mesmo... meu deus...",
          "Então, sua doce Helena se sacrificou, consequentemente o portal foi aberto e agora você está tendo a oportunidade de pelo menos uma vez na vida, limpar a própria bunda.",
          "A questão é que o portal abriu, mas não pode ficar assim pra sempre! Eu consigo segurar esse portal por 60 dias",
          "Esse é o tempo de você talvez acertar toda essa tragédia",
          "Ai, algumas situações podem acontecer no final do prazo, nada muito preocupante"
      ],
    'Options': [
      ("Que situações... ?", 9)
    ]
    },
    9: {
    'Text': [
          "Bem, você conseguindo ou não salvar o seu mundinho, o sacrifício precisa ser pago e você que precisa entregá-lo para mim ",
          "Então caso você fuja ou morra antes do prazo, todas as pessoas desse novo universo serão sacrificadas",
          "Um universo inteiro será o sacrifício por conta da sua burrice",
          "......",
          "... E ai? Está de acordo com as condições? Quer tanto assim tentar mais uma vez?"
      ],
    'Options': [
      ("Sim, se eu ficar parado agora todas essas mortes terão sido em vão.", 10),
      ("Não, eu acho que já causei problemas demais nesse mundo.", 11)
    ]
    },
    10: {
    'Text': [
          "Então, vamos lá"
      ],
    'Options': [],
    },
    11: {
    'Text': [
          "Bem, pena que Helena se sacrificou em vão",
          "Até"
      ],
    'Options': [],
    },
}

with open('chapter1.ch', 'wb') as chapter:
  pickle.dump(story, chapter)