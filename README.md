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
## Exemplo de Saída

```text
=== MENU PRINCIPAL ===
1 – Métricas de Conteúdos
2 – Informações de Usuários
3 – Informações de Conteúdos
4 – Informações de Plataformas
5 – Listar Podcasts
0 – Sair
Escolha uma opção: 1

=== MENU DE MÉTRICAS ===
1 – Total de interações por conteúdo
2 – Contagem por tipo de interação
3 – Tempo total de visualização
4 – Tempo médio de visualização
5 – Listar comentários
6 – Top-5 conteúdos mais visualizados
```
---
### Autores
- André Carioca
- Diego Teixeira
- Marcelo Zilotti
- Mirra Bernardo
- Tales Honorio
- William Lopes