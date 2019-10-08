from datetime import (datetime, timedelta)
from constants import (MONGO_DEFAULT_DB, MONGO_HOST, MONGO_PASS, MONGO_PORT, MONGO_USER)
from faker import Faker
from find_manage import *
from interfaces import *
from insert_manage import *
from fake_profile import *
import random
from openpyxl import load_workbook
import logging

fake = Faker('pt_BR')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class excel:
    def __init__(self):
        self.ws = []

    def load_backlog(self):
        """ carrega um backlog em self.ws """
        try:
            print('insira o caminho para o arquivo de backlog: ')
            diretorio = input('')
            wb = load_workbook(diretorio)
            self.ws = wb.active
            return self.ws
        except Exception as log:
            print('Falha ao encontrar backlog')
            return None
    
    def read_cell(self, nrow, ncolumn):
        '''ler celula e retornar data'''
        try:
            data = self.ws.cell(nrow, ncolumn).value
            return data
        except:
            print('Por algum motivo não foi possivel ler linha')
            return None

    def max_row_column(self):
        """retorna o numero maximo de linhas e colunas"""
        try:
            rows = self.ws.max_row
            columns = self.ws.max_column
            return rows, columns
        except:
            print("não foi possivel calcular os valores maximos")
            return None


if __name__ == '__main__':
    e = excel()
    e.load_backlog()
    print(e.max_row_column())

