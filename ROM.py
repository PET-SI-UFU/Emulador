class ROM:
    """Classe contendo as informações extraidas de uma ROM .nes

    Classe onde as informações extraidas da ROM .nes (normalmente no formato iNES) serão salvas para poderem ser lidas mais rapidamente durante o processo de emulação.
    A função readRom() retorna um objeto dessa classe com todas as informações devidamente preenchidas

    Attributes:
        verify: String 'nes' presete no cabeçalho da rom presente aqui apenas para verificação
        Npgr: variavel contendo o número de bancos de pgr-rom
        Nchr: variavel contendo o número de bancos de chr-rom
        cB1: primeiro byte de controle extraido da rom
        cb2: segundo byte de controle extraido da rom
        Nmb: número de bancos de memoria RAM presentes no cartucho
        bTrainer: variavel contendo o 512-Byte trainning, caso presente
        pgrRom: variavel contendo o pgr-ROM do cartucho
        chrRom: variavel contendo os bancos de chr-ROM (informações graficas)
    """
    verify = None
    Npgr = None
    Nchr = None
    cB1 = None
    cB2 = None
    Nmb = None
    bTrainer = None
    pgrRom = None
    chrRom = None

    def setV(self, v):
        '''Função criada para contornar problemas durante a leitura da rom

        Essa função foi criada na tentvim ativa de contornar alguns problemas durante a codificação da função de leitura da ROM e provavelmente será removida
        A função é apenas um setter para a string de verificação
        '''
        self.verify = v

