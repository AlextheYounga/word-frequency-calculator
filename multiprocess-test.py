from multiprocessing import Pool

def process_image(name):
    print(name)
    <process>

if __name__ == '__main__':
    pool = Pool()
    pool.map(process_image, data_inputs