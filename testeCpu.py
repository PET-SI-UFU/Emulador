import sys

from ROM import *


def readRom(src):
    """Função que le uma rom no formato iNES e retorna o objeto correspondente da classe ROM

    A função recebe um caminho para a uma rom .nes, verifica sua compatibilidade, le o binario,e retorna um objeto ROM() com as informações extraidas dado arquivo.

    Args:
        src:
            caminho para a rom a ser lida

        Returns:
            A função retorna um objeto da classe ROM contendo o cabeçalho e todas as informações presentes na rom

    Raises:
        Exception:
            Arquivo fornecido não está no formato iNes (formato incompativel)
    """
    with open(src, 'rb') as f:
        data = f.read()
    rom = ROM()
    rom.verify = data[:3]
    if str(data[:3]).lower() != "b'nes'":  # verificar se a rom começa com 'NES'
        raise Exception("ROM incompativel")
    if data[3] != 0x1A:  # verificar se a rom tem 1A no byte 3
        raise Exception("ROM incompativel")

    rom.Npgr = data[4]
    rom.Nchr = data[5]
    rom.cB1 = data[6]
    rom.cB2 = data[7]
    rom.Nmb = data[8]

    cont = 16  # a variavel 'cont' será similar ao PC (program counter) e indicara em qual byte da rom paramos nossa leitura

    bm = 0b00000100  # Bitmask para extrair o bit 2 (terceiro bit de um byte)
    if (rom.cB1 & bm) >> 2 == 1:  # Se o bit 2 do primeiro byte de controle for 1 então lemos o 512-Byte trainer
        rom.bTrainer = data[cont:cont + 512]
        cont += 512

    rom.pgrRom = data[cont:cont + 16 * 1024 * rom.Npgr]  # Ler os bancos de pgr-rom cada um tem 16kB
    cont += 16 * 1024 * rom.Npgr

    rom.chrRom = data[cont:cont + 8 * 1024 * rom.Nchr]  # Ler os bancos de chr-rom da um tem 8kB
    return rom


try:
    # rom = readRom("roms/HelloWorld.nes")
    rom = readRom(sys.argv[1])
    print(rom.verify)
    '''
    print(rom.Npgr)
    print(rom.Nchr)
    print(rom.cB1)
    print(rom.cB2)
    print(rom.Nmb)
    print(rom.bTrainer)
    print(rom.pgrRom)
    print(rom.chrRom)
    '''

except Exception as e:
    print(e)
