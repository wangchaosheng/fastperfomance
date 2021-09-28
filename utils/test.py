from fastperfomance.settings import BASE_DIR
import os



def run():
    os.system('cd %s/templates/;go run %s.go' % (BASE_DIR, 'main2'))
    time.sleep(3)


if __name__ == '__main__':
    run()