from typing import List

KB = 1024

class RAM():
    """ Classe que emula a memoria do console

    Classe contendo um vetor que representa a memoria do console e possui as funções de manipulão da mesma

    Attributes:
        memory_start_location: posição de inicio da memoria
        memory_end_location: posição final da memoria
        memory: lista onde a memoria sera armazenada

    """

    memory_start_location = 0x0  # Hexa posição 0
    memory_end_location = 0xFFFF  # Hexa posição 8byte

    def __init__(self):
        self.memory = [0]*KB*16

    def get_memory(self):
        return self.memory
