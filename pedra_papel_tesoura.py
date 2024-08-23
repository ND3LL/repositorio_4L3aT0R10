from random import choice

def exibir_placar(placar_player, placar_computador, nick):
	print('\n')
	print('Placar')
	print(f'{nick}: {placar_player')
	print(f'Computador: {placar_computador}')
	print('\n')
	
nick = input('Digite seu nickname >>> ')

computador = ['pedra', 'papel', 'tesoura']

rodadas = 0
placar_player =0
placar_computador =0

while rodadas <= 5:
	palpite = input('Pedra, papel ou tesoura? >>> ')
	palpite_computador = choice(computador)
	if palpite == 'pedra' and palpite_computador == 'tesoura' or palpite == 'tesoura' and palpite_computador == 'papel' or palpite == 'papel' and palpite_computador == 'pedra':
		rodadas += 1
		placar_player += 1
		print(f'{nick} ganhou a rodada!')
		exibir_placar(placar_player, placar_computador, nick)
		
	if palpite == 'pedra' and palpite_computador == 'papel' or palpite == 'papel' and palpite_computador == 'tesoura' or palpite == 'tesoura' and palpite_computador == 'pedra':
		print(f'{nick} perdeu a partida :/')
		placar_computador +=1
		rodadas += 1
		exibir_placar(placar_player, placar_computador, nick)
		
	if palpite == palpite_computador:
		print('Empate!')