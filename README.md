# UFRPE - BACHARELADO SISTEMAS DE INFORMAÇÃO

## Disciplina: Projeto Interdisciplinar II
## Professor: Cícero Garrozi

## Alunos: José Alberto, Davi Gomes, Rivan Barroso e Kauan Henrique

Sistema desenvolvido para a primeira VA da disciplina Projeto Interdisciplinar II, com o objetivo de resolver o menor caminho em uma matriz de entregas, partindo do ponto inicial R, visitando todos os pontos de entrega representados por letras e retornando ao ponto inicial ao final do percurso.

O programa utiliza, propositalmente, uma abordagem de força bruta, explorando todas as possibilidades de percurso. A escolha dessa abordagem tem como finalidade compreender, na prática, os limites e os custos computacionais envolvidos na resolução de problemas desse tipo, especialmente à medida que o número de pontos aumenta.

Dessa forma, o projeto também busca demonstrar a importância do uso de heurísticas e técnicas de otimização, que podem reduzir significativamente o custo computacional ao evitar a necessidade de avaliar todas as possibilidades.

### Visão geral

O projeto lê uma matriz em formato JSON, valida as regras da entrada e calcula a rota com menor distância total usando a distância Manhattan entre os pontos. A lógica considera todas as permutações possíveis dos pontos de entrega e escolhe a sequência com menor custo.

### Operações

- Leitura de matrizes em JSON
- Validação da entrada
- Identificação do ponto inicial `R`
- Busca do menor caminho entre os pontos de entrega
- Cálculo da distância total do percurso
- Medição do tempo de resolução
- Exibição opcional de informações do sistema operacional e hardware

### Requisitos

- Python 3.10 ou superior
- `pip` para instalação de dependências

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/josealbertoraios13/FlyFood.git
cd FlyFood
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execução

O projeto usa o arquivo `matrix.json` como entrada padrão. Para executar:

```bash
python src/main.py
```

Ao rodar, o programa:

- carrega a matriz do arquivo `matrix.json`
- calcula a melhor rota
- imprime a rota final, a distância e o tempo de resolução
- pergunta se deseja mostrar informações do PC

### Formato da matriz

```json
[
  ["R", "0", "0", "A"],
  ["G", "0", "B", "0"],
  ["0", "C", "0", "0"],
  ["F", "0", "H", "D"],
  ["0", "E", "0", "0"],
  ["I", "0", "K", "J"],
  ["0", "L", "0", "0"]
]
```

### Exemplo de saída

```text
Rota: R ... A ... D ...
Distância: 32 dronômetros
Tempo de resolução: 0.12s
```

A saída pode variar conforme a matriz informada, mas o comportamento principal é sempre calcular a rota mais curta possível.

### Estrutura do projeto

```text
FlyFood/
├── matrix.json
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── model/
│   │   ├── __init__.py
│   │   ├── matrix_input.py
│   │   ├── matrix_response.py
│   │   ├── menor_caminho_response.py
│   │   └── ponto.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── service.py
│   └── utils/
│       ├── __init__.py
│       ├── caminho_utils.py
│       ├── info_utils.py
│       └── matrix_utils.py
└── .venv/
```

Este projeto está em desenvolvimento e pode ser adaptado de acordo com a necessidade do usuário ou da disciplina em que for utilizado.