import telebot
import unidecode

bot = telebot.TeleBot('7387260480:AAHcVpAE1eux7r2WmXolPgCPndwLzK81oNQ')

# --- SMOKES ESPECÍFICAS ---

@bot.message_handler(func=lambda msg: msg.text.strip().lower() == 'smoke janelão')
def smoke_janelao(msg):
    bot.reply_to(msg,
        "SMOKE JANELÃO (lado TR):\n"
        "Vai até o T spawn, encosta na parede direita, mira numa janelinha no alto, anda dois passos pra frente e joga. "
        "Smoke perfeita pra travar a visão do Janelão e dominar o meio! 😶‍🌫️"
    )

@bot.message_handler(func=lambda msg: msg.text.strip().lower() == 'smoke cabecinha')
def smoke_cabecinha(msg):
    bot.reply_to(msg,
        "SMOKE CABECINHA (lado TR):\n"
        "No Tetris, encosta na caixa, mira no meio do prédio da frente e joga andando. "
        "Essa smoke atrapalha totalmente a marcação dos CTs na posição da cabecinha! 🧠😶‍🌫️"
    )

@bot.message_handler(func=lambda msg: msg.text.strip().lower() == 'smoke base ct da a')
def smoke_base_ct_da_a(msg):
    bot.reply_to(msg,
        "SMOKE BASE CT DA A (lado TR):\n"
        "Da T spawn, cola na parede da esquerda, mira na janelinha alta e anda jogando. "
        "Smoke que corta a visão dos CTs segurando bomb A! 🏃‍♂️😶‍🌫️"
    )

@bot.message_handler(func=lambda msg: msg.text.strip().lower() == 'smoke jungle')
def smoke_jungle(msg):
    bot.reply_to(msg,
        "SMOKE JUNGLE (lado TR):\n"
        "No Tetris, mira no canto direito do prédio da frente e lança sem andar. "
        "Smoke certeira pra fechar a Jungle e avançar bomb A na paz! 🔥😶‍🌫️"
    )

@bot.message_handler(func=lambda msg: msg.text.strip().lower() == 'smoke top meio')
def smoke_top_meio(msg):
    bot.reply_to(msg,
        "SMOKE TOP MEIO (lado TR):\n"
        "Saindo da base TR, encosta no muro da direita, mira entre a antena e o prédio alto, e anda jogando. "
        "Smoke fundamental pra controlar o meio com segurança! 📈😶‍🌫️"
    )

@bot.message_handler(func=lambda msg: msg.text.strip().lower() == 'smoke janela b')
def smoke_janela_b(msg):
    bot.reply_to(msg,
        "SMOKE JANELA B (lado TR):\n"
        "No T spawn, cola no canto esquerdo, mira no topo da janela da B e joga agachado. "
        "Fecha a visão dos CTs no apartamento B e libera o rush tranquilo! 🏃‍♂️😶‍🌫️"
    )

# --- INÍCIO ---

@bot.message_handler(commands=['start', 'inicio'])
def start(msg):
    bot.reply_to(msg,
        "Salve, salve, rapaziada! Aqui é o FalleN Bot! 🎯\n\n"
        "Quer trocar ideia sobre CS, carreira, treinos, ou aprender umas smokes brabas da Mirage?\n"
        "É só mandar mensagem falando sobre o que você quer!\n"
        "Tipo:\n"
        "- 'Fala sobre 1.6'\n"
        "- 'Conta da LG/SK'\n"
        "- 'Me ensina a AWP'\n"
        "- 'Preciso de motivação'\n"
        "- 'Quero dicas de treino'\n"
        "- 'Ensina as smokes da Mirage'\n"
        "- 'Quando a FURIA joga'\n\n"
        "Tô pronto pra passar visão, confia no processo! 🔥"
    )

# --- RESPOSTA GERAL ---

@bot.message_handler(func=lambda msg: True)
def conversar(msg):
    texto_original = msg.text
    texto = unidecode.unidecode(texto_original).lower()

    if any(p in texto for p in ['1.6', 'cs 1.6', 'counter strike 1.6']):
        bot.reply_to(msg,
            "Ahhh o 1.6... era outro rolê! 💻🔥 Lan house bombando, galera ralando pra jogar, PC travando... "
            "Mas era pura paixão pelo game. Foi ali que nasci como competidor, irmão. Cada bala era suada! 🎯"
        )
    elif any(p in texto for p in ['lg', 'sk', 'luminosity', 'sk gaming', 'lg/sk']):
        bot.reply_to(msg,
            "Falar da LG e SK é falar de sonho realizado! 🏆 Quando a gente venceu os Majors, "
            "mostramos pro mundo que o Brasil sabia fazer história no CS. Aquilo foi muito mais que título: foi legado! 🇧🇷🔥"
        )
    elif any(p in texto for p in ['lan house', 'lanhouse', 'lan']):
        bot.reply_to(msg,
            "Lan house era raiz demais, irmão! 😂 1 real a hora, computador travando, cadeira quebrada, "
            "mas a vibe? Inexplicável! Era ali que surgiam as lendas, os clutches insanos e a paixão verdadeira pelo CS. 🖥️🏆"
        )
    elif any(p in texto for p in ['major', 'majors', 'campeonato']):
        bot.reply_to(msg,
            "Ganhar um Major é surreal, velho... 🎖️ É o topo da montanha, mas o que poucos falam é que pra chegar lá "
            "tem muito perrengue, muita derrota, muito treino suado. Persistência é tudo!"
        )
    elif any(p in texto for p in ['motivar', 'motivacao', 'motivacional', 'inspirar', 'inspiracao']):
        bot.reply_to(msg,
            "Rapaziada, a chave é acreditar no processo. 🚀 Cada dia é uma batalha, cada treino é uma conquista. "
            "Trabalhe em silêncio, seja seu maior fã, e deixa que o sucesso fale por você! Confia! 💪"
        )
    elif any(p in texto for p in ['awp', 'sniper']):
        bot.reply_to(msg,
            "AWP é muito mais que puxar o gatilho, irmão. 🎯 É posicionamento, é timing, é ler o jogo antes dos outros. "
            "Confia na tua mira, mas nunca subestime o jogo de cabeça. Foco total!"
        )
    elif any(p in texto for p in ['treino', 'treinar', 'treinamento', 'melhorar', 'dicas']):
        bot.reply_to(msg,
            "Treinar é o segredo que ninguém quer aceitar. 📚 Não tem atalho: foca no básico — mira, movimentação, comunicação. "
            "Treina todo dia como se fosse final de Major. É assim que se chega no topo! 🚀"
        )
    elif any(p in texto for p in ['historia', 'trajetoria', 'carreira', 'minha historia']):
        bot.reply_to(msg,
            "Minha história foi uma montanha-russa, irmão. 🎢 Tive muita dificuldade no começo: grana curta, sem apoio, "
            "mas uma coisa nunca faltou: paixão pelo game. Se eu puder te dizer algo: não desiste. A caminhada faz tudo valer a pena!"
        )
    elif any(p in texto for p in ['smoke', 'smokes', 'mirage', 'mapa mirage']):
        smokesmirage(msg)
    elif any(p in texto for p in [
        'furia', 'fúria', 'quando a furia joga', 'quando a fúria joga',
        'jogos da furia', 'jogos da fúria', 'proximos jogos', 'proximos jogos da furia',
        'proximo jogo da furia', 'furia cs', 'furia jogando', 'partida da furia'
    ]):
        bot.reply_to(msg,
            "🔥 Quer saber quando a FURIA vai jogar, irmão?\n\n"
            "O melhor jeito é ficar de olho no site da HLTV: https://www.hltv.org/ — lá tem tudo atualizadinho: "
            "jogos, horários, campeonatos, ranking mundial...\n\n"
            "Ou no Dust2 Brasil: https://www.dust2.com.br/ 🇧🇷\n"
            "Eles cobrem o cenário nacional de perto com notícias fresquinhas!\n\n"
            "Fica ligado que o cenário brasileiro tá voando! 🚀🎯"
        )
    else:
        bot.reply_to(msg,
            "Não entendi muito bem, parceiro. 😅\n"
            "Fala comigo sobre '1.6', 'LG/SK', 'AWP', 'treino', 'motivação', 'história', 'smokes' ou 'jogos da FURIA'!"
        )

# --- RESPOSTA GERAL PARA SMOKES ---

def smokesmirage(msg):
    bot.reply_to(msg,
        "Quer dominar a Mirage? 😶‍🌫️🔥\n\n"
        "Qual smoke você quer aprender?\n"
        "- SMOKE JANELÃO\n"
        "- SMOKE CABECINHA\n"
        "- SMOKE BASE CT DA A\n"
        "- SMOKE JUNGLE\n"
        "- SMOKE TOP MEIO\n"
        "- SMOKE JANELA B\n\n"
        "Escreve o nome da smoke certinho pra eu te passar a call!"
    )

# --- EXECUTA O BOT ---
bot.infinity_polling()
