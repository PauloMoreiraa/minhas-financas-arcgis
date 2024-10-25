# 💸 Projeto Minhas Finanças - ETL para ArcGIS

## 📝 Descrição

Este projeto é uma aplicação para gerenciar e visualizar lançamentos financeiros utilizando o ArcGIS. O código contém funções para extrair dados de um arquivo JSON, transformar esses dados e carregá-los em um banco de dados geoespacial (GDB) no ArcGIS.

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o script.
- **ArcPy**: Biblioteca para automação de tarefas geoespaciais no ArcGIS.
- **JSON**: Formato de dados usado para a entrada de lançamentos financeiros.

## 🗃️ Estrutura do Projeto

```
minhasfinancas-arcgis/
├── scripts/
│   ├── main.py
│   ├── busca.py
│   ├── editor.py
│   └── update.py
└── json/
    └── lancamentos.json
```

## 🔧 Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://muralisti@dev.azure.com/muralisti/Programa%20de%20Est%C3%A1gio%20da%20Muralis/_git/pem-paulo-henrique-arcgis
   ```
2. Navegue até o diretório do projeto:
    ```bash
    cd pem-paulo-henrique-arcgis
    ```
3. Certifique-se de ter o ArcGIS e a biblioteca ArcPy instalados.

## 🔨 Configuração do Ambiente

- Configure o caminho do seu banco de dados geoespacial (GDB) e o arquivo JSON no código.
- Assegure-se de que as tabelas e campos correspondam às referências no código.

## 🧑‍💻 Uso

1. **Carregar Lançamentos**: O script `main.py` carrega dados de lançamentos financeiros do arquivo JSON especificado e os insere no banco de dados geoespacial.
2. **Buscar Dados**: O script `busca.py` permite buscar e exibir os dados de uma feature class no banco de dados.
3. **Editar Dados**: O script `editor.py` busca dados e permite a edição de registros com base em um critério especificado.
4. **Atualizar Dados**: O script `update.py` permite atualizar campos de registros na feature class.

### 🚨 Executar o Script
Execute os scripts no seu ambiente Python com suporte ao ArcPy:
```bash
python scripts/main.py
python scripts/busca.py
python scripts/editor.py
python scripts/update.py
```

## 📌 Funções

- **carregar_lancamentos(json_file)**: Carrega dados de lançamentos financeiros a partir de um arquivo JSON.
- **verificar_categoria(id_categoria, descricao)**: Verifica se uma categoria existe no banco de dados e a insere, se necessário.
- **extract_transform_data(json_file)**: Extrai e transforma os dados do arquivo JSON para o formato adequado ao banco de dados.
- **load_data_to_database(transformed_data, feature_class, fields)**: Carrega os dados transformados na feature class do ArcGIS.
- **search_data(feature_class, fields)**: Busca e exibe os dados da feature class.
- **editor.py**: Permite buscar e editar registros em uma feature class.
- **update.py**: Atualiza registros em uma feature class com base em critérios específicos.
