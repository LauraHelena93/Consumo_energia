# Informações iniciais
# Autor: Laura Santos

nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))   
horas_uso = float(input("Digite o número de horas que o aparelho é usado por dia: "))       

# Cálculo do consumo de energia
consumo_diario = (potencia * horas_uso) / 1000 
# Convertendo para kWh
consumo_mensal = consumo_diario * 30 
# Considerando um mês de 30 dias  

# Valor do Kwh
valor_kwh = float(input("Digite o valor do kWh R$: "))

# Cálculo do custo mensal
custo_mensal = consumo_mensal * valor_kwh

# Exibindo o resultado
print(f"O consumo diário de energia do {nome_aparelho} é: {consumo_diario:.2f} kWh")
print(f"O consumo mensal de energia do {nome_aparelho} é: {consumo_mensal:.2f} kWh")
print(f"O custo mensal de energia do {nome_aparelho} é: R$ {custo_mensal:.2f}") 