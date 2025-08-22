K = float(input('Quantos km voce fez com o automovel: '))
D = float(input('Quando dias voce ficou com o veiculo: '))
KD = K * 0.15
DD = D * 60
soma = KD + DD
print('Voce fez em KM {}, e ficou com {} dias, entao voce vai ter que pagar ao total R$ {:.2f}'.format(K, D, soma))