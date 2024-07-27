import requests
import uuid
import shutil

from multiprocessing import Process
from multiprocessing import freeze_support, Process, Pool, Pipe, Queue

def run_main():
    """
    This Method runs the main method
    :return:
    """
    images = ['https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U',
              'https://i.picsum.photos/id/866/200/300.jpg?hmac=rcadCENKh4rD6MAp6V_ma-AyWv641M4iiOpe1RyFHeI',
              'https://i.picsum.photos/id/1041/200/300.jpg?grayscale&hmac=_p5B0MOtog0liIBvMDpM_3qmbzEyfpWw6hJHro2D-fM']

    processes_new = []
    
    # Creating Multiple Processes for each request
    for img in images:
        process = Process(target=save_image, args=(img,))
        processes_new.append(process)
        process.start()

    # Wait until the set of processes completes 
    for z in processes_new:
        z.join()
    

def save_image(url):
    """
    This method saves the images to local machine
    :param url:
    :return:
    """
    image_id = uuid.uuid4().hex
    req = requests.get(url, stream=True)
    with open(f'{image_id}.png', 'wb') as out_file:
        shutil.copyfileobj(req.raw, out_file)


if __name__ == '__main__':
    run_main()