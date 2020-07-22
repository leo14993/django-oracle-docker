import threading
import schedule
import time


def run_threaded(job_func):
    """
    Metodo que retorna o status de conexão com uma URL 
    :param tag: type=string
    :return: webId, type=string
    """
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def executar(intervalo,unidade_tempo,funcao):

    schedule.every(intervalo).unidade.do(run_threaded,funcao)

    while True:
        schedule.run_pending()
        time.sleep(True)
    
    try:
        schedule.run(BlockingIOError=True)
    except KeyboardInterrupt:
        print("Agendador Interrompido Manualmente")

# executar()
