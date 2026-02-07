def cor(msg, corTexto=0, corFundo=0):
    """
    Função que troca cores de fundo e de caracteres.\n

    -- Parâmetros --
    
    msg - Texto a ser colorido\n
    cor - 0 Preto, 1 Vermelho, 2 Verde, 3 Amarelo, 4 Roxo, 5 Magenta, 6 Ciano, 7 Branco.\n
    cor_fundo - 0 Preto, 1 Vermelho, 2 Verde, 3 Amarelo, 4 Roxo, 5 Magenta, 6 Ciano, 7 Branco.
    """
    limpar = '\033[m'

    coresTexto = ('\033[90m',
             '\033[91m',
             '\033[92m',
             '\033[93m',
             '\033[94m',
             '\033[95m',
             '\033[96m',
             '\033[97m')

    coresFundo = ('\033[100m',
             '\033[101m',
             '\033[102m',
             '\033[103m',
             '\033[104m',
             '\033[105m',
             '\033[106m',
             '\033[107m')

    return f"{coresTexto[corTexto]}{coresFundo[corFundo]}{msg}{limpar}"
