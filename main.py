import csv
from analise.sistema import SistemaAnaliseEngajamento

def formatar_tempo(segundos):
    """
    Converte um valor em segundos para uma string legível no formato:
    'Xh Ymin Zs', 'Ymin Zs' ou 'Zs', dependendo do valor.
    """
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
    """Retorna todos os objetos Conteudo do sistema."""
    return [conteudo for _, conteudo in sistema._arvore_conteudos.percurso_em_ordem()]

def listar_usuarios(sistema):
    """Retorna todos os objetos Usuario do sistema."""
    return [usuario for _, usuario in sistema._arvore_usuarios.percurso_em_ordem()]

def listar_plataformas(sistema):
    """Retorna todas as Plataformas registradas no sistema."""
    return list(sistema._plataformas_registradas.values())

def listar_conteudos_por_tipo(sistema, tipo_classe):
    """
    Filtra conteúdos cuja classe seja igual ao tipo_classe (por ex. 'Podcast').
    Espera que o nome da classe dos objetos seja exato.
    """
    todos = listar_conteudos(sistema)
    return [c for c in todos if c.__class__.__name__.lower() == tipo_classe.lower()]

def menu_metricas(sistema):
    """
    Submenu de métricas de engajamento de conteúdo.
    """
    while True:
        print("\n=== MENU DE MÉTRICAS ===")
        print("1 - Total de interações por conteúdo")
        print("2 - Contagem por tipo de interação para cada conteúdo")
        print("3 - Tempo total de visualização por conteúdo")
        print("4 - Média de tempo de visualização por conteúdo")
        print("5 - Listar comentários por conteúdo")
        print("6 - Top-5 conteúdos por total de interações")
        print("0 - Voltar")

        opcao = input("Escolha uma métrica: ").strip()

        if opcao == "0":
            break

        all_conteudos = listar_conteudos(sistema)

        # 1) Total de interações por conteúdo
        if opcao == "1":
            print("\n=== TOTAL DE INTERAÇÕES POR CONTEÚDO ===")
            for c in all_conteudos:
                print(f"{c.nome} | {c.total_interacoes} interações")

        # 2) Contagem por tipo
        elif opcao == "2":
            print("\n=== CONTAGEM POR TIPO DE INTERAÇÃO ===")
            for c in all_conteudos:
                contagem = c.calcular_contagem_por_tipo_interacao()
                print(f"\n{c.nome}:")
                for tipo, qtd in contagem.items():
                    print(f"  {tipo}: {qtd}")

        # 3) Tempo total de visualização
        elif opcao == "3":
            print("\n=== TEMPO TOTAL DE CONSUMO POR CONTEÚDO ===")
            for c in all_conteudos:
                print(f"{c.nome} | {formatar_tempo(c.tempo_total_consumo)}")

        # 4) Média de tempo de visualização
        elif opcao == "4":
            print("\n=== TEMPO MÉDIO DE CONSUMO POR CONTEÚDO ===")
            for c in all_conteudos:
                media = c.calcular_media_tempo_consumo()
                print(f"{c.nome} | {formatar_tempo(media)}")

        # 5) Listar comentários
        elif opcao == "5":
            print("\n=== COMENTÁRIOS POR CONTEÚDO ===")
            for c in all_conteudos:
                comentarios = c.listar_comentarios()
                if comentarios:
                    print(f"\n{c.nome}:")
                    for texto in comentarios:
                        print(f"  - {texto}")

        # 6) Top-5 conteúdos
        elif opcao == "6":
            print("\n=== TOP-5 CONTEÚDOS POR INTERAÇÕES ===")
            top5 = sorted(
                all_conteudos,
                key=lambda c: c.total_interacoes,
                reverse=True
            )[:5]
            for c in top5:
                print(f"{c.nome} | {c.total_interacoes} interações")

        else:
            print("Opção inválida. Tente novamente.")

def menu_principal(sistema):
    """
    Menu principal com todas as funcionalidades.
    """
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Métricas de Conteúdos")
        print("2 - Informações de Usuários")
        print("3 - Listar Conteúdos")
        print("4 - Listar Plataformas")
        print("5 - Listar Podcasts")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Saindo...")
            break
        # Abre o Menu de Métricas    
        elif opcao == "1":
            menu_metricas(sistema)

        # Mostra só os 5 usuários com mais interações
        elif opcao == "2":
            print("\n=== TOP-5 USUÁRIOS POR INTERAÇÕES ===")
            usuarios = sorted(
                listar_usuarios(sistema),
                key=lambda u: u.total_interacoes,
                reverse=True
            )[:5]
            for u in usuarios:
                print(f"ID: {u.id} | Interações: {u.total_interacoes}")
        
        # Mostra todos os conteúdos
        elif opcao == "3":
            print("\n=== CONTEÚDOS CADASTRADOS ===")
            for c in listar_conteudos(sistema):
                print(f"ID: {c.id} | Nome: {c.nome}")
        
        # Mostra todas as plataformas
        elif opcao == "4":
            print("\n=== PLATAFORMAS CADASTRADAS ===")
            for p in listar_plataformas(sistema):
                print(f"Nome: {p.nome} | Interações: {p.total_interacoes}")
        
        # Nova opção: listar podcasts com tipos de interação
        elif opcao == "5":
            print("\n=== PODCASTS & INTERAÇÕES ===")
            podcasts = listar_conteudos_por_tipo(sistema, "podcast")
            if not podcasts:
                print("Nenhum podcast encontrado.")
            else:
                for p in podcasts:
                    print(f"\nPodcast: {p.nome}")
                    contagem = p.calcular_contagem_por_tipo_interacao()
                    for tipo, qtd in contagem.items():
                        print(f"  {tipo}: {qtd}")

        else:
            print("Opção inválida. Tente novamente.")

def main():
    sistema = SistemaAnaliseEngajamento()
    sistema.carregar_interacoes_csv("interacoes_globo.csv")
    sistema.processar_interacoes_da_fila()
    menu_principal(sistema)

if __name__ == "__main__":
    main()