"""
🏆 QUIZ COPA DO MUNDO — Interface Gráfica com Pygame
Instale o pygame se necessário: pip install pygame
"""

import pygame
import sys
import random
import time
import math

pygame.init()

# ── Janela ──────────────────────────────────────────────────────────────────
W, H = 820, 620
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("🏆 Quiz Copa do Mundo")
clock = pygame.time.Clock()

# ── Cores ────────────────────────────────────────────────────────────────────
C = {
    "bg":        (15,  23,  42),
    "card":      (26,  38,  64),
    "card2":     (32,  48,  80),
    "green":     (34, 197, 120),
    "green_dk":  (22, 140,  80),
    "red":       (239, 68,  68),
    "red_dk":    (180, 40,  40),
    "gold":      (250, 189,  20),
    "gold_dk":   (200, 140,   0),
    "blue":      ( 56, 139, 253),
    "blue_lt":   (100, 170, 255),
    "white":     (240, 248, 255),
    "gray":      (120, 140, 170),
    "gray_lt":   (160, 180, 210),
    "opt_bg":    ( 36,  52,  88),
    "opt_hover": ( 48,  70, 115),
    "opt_cor":   ( 22,  80,  50),
    "opt_err":   ( 80,  25,  25),
    "stripe":    ( 20,  32,  58),
}

# ── Fontes ────────────────────────────────────────────────────────────────────
def fonte(size, bold=False):
    return pygame.font.SysFont("Segoe UI" if sys.platform == "win32" else "DejaVu Sans", size, bold=bold)

F = {
    "title":   fonte(38, True),
    "subtitle":fonte(18),
    "big":     fonte(26, True),
    "med":     fonte(20, True),
    "body":    fonte(17),
    "small":   fonte(14),
    "tiny":    fonte(12),
    "cat":     fonte(13, True),
}

# ── Banco de perguntas ────────────────────────────────────────────────────────
QUESTIONS = {
    "classico": {
        "label": "⚽ Modo Clássico",
        "color": C["blue"],
        "data": [
            ("História", "Qual país sediou a PRIMEIRA Copa do Mundo FIFA?",
             ["Uruguai","Brasil","França","Argentina"], 0,
             "O Uruguai sediou e venceu a Copa de 1930, derrotando a Argentina na final por 4 a 2."),
            ("Campeões", "Quantas vezes o Brasil venceu a Copa do Mundo?",
             ["3 vezes","4 vezes","5 vezes","6 vezes"], 2,
             "O Brasil é o maior campeão da Copa: 1958, 1962, 1970, 1994 e 2002."),
            ("Recordes", "Qual país venceu mais Copas depois do Brasil?",
             ["Argentina","Itália","Alemanha","França"], 2,
             "Alemanha e Itália têm 4 títulos cada; a Alemanha disputou mais finais (8)."),
            ("Brasil", "Em qual ano o Brasil perdeu por 7 a 1 para a Alemanha em casa?",
             ["2010","2014","2018","2006"], 1,
             "O 'Mineirazo' foi em 2014 no Mineirão. 5 gols alemães em apenas 18 minutos!"),
            ("Artilheiros", "Quem é o maior artilheiro da história das Copas?",
             ["Ronaldo Fenômeno","Miroslav Klose","Gerd Müller","Pelé"], 1,
             "Klose marcou 16 gols em 4 Copas (2002, 2006, 2010, 2014)."),
            ("Sedes", "Onde será a Copa do Mundo de 2026?",
             ["Arábia Saudita","Portugal e Espanha","Canadá, México e EUA","Austrália"], 2,
             "A Copa de 2026 terá 48 seleções — a maior da história!"),
            ("Copa 2022", "Qual seleção africana chegou às semifinais em 2022?",
             ["Senegal","Gana","Marrocos","Tunísia"], 2,
             "O Marrocos fez história eliminando Espanha e Portugal antes de cair para a França."),
            ("Brasil", "O Brasil é o único país a disputar todas as Copas. Quantas foram?",
             ["20","21","22","23"], 2,
             "O Brasil participou das 22 edições e nunca foi eliminado na fase de grupos."),
            ("Final", "Qual time europeu venceu a Copa em solo americano?",
             ["Itália","Espanha","Alemanha","França"], 2,
             "A Alemanha venceu a Copa de 2014 no Brasil — único europeu campeão nas Américas."),
            ("Copa 2022", "Qual goleiro ganhou a Luva de Ouro em 2022?",
             ["Hugo Lloris","Alisson Becker","Bounou","Emiliano Martínez"], 3,
             "Dibu Martínez foi decisivo para a Argentina ser campeã no Qatar."),
        ]
    },
    "placares": {
        "label": "📋 Grandes Placares",
        "color": C["gold"],
        "data": [
            ("Placar histórico", "Qual o MAIOR placar de uma partida na história da Copa?",
             ["Hungria 9x0 Coreia","Hungria 10x1 El Salvador","Alemanha 8x0 Arábia Saudita","Iugoslávia 9x0 Zaire"], 1,
             "Hungria 10x1 El Salvador em 1982 — o maior placar da história das Copas!"),
            ("Final 1970", "Qual foi o placar da final de 1970 (Brasil x Itália)?",
             ["3x1","3x2","4x1","4x2"], 2,
             "Brasil 4x1 Itália. Carlos Alberto fez um dos gols mais bonitos da história."),
            ("Mineirazo", "Qual foi o placar exato do Mineirazo (2014)?",
             ["Brasil 0x7","Brasil 1x8","Brasil 2x7","Brasil 1x7"], 3,
             "5 gols alemães entre o 23' e o 41'. Müller, Klose, Kroos (2) e Khedira marcaram."),
            ("Copa 2022", "Qual foi o placar da final da Copa de 2022?",
             ["3x3 (4x2 pênaltis)","2x2 (4x3 pênaltis)","3x2 (prorrogação)","4x3 (prorrogação)"], 0,
             "A final de 2022: 3x3 com hat-trick de Mbappé e dupla de Messi. Argentina venceu nos pênaltis!"),
            ("Maracanazo", "Qual foi o placar do 'Maracanazo' (Brasil x Uruguai, 1950)?",
             ["Uruguai 2x0","Uruguai 3x1","Uruguai 2x1","Uruguai 1x0"], 2,
             "O Maracanazo é a maior tragédia do futebol brasileiro. Brasil precisava só do empate."),
            ("Recorde", "Quantos gols Just Fontaine marcou na Copa de 1958?",
             ["11 gols","12 gols","13 gols","14 gols"], 2,
             "13 gols na Copa de 1958 na Suécia — recorde imbatível até hoje!"),
            ("Brasil", "Qual o maior placar do Brasil em uma Copa do Mundo?",
             ["7x1 vs Haiti","6x1 vs Polônia","8x2 vs Bolívia","6x0 vs Honduras"], 1,
             "Brasil 6x1 Polônia em 1938. Leônidas da Silva (o Diamante Negro) marcou 4 gols."),
            ("Final histórica", "Qual final de Copa teve mais gols sem prorrogação?",
             ["França 3x2 Brasil (1998)","Alemanha 4x2 Hungria (1954)","Brasil 4x1 Itália (1970)","Argentina 3x2 Holanda (1978)"], 1,
             "A final de 1954 ficou conhecida como 'O Milagre de Berna'. A Hungria era invencível!"),
            ("Copa 2006", "Qual foi o placar da goleada da Alemanha sobre Portugal em 2006?",
             ["Alemanha 4x0","França 4x0","Itália 3x0","Alemanha 3x0"], 0,
             "Alemanha 4x0 Portugal foi um dos maiores placares em semifinais recentes."),
            ("Copa 2002", "Por quanto a Alemanha goleou a Arábia Saudita em 2002?",
             ["6x0","8x0","7x1","5x0"], 1,
             "Alemanha 8x0 em 2002 — segunda maior vitória europeia em Copas. Klose fez hat-trick."),
        ]
    },
    "artilheiros": {
        "label": "🥅 Artilheiros",
        "color": C["green"],
        "data": [
            ("Recorde", "Com quantos gols Klose é o maior artilheiro da Copa?",
             ["14","15","16","17"], 2,
             "16 gols em 4 Copas: 2002 (5), 2006 (5), 2010 (4), 2014 (2). Superou Ronaldo em 2014."),
            ("Copa 2022", "Quem foi o artilheiro da Copa de 2022 no Qatar?",
             ["Messi","Mbappé","Giroud","Gakpo"], 1,
             "Mbappé marcou 8 gols em 2022, incluindo hat-trick na final. 12 gols em 2 Copas com 23 anos!"),
            ("Brasil", "Quem é o maior artilheiro do Brasil em Copas?",
             ["Pelé","Romário","Ronaldo Fenômeno","Zico"], 2,
             "Ronaldo Fenômeno marcou 15 gols em 3 Copas (1994, 1998, 2002)."),
            ("Copa 2018", "Quem foi o artilheiro da Copa de 2018 na Rússia?",
             ["Cristiano Ronaldo","Messi","Harry Kane","Griezmann"], 2,
             "Harry Kane ganhou a Chuteira de Ouro de 2018 com 6 gols como capitão da Inglaterra."),
            ("Pelé", "Quantos gols Pelé marcou em Copas do Mundo?",
             ["10","12","14","16"], 1,
             "Pelé marcou 12 gols em 4 Copas. Em 1958, com 17 anos, foi o mais jovem a marcar numa final."),
            ("Copa 1930", "Quem foi o artilheiro da primeira Copa em 1930?",
             ["Scarone (Uruguai)","Pedro Cea (Uruguai)","Guillermo Stábile (Argentina)","Héctor Castro (Uruguai)"], 2,
             "Guillermo Stábile marcou 8 gols pela Argentina em 1930 — o 'El Filtrador'."),
            ("Hat-tricks", "Em qual Copa Cristiano Ronaldo marcou um hat-trick?",
             ["2010 vs México","2014 vs EUA","2018 vs Espanha","2022 vs Gana"], 2,
             "Em 2018, Ronaldo marcou 3 gols em Portugal 3x3 Espanha, incluindo falta no fim!"),
            ("Copa 2006", "Quem ganhou a Chuteira de Ouro da Copa de 2006?",
             ["Ronaldo Fenômeno","Miroslav Klose","Zidane","Thierry Henry"], 1,
             "Klose marcou 5 gols em 2006 jogando em sua casa, na Alemanha."),
            ("Finais", "Quem marcou mais gols em finais da Copa do Mundo?",
             ["Pelé","Vavá","Helmut Rahn","Zidane"], 1,
             "Vavá marcou 4 gols em finais: 2 em 1958 e 2 em 1962 — mais do que qualquer outro jogador."),
            ("Copa 2014", "Quem foi o artilheiro da Copa de 2014 no Brasil?",
             ["Messi","Neymar","Thomas Müller","James Rodríguez"], 2,
             "Thomas Müller foi artilheiro em 2010 e 2014, ambos com 5 gols. Um fenômeno das Copas!"),
        ]
    },
    "paises": {
        "label": "🌍 Países e Sedes",
        "color": (180, 100, 230),
        "data": [
            ("Países", "Quantos países diferentes já venceram a Copa?",
             ["7","8","9","10"], 1,
             "8 países: Brasil (5), Alemanha (4), Itália (4), Argentina (3), França (2), Uruguai (2), Inglaterra e Espanha (1 cada)."),
            ("África", "Qual foi o primeiro país africano a sediar a Copa?",
             ["Nigéria","Egito","África do Sul","Marrocos"], 2,
             "A África do Sul sediou a Copa de 2010. 'Waka Waka' de Shakira ficou mundialmente famosa."),
            ("Ásia", "Quais países asiáticos co-sediaram a Copa de 2002?",
             ["Japão e China","China e Coreia","Japão e Coreia do Sul","Japão e Austrália"], 2,
             "A Copa de 2002 foi a primeira na Ásia e a primeira co-sediada por dois países."),
            ("Qatar", "O Qatar foi o 1º país-sede eliminado na fase de grupos?",
             ["Sim, em 2022","Não, África do Sul (2010) também","Não, houve outro antes","Sim, e compartilha com outro"], 0,
             "O Qatar foi o único país-sede eliminado na fase de grupos, sem vencer nenhuma partida em 2022."),
            ("Brasil", "Para qual Copa o Maracanã foi construído?",
             ["1938","1950","1954","1958"], 1,
             "O Maracanã foi inaugurado em 1950 com capacidade original de 200 mil pessoas — o maior do mundo à época."),
            ("Espanha", "Em qual Copa a Espanha conquistou seu único título?",
             ["2006","2010","2014","2018"], 1,
             "A Espanha venceu em 2010 na África do Sul com gol de Iniesta na prorrogação contra a Holanda."),
            ("Recordes", "Qual país disputou MAIS finais de Copa do Mundo?",
             ["Brasil","Itália","Alemanha","Argentina"], 2,
             "A Alemanha disputou 8 finais: 1954, 1966, 1974, 1982, 1986, 1990, 2002 e 2014 — campeã em 4."),
            ("México", "Em quais anos o México sediou duas Copas do Mundo?",
             ["1966 e 1978","1970 e 1986","1970 e 1994","1978 e 1986"], 1,
             "México sediou em 1970 (Pelé campeão) e 1986 (Maradona e o 'Gol do Século' vs Inglaterra)."),
            ("Colômbia", "Qual foi o melhor resultado da Colômbia em Copas?",
             ["3º lugar (1962)","Semifinal (2002)","Quartas de final (2014)","Oitavas (2018)"], 2,
             "Em 2014, a Colômbia chegou às quartas com James Rodríguez ganhando o prêmio de melhor gol."),
            ("Copa 2030", "Quais países sediarão a Copa de 2030?",
             ["Espanha e Portugal","Marrocos, Espanha e Portugal (+3)","Inglaterra e Escócia","Alemanha e Áustria"], 1,
             "A Copa de 2030 será no Marrocos, Espanha e Portugal, com jogos no Uruguai, Argentina e Paraguai para marcar o centenário."),
        ]
    },
}

# ── Utilitários de desenho ────────────────────────────────────────────────────
def draw_rect_rounded(surf, color, rect, radius=12, border=0, border_color=None):
    pygame.draw.rect(surf, color, rect, border_radius=radius)
    if border and border_color:
        pygame.draw.rect(surf, border_color, rect, border, border_radius=radius)

def draw_text_wrapped(surf, text, font, color, x, y, max_w, line_h=26):
    words = text.split()
    line, lines = [], []
    for w in words:
        test = " ".join(line + [w])
        if font.size(test)[0] <= max_w:
            line.append(w)
        else:
            if line:
                lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    for i, ln in enumerate(lines):
        s = font.render(ln, True, color)
        surf.blit(s, (x, y + i * line_h))
    return len(lines) * line_h

def text_center(surf, text, font, color, cx, y):
    s = font.render(text, True, color)
    surf.blit(s, (cx - s.get_width()//2, y))
    return s.get_height()

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

# ── Partículas de confete ──────────────────────────────────────────────────────
class Particle:
    def __init__(self):
        self.x = random.randint(0, W)
        self.y = random.randint(-40, 0)
        self.vx = random.uniform(-1.5, 1.5)
        self.vy = random.uniform(2, 5)
        self.size = random.randint(6, 14)
        self.color = random.choice([C["gold"], C["green"], C["blue"], C["red"], (255,255,255)])
        self.angle = random.uniform(0, 360)
        self.spin = random.uniform(-4, 4)
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.angle += self.spin
    def draw(self, surf):
        s = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.rect(s, self.color, (0,0,self.size,self.size))
        rot = pygame.transform.rotate(s, self.angle)
        surf.blit(rot, (self.x - rot.get_width()//2, self.y - rot.get_height()//2))

# ── Classe principal do jogo ───────────────────────────────────────────────────
class QuizGame:
    def __init__(self):
        self.state = "menu"          # menu | game | result
        self.mode_key = "classico"
        self.questions = []
        self.current = 0
        self.score = 0
        self.correct = 0
        self.chosen = None           # índice escolhido
        self.answered = False
        self.timer = 20.0
        self.timer_start = 0
        self.hover = -1
        self.particles = []
        self.anim = 0.0              # contador geral de animação
        self.feedback_alpha = 0
        self.transition = 0.0        # fade entre perguntas
        self.times = []
        self.mode_hover = None

        # botões do menu
        self.mode_keys = list(QUESTIONS.keys())

    def start(self, mode_key):
        self.mode_key = mode_key
        pool = list(QUESTIONS[mode_key]["data"])
        random.shuffle(pool)
        self.questions = pool[:10]
        self.current = 0
        self.score = 0
        self.correct = 0
        self.times = []
        self.particles = []
        self.state = "game"
        self._load_question()

    def _load_question(self):
        self.chosen = None
        self.answered = False
        self.timer = 20.0
        self.timer_start = time.time()
        self.hover = -1
        self.feedback_alpha = 0
        self.transition = 0.0

    def update(self):
        self.anim += 0.025
        if self.state == "game" and not self.answered:
            elapsed = time.time() - self.timer_start
            self.timer = max(0, 20.0 - elapsed)
            if self.timer <= 0:
                self._do_answer(-1)  # tempo esgotado
        if self.answered:
            self.feedback_alpha = min(255, self.feedback_alpha + 12)
        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.y < H + 30]

    def _do_answer(self, idx):
        if self.answered:
            return
        self.answered = True
        self.chosen = idx
        q = self.questions[self.current]
        t = 20.0 - self.timer
        self.times.append(t)
        if idx == q[3]:
            self.correct += 1
            pts = max(100, int(500 - t * 20))
            self.score += pts
            for _ in range(30):
                self.particles.append(Particle())

    def next_question(self):
        self.current += 1
        if self.current >= len(self.questions):
            self.state = "result"
            for _ in range(80):
                self.particles.append(Particle())
        else:
            self._load_question()

    def handle_click(self, pos):
        mx, my = pos
        if self.state == "menu":
            # cards de modo
            for i, k in enumerate(self.mode_keys):
                r = self._mode_rect(i)
                if r.collidepoint(mx, my):
                    self.start(k)
                    return
        elif self.state == "game":
            if self.answered:
                # botão próxima
                btn = pygame.Rect(W//2 - 120, H - 70, 240, 46)
                if btn.collidepoint(mx, my):
                    self.next_question()
            else:
                for i in range(4):
                    r = self._opt_rect(i)
                    if r.collidepoint(mx, my):
                        self._do_answer(i)
        elif self.state == "result":
            btn_menu = pygame.Rect(W//2 - 250, H - 80, 220, 46)
            btn_retry = pygame.Rect(W//2 + 30, H - 80, 220, 46)
            if btn_menu.collidepoint(mx, my):
                self.state = "menu"
            elif btn_retry.collidepoint(mx, my):
                self.start(self.mode_key)

    def handle_motion(self, pos):
        mx, my = pos
        if self.state == "menu":
            self.mode_hover = None
            for i, k in enumerate(self.mode_keys):
                if self._mode_rect(i).collidepoint(mx, my):
                    self.mode_hover = i
        elif self.state == "game" and not self.answered:
            self.hover = -1
            for i in range(4):
                if self._opt_rect(i).collidepoint(mx, my):
                    self.hover = i

    def _mode_rect(self, i):
        cols, rows = 2, 2
        cw, ch = 360, 130
        gx, gy = 20, 20
        col = i % cols
        row = i // cols
        x = W//2 - (cols*cw + (cols-1)*gx)//2 + col*(cw+gx)
        y = 300 + row*(ch+gy)
        return pygame.Rect(x, y, cw, ch)

    def _opt_rect(self, i):
        cols = 2
        ow, oh = 370, 66
        gx, gy = 16, 12
        col = i % cols
        row = i // cols
        x = W//2 - (cols*ow + (cols-1)*gx)//2 + col*(ow+gx)
        y = 370 + row*(oh+gy)
        return pygame.Rect(x, y, ow, oh)

    # ── Desenhos ──────────────────────────────────────────────────────────────
    def draw(self):
        screen.fill(C["bg"])
        # fundo decorativo — linhas sutis
        for row in range(0, H, 40):
            pygame.draw.line(screen, C["stripe"], (0, row), (W, row), 1)

        if self.state == "menu":
            self._draw_menu()
        elif self.state == "game":
            self._draw_game()
        elif self.state == "result":
            self._draw_result()

        for p in self.particles:
            p.draw(screen)

        pygame.display.flip()

    def _draw_menu(self):
        # Troféu animado
        bob = math.sin(self.anim * 2) * 5
        text_center(screen, "🏆", F["title"], C["gold"], W//2, 55 + bob)
        text_center(screen, "QUIZ COPA DO MUNDO", F["title"], C["gold"], W//2, 110)
        text_center(screen, "Escolha um modo de jogo para começar", F["body"], C["gray"], W//2, 158)

        for i, k in enumerate(self.mode_keys):
            m = QUESTIONS[k]
            r = self._mode_rect(i)
            hover = self.mode_hover == i
            bg = C["card2"] if hover else C["card"]
            border_c = m["color"] if hover else C["card2"]
            draw_rect_rounded(screen, bg, r, 14, 2 if hover else 0, border_c)

            # barra colorida lateral
            bar = pygame.Rect(r.x, r.y + 14, 4, r.h - 28)
            pygame.draw.rect(screen, m["color"], bar, border_radius=2)

            lbl = m["label"]
            s = F["med"].render(lbl, True, C["white"])
            screen.blit(s, (r.x + 18, r.y + 20))
            desc_map = {
                "classico": "Perguntas variadas sobre a Copa",
                "placares": "Resultados históricos e goleadas",
                "artilheiros": "Os maiores goleadores da história",
                "paises": "Sedes, campeões e curiosidades",
            }
            draw_text_wrapped(screen, desc_map[k], F["small"], C["gray_lt"], r.x+18, r.y+54, r.w-36, 20)

            # qtd perguntas
            qt = F["tiny"].render("10 perguntas", True, m["color"])
            screen.blit(qt, (r.x + r.w - qt.get_width() - 14, r.y + r.h - qt.get_height() - 12))

    def _draw_game(self):
        if not self.questions:
            return
        q = self.questions[self.current]
        cat, qtext, opts, ans, fact = q
        mode = QUESTIONS[self.mode_key]

        # ── Cabeçalho ──────────────────────────────────────────────────────
        # Barra de progresso
        prog_w = W - 80
        prog_rect = pygame.Rect(40, 28, prog_w, 8)
        draw_rect_rounded(screen, C["card2"], prog_rect, 4)
        fill_w = int(prog_w * (self.current / len(self.questions)))
        if fill_w > 0:
            draw_rect_rounded(screen, mode["color"], pygame.Rect(40, 28, fill_w, 8), 4)

        # Pergunta X/10
        s = F["small"].render(f"{self.current+1} / {len(self.questions)}", True, C["gray"])
        screen.blit(s, (40, 44))

        # Placar
        sc_s = F["small"].render(f"⭐ {self.score} pts", True, C["gold"])
        screen.blit(sc_s, (W - sc_s.get_width() - 40, 44))

        # ── Timer ──────────────────────────────────────────────────────────
        t_pct = self.timer / 20.0
        timer_col = lerp_color(C["red"], C["green"], t_pct)
        t_rect = pygame.Rect(40, 65, W - 80, 6)
        draw_rect_rounded(screen, C["card2"], t_rect, 3)
        tw = int((W-80) * t_pct)
        if tw > 0:
            draw_rect_rounded(screen, timer_col, pygame.Rect(40, 65, tw, 6), 3)
        ts = F["small"].render(f"{self.timer:.1f}s", True, timer_col)
        screen.blit(ts, (W//2 - ts.get_width()//2, 76))

        # ── Card da pergunta ───────────────────────────────────────────────
        qcard = pygame.Rect(40, 100, W - 80, 240)
        draw_rect_rounded(screen, C["card"], qcard, 16)
        # barra top colorida
        pygame.draw.rect(screen, mode["color"], pygame.Rect(40, 100, W-80, 5), border_radius=16)

        # Categoria
        cat_s = F["cat"].render(cat.upper(), True, mode["color"])
        screen.blit(cat_s, (60, 120))

        # Texto da pergunta
        draw_text_wrapped(screen, qtext, F["big"], C["white"], 60, 148, W-120, 34)

        # ── Opções ─────────────────────────────────────────────────────────
        letters = ["A", "B", "C", "D"]
        for i in range(4):
            r = self._opt_rect(i)
            if self.answered:
                if i == ans:
                    bg = C["opt_cor"]
                    border_c = C["green"]
                elif i == self.chosen and self.chosen != ans:
                    bg = C["opt_err"]
                    border_c = C["red"]
                else:
                    bg = C["card"]
                    border_c = C["card"]
                alpha = min(255, self.feedback_alpha)
            else:
                bg = C["opt_hover"] if self.hover == i else C["opt_bg"]
                border_c = mode["color"] if self.hover == i else C["opt_bg"]
                alpha = 255

            draw_rect_rounded(screen, bg, r, 10, 1 if self.hover == i or self.answered else 0, border_c)

            # Letra
            ls = F["med"].render(letters[i], True, mode["color"] if not self.answered else (C["green"] if i == ans else C["red"] if i == self.chosen else C["gray"]))
            screen.blit(ls, (r.x + 14, r.y + r.h//2 - ls.get_height()//2))

            # Texto opção
            draw_text_wrapped(screen, opts[i], F["body"], C["white"], r.x + 44, r.y + r.h//2 - 10, r.w - 56, 20)

            # Ícone de resultado
            if self.answered and self.feedback_alpha > 80:
                if i == ans:
                    ic = F["med"].render("✓", True, C["green"])
                    screen.blit(ic, (r.x + r.w - ic.get_width() - 12, r.y + r.h//2 - ic.get_height()//2))
                elif i == self.chosen and self.chosen != ans:
                    ic = F["med"].render("✗", True, C["red"])
                    screen.blit(ic, (r.x + r.w - ic.get_width() - 12, r.y + r.h//2 - ic.get_height()//2))

        # ── Feedback / fato ────────────────────────────────────────────────
        if self.answered and self.feedback_alpha > 40:
            fb_rect = pygame.Rect(40, H - 150, W - 80, 68)
            if self.chosen == ans:
                fb_bg = (20, 60, 40)
                fb_col = C["green"]
                pts = max(100, int(500 - self.times[-1] * 20)) if self.times else 0
                header = f"✅  Correto! +{pts} pts"
            elif self.chosen == -1:
                fb_bg = (60, 30, 20)
                fb_col = C["red"]
                header = "⏱  Tempo esgotado!"
            else:
                fb_bg = (60, 20, 20)
                fb_col = C["red"]
                header = f"❌  Incorreto — a certa era: {opts[ans]}"

            draw_rect_rounded(screen, fb_bg, fb_rect, 10)
            hs = F["small"].render(header, True, fb_col)
            screen.blit(hs, (fb_rect.x + 14, fb_rect.y + 8))
            draw_text_wrapped(screen, "💡 " + fact, F["tiny"], C["gray_lt"], fb_rect.x+14, fb_rect.y+32, fb_rect.w-28, 18)

            # Botão próxima
            if self.feedback_alpha > 120:
                btn = pygame.Rect(W//2 - 120, H - 70, 240, 46)
                lbl = "Ver resultado →" if self.current == len(self.questions)-1 else "Próxima pergunta →"
                draw_rect_rounded(screen, mode["color"], btn, 10)
                bs = F["body"].render(lbl, True, C["bg"])
                screen.blit(bs, (btn.x + btn.w//2 - bs.get_width()//2, btn.y + btn.h//2 - bs.get_height()//2))

    def _draw_result(self):
        acertos = self.correct
        total = len(self.questions)
        pct = int(acertos / total * 100)
        avg = round(sum(self.times)/len(self.times), 1) if self.times else 0
        mode = QUESTIONS[self.mode_key]

        if pct == 100:
            emoji, titulo = "🏆", "CAMPEÃO MUNDIAL!"
            cat, cat_col = "Categoria: Pelé", C["gold"]
        elif pct >= 80:
            emoji, titulo = "🥇", "EXCELENTE!"
            cat, cat_col = "Categoria: Ronaldo Fenômeno", C["gold"]
        elif pct >= 60:
            emoji, titulo = "🥈", "MUITO BOM!"
            cat, cat_col = "Categoria: Torcedor Especialista", C["blue_lt"]
        elif pct >= 40:
            emoji, titulo = "🥉", "RAZOÁVEL"
            cat, cat_col = "Categoria: Torcedor em Formação", C["gray_lt"]
        else:
            emoji, titulo = "⚽", "CONTINUE TENTANDO!"
            cat, cat_col = "Categoria: Novato", C["gray"]

        bob = math.sin(self.anim * 2) * 6
        text_center(screen, emoji, F["title"], C["gold"], W//2, 55 + bob)
        text_center(screen, titulo, F["title"], C["gold"], W//2, 115)
        text_center(screen, cat, F["med"], cat_col, W//2, 158)

        # Cards de stats
        stats = [
            ("Acertos", f"{acertos}/{total}",  C["green"]),
            ("Aproveitamento", f"{pct}%",       mode["color"]),
            ("Pontuação", f"{self.score}",       C["gold"]),
            ("Tempo médio", f"{avg}s",           C["blue_lt"]),
        ]
        sw, sh, gx = 170, 90, 14
        total_w = len(stats)*sw + (len(stats)-1)*gx
        sx0 = W//2 - total_w//2
        for i, (lbl, val, col) in enumerate(stats):
            r = pygame.Rect(sx0 + i*(sw+gx), 200, sw, sh)
            draw_rect_rounded(screen, C["card"], r, 12)
            pygame.draw.rect(screen, col, pygame.Rect(r.x, r.y, r.w, 4), border_radius=12)
            text_center(screen, val, F["big"], col, r.centerx, r.y + 22)
            text_center(screen, lbl, F["small"], C["gray"], r.centerx, r.y + 62)

        # Fato bônus
        fatos = [
            "A Copa de 2026 terá 48 seleções pela primeira vez na história!",
            "O Brasil é o único país a disputar todas as edições da Copa.",
            "A Argentina conquistou seu 3º título em 2022, igualando a Itália.",
            "O VAR foi usado pela primeira vez na Copa de 2018 na Rússia.",
            "Kylian Mbappé tinha 19 anos quando venceu a Copa de 2018.",
        ]
        fact_rect = pygame.Rect(60, 320, W-120, 72)
        draw_rect_rounded(screen, C["card"], fact_rect, 12)
        pygame.draw.rect(screen, C["gold"], pygame.Rect(60, 320, W-120, 4), border_radius=12)
        fl = F["small"].render("💡  Você sabia?", True, C["gold"])
        screen.blit(fl, (fact_rect.x + 16, fact_rect.y + 12))
        draw_text_wrapped(screen, random.choice(fatos), F["small"], C["gray_lt"], fact_rect.x+16, fact_rect.y+36, fact_rect.w-32, 20)

        # Barra de acertos visual
        bar_y = 420
        text_center(screen, "Desempenho por pergunta", F["small"], C["gray"], W//2, bar_y)
        bw = min(30, (W - 120) // total - 4)
        total_bw = total * (bw+4) - 4
        bx0 = W//2 - total_bw//2
        for i, t in enumerate(self.times):
            q = self.questions[i]
            ans_ok = (self.correct > 0)  # simplificado: usamos lista separada
        # recalcular corretos por índice
        # (guardamos chosen por pergunta se quisermos detalhar; aqui mostramos progresso temporal)
        for i in range(total):
            bh = int(60 * (1 - min(self.times[i], 20)/20)) + 10 if i < len(self.times) else 10
            col = C["green"] if i < self.correct else C["red"]
            r = pygame.Rect(bx0 + i*(bw+4), bar_y + 20 + (60 - bh), bw, bh)
            draw_rect_rounded(screen, col, r, 3)

        # Botões
        btn_menu  = pygame.Rect(W//2 - 250, H - 80, 220, 46)
        btn_retry = pygame.Rect(W//2 +  30, H - 80, 220, 46)
        draw_rect_rounded(screen, C["card2"], btn_menu, 10, 1, C["gray"])
        draw_rect_rounded(screen, mode["color"], btn_retry, 10)
        ms = F["body"].render("← Menu principal", True, C["white"])
        rs = F["body"].render("Jogar novamente", True, C["bg"])
        screen.blit(ms, (btn_menu.x  + btn_menu.w//2  - ms.get_width()//2, btn_menu.y  + 13))
        screen.blit(rs, (btn_retry.x + btn_retry.w//2 - rs.get_width()//2, btn_retry.y + 13))


# ── Main loop ─────────────────────────────────────────────────────────────────
def main():
    game = QuizGame()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game.state != "menu":
                        game.state = "menu"
                    else:
                        pygame.quit()
                        sys.exit()
                # Atalhos de teclado nas opções (A B C D ou 1 2 3 4)
                if game.state == "game" and not game.answered:
                    key_map = {
                        pygame.K_a: 0, pygame.K_1: 0,
                        pygame.K_b: 1, pygame.K_2: 1,
                        pygame.K_c: 2, pygame.K_3: 2,
                        pygame.K_d: 3, pygame.K_4: 3,
                    }
                    if event.key in key_map:
                        game._do_answer(key_map[event.key])
                if game.state == "game" and game.answered:
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        game.next_question()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                game.handle_motion(event.pos)

        game.update()
        game.draw()
        clock.tick(60)

if __name__ == "__main__":
    main()
