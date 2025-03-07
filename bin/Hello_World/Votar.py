idade = int(input("Quantos anos você tem: "))
if idade < 16:
    print("Você não pode votar!")
elif 16 <= idade < 18 or idade > 65:
    print("Seu voto é opcional!")
else:
    print("Seu voto é obrigatorio")