from genetic import GA

NUM_GER = 3
TAM_POP = 10
PROB_MUT = 0.01

print(f'Rodando o modelo para {NUM_GER} geracoes {TAM_POP} de tamanho da populacao e {PROB_MUT} como prob de mutacao')
ga = GA(num_geracoes=NUM_GER, 
      tam_populacao=TAM_POP, 
      prob_mut=PROB_MUT)

ga.executa()
