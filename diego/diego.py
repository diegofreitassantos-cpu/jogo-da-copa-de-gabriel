"""
🏆 QUIZ COPA DO MUNDO 🏆
Jogue no terminal do VS Code — basta dar um Play!
"""

import random
import time
import os
import sys

# ─── Cores ANSI ────────────────────────────────────────────────────────────────
class Cor:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    VERDE   = "\033[92m"
    VERMELHO= "\033[91m"
    AMARELO = "\033[93m"
    AZUL    = "\033[94m"
    CIANO   = "\033[96m"
    BRANCO  = "\033[97m"
    CINZA   = "\033[90m"
    BG_AZUL = "\033[44m"
    BG_VERD = "\033[42m"
    BG_VERM = "\033[41m"
    BG_AMAR = "\033[43m"

def c(texto, *estilos):
    return "".join(estilos) + texto + Cor.RESET

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar(msg="Pressione ENTER para continuar..."):
    input(c(f"\n  {msg}", Cor.CINZA))

# ─── Banco de perguntas ─────────────────────────────────────────────────────────
MODOS = {
    "1": {
        "nome": "⚽  Modo Clássico",
        "desc": "Perguntas variadas sobre a Copa do Mundo",
        "perguntas": [
            {
                "cat": "História",
                "q": "Qual país sediou a PRIMEIRA Copa do Mundo FIFA?",
                "opts": ["A) Brasil", "B) França", "C) Uruguai", "D) Argentina"],
                "ans": "C",
                "fato": "O Uruguai sediou e venceu a Copa de 1930, derrotando a Argentina na final por 4 a 2."
            },
            {
                "cat": "Campeões",
                "q": "Quantas vezes o Brasil venceu a Copa do Mundo?",
                "opts": ["A) 3 vezes", "B) 4 vezes", "C) 5 vezes", "D) 6 vezes"],
                "ans": "C",
                "fato": "O Brasil é o maior campeão da Copa do Mundo: 1958, 1962, 1970, 1994 e 2002."
            },
            {
                "cat": "Recordes",
                "q": "Qual país venceu a Copa do Mundo mais vezes, depois do Brasil?",
                "opts": ["A) Argentina", "B) Itália", "C) Alemanha", "D) França"],
                "ans": "C",
                "fato": "Alemanha e Itália têm 4 títulos cada. A Alemanha, porém, disputou mais finais (8 ao total)."
            },
            {
                "cat": "Brasil",
                "q": "Em qual ano o Brasil perdeu por 7 a 1 para a Alemanha, em casa?",
                "opts": ["A) 2010", "B) 2014", "C) 2018", "D) 2006"],
                "ans": "B",
                "fato": "O 'Mineirazo' foi em 2014, no Estádio Mineirão em BH. 5 gols alemães em apenas 18 minutos!"
            },
            {
                "cat": "Artilheiros",
                "q": "Quem é o maior artilheiro da história das Copas do Mundo?",
                "opts": ["A) Ronaldo Fenômeno", "B) Miroslav Klose", "C) Gerd Müller", "D) Pelé"],
                "ans": "B",
                "fato": "Miroslav Klose marcou 16 gols em 4 Copas (2002, 2006, 2010 e 2014)."
            },
            {
                "cat": "Sedes",
                "q": "Qual será a sede da Copa do Mundo de 2026?",
                "opts": ["A) Arábia Saudita", "B) Portugal e Espanha", "C) Canadá, México e EUA", "D) Austrália"],
                "ans": "C",
                "fato": "A Copa de 2026 terá 48 seleções e jogos no Canadá, México e EUA — a maior da história!"
            },
            {
                "cat": "Copa 2022",
                "q": "Qual seleção africana chegou às semifinais pela 1ª vez em 2022?",
                "opts": ["A) Senegal", "B) Gana", "C) Marrocos", "D) Tunísia"],
                "ans": "C",
                "fato": "O Marrocos fez história em 2022 eliminando Espanha e Portugal antes de cair para a França."
            },
            {
                "cat": "Brasil",
                "q": "O Brasil é o único país a disputar TODAS as edições da Copa. Quantas foram?",
                "opts": ["A) 20", "B) 21", "C) 22", "D) 23"],
                "ans": "C",
                "fato": "O Brasil participou das 22 edições da Copa e nunca foi eliminado na fase de grupos."
            },
            {
                "cat": "Final",
                "q": "Qual foi o único time europeu a vencer a Copa em solo americano?",
                "opts": ["A) Itália", "B) Espanha", "C) Alemanha", "D) França"],
                "ans": "C",
                "fato": "A Alemanha venceu a Copa de 2014 no Brasil, único europeu campeão nas Américas."
            },
            {
                "cat": "Copa 2022",
                "q": "Qual goleiro ganhou a Luva de Ouro na Copa do Mundo de 2022?",
                "opts": ["A) Hugo Lloris", "B) Alisson Becker", "C) Yassine Bounou", "D) Emiliano Martínez"],
                "ans": "D",
                "fato": "Dibu Martínez foi decisivo para a Argentina conquistar o título no Qatar em 2022."
            },
        ]
    },
    "2": {
        "nome": "📋  Grandes Placares",
        "desc": "Resultados históricos e jogos memoráveis",
        "perguntas": [
            {
                "cat": "Placar histórico",
                "q": "Qual foi o MAIOR placar de uma partida na história da Copa?",
                "opts": ["A) Hungria 9x0 Coreia", "B) Hungria 10x1 El Salvador", "C) Alemanha 8x0 Arábia Saudita", "D) Iugoslávia 9x0 Zaire"],
                "ans": "B",
                "fato": "Hungria 10x1 El Salvador em 1982 é o maior placar da história das Copas."
            },
            {
                "cat": "Final histórica",
                "q": "Qual foi o placar da final de 1970 (Brasil x Itália)?",
                "opts": ["A) Brasil 3x1 Itália", "B) Brasil 3x2 Itália", "C) Brasil 4x1 Itália", "D) Brasil 4x2 Itália"],
                "ans": "C",
                "fato": "Brasil 4x1 em 1970. Carlos Alberto fez um dos gols mais bonitos da história no 4º gol."
            },
            {
                "cat": "Mineirazo",
                "q": "Qual foi o placar exato do Mineirazo (Brasil x Alemanha, 2014)?",
                "opts": ["A) Brasil 0x7 Alemanha", "B) Brasil 1x8 Alemanha", "C) Brasil 2x7 Alemanha", "D) Brasil 1x7 Alemanha"],
                "ans": "D",
                "fato": "5 gols alemães entre o 23' e o 41'. Müller, Klose, Kroos (2) e Khedira marcaram."
            },
            {
                "cat": "Copa 2022",
                "q": "Qual foi o placar da final da Copa do Mundo de 2022?",
                "opts": ["A) Argentina 3x2 França", "B) Argentina 2x2 França (4x2 pênaltis)", "C) Argentina 3x3 França (4x2 pênaltis)", "D) Argentina 4x3 França"],
                "ans": "C",
                "fato": "A final de 2022 foi a mais emocionante: 3x3 com hat-trick de Mbappé e dupla de Messi!"
            },
            {
                "cat": "Maracanazo",
                "q": "Qual foi o placar do 'Maracanazo' (Brasil x Uruguai, 1950)?",
                "opts": ["A) Uruguai 2x0 Brasil", "B) Uruguai 3x1 Brasil", "C) Uruguai 2x1 Brasil", "D) Uruguai 1x0 Brasil"],
                "ans": "C",
                "fato": "O Maracanazo de 1950 é a maior tragédia do futebol brasileiro. Brasil precisava só do empate."
            },
            {
                "cat": "Artilharia",
                "q": "Quantos gols Just Fontaine marcou na Copa de 1958 (recorde em uma única edição)?",
                "opts": ["A) 11 gols", "B) 12 gols", "C) 13 gols", "D) 14 gols"],
                "ans": "C",
                "fato": "Just Fontaine marcou 13 gols na Copa de 1958 na Suécia. Recorde que permanece imbatível!"
            },
            {
                "cat": "Brasil",
                "q": "Qual o maior placar do Brasil em uma partida de Copa do Mundo?",
                "opts": ["A) Brasil 7x1 Haiti", "B) Brasil 6x1 Polônia", "C) Brasil 8x2 Bolívia", "D) Brasil 6x0 Honduras"],
                "ans": "B",
                "fato": "Brasil 6x1 Polônia em 1938. Leônidas da Silva (o 'Diamante Negro') marcou 4 gols."
            },
            {
                "cat": "Final",
                "q": "Qual foi a final de Copa do Mundo com mais gols (sem prorrogação)?",
                "opts": ["A) França 3x2 Brasil (1998)", "B) Alemanha 4x2 Hungria (1954)", "C) Brasil 4x1 Itália (1970)", "D) Argentina 3x2 Holanda (1978)"],
                "ans": "B",
                "fato": "A final de 1954 ficou conhecida como 'O Milagre de Berna'. A Hungria era invencível mas perdeu!"
            },
            {
                "cat": "Copa 2006",
                "q": "Qual foi o placar da semifinal mais goleada da Copa de 2006?",
                "opts": ["A) Alemanha 4x0 Portugal", "B) França 4x0 Portugal", "C) Itália 3x0 Alemanha", "D) Alemanha 3x0 Itália"],
                "ans": "A",
                "fato": "Alemanha 4x0 Portugal foi um dos maiores placares de uma semifinal na história recente das Copas."
            },
            {
                "cat": "Surpresa",
                "q": "Por quanto a Alemanha goleou a Arábia Saudita na Copa de 2002?",
                "opts": ["A) Alemanha 6x0 Arábia Saudita", "B) Alemanha 8x0 Arábia Saudita", "C) Alemanha 7x1 Arábia Saudita", "D) Alemanha 5x0 Arábia Saudita"],
                "ans": "B",
                "fato": "Alemanha 8x0 em 2002 é a segunda maior vitória de um europeu em Copas. Miroslav Klose fez hat-trick."
            },
        ]
    },
    "3": {
        "nome": "🥅  Artilheiros",
        "desc": "Os maiores goleadores da história das Copas",
        "perguntas": [
            {
                "cat": "Recorde",
                "q": "Com quantos gols Miroslav Klose é o maior artilheiro da Copa?",
                "opts": ["A) 14 gols", "B) 15 gols", "C) 16 gols", "D) 17 gols"],
                "ans": "C",
                "fato": "Klose marcou 16 gols em 4 Copas (2002, 2006, 2010, 2014). Superou Ronaldo Fenômeno em 2014."
            },
            {
                "cat": "Copa 2022",
                "q": "Quem foi o artilheiro da Copa do Mundo de 2022 no Qatar?",
                "opts": ["A) Lionel Messi", "B) Kylian Mbappé", "C) Olivier Giroud", "D) Cody Gakpo"],
                "ans": "B",
                "fato": "Mbappé marcou 8 gols em 2022, incluindo hat-trick na final. Aos 23 anos tinha 12 gols em 2 Copas!"
            },
            {
                "cat": "Brasil",
                "q": "Quem é o maior artilheiro do Brasil em Copas do Mundo?",
                "opts": ["A) Pelé", "B) Romário", "C) Ronaldo Fenômeno", "D) Zico"],
                "ans": "C",
                "fato": "Ronaldo Fenômeno marcou 15 gols em 3 Copas (1994, 1998 e 2002), maior artilheiro brasileiro."
            },
            {
                "cat": "Copa 2018",
                "q": "Quem foi o artilheiro da Copa do Mundo de 2018 na Rússia?",
                "opts": ["A) Cristiano Ronaldo", "B) Lionel Messi", "C) Harry Kane", "D) Antoine Griezmann"],
                "ans": "C",
                "fato": "Harry Kane ganhou a Chuteira de Ouro de 2018 com 6 gols, sendo capitão da Inglaterra nas semis."
            },
            {
                "cat": "Pelé",
                "q": "Quantos gols Pelé marcou em Copas do Mundo ao longo da carreira?",
                "opts": ["A) 10 gols", "B) 12 gols", "C) 14 gols", "D) 16 gols"],
                "ans": "B",
                "fato": "Pelé marcou 12 gols em 4 Copas (1958, 1962, 1966 e 1970). Em 1958 foi o mais jovem a marcar em uma final."
            },
            {
                "cat": "Copa 1930",
                "q": "Quem foi o artilheiro da primeira Copa do Mundo em 1930?",
                "opts": ["A) Scarone (Uruguai)", "B) Pedro Cea (Uruguai)", "C) Guillermo Stábile (Argentina)", "D) Héctor Castro (Uruguai)"],
                "ans": "C",
                "fato": "Stábile marcou 8 gols pela Argentina em 1930, ficando famoso como 'El Filtrador'."
            },
            {
                "cat": "Hat-tricks",
                "q": "Cristiano Ronaldo marcou um hat-trick em qual Copa do Mundo?",
                "opts": ["A) 2010 vs México", "B) 2014 vs EUA", "C) 2018 vs Espanha", "D) 2022 vs Gana"],
                "ans": "C",
                "fato": "Em 2018, Ronaldo marcou 3 gols em Portugal 3x3 Espanha, incluindo falta no fim. Jogo lendário!"
            },
            {
                "cat": "Copa 2006",
                "q": "Quem ganhou a Chuteira de Ouro da Copa de 2006 na Alemanha?",
                "opts": ["A) Ronaldo Fenômeno", "B) Miroslav Klose", "C) Zinedine Zidane", "D) Thierry Henry"],
                "ans": "B",
                "fato": "Klose marcou 5 gols em 2006 jogando em casa, na Alemanha."
            },
            {
                "cat": "Finais",
                "q": "Quem marcou mais gols em finais de Copa do Mundo na história?",
                "opts": ["A) Pelé", "B) Vavá", "C) Helmut Rahn", "D) Zinedine Zidane"],
                "ans": "B",
                "fato": "Vavá marcou 4 gols em finais de Copa: 2 em 1958 e 2 em 1962, mais do que qualquer outro."
            },
            {
                "cat": "Copa 2014",
                "q": "Quem foi o artilheiro da Copa do Mundo de 2014 no Brasil?",
                "opts": ["A) Lionel Messi", "B) Neymar", "C) Thomas Müller", "D) James Rodríguez"],
                "ans": "C",
                "fato": "Thomas Müller foi artilheiro em 2010 e 2014, ambos com 5 gols. Um fenômeno das Copas!"
            },
        ]
    },
    "4": {
        "nome": "🌍  Países e Sedes",
        "desc": "Campeões, sedes e curiosidades por nação",
        "perguntas": [
            {
                "cat": "Países",
                "q": "Quantos países diferentes já venceram a Copa do Mundo?",
                "opts": ["A) 7 países", "B) 8 países", "C) 9 países", "D) 10 países"],
                "ans": "B",
                "fato": "8 países já foram campeões: Brasil (5), Alemanha (4), Itália (4), Argentina (3), França (2), Uruguai (2), Inglaterra e Espanha (1 cada)."
            },
            {
                "cat": "África",
                "q": "Qual foi o primeiro país africano a sediar uma Copa do Mundo?",
                "opts": ["A) Nigéria", "B) Egito", "C) África do Sul", "D) Marrocos"],
                "ans": "C",
                "fato": "A África do Sul sediou a Copa de 2010. 'Waka Waka' de Shakira ficou mundialmente famosa."
            },
            {
                "cat": "Ásia",
                "q": "Quais países asiáticos co-sediaram a Copa do Mundo de 2002?",
                "opts": ["A) Japão e China", "B) China e Coreia do Sul", "C) Japão e Coreia do Sul", "D) Japão e Austrália"],
                "ans": "C",
                "fato": "A Copa de 2002 foi a primeira na Ásia e a primeira co-sediada por dois países."
            },
            {
                "cat": "Qatar 2022",
                "q": "O Qatar foi o primeiro país-sede eliminado na fase de grupos. É verdade?",
                "opts": ["A) Sim, em 2022", "B) Não, a África do Sul também foi em 2010", "C) Não, houve outro antes", "D) Sim, mas compartilha com outro"],
                "ans": "A",
                "fato": "O Qatar foi o primeiro e único país-sede eliminado na fase de grupos, sem vencer nenhuma partida."
            },
            {
                "cat": "Brasil",
                "q": "Para qual Copa do Mundo foi construído o Maracanã no Rio de Janeiro?",
                "opts": ["A) 1938", "B) 1950", "C) 1954", "D) 1958"],
                "ans": "B",
                "fato": "O Maracanã foi inaugurado em 1950, com capacidade original de 200 mil pessoas — o maior estádio do mundo à época."
            },
            {
                "cat": "Espanha",
                "q": "Em qual Copa do Mundo a Espanha conquistou seu único título?",
                "opts": ["A) 2006", "B) 2010", "C) 2014", "D) 2018"],
                "ans": "B",
                "fato": "A Espanha venceu em 2010 na África do Sul com gol de Iniesta na prorrogação contra a Holanda."
            },
            {
                "cat": "Recordes",
                "q": "Qual país disputou MAIS finais de Copa do Mundo?",
                "opts": ["A) Brasil", "B) Itália", "C) Alemanha", "D) Argentina"],
                "ans": "C",
                "fato": "A Alemanha disputou 8 finais: 1954, 1966, 1974, 1982, 1986, 1990, 2002 e 2014 — campeã em 4."
            },
            {
                "cat": "México",
                "q": "O México sediou duas Copas do Mundo. Em quais anos?",
                "opts": ["A) 1966 e 1978", "B) 1970 e 1986", "C) 1970 e 1994", "D) 1978 e 1986"],
                "ans": "B",
                "fato": "O México sediou em 1970 (Pelé campeão) e 1986 (Maradona com o 'Gol do Século' contra a Inglaterra)."
            },
            {
                "cat": "Colômbia",
                "q": "Qual foi o melhor resultado da Colômbia em Copas do Mundo?",
                "opts": ["A) Terceiro lugar em 1962", "B) Semifinal em 2002", "C) Quartas de final em 2014", "D) Oitavas de final em 2018"],
                "ans": "C",
                "fato": "Em 2014, a Colômbia chegou às quartas de final, com James Rodríguez sendo artilheiro e ganhando o prêmio de melhor gol."
            },
            {
                "cat": "Copa 2030",
                "q": "Quais países serão sede da Copa do Mundo de 2030?",
                "opts": ["A) Espanha e Portugal", "B) Marrocos, Espanha e Portugal (+ 3 países)", "C) Inglaterra e Escócia", "D) Alemanha e Áustria"],
                "ans": "B",
                "fato": "A Copa de 2030 será realizada no Marrocos, Espanha e Portugal, com jogos especiais no Uruguai, Argentina e Paraguai para marcar o centenário."
            },
        ]
    },
}

# ─── Tela de título ─────────────────────────────────────────────────────────────
def tela_titulo():
    limpar()
    print()
    print(c("  ╔══════════════════════════════════════════════════╗", Cor.AMARELO, Cor.BOLD))
    print(c("  ║                                                  ║", Cor.AMARELO, Cor.BOLD))
    print(c("  ║   🏆  QUIZ COPA DO MUNDO  🏆                    ║", Cor.AMARELO, Cor.BOLD))
    print(c("  ║                                                  ║", Cor.AMARELO, Cor.BOLD))
    print(c("  ║   Teste seus conhecimentos sobre o maior         ║", Cor.AMARELO, Cor.BOLD))
    print(c("  ║   torneio de futebol do planeta!                 ║", Cor.AMARELO, Cor.BOLD))
    print(c("  ║                                                  ║", Cor.AMARELO, Cor.BOLD))
    print(c("  ╚══════════════════════════════════════════════════╝", Cor.AMARELO, Cor.BOLD))
    print()

# ─── Menu de modos ──────────────────────────────────────────────────────────────
def escolher_modo():
    tela_titulo()
    print(c("  ESCOLHA O MODO DE JOGO:\n", Cor.CIANO, Cor.BOLD))
    for k, v in MODOS.items():
        print(c(f"  [{k}]", Cor.AZUL, Cor.BOLD) + f"  {v['nome']}")
        print(c(f"       {v['desc']}", Cor.CINZA))
        print()
    print(c("  [0]", Cor.VERMELHO) + "  Sair do jogo\n")

    while True:
        escolha = input(c("  Digite o número do modo: ", Cor.BRANCO)).strip()
        if escolha == "0":
            print(c("\n  Até a próxima! ⚽\n", Cor.VERDE))
            sys.exit()
        if escolha in MODOS:
            return escolha
        print(c("  Opção inválida! Tente novamente.", Cor.VERMELHO))

# ─── Barra de progresso ─────────────────────────────────────────────────────────
def barra_progresso(atual, total, acertos):
    preenchido = int((atual / total) * 30)
    barra = "█" * preenchido + "░" * (30 - preenchido)
    pct = int((atual / total) * 100)
    return (
        c(f"  [{barra}]", Cor.AZUL) +
        c(f" {pct}%", Cor.CIANO) +
        c(f"  |  Pergunta {atual}/{total}", Cor.CINZA) +
        c(f"  |  ✅ {acertos} acertos", Cor.VERDE)
    )

# ─── Exibir pergunta ────────────────────────────────────────────────────────────
def exibir_pergunta(numero, total, pergunta, acertos):
    limpar()
    tela_titulo()
    print(barra_progresso(numero, total, acertos))
    print()
    print(c(f"  [{pergunta['cat'].upper()}]", Cor.CIANO, Cor.BOLD))
    print()

    # Quebra o enunciado em linhas de ~55 chars
    texto = pergunta['q']
    while len(texto) > 55:
        idx = texto[:55].rfind(' ')
        if idx == -1:
            idx = 55
        print(c(f"  {texto[:idx]}", Cor.BRANCO, Cor.BOLD))
        texto = texto[idx+1:]
    print(c(f"  {texto}", Cor.BRANCO, Cor.BOLD))
    print()

    for opt in pergunta['opts']:
        letra = opt[0]
        print(c(f"  {letra}", Cor.AMARELO, Cor.BOLD) + c(opt[1:], Cor.BRANCO))
    print()

# ─── Receber resposta ────────────────────────────────────────────────────────────
def receber_resposta(pergunta):
    validas = {"A", "B", "C", "D"}
    while True:
        resp = input(c("  Sua resposta (A/B/C/D): ", Cor.CIANO)).strip().upper()
        if resp in validas:
            return resp
        print(c("  ⚠  Digite apenas A, B, C ou D.", Cor.VERMELHO))

# ─── Resultado da pergunta ───────────────────────────────────────────────────────
def mostrar_resultado(acertou, pergunta, resposta):
    print()
    if acertou:
        print(c("  ✅  CORRETO! Muito bem!", Cor.VERDE, Cor.BOLD))
    else:
        ans = pergunta['ans']
        opt_correta = next(o for o in pergunta['opts'] if o.startswith(ans))
        print(c("  ❌  INCORRETO!", Cor.VERMELHO, Cor.BOLD))
        print(c(f"  Resposta certa: {opt_correta}", Cor.VERDE))

    print()
    print(c("  💡 Você sabia?", Cor.AMARELO, Cor.BOLD))
    # Quebra o fato em linhas
    fato = pergunta['fato']
    while len(fato) > 60:
        idx = fato[:60].rfind(' ')
        if idx == -1:
            idx = 60
        print(c(f"     {fato[:idx]}", Cor.CINZA))
        fato = fato[idx+1:]
    print(c(f"     {fato}", Cor.CINZA))
    print()

# ─── Tela de resultado final ────────────────────────────────────────────────────
def tela_final(acertos, total, tempo_total, modo_nome):
    limpar()
    pct = int((acertos / total) * 100)
    tempo_medio = round(tempo_total / total, 1)

    if pct == 100:
        emoji, titulo, cat = "🏆", "CAMPEÃO MUNDIAL!", "Categoria: Pelé"
    elif pct >= 80:
        emoji, titulo, cat = "🥇", "EXCELENTE!", "Categoria: Ronaldo Fenômeno"
    elif pct >= 60:
        emoji, titulo, cat = "🥈", "MUITO BOM!", "Categoria: Torcedor Especialista"
    elif pct >= 40:
        emoji, titulo, cat = "🥉", "RAZOÁVEL", "Categoria: Torcedor em Formação"
    else:
        emoji, titulo, cat = "⚽", "CONTINUE TENTANDO!", "Categoria: Novato"

    print()
    print(c("  ╔══════════════════════════════════════════════════╗", Cor.AMARELO, Cor.BOLD))
    print(c(f"  ║   {emoji}  FIM DE JOGO — {titulo:<31}║", Cor.AMARELO, Cor.BOLD))
    print(c("  ╚══════════════════════════════════════════════════╝", Cor.AMARELO, Cor.BOLD))
    print()
    print(c(f"  Modo:         ", Cor.CINZA) + c(modo_nome, Cor.BRANCO, Cor.BOLD))
    print(c(f"  Acertos:      ", Cor.CINZA) + c(f"{acertos}/{total}  ({pct}%)", Cor.VERDE, Cor.BOLD))
    print(c(f"  Tempo médio:  ", Cor.CINZA) + c(f"{tempo_medio}s por pergunta", Cor.BRANCO))
    print(c(f"  Classificação:", Cor.CINZA) + c(f" {cat}", Cor.AMARELO, Cor.BOLD))
    print()

    fatos_extras = [
        "A Copa do Mundo de 2026 terá 48 seleções pela primeira vez na história.",
        "O Brasil é o único país a ter disputado todas as Copas do Mundo.",
        "A Argentina conquistou seu 3º título em 2022, igualando a Itália.",
        "O VAR foi usado pela primeira vez na Copa de 2018 na Rússia.",
        "A bola da Copa de 2022 se chamava 'Al Rihla' — 'a jornada' em árabe.",
        "Em 1930, apenas 13 seleções participaram da primeira Copa do Mundo.",
        "Kylian Mbappé tinha 19 anos quando venceu a Copa de 2018 com a França.",
    ]
    print(c("  💡 Fato bônus:", Cor.CIANO, Cor.BOLD))
    fato = random.choice(fatos_extras)
    while len(fato) > 58:
        idx = fato[:58].rfind(' ')
        if idx == -1: idx = 58
        print(c(f"     {fato[:idx]}", Cor.CINZA))
        fato = fato[idx+1:]
    print(c(f"     {fato}", Cor.CINZA))
    print()

# ─── Loop principal do jogo ─────────────────────────────────────────────────────
def jogar():
    while True:
        chave = escolher_modo()
        modo = MODOS[chave]
        perguntas = random.sample(modo['perguntas'], min(10, len(modo['perguntas'])))

        acertos = 0
        tempo_total = 0.0
        total = len(perguntas)

        for i, pergunta in enumerate(perguntas, start=1):
            exibir_pergunta(i, total, pergunta, acertos)
            inicio = time.time()
            resposta = receber_resposta(pergunta)
            tempo_total += time.time() - inicio

            acertou = resposta == pergunta['ans']
            if acertou:
                acertos += 1

            mostrar_resultado(acertou, pergunta, resposta)
            pausar()

        tela_final(acertos, total, tempo_total, modo['nome'])

        print(c("  O que deseja fazer?\n", Cor.CIANO, Cor.BOLD))
        print(c("  [1]", Cor.AZUL, Cor.BOLD) + "  Jogar novamente (mesmo modo)")
        print(c("  [2]", Cor.AZUL, Cor.BOLD) + "  Escolher outro modo")
        print(c("  [0]", Cor.VERMELHO) + "  Sair\n")

        op = input(c("  Escolha: ", Cor.BRANCO)).strip()
        if op == "0":
            print(c("\n  Obrigado por jogar! Até a próxima Copa! 🏆⚽\n", Cor.VERDE, Cor.BOLD))
            break
        elif op == "1":
            continue  # reinicia com mesmo modo
        else:
            continue  # volta ao menu de modos

# ─── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        jogar()
    except KeyboardInterrupt:
        print(c("\n\n  Jogo encerrado. Até a próxima! ⚽\n", Cor.AMARELO))
        sys.exit(0)