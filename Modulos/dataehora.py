# Trabalhando com data e hora

from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import  relativedelta

"""Mostrando uma data qualquer"""
data = datetime(1995, 4, 23) # sempre na ordem: ano, mes, dia, hora, minutos, segundos, milisegundos
print(data)

# Passando uma data a partir de uma string

data_str = '08/08/1996' # DATA QUALQER PARA TESTE
data_format = '%d/%m/%Y' # Formato de data que estamos utilizando

# Aqui nos estamos padronizando o formato para o formato que o timedate utiliza yyyy-mm-dd
data2 = datetime.strptime(data_str,data_format)
print(data)

# Para mostrar a hora de agora
print(datetime.now(timezone('America/Sao_Paulo')))

# Utilizando o unix timestamp (que é a criação do unix até a data que nos passamos)
print(int(data.timestamp()))

# retornando a data pelo timestamp
print(datetime.fromtimestamp(data.timestamp()))

# Utilizando deltas
data = datetime.strptime('23/04/1995', data_format)
delta = data - data2 # A.K.A diferença de duas datas qualquer
print(delta)

# utilizando o método
delta = timedelta(days=10)
print(data2 + delta)

# Relative timedelta
print(data + relativedelta(days=30))
print(relativedelta(data, data2).days)

# Formatando datas
data = data.strftime(data_format)
print(data, type(data))
