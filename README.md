# 🪖 WAR - Jogo de Cartas (Python - Terminal)

## -->> Sobre o Projeto
Este projeto é uma implementação em **Python** do clássico jogo de cartas **WAR**, jogável diretamente no **terminal**.  
A proposta é simular uma disputa entre dois jogadores onde cada um utiliza suas cartas para vencer batalhas sucessivas, até que um deles fique sem cartas.

---

## -->> Lógica e Estrutura do Código

O código foi desenvolvido com **programação orientada a objetos (POO)**, utilizando três classes principais:

### **1. Classe `Card`**
Representa uma carta individual do baralho.  
Cada carta possui:
- **Naipe (`suit`)** → Copas, Espadas, Ouros, Paus  
- **Valor (`rank`)** → Dois, Três, ... Ás  
- **Força (`value`)** → Mapeada por um dicionário `values` para permitir comparação durante as batalhas  

📄 **Exemplo:**  
`Ace of Spades` possui `value = 14`, sendo uma das cartas mais fortes.

---

### **2. Classe `Deck`**
Gerencia o **baralho completo** de 52 cartas.  
- O método `__init__` cria todas as combinações possíveis de `suit` + `rank`.  
- `shuffle()` embaralha as cartas usando `random.shuffle()`.  
- `deal_one()` entrega (remove) a última carta do baralho.

-->> **Responsabilidade:** controlar a criação, embaralhamento e distribuição das cartas.

---

### **3. Classe `Player`**
Controla as ações e cartas de cada jogador:
- `remove_one()` → remove a primeira carta do jogador (para jogar na mesa).  
- `add_cards()` → adiciona cartas ao final do baralho do jogador (quando vence uma rodada).  
- `__str__()` → retorna o nome do jogador e quantas cartas ele tem.

---

## -->> Lógica do Jogo

1. **Criação dos jogadores**  
```python
player_one = Player("One")
player_two = Player("Two")
````

2. **Criação e embaralhamento do baralho**
  ```python
new_deck = Deck()
new_deck.shuffle()
````
3.**Distribuição das cartas (26 para cada jogador)**
```python
for x in range(26):
  player_one.add_cards(new_deck.deal_one())
  player_two.add_cards(new_deck.deal_one())
````
4.**Rodadas do jogo (while game_on)**
```python
Cada jogador joga uma carta por rodada.
A carta com maior valor vence.
O vencedor leva todas as cartas da rodada para o fim do seu baralho.

Empate (WAR!)

Se as cartas tiverem o mesmo valor → ocorre uma “guerra”.
Cada jogador adiciona 3 cartas adicionais viradas para baixo e 1 carta virada para cima.
A comparação é refeita com a nova carta.
Se um jogador não tiver cartas suficientes, o outro vence automaticamente.
````

   
