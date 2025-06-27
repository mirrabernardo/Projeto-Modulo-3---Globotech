class Conteudo:
    """
    Representa um conteúdo (video, podcast ou artigo) e suas interações.
    Métricas disponíveis:
        - tempo_total_consumo: soma de durações de visualizações (view_start)
        - total_interacoes: contagem de todas as interações
        - total_engajamento: soma de likes, shares e comments
        - contagens_por_tipo: dicionário com quantidade por tipo de interação
    Complexidades:
        registrar_interacao: O(1)
        calcular_total_interacoes_engajamento: O(n)
        calcular_contagem_por_tipo_interacao: O(n)
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
            # acumula duração apenas para visualizações
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

    def __repr__(self):
        return f"<Conteudo id={self.id} nome='{self.nome}'>"


class Video(Conteudo):
    """Conteúdo do tipo Vídeo."""
    def __init__(self, id_conteudo: int, nome: str = None):
        super().__init__(id_conteudo, nome)


class Podcast(Conteudo):
    """Conteúdo do tipo Podcast."""
    def __init__(self, id_conteudo: int, nome: str = None):
        super().__init__(id_conteudo, nome)


class Artigo(Conteudo):
    """Conteúdo do tipo Artigo."""
    def __init__(self, id_conteudo: int, nome: str = None):
        super().__init__(id_conteudo, nome)
