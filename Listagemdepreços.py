# Listagem de Preço de alguns produtos Material Escolar de uma loja Casa do Papel

print('- ' *39)
print(f'{"LISTAGEM DE PREÇOS":^39}')
print('- ' *39)

produtos = ('Régua', 5.85,
            'Fichário', 35.99,
            'Agenda', 13.75,
            'Folha ofício', 19.00,
            'Lapis de cor Faber Castell', 45.00,
            'Giz de Cera', 11.99,
            'Lancheira', 20.00,
            'Canetinha Bic', 13.00,
            'Caneta Bic 4 cores', 9.00,
            'Apontador',12.00,
            'Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.00,
            'Caneta', 22.30,
            'Livros', 34.90)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('- ' *39)

# Renato Barbosa
