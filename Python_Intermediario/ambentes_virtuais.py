"""
Ambientes virtuais em python (venv)
Um ambiente virtual carrega toda a sua instalação do python para uma pasta no caminho escolhido
Ao ativar um abiente virtual, a instalação do ambiente virtual será usada.
Venv é o módulo que vamos usar para criar ambientes virtuais.

Você pod dar o nome que preferir par um ambiente virtual, mas
os mais comuns são: venv env .venv .env

requirements.txt - tem todas as blibliotecas utilizadas no ambiente virtual

"""
# python -m venv venv -> comando para criar 2° venv é o nome

# .\venv\Scripts\activate - > comando para ativar o ambiente virtual

# deactivate -> desativa o ambiente virtual

# pip install - instalar
# pip uninstall - Desinstalar
# pip freeze - listar bibliotecas instaladas

"""
requiriments.txt -> armazena todos os pacotes instalados, é possível instalar todas as bibliotecas através desse arquivo.

"""

# pip freeze > requirements.txt -> cria o arquivo com as bibliotecas (toda vez que instalar um pacote atualizar)

#  pip install -r .\requirements.txt -> instala os arquivos do requirements.txt