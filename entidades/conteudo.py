class Conteudo:
    """
    Representa um conteúdo (video, podcast ou artigo) e suas interações.

    Métricas disponíveis:
        - tempo_total_consumo: soma de durações de visualizações ('view_start')
        - total_interacoes: contagem de todas as interações
        - total_engajamento: soma de likes, shares e comments
        - contagens_por_tipo: dicionário com quantidade por tipo de interação
        - media de tempo de consumo: tempo_total_consumo / número de visualizações
        - comentários registrados

    Complexidades:
        registrar_interacao: O(1)
        calcular_total_interacoes_engajamento: O(n)
        calcular_contagem_por_tipo_interacao: O(n)
        calcular_media_tempo_consumo: O(n)
        listar_comentarios: O(n)
    """
    def __init__(self, id_conteudo: int, nome: str = None):
        self.id = id_conteudo
        self.nome = nome or f"conteudo_{id_conteudo}"
        self._interacoes = []
        self.tempo_total_consumo = 0.0
        self.total_interacoes = 0

    def registrar_interacao(self, interacao):
        """Adiciona uma interação ao conteúdo e atualiza métricas."""
        self._interacoes.append(interacao)
        self.total_interacoes += 1
        if interacao.tipo == "view_start":
            self.tempo_total_consumo += interacao.duracao

    def calcular_total_interacoes_engajamento(self) -> int:
        """Retorna a soma de likes, shares e comments."""
        return sum(1 for i in self._interacoes if i.tipo in {"like", "share", "comment"})

    def calcular_contagem_por_tipo_interacao(self) -> dict:
        """Retorna um dicionário {tipo: contagem} para todos os tipos de interação."""
        contagens = {}
        for i in self._interacoes:
            contagens[i.tipo] = contagens.get(i.tipo, 0) + 1
        return contagens

    def calcular_media_tempo_consumo(self) -> float:
        """Retorna o tempo médio de consumo (view_start) em segundos."""
        qtd_views = sum(1 for i in self._interacoes if i.tipo == "view_start")
        return (self.tempo_total_consumo / qtd_views) if qtd_views > 0 else 0.0

    def listar_comentarios(self) -> list:
        """Retorna uma lista de todos os textos de comentários."""
        return [i.comentario for i in self._interacoes if i.tipo == "comment" and i.comentario]

    def __repr__(self):
        return f"<Conteudo id={self.id} nome='{self.nome}'>"


class Video(Conteudo):
    """Conteúdo do tipo Vídeo."""
    pass


class Podcast(Conteudo):
    """Conteúdo do tipo Podcast."""
    pass


class Artigo(Conteudo):
    """Conteúdo do tipo Artigo."""
    pass
