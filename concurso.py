import json


def carregar_concursos(nome_arquivo):
    with open(nome_arquivo) as arquivo_json:
        dados_concursos = json.load(arquivo_json)
    return dados_concursos


def calcular_pontuacao_total(concurso):
    salario = int(concurso.get('salario', 0))
    beneficios = int(concurso.get('beneficios', 0))
    localizacao = int(concurso.get('localizacao', 0))
    concorrencia = int(concurso.get('concorrencia', 0))
    tempo = int(concurso.get('tempo', 0))
    disciplinas = int(concurso.get('disciplinas', 0))  # quanto menor o numero mais pontos
    dificuldade = int(concurso.get('dificuldade', 0))  # quanto mais pontos mais facil
    pontuacao_total = abs(salario + beneficios + localizacao - concorrencia - tempo - disciplinas - dificuldade)
    
    return pontuacao_total


def ordenar_por_pontuacao_total(concursos):
    return sorted(concursos, key=calcular_pontuacao_total, reverse=True)


def imprimir_concursos_ordenados(concursos):
    print("Concursos ordenados por pontuação total:")
    for concurso in concursos:
        nome_concurso = concurso.get('nome', 'Nome não encontrado')
        pontuacao_total = calcular_pontuacao_total(concurso)
        if isinstance(pontuacao_total, int):
            print(f"{nome_concurso}: {pontuacao_total}")
        else:
            print(f"{nome_concurso}: Não foi possível calcular a pontuação total")


if __name__ == '__main__':
    # Carregue os dados dos concursos do arquivo JSON
    dados_concursos = carregar_concursos('concursos.json')

    # Crie uma lista de concursos a partir dos dados carregados
    concursos = []
    for dados_concurso in dados_concursos:
        concurso = dict(dados_concurso)
        nome_concurso = concurso.pop('nome', 'Nome não encontrado')
        concurso['nome'] = nome_concurso
        concursos.append(concurso)

    # Ordene os concursos por pontuação total
    concursos_ordenados = ordenar_por_pontuacao_total(concursos)

    # Imprima o nome do concurso e sua pontuação total em ordem de prioridade
    imprimir_concursos_ordenados(concursos_ordenados)
