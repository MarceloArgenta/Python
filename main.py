import os

#Abre o arquivo e lê linha por linha
with open('cozinha.csv') as file:
    file_content = file.readlines()
    #print(file_content)
#Define o cabeçalho
header = file_content[0]

#Configura o cabeçalho
def cabecalho(line0):
    return header.strip().split(',')

#configura os valores de cada linha
def valores(lineX):
    values = []
    for item in lineX.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values

#cria um dicionário com os cabeçalhos e valores
def dict_de_items(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result


# Abre um arquivo e faz todas as função acima e coloca todos os dados em um único dicionário
def read_csv(path):
    result = []
    #open the file in read mode
    with open(path,'r') as f:
        #Get a list of lines
        lines = f.readlines()
        #parse the header
        headers = cabecalho(lines[0])
        #Loop over the remaining lines
        for data_line in lines[1:]:
            #parse the values
            values = valores(data_line)
            #create a dictionary using values and headers
            item_dict = dict_de_items(values, headers)
            #Add the dicionary to the result
            result.append(item_dict)
    return result

file_open = read_csv('cozinha.csv')

#Função que será aplicada, nesse caso quantidade*custo
def total(quantidade, custo):
    valor_total = quantidade * custo
    return valor_total


#Adicionar um item no cabeçalho que será o valor total e aplicar a função "Total"
for line in file_open:
    line['Total'] = total(line['quantidade'], line['custo'])

#print(file_open)
#criar/sobrescrever um arquivo com os resultados


def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return

        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")
    print("Arquivo criado/modificado com sucesso!")


write_csv(file_open, './arquivoTratado.csv')
print(os.listdir('.'))
