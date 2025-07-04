import csv
from analise.sistema import SistemaAnaliseEngajamento

def formatar_tempo(segundos):
    segundos = int(segundos)
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg = segundos % 60
    if horas > 0:
        return f"{horas}h {minutos}min {seg}s"
    elif minutos > 0:
        return f"{minutos}min {seg}s"
    else:
        return f"{seg}s"

def listar_conteudos(sistema):
    return [v for _, v in sistema._arvore_conteudos.percurso_em_ordem()]

def listar_usuarios(sistema):
    return [v for _, v in sistema._arvore_usuarios.percurso_em_ordem()]

def listar_plataformas(sistema):
    return list(sistema._plataformas_registradas.values())

def listar_conteudos_por_tipo(sistema, tipo):
    return [c for c in listar_conteudos(sistema) if c.__class__.__name__.lower() == tipo.lower()]

def menu_metricas(sistema):
    while True:
        print("\n=== MENU DE MÉTRICAS ===")
        print("1 - Total de interações por conteúdo")
        print("2 - Contagem por tipo de interação por conteúdo")
        print("3 - Tempo total de consumo por conteúdo")
        print("4 - Média de tempo de consumo por conteúdo")
        print("5 - Listar comentários por conteúdo")
        print("6 - Top-5 conteúdos por interações")
        print("0 - Voltar")
        opc = input("Escolha uma métrica: ").strip()
        if opc == '0': break
        conteudos = listar_conteudos(sistema)
        if opc == '1':
            print("\nTotal de interações por conteúdo:")
            for c in conteudos:
                print(f"{c.nome}: {c.total_interacoes}")
        elif opc == '2':
            print("\nContagem por tipo de interação:")
            for c in conteudos:
                cont = c.calcular_contagem_por_tipo_interacao()
                print(f"\n{c.nome}:")
                for t,q in cont.items(): print(f"  {t}: {q}")
        elif opc == '3':
            print("\nTempo total de consumo:")
            for c in conteudos:
                print(f"{c.nome}: {formatar_tempo(c.tempo_total_consumo)}")
        elif opc == '4':
            print("\nTempo médio de consumo:")
            for c in conteudos:
                print(f"{c.nome}: {formatar_tempo(c.calcular_media_tempo_consumo())}")
        elif opc == '5':
            print("\nComentários por conteúdo:")
            for c in conteudos:
                coms = c.listar_comentarios()
                if coms:
                    print(f"\n{c.nome}:")
                    for txt in coms: print(f"  - {txt}")
        elif opc == '6':
            print("\nTop-5 conteúdos por interações:")
            top5 = sorted(conteudos, key=lambda x:x.total_interacoes, reverse=True)[:5]
            for c in top5: print(f"{c.nome}: {c.total_interacoes}")
        else:
            print("Opção inválida.")

def menu_relatorios_solicitados(sistema):
    while True:
        print("\n=== RELATÓRIOS SOLICITADOS ===")
        print("1 - Ranking de conteúdos mais consumidos")
        print("2 - Usuários por tempo total de consumo")
        print("3 - Plataformas por engajamento")
        print("4 - Conteúdos mais comentados")
        print("5 - Total de interações por tipo de conteúdo")
        print("6 - Tempo médio de consumo por plataforma")
        print("7 - Quantidade de comentários por conteúdo")
        print("0 - Voltar")
        opc = input("Escolha um relatório: ").strip()
        if opc == '0': break
        if opc == '1':
            print("\nRanking de conteúdos mais consumidos:")
            for c in sistema.gerar_top_conteudos_por_tempo():
                print(f"{c.nome}: {formatar_tempo(c.tempo_total_consumo)}")
        elif opc == '2':
            print("\nUsuários por tempo total de consumo:")
            for u in sistema.gerar_ranking_usuarios_por_tempo():
                print(f"ID {u.id}: {formatar_tempo(u.tempo_total_consumo)}")
        elif opc == '3':
            print("\nPlataformas por engajamento:")
            for p in sistema.gerar_ranking_plataformas_por_engajamento():
                print(f"{p.nome}: {p.calcular_total_interacoes_engajamento()} engajamentos")
        elif opc == '4':
            print("\nConteúdos mais comentados:")
            for c in sistema.gerar_ranking_conteudos_por_comentarios():
                print(f"{c.nome}: {c.calcular_contagem_por_tipo_interacao().get('comment',0)} comentários")
        elif opc == '5':
            print("\nTotal de interações por tipo de conteúdo:")
            for c in sistema.gerar_conteudos_por_total_interacoes():
                print(f"{c.nome}: {c.total_interacoes}")
        elif opc == '6':
            print("\nTempo médio de consumo por plataforma:")
            medias = sistema.calcular_tempo_medio_consumo_por_plataforma()
            for nome, m in medias.items(): print(f"{nome}: {formatar_tempo(m)}")
        elif opc == '7':
            print("\nQuantidade de comentários por conteúdo:")
            coms = sistema.contar_comentarios_por_conteudo()
            for nome, q in coms.items(): print(f"{nome}: {q} comentários")
        else:
            print("Opção inválida.")

def menu_principal(sistema):
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Métricas de Conteúdos")
        print("2 - Top-5 Usuários por Interações")
        print("3 - Listar Conteúdos")
        print("4 - Listar Plataformas")
        print("5 - Listar Podcasts")
        print("6 - Relatórios Solicitados")
        print("0 - Sair")
        opc = input("Escolha uma opção: ").strip()
        if opc == '0':
            print("Saindo...")
            break
        elif opc == '1': menu_metricas(sistema)
        elif opc == '2':
            print("\nTop-5 Usuários por Interações:")
            for u in sistema.gerar_top_usuarios_por_interacoes(5):
                print(f"ID {u.id}: {u.total_interacoes} interações")
        elif opc == '3':
            print("\nConteúdos cadastrados:")
            for c in listar_conteudos(sistema): print(f"ID {c.id}: {c.nome}")
        elif opc == '4':
            print("\nPlataformas cadastradas:")
            for p in listar_plataformas(sistema): print(f"{p.nome}: {p.total_interacoes} interações")
        elif opc == '5':
            print("\nPodcasts & Interações:")
            pods = listar_conteudos_por_tipo(sistema, 'podcast')
            if not pods: print("Nenhum podcast encontrado.")
            for p in pods:
                print(f"\n{p.nome}:")
                for t,q in p.calcular_contagem_por_tipo_interacao().items(): print(f"  {t}: {q}")
        elif opc == '6': menu_relatorios_solicitados(sistema)
        else: print("Opção inválida.")

def main():
    sistema = SistemaAnaliseEngajamento()
    sistema.carregar_interacoes_csv('interacoes_globo.csv')
    sistema.processar_interacoes_da_fila()
    menu_principal(sistema)

if __name__ == '__main__':
    main()
