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
  - Ranking de conteúdos mais consumidos (ordenados pelo maior tempo total de consumo)  
  - Ranking de usuários por tempo total de consumo  
  - Ranking de plataformas por engajamento (likes, shares e comentários)  
  - Conteúdos mais comentados  
  - Total de interações por tipo de conteúdo  
  - Tempo médio de consumo por plataforma  
  - Quantidade de comentários por conteúdo


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
├── diagrama.mermaid           # Diagrama com representação do sistema
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
6 - Relatórios Solicitados
0 – Sair
Escolha uma opção: 6

=== RELATÓRIOS SOLICITADOS ===
1 - Ranking de conteúdos mais consumidos
2 - Usuários por tempo total de consumo
3 - Plataformas por engajamento
4 - Conteúdos mais comentados
5 - Total de interações por tipo de conteúdo
6 - Tempo médio de consumo por plataforma
7 - Quantidade de comentários por conteúdo
0 - Voltar
```
---
### Autores
- André Carioca
- Diego Teixeira
- Marcelo Zilotti
- Mirra Bernardo
- Tales Honorio
- William Lopes