from dataclasses import dataclass, field


# existem varias formas de configurar o dataclass, uma delas é adicionando parametros ao @dataclass
# @dataclass(frozen=True) transforma o objeto em uma "constante"
# não daria para editar os campos após o init, e faria nosso __post_init__ atual não funcionar
# outros exemplos seriam @dataclass(init=False, repr=False, kw_only=True, compare=False, slots=True) etc
@dataclass
class Person:
    firstname: str
    lastname: str
    active: bool = True
    addresses: list = field(default_factory=list, repr=False, compare=False)
    fullname: str = field(default='Missing', init=False, repr=False)
    # dataclasses não aceitam campos mutaveis como lists
    # por isso tivemos que usar field(default_factory=list)
    # field também pode ser usado para configurar outras propriedades da dataclass
    # propriedades com init=False não pode ser recebido como parametro do init
    # propriedades com repr=False faz não ser exibido no repr
    # propriedades com compare=False faz o campo ser ignorado no caso de comparações

    def __post_init__(self):
        self.fullname = f'{self.firstname} ' f'{self.lastname}'
