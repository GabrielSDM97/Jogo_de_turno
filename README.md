# Jogo de Turno — Aventura no Terminal

RPG de exploração e combate por turnos jogado inteiramente no terminal, com sons em MP3 e textos coloridos.

## Como funciona

Você inicia com **100 HP** e inventário vazio. A cada exploração um evento aleatório acontece:

1. **Nada encontrado** — continue explorando.
2. **Loot** — recebe 1 item aleatório do `drop`.
3. **Encontro com monstro** — escolha lutar ou poupar.

### Combate por turnos

- Monstro nasce com HP aleatório entre **80 e 120**.
- Seu ataque causa **10–30** de dano por round.
- Contra-ataque do monstro causa **5–15** de dano por round.
- A cada turno você escolhe: `1` Atacar ou `2` Abrir inventário.
- Ao vencer, coleta **3 itens** do monstro.
- Ao perder (HP ≤ 0), é oferecida uma nova aventura.

### Itens e cura

| Item | Cura |
|---|---|
| Pão | 25 |
| Maçã | 10 |
| Poção | 75 |
| Pera | 12 |
| Água | 5 |

No inventário, digite o nome exato do item para consumi-lo e recuperar vida, ou deixe em branco para fechar.

## Requisitos

- Python 3
- pygame (para reproduzir os áudios)

```bash
pip install pygame
```

## Como jogar

```bash
python __main__.py
```

Responda aos prompts com `S/N` para explorar/aventura e `1/2` em combate.

## Estrutura

```
Jogo_de_turno/
├── __main__.py          # ponto de entrada -> engineJogo.engine.aventura()
├── engineJogo/
│   ├── engine.py        # loop do jogo: aventura, exploração, conflito, inv
│   └── textos.py        # formatação de rounds e inventário
├── utilidades/
│   ├── mp3.py           # player de áudio com pygame.mixer
│   └── cores.py         # cores ANSI para o terminal
└── audios/              # 9 efeitos: explorando, loot, encontro, jogador, monstro, consumir, inventário abrir/fechar, game_over
```

## Módulos

- `engineJogo/engine.py`: `aventura()`, `exploração()`, `evento1/2/3()`, `conflito()`, `inv()`.
- `engineJogo/textos.py`: `RoundJogador()`, `RoundMonstro()`, `invInfo()`.
- `utilidades/mp3.py`: `som("arquivo.mp3")` — bloqueia até o áudio terminar.
- `utilidades/cores.py`: `cor(msg, corTexto, corFundo)` — 0 Preto, 1 Vermelho, 2 Verde, 3 Amarelo, 4 Roxo, 5 Magenta, 6 Ciano, 7 Branco.
