# -*- coding: utf-8 -*-
import schedule
import pandas as pd
import time
from datetime import datetime,timedelta
import threading
import os
import parmap
import requests

#URLs 
from src.configs.myproject_configs import redirect





def run_threaded(job_func):
    """
    Metodo que retorna o status de conexão com uma URL 
    :param tag: type=string
    :return: webId, type=string
    """
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def status():
    print(f"Teste Endpoint Status a cada 10 s. {datetime.now()} ") 
    try:
        health = requests.get(redirect.STATUS)
        print(health.json())
    except Exception as e:
        print(f"sem conexao. Erro {e}")




def executar():
    # schedule.every(5).minutes.do(run_threaded,function)
    # schedule.every(720).minutes.do(run_threaded, function)
    # schedule.every().day.at("07:00").do(run_threaded,function)
    schedule.every(1).minutes.do(run_threaded,status)
    #schedule.every(1).hours.do(run_threaded,function_off)
    # schedule.every(360).minutes.do(run_threaded, function)
    # schedule.every(360).minutes.do(run_threaded, function)
    # schedule.every(60).minutes.do(run_threaded, function)

    while True:
        schedule.run_pending()
        time.sleep(True)
    
    try:
        schedule.run(BlockingIOError=True)
    except KeyboardInterrupt:
        print("Agendador Interrompido Manualmente")

executar()

