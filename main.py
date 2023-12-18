# from genetic import GA

# NUM_GER = 3
# TAM_POP = 10
# PROB_MUT = 0.01

# print(f'Rodando o modelo para {NUM_GER} geracoes {TAM_POP} de tamanho da populacao e {PROB_MUT} como prob de mutacao')
# ga = GA(num_geracoes=NUM_GER, 
#       tam_populacao=TAM_POP, 
#       prob_mut=PROB_MUT)

# ga.executa()

from main_ga import main

# alpha = input('Valor de alpha: ')
# beta = input('Valor de beta: ')


#main(0.1, 0.75)
main(0.15, 0.8)
main(0.2, 0.85)
main(0.25, 0.9)
main(0.30, 0.95)
main(0.35, 1.0)
main(0.4, 0.75)
main(0.45, 0.75)
main(0.5, 0.75)
main(0.55, 0.75)
main(0.6, 0.75)
# nOVOS
main(0.001, 0.75)
main(0.005, 0.75)
main(0.01, 0.75)



