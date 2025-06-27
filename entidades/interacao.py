class Interacao:
    """
    Representa uma interação de um usuário com um conteúdo em uma plataforma.

    Atributos:
        usuario (Usuario): objeto Usuário que realizou a interação.
        conteudo (Conteudo): objeto Conteúdo alvo da interação.
        plataforma (Plataforma): plataforma onde ocorreu a interação.
        tipo (str): tipo de interação ('view_start', 'like', 'share', 'comment', etc.).
        duracao (int): duração em segundos de visualização (apenas para 'view_start').
        comentario (str, opcional): texto do comentário, se houver.
    """
    def __init__(
        self,
        usuario,
        conteudo,
        plataforma,
        tipo: str,
        duracao: int = 0,
        comentario: str = None
    ):
        self.usuario = usuario
        self.conteudo = conteudo
        self.plataforma = plataforma
        self.tipo = tipo
        self.duracao = duracao
        self.comentario = comentario

    def __repr__(self):
        base = f"<Interacao tipo={self.tipo} usuario={self.usuario.id} conteudo={self.conteudo.id}"  
        if self.tipo == 'view_start':
            base += f" duracao={self.duracao}s"
        elif self.tipo == 'comment' and self.comentario:
            base += f" comentario='{self.comentario}'"
        base += ">"
        return base
