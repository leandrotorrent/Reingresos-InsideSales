import pandas as pd
import csv
from datetime import datetime


fechaActual = datetime.today()
listaTotalCanceladas = []
listaTotalBO = []
cliente= ""
contadorClientes = 0
contadorOrdenes = 0
contadorDesignaciones = 0
designacionesCliente = []
listaDesignacionCliente = []
orden = ""
designacion = ""
listaReingresos = []

#read_file = pd.read_excel (r'C:\Users\wg8468\OneDrive - SKF\Documentos\LAM Graduate Program\insidesales\LAT CAN 2 con precio v5 (Cancelada con Precios).xlsx')
#read_file.to_csv (r'C:\Users\wg8468\OneDrive - SKF\Documentos\LAM Graduate Program\insidesales\canceladas.csv', index = None, header=True)

#read_file = pd.read_excel (r'C:\Users\wg8468\OneDrive - SKF\Documentos\LAM Graduate Program\insidesales\bo.xlsx')
#read_file.to_csv (r'C:\Users\wg8468\OneDrive - SKF\Documentos\LAM Graduate Program\insidesales\bo.csv', index = None, header=True)

        
with open(r'C:\Users\wg8468\OneDrive - SKF\Documentos\LAM Graduate Program\insidesales\canceladas.csv') as canceladascsv:
    reader = csv.DictReader(canceladascsv)
    for row in reader:
        if row['""LOTE'] == "" :
            if (row['""USER']  != "RW1938" and row['""USER']  !="GV3367" and row['""USER']  !="TM5582" and row['""USER']  !="BC0676" and row['""USER']  !="UP7547" and row['""USER']  !="GR8643"):
                #print(row)
                listaTotalCanceladas.append([row['""CUSTOMER'], row['""Order'], row['""Designation'], int(row['""QTY 1']),
                                  row['""USER'], row['""LOTE'], datetime.strptime(row['""Cancelation Date'], '%Y%m%d')])
                
with open(r'C:\Users\wg8468\OneDrive - SKF\Documentos\LAM Graduate Program\insidesales\bo.csv', encoding="utf8") as bocsv:
    reader = csv.DictReader(bocsv)
    for row in reader:
        #print(row)
        if row['""CLIENTE""'] != "":
            listaTotalBO.append([row['""CLIENTE""'], row['""ORDEN SKF""'], row['""DESIGNACION""'], int(row['""CANTIDAD""'][:-2]), datetime.strptime(row['""REQ DATE""'][:-2], '%Y%m%d')] )
                

listaTotalCanceladas = sorted(listaTotalCanceladas, key=lambda x:x[0])


cliente = listaTotalCanceladas[contadorClientes][0]
contador = 0

#canceladaEjemplo = ['AGEN DOMIN', '22D0000305', '22316 E/C3', 4, 'O690', '', datetime.strptime('20220523', '%Y%m%d')]
#canceladaEjemplo = ['CEMASA', '21D0005165', 'FY 2.1/2 TF', 3, 'O690', '', datetime.strptime('20220530', '%Y%m%d')]
#canceladaEjemplo = ['CEMASA', '21D0007308', '1209 EKTN9/C3', 3, 'O690', '', datetime.strptime('20220530', '%Y%m%d')]
canceladaEjemplo = ['SR BEARINGS', '22D0004508', 'VKT 1000', 10, 'COHLT', '', datetime.strptime('20220525', '%Y%m%d')]

for cancelada in listaTotalCanceladas:
    for ingreso in listaTotalBO:
    #if (canceladaEjemplo[0] == ingreso[0] and canceladaEjemplo[2] == ingreso[2] and canceladaEjemplo[3] >= ingreso[3] and canceladaEjemplo[6] >= ingreso[4]):
    #if (canceladaEjemplo[0] == ingreso[0] and ingreso[4] >= canceladaEjemplo[6] and canceladaEjemplo[2] == ingreso[2] and canceladaEjemplo[3] >= ingreso[3]):
    #if (canceladaEjemplo[0] == ingreso[0] and ingreso[4] >= canceladaEjemplo[6] and canceladaEjemplo[2] == ingreso[2]): 
        if (cancelada[0] == ingreso[0] and ingreso[4] >= cancelada[6] and cancelada[2] == ingreso[2]): 
            listaReingresos.append(ingreso)

     
my_df = pd.DataFrame(listaReingresos)
my_df.to_csv('my_csv.csv', index=False, header=["Cliente", "Orden", "Designación", "Cantidad", "Fecha de Reingreso"])
