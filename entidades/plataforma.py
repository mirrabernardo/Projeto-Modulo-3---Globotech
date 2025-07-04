class Plataforma:
    """
    Representa uma plataforma de mídia onde ocorrem interações.

    Métricas disponíveis:
        - tempo_total_consumo: soma de durações de visualizações ('view_start')
        - total_interacoes: quantidade total de interações registradas
        - total_engajamento: soma de likes, shares e comments
        - contagens_por_tipo: dicionário com a contagem de cada tipo de interação
    Complexidades:
        registrar_interacao: O(1)
        calcular_total_interacoes_engajamento: O(n)
        calcular_contagem_por_tipo_interacao: O(n)
    """
    def __init__(self, nome: str):
        self.nome = nome
        self._interacoes = []
        self.tempo_total_consumo = 0.0
        self.total_interacoes = 0

    def registrar_interacao(self, interacao):
        # Adiciona uma interação à plataforma e atualiza métricas.
        self._interacoes.append(interacao)
        self.total_interacoes += 1
        if interacao.tipo == 'view_start':
            self.tempo_total_consumo += interacao.duracao

    def calcular_total_interacoes_engajamento(self) -> int:
        # Retorna a soma de likes, shares e comments.
        return sum(1 for i in self._interacoes if i.tipo in {'like', 'share', 'comment'})

    def calcular_contagem_por_tipo_interacao(self) -> dict:
        # Retorna um dicionário {tipo: contagem} para todos os tipos de interação. 
        contagens = {}
        for i in self._interacoes:
            contagens[i.tipo] = contagens.get(i.tipo, 0) + 1
        return contagens

    def __repr__(self):
        return (f"<Plataforma nome='{self.nome}' total_interacoes={self.total_interacoes} "
                f"tempo_total_consumo={self.tempo_total_consumo}s>")
