# 🧮 Calculadora Maluca

Este projeto é uma API REST desenvolvida em **Python** utilizando o framework **Flask**. O objetivo da aplicação é fornecer serviços de cálculos matemáticos e estatísticos (como desvio padrão e variância) através de diferentes módulos de calculadora, tudo estruturado seguindo princípios de **Clean Architecture** para garantir desacoplamento e facilidade de testes.

## 🚀 Tecnologias Utilizadas
- **Python 3.x**
- **Flask** (Servidor Web)
- **NumPy** (Processamento matemático performático)
- **Pytest** (Testes automatizados)
- **Clean Architecture** (Design Pattern)

## 📂 Estrutura do Projeto
O projeto segue uma divisão rigorosa de responsabilidades:

```
Calculadora-maluca/
├── src/
│   ├── calculators/   # Lógica de negócio (Cálculos 1, 2, 3 e 4)
│   ├── drivers/       # Interfaces com bibliotecas externas (ex: NumPy Handler)
│   ├── errors/        # Gerenciamento de erros e exceções HTTP
│   └── main/
│       ├── factories/ # Fábricas para instanciar rotas e casos de uso
│       ├── routes/    # Definição das rotas da API (Blueprints)
│       └── server/    # Configuração do App Flask
├── interface_raw.py   # Script para teste manual/integração
├── run.py             # Ponto de entrada da aplicação
└── ...
```

## ⚙️ Funcionalidades
A API expõe endpoints para diferentes tipos de operações matemáticas:

- **Calculadora 1:** Lógica básica de processamento.
- **Calculadora 2:** Processamento estatístico avançado utilizando drivers NumPy.
- **Calculadora 3:** Variações de fluxo e validação.
- **Calculadora 4:** Operações complexas (ex: médias, vetores).

## 🛠️ Instalação e Execução

### 1. Clone o repositório:
```bash
git clone https://github.com/Brunogodoy2911/Calculadora-maluca.git
cd Calculadora-maluca
```

### 2. Crie e ative um ambiente virtual (recomendado):
```bash
# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```
*(Caso não tenha o arquivo requirements, instale manualmente: `pip install flask numpy pytest`)*

### 4. Execute a aplicação:
```bash
python run.py
```
O servidor iniciará em `http://0.0.0.0:3000` (ou porta definida no seu `run.py`).

## 🧪 Como Testar

### Testes Automatizados
```bash
pytest
```

### Teste Manual (Interface Raw)
Você pode utilizar o script `interface_raw.py`:

```bash
python interface_raw.py
```

## 📝 Licença
Este projeto está sob a licença **MIT**. Sinta-se à vontade para contribuir!
