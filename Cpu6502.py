class Cpu6502:
    """Classe que emula o comportamento do processador MOS 6502

    Classe contendo os dados e as funções referentes ao processador MOS 6502, registradores e instrucões

    Attributes:
        pc: registrador contador de programas (program counter) 16 bits
        A: registrador A (acumulador) 8 bits
        X: registrador X 8 bits
        Y: registrador Y 8 bits
        instruction: dicionario que mapeia o codigo binario de uma instrução para seu respectivo nome(função)
        objC: dicionario que mapeia o formato da instrução e sua representação binaria ao número de argumentos da
            respectiva instrução

    """

    pc = 0x00
    A = 0x0
    X = 0x0
    Y = 0x0
    S = 0x0


    def ADC(self, ins):
        """Função que emula a instrução ADC

        Função que emula a instrução de soma com carrier ADC, com todos seus tipos de endereçamento

        Args:
            ins: binario da instrução

        """
        bk = 0b00011100 # bitmask para extração do formato de endereçamento
        add = (ins & bk) >> 2 # extraindo os bits referentes ao formato de endereçamento
        nx = self.objC['aaa'][add] # verificando na tabela de endereçamento quantos bytes são recebidos por argumento
        args = #pegar da memoria nx bytes
        if add == 0b000: # processar a memoria devidademente para cada tipo de endereçamento e fazer a soma (um if para cada endereçamento)
            pass
        elif add == 0b001:
            pass
        elif add == 0b010:
            pass
        elif add == 0b011:
            pass
        elif add == 0b100:
            pass
        elif add == 0b101:
            pass
        elif add == 0b110:
            pass
        elif add == 0b111:
            pass

        self.pc += nx # atualizando o PC para a posição depois dos argumentos

        if self.A > 0xFF: # verificação se houve overflow
            self.A &= 0xFF # apagando os bits que não pertencem ao registrador
            self.S |= 0b00000001 # settando o bit de carrier do registrador de Status


    instruction = {  # conjunto de instruções do 6502
        0b01100001: ADC,
        0b00100001: "AND",
        0b00000110: "ASL",
        0b10010000: "BCC",
        0b10110000: "BCS",
        0b11110000: "BEQ",
        0b00100100: "BIT",
        0b00110000: "BMI",
        0b11010000: "BNE",
        0b00010000: "BPL",
        0b00000000: "BRK",
        0b01010000: "BVC",
        0b01110000: "BVS",
        0b00011000: "CLC",
        0b11011000: "CLD",
        0b01011000: "CLI",
        0b10111000: "CLV",
        0b11000001: "CMP",
        0b11100000: "CPX",
        0b11000000: "CPY",
        0b11000110: "DEC",
        0b11001010: "DEX",
        0b10001000: "DEY",
        0b01000001: "EOR",
        0b11100110: "INC",
        0b11101000: "INX",
        0b11001000: "INY",
        0b01001100: "JPM",
        0b00100000: "JSR",
        0b10100001: "LDA",
        0b10100010: "LDX",
        0b10100000: "LDY",
        0b01001010: "LSR",
        0b11101010: "NOP",
        0b00000001: "ORA",
        0b01001000: "PHA",
        0b00001000: "PHP",
        0b01101000: "PLA",
        0b00101000: "PLP",
        0b00101010: "ROL",
        0b01101010: "ROR",
        0b01000000: "RTI",
        0b01100000: "RTS",
        0b11100001: "SBC",
        0b00111000: "SEC",
        0b11111000: "SED",
        0b01111000: "SEI",
        0b10000001: "STA",
        0b10000110: "STX",
        0b10000100: "STY",
        0b10101010: "TAX",
        0b10101000: "TAY",
        0b10111010: "TSX",
        0b10001010: "TXA",
        0b10011010: "TXA",
        0b10011000: "TYA"
    }

    objC = {  # tabela de endereçamento
        "aaa": {
            0b000: 1,  # pre indexado indireto
            0b001: 1,  # direto
            0b010: 1,  # imediato
            0b011: 2,  # direto extendido
            0b100: 1,  # pos indexado indireto
            0b101: 1,  # base page indexado
            0b110: 2,  # indexado absoluto X
            0b111: 2,  # indexado absoluto Y
        },

        "bb": {
            0b000: 1,  # direto
            0b001: 2,  # extendido direto
            0b010: 1,  # base page indexado
            0b011: 2,  # indexado absoluto
        },

        "bbb": {
            0b001: 1,  # direto
            0b010: 0,  # acumulador
            0b011: 2,  # direto extendido
            0b101: 1,  # base page indexado
            0b111: 2,  # indexado absoluto
        },

        "cc": {
            0b000: 1,  # imediato
            0b001: 1,  # direto
            0b011: 2,  # direto extendido
        },

        "ddd": {
            0b000: 1,  # imediato
            0b001: 1,  # direto
            0b011: 2,  # direto extendido
            0b101: 1,  # base page indexado
            0b111: 2,  # indexado absoluto
        },

        "x": {
            0b0: 1,  # direto
            0b1: 2,  # direto extendido
        },

        "y": {
            0b0: 2,  # direto extendido (label)
            0b1: 2,  # indireto (label)
        }
    }