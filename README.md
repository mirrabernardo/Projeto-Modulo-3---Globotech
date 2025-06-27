# Projeto Unificado - Fase 3: Análise de Engajamento de Mídias Globo com Estruturas de Dados

Este projeto implementa um sistema de análise de engajamento de mídias da Globo, utilizando princípios de algoritmos e estruturas de dados para otimizar o processamento e a recuperação de informações. A ênfase está no uso de fila para ingestão de dados e árvores de busca binária (BST) para gerenciamento de conteúdos e usuários.

## Funcionalidades

- **Carregamento de interações**  
  Leitura de um arquivo CSV (`interacoes_globo.csv`) em uma fila (FIFO) para processamento sequencial.

- **Estruturas de dados**  
  - **Fila**: armazenamento das linhas brutas do CSV para processamento contínuo.  
  - **BST para Conteúdos**: inserção, busca, remoção e percurso em ordem de objetos `Conteudo` identificados por `id_conteudo`.  
  - **BST para Usuários**: mesmas operações para objetos `Usuario` identificados por `id_usuario`.  

- **Entidades**  
  - `Conteudo` (e subclasses `Video`, `Podcast`, `Artigo`)  
  - `Usuario`  
  - `Plataforma`  
  - `Interacao`  

- **Geração de relatórios**  
  - Top N conteúdos por tempo total de consumo.  
  - Top N usuários por número de interações.  
  - Top N plataformas por tempo total de consumo.  

## Tecnologias e Dependências

- Python 3.8+  
- Módulo padrão `csv`  
- `collections.deque` para implementação de fila  

## Estrutura do Projeto

```plaintext
projeto_engajamento_fase_3/
│
├── analise/
│   └── sistema.py             # Classe principal de orquestração
│
├── entidades/
│   ├── conteudo.py            # Classes Conteudo, Video, Podcast, Artigo
│   ├── usuario.py             # Classe Usuario
│   ├── plataforma.py          # Classe Plataforma
│   └── interacao.py           # Classe Interacao
│
├── estruturas_dados/
│   ├── fila.py                # Implementação de Fila (deque)
│   └── arvore_binaria_busca.py # Implementação de BST
│
├── interacoes_globo.csv       # Dados de exemplo de interações
├── main.py                    # Script de execução e exibição de relatórios
└── README.md                  # Documentação do projeto
```

### Autores
- André Carioca
- Diego Teixeira
- Marcelo Zilotti
- Mirra Bernardo
- Tales Honorio
- William Lopes