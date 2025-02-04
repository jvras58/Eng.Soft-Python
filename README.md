# Projeto de Gerenciamento de Tarefas.

Este projeto é um exemplo prático que integra conceitos avançados de engenharia de software e ciência de dados. Nele, você encontrará a implementação e utilização de:

- **Design Patterns:** Factory, Singleton, Adapter, Decorator, entre outros.
- **Padrões de Arquitetura:** Microservices, comunicação Event-driven, CQRS.
- **Princípios SOLID:** Organização de código modular e de fácil manutenção.
- **Técnicas de Deployment:** Canary, Blue-Green Deployment e containerização.
- **Pirâmide de Testes:** Testes Unitários, de Integração e End-to-End (E2E).

## Visão Geral

O objetivo do projeto é desenvolver um sistema simples de gerenciamento de tarefas (to-do list) que demonstre:
- Criação e manipulação de tarefas utilizando **Design Patterns**.
- Separação clara entre comandos e consultas (CQRS) e comunicação entre serviços (Event-driven).
- Aplicação dos **Princípios SOLID** para manter o código limpo, modular e extensível.

## Funcionalidades

- **Criação de Tarefas:** Utilizando uma *factory* para instanciar tarefas normais ou com flag de urgência.
- **Atualização de Status:** Comandos para marcar tarefas como concluídas.
- **Listagem de Tarefas:** Separação de comandos (escrita) e consultas (leitura) para exemplificar CQRS.
- **Notificações:** Simulação de envio de notificações através de um adapter, integrando módulos de forma desacoplada.

## Estrutura do Projeto

```plaintext
/
├── 📁 commands/                # Comandos para operações (criação, atualização)
│   └── 🐍 commands.py
├── 📁 queries/                 # Consultas (listagem de tarefas)
│   └── 🐍 queries.py
├── 📁 services/                # Lógica de negócio e simulação de microserviços
│   ├── 🐍 task_service.py
│   └── 🐍 notification_service.py
├── 📁 adapters/                # Adapters para integração com serviços externos
│   └── 🐍 adapter.py
├── 📁 api/                     # entrypoint da API da aplicação
│   ├── 📁 task/                # MVC
│   │   |── 🐍 controller.py
│   │   │── 🐍 router.py
│   │   └── 🐍 schemas.py
├── 📁 models/                  # Modelos de dados (classe Task e enums)
│   └── 🐍 task.py
├── 📁 config/                  # Configuração global (Singleton)
│   └── 🐍 config.py
├── 📁 decorators/              # Decorators para funcionalidades (ex.: logging)
│   └── 🐍 decorators.py
├── 📁 tests/                   # Testes unitários, de integração e E2E
│   ├── 📁 unit/
│   │   └── 🐍 test_task.py
│   ├── 📁 integration/
│   │   └── 🐍 test_task_integration.py
│   ├── 📁 e2e/
│   │   └── 🐍 test_task_flow.py
└── 🐍 main.py                  # Ponto de entrada da aplicação
```

## Tecnologias Utilizadas

- **Python 3.12+**
- **Pytest:** Para execução dos testes.
- **Docker:** Para exemplificar containerização.


## Princípios SOLID e Design Patterns

O código deste projeto foi estruturado para demonstrar:

- **SRP (Single Responsibility):** Cada classe ou módulo tem uma única responsabilidade.
- **OCP (Open/Closed):** O código está aberto a extensões sem a necessidade de modificações em classes existentes.
- **LSP (Liskov Substitution), ISP (Interface Segregation) e DIP (Dependency Inversion):** São praticados ao longo da implementação.
- **Design Patterns:**  
  - **Factory:** Criação de tarefas através de uma fábrica.
  - **Singleton:** Para a configuração global.
  - **Adapter:** Integração com serviços externos (notificações).
  - **Decorator:** Implementação de funcionalidades extras, como logging.


## Iniciando o Projeto:

### 1. Criar e Ativar o Ambiente Virtual

```bash
uv venv # uv já cria e ativa sozinho o ambiente...
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2. Instalar Dependências

```bash
uv sync
```

### 3. Aplicar as migrations

```bash
 alembic upgrade head  #<-- Aplique as migrations da pasta de versions
```


### 4. Executar a Aplicação

```bash
task run
```

### 5. Entrar no docs do Fastapi

```bash
http://localhost:8000/docs
```

### 4. Gere uma migrations nova:

```bash
 alembic revision --autogenerate -m "nome_da_migraçao"  #<-- Dê um nome para a migrations
```

## Executando os Testes

### 5. Testes

```bash
# Executar todos os testes
pytest

# Executar testes com cobertura
pytest --cov=src

# Executar testes específicos
pytest src/tests/unit/
pytest src/tests/integration/
pytest src/tests/e2e/
```

>Executar testes especificos:
```bash
pytest src/tests/pasta/arquivo.py::nome_do_teste
```
