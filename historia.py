def inicio():
    return (
        "Olá, vocês foram escolhidos para fazer parte dos Heróis dos Elementos.\n"
        "Cuidado! Nesse momento A Pedra dos Elementos desapareceu e o templo mágico começa a tremer.\n"
        "A missao de vocês é entrar no templo para recuperá-la. Boa sorte!"
    )

def escolha_porta():
    return (
        "Vocês acabam de chegar a uma sala com duas portas.\n"
        "O Herói do Fogo olha para a porta vermelha.\n"
        "A Heroína da Água observa a porta azul."
    )

def sala_lava():
    return (
        "Agora vocês entram na Sala de Lava.\n"
        "A sala está cheia de lava e plataformas perigosas."
    )

def escadas():
    return (
        "O Herói do Fogo puxa a alavanca.\n"
        "E uma porta secreta se abre.\n"
        "Existem duas escadas: esquerda ou direita, mas tome cuidado. Faça sua escolha muito bem!"
    )

def bau():
    return (
        "Vocês sobem a escada esquerda.\n"
        "No topo existe um baú mágico."
    )

def sala_agua():
    return (
        "Vocês entram na Sala de Água.\n"
        "A sala está cheia de água profunda."
    )

def ponte():
    return (
        "A Heroína da Água aperta um botão.\n"
        "Uma ponte aparece sobre a água para atravessar."
    )

def final_bom():
    return (
        "Vocês encontram a Pedra dos Elementos.\n"
        "FINAL BOM: Os Heróis dos Elementos salvam o templo. Parabéns!"
    )

def final_ruim(motivo):
    return (
        "FINAL RUIM: Um dos heróis cai em perigo ou se perde, e o templo é perdido."
    )