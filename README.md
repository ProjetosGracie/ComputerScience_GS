<div align="center">

# 🏛️ Citizen Assist AI

**Assistente de terminal que orienta o cidadão sobre o tipo de atendimento (presencial ou online) usando lógica booleana.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Interface](https://img.shields.io/badge/interface-terminal-black)
![FIAP](https://img.shields.io/badge/FIAP-Global%20Solution%20GS26__2-ED145B)

</div>

---

## 📌 Sobre o projeto

O **Citizen Assist AI** é um programa em Python, executado no terminal, que simula um módulo de decisão para serviços públicos. A partir de quatro perguntas de **Sim/Não**, o sistema aplica uma regra lógica e informa se o cidadão pode seguir para o **agendamento presencial** ou **online**. Quando não pode, o programa explica quais requisitos não foram atendidos.

Projeto desenvolvido para a **Global Solution GS26_2** do curso de **Ciência da Computação – FIAP**.

> ⚠️ **Aviso:** este sistema tem caráter **demonstrativo e educacional**. Não representa um canal oficial do governo e não confirma a concessão de serviços ou direitos.

---

## 🧠 Regra de decisão

O cidadão pode ser encaminhado para:

- **Agendamento presencial**, quando o serviço **exige** atendimento presencial, a documentação está completa e há disponibilidade de agendamento.
- **Agendamento online**, quando o serviço **não exige** atendimento presencial, a documentação está completa, há disponibilidade de agendamento e o serviço permite atendimento online.

### Variáveis

| Variável | Pergunta feita ao usuário                     |
|:--------:|-----------------------------------------------|
| **A**    | O serviço exige atendimento presencial?       |
| **B**    | A documentação está completa?                 |
| **C**    | Existe disponibilidade de agendamento?        |
| **D**    | O serviço permite atendimento online?         |
| **X**    | Saída: pode prosseguir com o atendimento (1) ou não (0) |

### Expressões booleanas

| Forma                    | Expressão                                  |
|--------------------------|--------------------------------------------|
| Original                 | `X = A'·B·C·D + A·B·C·D'`                  |
| Canônica (soma de mintermos) | `X = Σm(7, 14)`                        |
| Simplificada             | `X = B·C·(A'·D + A·D')`                    |
| Com XOR                  | `X = B·C·(A ⊕ D)`                          |

A simplificação coloca `B·C` em evidência e reconhece que `A'·D + A·D'` é exatamente a operação **XOR** entre `A` e `D`. Em Python, isso vira:

```python
X = int(B and C and (A != D))
```

### Tabela-verdade

Somente duas das 16 combinações resultam em `X = 1`:

| A | B | C | D | X | Interpretação          |
|:-:|:-:|:-:|:-:|:-:|------------------------|
| 0 | 1 | 1 | 1 | **1** | Atendimento **online** (mintermo 7)      |
| 1 | 1 | 1 | 0 | **1** | Atendimento **presencial** (mintermo 14) |
| demais | | | | 0 | Não é possível prosseguir |

---

## ✨ Funcionalidades

O programa possui um menu interativo com as seguintes opções:

| Opção | Descrição |
|:-----:|-----------|
| **1** | **Realizar atendimento:** faz as 4 perguntas e exibe a orientação (online, presencial ou requisitos pendentes) |
| **2** | **Exibir expressão booleana:** mostra a forma original, canônica, simplificada e em XOR |
| **3** | **Exibir tabela-verdade:** imprime as 16 combinações geradas pela função simplificada |
| **4** | **Validar as 16 combinações:** compara a expressão original com a simplificada e informa erros |
| **0** | Encerrar o programa |

### Destaques técnicos

- ✅ **Validação de entrada** com `try/except`: aceita apenas `1` ou `0` e trata valores inválidos sem quebrar o programa.
- ✅ **Prova de equivalência**: a opção 4 confirma automaticamente que a expressão simplificada produz o mesmo resultado da original em todas as 16 combinações.
- ✅ **Feedback claro**: quando o resultado é negativo, o sistema lista o motivo (documentação incompleta, sem agendamento ou modalidade incompatível).

---

## 🗂️ Estrutura do código

| Função | Responsabilidade |
|--------|------------------|
| `perguntar(mensagem)` | Lê e valida uma resposta Sim/Não (1 ou 0) |
| `menu()` | Faz as quatro perguntas e retorna `A, B, C, D` |
| `regra_original(A, B, C, D)` | Implementa a expressão booleana original |
| `calcular(A, B, C, D)` | Implementa a expressão simplificada (com XOR) |
| `orientacao(A, B, C, D)` | Exibe o resultado e as orientações ao cidadão |
| `expressao_booleana()` | Mostra as formas da expressão |
| `tabela_verdade()` | Imprime a tabela-verdade completa |
| `validar()` | Compara original × simplificada nas 16 combinações |
| `main()` | Loop principal do menu |

---

## 🚀 Como executar

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/) instalado (não há bibliotecas externas).

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/ProjetosGracie/<nome-do-repositorio>.git

# 2. Entre na pasta do projeto
cd <nome-do-repositorio>

# 3. Execute o programa
python citizen_assist_ai.py
```

> Ajuste o nome do repositório e do arquivo `.py` conforme o seu projeto.

---

## 💻 Exemplos de uso

### Atendimento online

```text
O servico exige atendimento presencial?     -> 0 (Nao)
A documentacao esta completa?               -> 1 (Sim)
Existe disponibilidade de agendamento?      -> 1 (Sim)
O servico permite atendimento online?       -> 1 (Sim)

================================
     RESULTADO DO ATENDIMENTO
================================
Todas as condicoes foram atendidas.
Voce pode prosseguir para a proxima etapa.
Orientacao: atendimento online.
```

### Atendimento negado

```text
O servico exige atendimento presencial?     -> 1 (Sim)
A documentacao esta completa?               -> 0 (Nao)
Existe disponibilidade de agendamento?      -> 1 (Sim)
O servico permite atendimento online?       -> 0 (Nao)

================================
     RESULTADO DO ATENDIMENTO
================================
Nao foi possivel prosseguir com o atendimento.

Verifique os seguintes requisitos:
- A documentacao esta incompleta.
```

### Validação das combinações

```text
A B C D | original | simplificada | status
0 1 1 1 |    1     |      1       |  OK
1 1 1 0 |    1     |      1       |  OK
...
Total de combinacoes: 16
Total de erros: 0

Todas as combinacoes foram validadas!
```

---

## 🛠️ Tecnologias

- **Python 3**: linguagem principal
- **Lógica booleana**: tabela-verdade, mintermos, simplificação algébrica e XOR

---

## 👤 Autor

**Conrado Gracie**
Estudante de Ciência da Computação, FIAP

[![GitHub](https://img.shields.io/badge/GitHub-ProjetosGracie-181717?logo=github)](https://github.com/ProjetosGracie)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-conrado--gracie--0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/conrado-gracie-)

---

<div align="center">

Desenvolvido para a **Global Solution GS26_2** · FIAP · 2026

</div>