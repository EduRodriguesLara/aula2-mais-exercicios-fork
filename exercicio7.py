# ==============================================================================
# EXERCÍCIO - CLASSE BICICLETA
# ==============================================================================
# Crie uma estrutura para controlar a velocidade de uma bicicleta:
#
# 1. Classe Bicicleta:
#    - Atributos (__init__): modelo (str) e velocidade (int, iniciando em 0).
#    - Método pedalar(self): aumenta a velocidade em 5 e exibe:
#      "A bike [modelo] acelerou! Velocidade: X km/h"
#      A bike não pode passar de 60 km/h
#    - Método frear(self):
#      * Se a velocidade for maior que 0, diminui em 5 e exibe:
#        "Reduzindo... Velocidade: X km/h"
#      * Se a velocidade já for 0, exibe:
#        "A bicicleta já está totalmente parada!"
#    - Método radar_de_velocidade(self): exibe a velocidade atual.
#
# 2. Teste no Código:
#    - Instancie uma bicicleta: minha_bike = Bicicleta("Caloi")
#    - Chame o método pedalar() 2 vezes.
#    - Chame o método radar_de_velocidade().
#    - Chame o método frear() 3 vezes para validar a trava de velocidade zero.
# ==============================================================================