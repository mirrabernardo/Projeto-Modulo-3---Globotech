import csv
from estruturas_dados.fila import Fila
from estruturas_dados.arvore_binaria_busca import ArvoreBinariaBusca
from entidades.plataforma import Plataforma
from entidades.conteudo import Conteudo
from entidades.usuario import Usuario
from entidades.interacao import Interacao

class SistemaAnaliseEngajamento:
    """
    Orquestra o fluxo de processamento de interações usando Fila e BSTs.

    Operações:
      - carregar_interacoes_csv: O(n)
      - processar_interacoes_da_fila: O(n log m)
      - geração de relatórios: O(k log k)
    """
    def __init__(self):
        self._fila_interacoes_brutas = Fila()
        self._arvore_conteudos = ArvoreBinariaBusca()
        self._arvore_usuarios = ArvoreBinariaBusca()
        self._plataformas_registradas = {}

    def carregar_interacoes_csv(self, caminho_arquivo: str):
        """Carrega linhas do CSV na fila (raw)."""
        with open(caminho_arquivo, newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                self._fila_interacoes_brutas.enfileirar(linha)

    def processar_interacoes_da_fila(self):
        """Processa cada item da fila, instanciando entidades e registrando interações."""
        while not self._fila_interacoes_brutas.esta_vazia():
            dados = self._fila_interacoes_brutas.desenfileirar()
            raw_content = dados.get('id_conteudo')
            raw_user = dados.get('id_usuario')
            if not raw_content or not raw_user:
                continue
            try:
                id_conteudo = int(raw_content)
                id_usuario = int(raw_user)
            except ValueError:
                continue
            nome_conteudo = dados.get('nome_conteudo') or f"conteudo_{id_conteudo}"

            # Plataforma
            nome_plataforma = dados.get('plataforma')
            if not nome_plataforma:
                continue
            plataforma = self._plataformas_registradas.get(nome_plataforma)
            if plataforma is None:
                plataforma = Plataforma(nome_plataforma)
                self._plataformas_registradas[nome_plataforma] = plataforma

            # Conteúdo (genérico)
            conteudo = self._arvore_conteudos.buscar(id_conteudo)
            if conteudo is None:
                conteudo = Conteudo(id_conteudo, nome_conteudo)
                self._arvore_conteudos.inserir(id_conteudo, conteudo)

            # Usuário
            usuario = self._arvore_usuarios.buscar(id_usuario)
            if usuario is None:
                usuario = Usuario(id_usuario)
                self._arvore_usuarios.inserir(id_usuario, usuario)

            # Interação
            tipo_int = dados.get('tipo_interacao')
            comentario = dados.get('comment_text')
            try:
                duracao = float(dados.get('watch_duration_seconds') or 0)
            except ValueError:
                duracao = 0.0

            inter = Interacao(usuario, conteudo, plataforma, tipo_int, duracao, comentario)

            # Registro
            conteudo.registrar_interacao(inter)
            usuario.registrar_interacao(inter)
            plataforma.registrar_interacao(inter)

    def gerar_top_conteudos_por_tempo(self, n: int = None):
        """Retorna top N conteúdos ordenados por tempo_total_consumo desc."""
        pares = self._arvore_conteudos.percurso_em_ordem()
        conteudos = [v for _, v in pares]
        ordenados = sorted(conteudos, key=lambda c: c.tempo_total_consumo, reverse=True)
        return ordenados[:n] if n else ordenados

    def gerar_top_usuarios_por_interacoes(self, n: int = None):
        """Retorna top N usuários ordenados por total_interacoes desc."""
        pares = self._arvore_usuarios.percurso_em_ordem()
        usuarios = [v for _, v in pares]
        ordenados = sorted(usuarios, key=lambda u: u.total_interacoes, reverse=True)
        return ordenados[:n] if n else ordenados

    def gerar_tempo_total_por_plataforma(self, n: int = None):
        """Retorna top N plataformas ordenadas por tempo_total_consumo desc."""
        plataformas = list(self._plataformas_registradas.values())
        ordenados = sorted(plataformas, key=lambda p: p.tempo_total_consumo, reverse=True)
        return ordenados[:n] if n else ordenados

    def obter_fila_interacoes(self):
        return self._fila_interacoes_brutas

    def limpar_fila_interacoes(self):
        """Esvazia a fila de interações."""
        while not self._fila_interacoes_brutas.esta_vazia():
            self._fila_interacoes_brutas.desenfileirar()

    def esta_fila_vazia(self) -> bool:
        return self._fila_interacoes_brutas.esta_vazia()

    def tamanho_fila(self) -> int:
        return len(self._fila_interacoes_brutas)
