"""
CONSTANTE = "Variáveis" que não vão mudar 
Muitas condições no mesmo IF (ruim)
    <- Contagem de complexidade (ruim)

"""
velocidade = 61
local_carro = 101

# Convesão para criar variáveis constantes no python 

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

# Resumindo as expressões em variáveis
vel_carro_pass_radar_1 = velocidade > RADAR_1
carr_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE )
carr_multado_radar_1 = carr_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')
if carr_passou_radar_1:
    print('carro passou em radar 1')
if carr_multado_radar_1:
    print('Carro multado em radar 1')