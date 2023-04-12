from math import inf
import json

FATURAMENTO_JSON = "dados.json"

# faturamento_mensal = [10, 5, 3, 6, 17, 8]

def get_faturamento_average(faturamento_mensal):
    sum = 0

    for i in range(0, len(faturamento_mensal)):
        sum += faturamento_mensal[i]["valor"]
    
    return sum/len(faturamento_mensal)

def clean_faturamento_mensal(faturamento_mensal):

    cleaned_faturamento_mensal = []

    for i in range(0, len(faturamento_mensal)):
        if faturamento_mensal[i]["valor"] != 0.0:
            cleaned_faturamento_mensal.append(faturamento_mensal[i])

        
    return cleaned_faturamento_mensal

def get_faturamento_mensal():
    with open(FATURAMENTO_JSON) as faturamento:
        faturamento_mensal = json.load(faturamento)
    return faturamento_mensal

def menor_faturamento_mensal(faturamento_mensal):
    menor = inf
    pior_dia = None
    for i in range(0,len(faturamento_mensal)):
        if faturamento_mensal[i]["valor"] < menor:
            menor = faturamento_mensal[i]["valor"]
            pior_dia = faturamento_mensal[i]
    
    return pior_dia

def maior_faturamento_mensal(faturamento_mensal):
    maior = -inf
    melhor_dia = None

    for i in range(0,len(faturamento_mensal)):
        if faturamento_mensal[i]["valor"] > maior:
            maior = faturamento_mensal[i]["valor"]
            melhor_dia = faturamento_mensal[i]

    return melhor_dia

def get_days_above_average(faturamento_mensal):
    media_faturamento = get_faturamento_average(faturamento_mensal)

    count = 0

    for faturamento in faturamento_mensal:
        if faturamento["valor"] > media_faturamento:
            count += 1
    
    return count

def jprint(json_struct):
    json_struct = json.dumps(json_struct, indent= 4)
    print(json_struct)

if __name__ == "__main__":
    faturamento_mensal = get_faturamento_mensal()
    # jprint(faturamento_mensal)

    faturamento_mensal = clean_faturamento_mensal(faturamento_mensal)
    # jprint(faturamento_mensal)

    menor_faturamento, maior_faturamento = menor_faturamento_mensal(faturamento_mensal), maior_faturamento_mensal(faturamento_mensal)

    media_de_faturamento = get_faturamento_average(faturamento_mensal)

    dias_acima_da_media = get_days_above_average(faturamento_mensal)

    print(f"""
    Dia de Menor Faturamento: {menor_faturamento["dia"]}\tFaturamento: {round(menor_faturamento["valor"], 2)}
    Dia de Maior Faturamento: {maior_faturamento["dia"]}\tFaturamento: {round(maior_faturamento["valor"], 2)}

    Dias acima da Média: {dias_acima_da_media}\t Media de Faturamento: {round(media_de_faturamento, 2)}
    """)