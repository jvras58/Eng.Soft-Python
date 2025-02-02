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
├── 📁 models/                  # Modelos de dados (classe Task e enums)
│   └── 🐍 task.py
├── 📁 config/                  # Configuração global (Singleton)
│   └── 🐍 config.py
├── 📁 decorators/              # Decorators para funcionalidades (ex.: logging)
│   └── 🐍 decorators.py
├── 📁 tests/                   # Testes unitários, de integração e E2E
│   ├── unit/
│   │   └── 🐍 test_models.py
└── 🐍 main.py                  # Ponto de entrada da aplicação
```

## Tecnologias Utilizadas

- **Python 3.12+**
- **Pytest:** Para execução dos testes.
- **Docker:** Para exemplificar containerização.


### 2. Criar e Ativar o Ambiente Virtual

```bash
uv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar Dependências

```bash
uv sync
```

### 4. Executar a Aplicação

```bash
uv run src/main.py
```

Você deverá ver a listagem inicial das tarefas, seguido da atualização do status e a listagem final.

## Executando os Testes

### 1. Testes Unitários

Verificar todos os testes juntos, basta executar:
```bash
pytest
```



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
