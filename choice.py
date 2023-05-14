import json


def load_choices(file):
    with open(file) as file_json:
        data_choices = json.load(file_json)
    return data_choices


def calc_points(choice):
    salario = int(choice.get('salario', 0))
    beneficios = int(choice.get('beneficios', 0))
    localizacao = int(choice.get('localizacao', 0))
    concorrencia = int(choice.get('concorrencia', 0))
    tempo = int(choice.get('tempo', 0))
    disciplinas = int(choice.get('disciplinas', 0))
    dificuldade = int(choice.get('dificuldade', 0))
    total_points = abs(salario + beneficios + localizacao - concorrencia - tempo - disciplinas - dificuldade)
    
    return total_points


def order_choices(choices):
    return sorted(choices, key=calc_points, reverse=True)


def print_choices_order(choices):
    print("Escolhas ordenados por pontuação total:")
    for choice in choices:
        choice_name = choice.get('nome', 'Nome não encontrado')
        total_points = calc_points(choice)
        if isinstance(total_points, int):
            print(f"{choice_name}: {total_points}")
        else:
            print(f"{choice_name}: Não foi possível calcular a pontuação total")


if __name__ == '__main__':
    # Carregue os dados dos choices do arquivo JSON
    data_choices = load_choices('choices.json')

    # Crie uma lista de choices a partir dos dados carregados
    choices = []
    for data_choice in data_choices:
        choice = dict(data_choice)
        choice_name = choice.pop('nome', 'Nome não encontrado')
        choice['nome'] = choice_name
        choices.append(choice)

    # Ordene os choices por pontuação total
    choices_order = order_choices(choices)

    # Imprima o nome do choice e sua pontuação total em ordem de prioridade
    print_choices_order(choices_order)
