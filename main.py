from pastas import *
import easygui

# LENDO CSV

arquivo = easygui.fileopenbox(msg=None, title="Selecione o Arquivo CSV", default="*",filetypes=["*.csv"])
localfinal = easygui.diropenbox()

# CRIANDO PASTA PARA CADA NUMERO

criar_pasta_num(arquivo, localfinal)