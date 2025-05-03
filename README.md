"# Telegram-FURIAFALLENBOT" 

FalleN Bot  - Telegram CS:GO Chatbot
Projeto desenvolvido para teste técnico.
O FalleN Bot é um chatbot no Telegram inspirado no jogador de CS:GO Gabriel "FalleN" Toledo. Ele interage com os usuários de maneira descontraída, respondendo perguntas sobre Counter-Strike, dicas de treino, história de times brasileiros, estratégias de smokes na Mirage, motivação e notícias de times como a FURIA.
________________________________________
 Funcionalidades
•	Respostas personalizadas sobre:
o	História do CS 1.6
o	Times LG e SK Gaming
o	AWP (sniper)
o	Treinos e dicas de evolução
o	Mensagens de motivação
o	Estratégias de smokes no mapa Mirage
o	Informações sobre os próximos jogos da FURIA
•	Linguagem de conversa humanizada, inspirada no jeito "resenha" do FalleN.
•	Comandos de navegação simples para o usuário.
________________________________________
 Tecnologias utilizadas
•	Python 3
•	PyTelegramBotAPI (biblioteca para criar bots no Telegram)
•	Biblioteca unidecode
________________________________________
 Estrutura do Código
•	start: Mensagem de boas-vindas e instruções de uso.
•	conversar: Função principal que analisa o texto do usuário e envia respostas baseadas em palavras-chave.
•	Funções específicas para ensinar smokes no mapa Mirage:
o	smoke_janelao
o	smoke_cabecinha
o	smoke_base_ct_da_a
o	smoke_jungle
o	smoke_top_meio
o	smoke_janela_b
________________________________________
 Como o Bot entende as mensagens?
O bot verifica se o texto da mensagem contém palavras-chave específicas para cada assunto.
Por exemplo:
•	Se o usuário fala "treino" ou "dicas", o bot responde com sugestões de treinamento.
•	Se fala "FURIA" ou "próximos jogos", ele recomenda sites confiáveis como HLTV.org e Dust2 Brasil.
Se o assunto não for reconhecido, o bot responde pedindo que o usuário escolha um dos temas disponíveis.
________________________________________
 Como rodar o projeto
1.	Clone o repositório:
bash
git clone https://github.com/seu-usuario/fallen-bot.git
cd fallen-bot
2.	Instale as dependências:
bash
pip install pyTelegramBotAPI
3.	Configure seu Token do Bot no código:
o	No arquivo principal, substitua 'SEU_TOKEN_AQUI' pelo token que você obteve ao criar seu bot no Telegram (BotFather).
4.	Execute o bot:
bash
python fallen_bot.py
5.	No Telegram, procure seu bot e envie /start para começar a interação!
________________________________________
 Melhorias futuras (ideias)
•	Adicionar botões interativos (inline keyboard) para facilitar navegação.
•	Integrar com APIs de notícias para puxar atualizações automáticas sobre CS:GO.
•	Sistema de rankeamento dos usuários mais ativos.
•	Novas smokes de outros mapas (Inferno, Overpass, etc).
________________________________________
 Autor
•	Rafael Pereira Reis - Estudante de Sistemas de Informação | Fã de e-sports e desenvolvimento de soluções com impacto real.
•	GitHub: @RafaelPReis
•	Contato: rafaelpreis75@gmail.com
________________________________________
Licença
Este projeto é open-source e pode ser utilizado livremente para fins de aprendizado ou como base para novos projetos.

