from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('José')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# Exemplos de associação
# Passando um objeto como atributo para outro objeto
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
