import pandas as pd
from meza import io, process as pr, convert as cv
from io import open
records = io.read('/home/ariviere/Documents/Bassin_Seine/Temperature/Temperature_data/Temper_Data_2020.mdb')
print(records)