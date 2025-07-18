# 🎯 Jogo de Adivinhação - Python

Um simples e divertido jogo de adivinhação em Python, onde o jogador tenta descobrir um número secreto entre 1 e 500 com um limite de 10 tentativas. A cada partida, o jogador acumula pontos de acordo com sua performance.

---

## 📋 Descrição

O jogo sorteia um número aleatório entre **1 e 500**, e o jogador tem **10 tentativas** para adivinhar qual é esse número.  
O número de pontos obtidos depende de quão rápido o jogador acerta:

- **1ª tentativa** → 10 pontos  
- **2ª tentativa** → 9 pontos  
- ...  
- **10ª tentativa** → 1 ponto  
- **Não acertou** → 0 pontos

A qualquer momento, o jogador pode digitar **`desistir`** para encerrar a rodada.

A cada **6 jogatinas**, os pontos acumulados são zerados.

---

## ▶️ Como Jogar

1. **Execute o script**:
   ```bash
   python nome_do_arquivo.py
   ```
2. **Siga as instruções no terminal**:
   - Digite um número entre 1 e 500  
   - Ou digite `desistir` para sair da partida atual

3. **Após cada partida**, o jogo pergunta se deseja continuar:
   - `s` → jogar novamente  
   - `n` → encerrar

---

## 💡 Exemplo de Execução

```text
Bem-vindo ao jogo de adivinhação!
Tente adivinhar o número entre 1 e 500.
Você tem 10 tentativas.
A qualquer momento, digite 'desistir' para encerrar o jogo.

Tentativa 1/10 - Digite seu palpite ou 'desistir': 250
Errado! O número secreto é menor que 250
...

Parabéns! Você acertou o número 123 em 5 tentativas e ganhou 6 pontos.
Pontos acumulados: 6
Deseja jogar novamente? (s/n):
```

---

## 🛠️ Requisitos

- Python 3.6 ou superior

---

## 📁 Organização do Código

- **`jogar()`** — Função principal de cada rodada  
- Loop principal permite múltiplas partidas  
- Lógica para zerar pontos a cada 6 partidas

---

## ✨ Funcionalidades Futuras (sugestões)

- Ranking de pontuações  
- Níveis de dificuldade  
- Interface gráfica (usando tkinter, por exemplo)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar!

---

## 👨‍💻 Autor

Feito por **Seu Nome Aqui** — contribuições são bem-vindas! 🤝
