from analise.sistema import SistemaAnaliseEngajamento


def exibir_top_conteudos(conteudos):
    print("\nTop Conteúdos por Tempo de Consumo:")
    for i, c in enumerate(conteudos, 1):
        print(f"{i}. {c.nome} — {c.tempo_total_consumo:.2f} segundos")


def exibir_top_usuarios(usuarios):
    print("\nUsuários Mais Ativos:")
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. Usuário {u.id} — {u.total_interacoes} interações")


def exibir_top_plataformas(plataformas):
    print("\nPlataformas com Maior Tempo de Consumo:")
    for i, p in enumerate(plataformas, 1):
        print(f"{i}. {p.nome} — {p.tempo_total_consumo:.2f} segundos")


if __name__ == "__main__":
    sistema = SistemaAnaliseEngajamento()
    sistema.carregar_interacoes_csv("interacoes_globo.csv")
    sistema.processar_interacoes_da_fila()

    top_conteudos = sistema.gerar_top_conteudos_por_tempo(n=5)
    top_usuarios = sistema.gerar_top_usuarios_por_interacoes(n=5)
    top_plataformas = sistema.gerar_tempo_total_por_plataforma()

    exibir_top_conteudos(top_conteudos)
    exibir_top_usuarios(top_usuarios)
    exibir_top_plataformas(top_plataformas)
