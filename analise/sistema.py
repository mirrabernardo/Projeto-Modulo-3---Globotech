import csv
from estruturas_dados.fila import Fila
from estruturas_dados.arvore_binaria_busca import ArvoreBinariaBusca
from entidades.plataforma import Plataforma
from entidades.conteudo import Conteudo, Video, Podcast, Artigo
from entidades.usuario import Usuario
from entidades.interacao import Interacao

class SistemaAnaliseEngajamento:
    """
    Orquestra o fluxo de processamento de interações usando Fila e BSTs.

    Principais operações:
      - carregar_interacoes_csv: O(n)
      - processar_interacoes_da_fila: O(n log m)
      - relatórios diversos: O(k log k)
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
            raw_c = dados.get('id_conteudo')
            raw_u = dados.get('id_usuario')
            if not raw_c or not raw_u:
                continue
            try:
                id_conteudo = int(raw_c)
                id_usuario = int(raw_u)
            except ValueError:
                continue
            nome_c = dados.get('nome_conteudo') or f"conteudo_{id_conteudo}"
            # Plataforma
            nome_plat = dados.get('plataforma')
            if not nome_plat:
                continue
            plat = self._plataformas_registradas.get(nome_plat)
            if plat is None:
                plat = Plataforma(nome_plat)
                self._plataformas_registradas[nome_plat] = plat
            # Conteúdo
            conteudo = self._arvore_conteudos.buscar(id_conteudo)
            if conteudo is None:
                conteudo = Conteudo(id_conteudo, nome_c)
                self._arvore_conteudos.inserir(id_conteudo, conteudo)
            # Usuário
            usuario = self._arvore_usuarios.buscar(id_usuario)
            if usuario is None:
                usuario = Usuario(id_usuario)
                self._arvore_usuarios.inserir(id_usuario, usuario)
            # Interação
            tipo_int = dados.get('tipo_interacao')
            try:
                dur = float(dados.get('watch_duration_seconds') or 0)
            except ValueError:
                dur = 0.0
            comentario = dados.get('comment_text')
            inter = Interacao(usuario, conteudo, plat, tipo_int, dur, comentario)
            # Registro
            conteudo.registrar_interacao(inter)
            usuario.registrar_interacao(inter)
            plat.registrar_interacao(inter)

    # Relatórios conforme solicitação
    def gerar_top_conteudos_por_tempo(self, n=None):
        pares = self._arvore_conteudos.percurso_em_ordem()
        lista = [v for _, v in pares]
        orden = sorted(lista, key=lambda c: c.tempo_total_consumo, reverse=True)
        return orden[:n] if n else orden

    def gerar_top_usuarios_por_interacoes(self, n=None):
        pares = self._arvore_usuarios.percurso_em_ordem()
        lista = [v for _, v in pares]
        orden = sorted(lista, key=lambda u: u.total_interacoes, reverse=True)
        return orden[:n] if n else orden

    def gerar_ranking_usuarios_por_tempo(self, n=None):
        pares = self._arvore_usuarios.percurso_em_ordem()
        lista = [v for _, v in pares]
        orden = sorted(lista, key=lambda u: u.tempo_total_consumo, reverse=True)
        return orden[:n] if n else orden

    def gerar_ranking_plataformas_por_engajamento(self, n=None):
        lista = list(self._plataformas_registradas.values())
        orden = sorted(lista, key=lambda p: p.calcular_total_interacoes_engajamento(), reverse=True)
        return orden[:n] if n else orden

    def gerar_ranking_conteudos_por_comentarios(self, n=None):
        pares = self._arvore_conteudos.percurso_em_ordem()
        lista = [v for _, v in pares]
        orden = sorted(lista, key=lambda c: c.calcular_contagem_por_tipo_interacao().get('comment', 0), reverse=True)
        return orden[:n] if n else orden

    def gerar_conteudos_por_total_interacoes(self, n=None):
        pares = self._arvore_conteudos.percurso_em_ordem()
        lista = [v for _, v in pares]
        orden = sorted(lista, key=lambda c: c.total_interacoes, reverse=True)
        return orden[:n] if n else orden

    def calcular_tempo_medio_consumo_por_plataforma(self):
        medias = {}
        for p in self._plataformas_registradas.values():
            contagem = p.calcular_contagem_por_tipo_interacao()
            qtd_views = contagem.get('view_start', 0)
            medias[p.nome] = (p.tempo_total_consumo / qtd_views) if qtd_views else 0.0
        return medias

    def contar_comentarios_por_conteudo(self):
        pares = self._arvore_conteudos.percurso_em_ordem()
        return {v.nome: v.calcular_contagem_por_tipo_interacao().get('comment', 0) for _, v in pares}

    def obter_fila_interacoes(self):
        return self._fila_interacoes_brutas

    def limpar_fila_interacoes(self):
        while not self._fila_interacoes_brutas.esta_vazia():
            self._fila_interacoes_brutas.desenfileirar()

    def esta_fila_vazia(self):
        return self._fila_interacoes_brutas.esta_vazia()

    def tamanho_fila(self):
        return len(self._fila_interacoes_brutas)
