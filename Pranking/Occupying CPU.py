from multiprocessing import Process

import time

import setproctitle


def deadloop():
    while True:
        pass


def task(name):
    print("name=", name)
    deadloop()

    time.sleep(30)


if __name__ == "__main__":
    setproctitle.setproctitle('quark3')

    start = time.time()

    p1 = Process(target=task, args=("safly1",), name='quark service1')
    p2 = Process(target=task, args=("safly2",), name='quark service2')
    p3 = Process(target=task, args=("safly3",), name='quark service3')
    p4 = Process(target=task, args=("safly4",), name='quark service4')
    p5 = Process(target=task, args=("safly5",), name='quark service5')
    p6 = Process(target=task, args=("safly6",), name='quark service6')
    p7 = Process(target=task, args=("safly7",), name='quark service7')
    p8 = Process(target=task, args=("safly8",), name='quark service8')
    p9 = Process(target=task, args=("safly9",), name='quark service9')
    p10 = Process(target=task, args=("safly10",), name='quark service10')
    p11 = Process(target=task, args=("safly11",), name='quark service11')
    p12 = Process(target=task, args=("safly12",), name='quark service12')
    p13 = Process(target=task, args=("safly13",), name='quark service13')
    p14 = Process(target=task, args=("safly14",), name='quark service14')
    p15 = Process(target=task, args=("safly15",), name='quark service15')
    p16 = Process(target=task, args=("safly16",), name='quark service16')

    p17 = Process(target=task, args=("safly10",), name='quark service17')
    p18 = Process(target=task, args=("safly11",), name='quark service18')
    p19 = Process(target=task, args=("safly12",), name='quark service19')
    p20 = Process(target=task, args=("safly13",), name='quark service20')
    p21 = Process(target=task, args=("safly14",), name='quark service21')
    p22 = Process(target=task, args=("safly15",), name='quark service22')
    p23 = Process(target=task, args=("safly16",), name='quark service23')
    p24 = Process(target=task, args=("safly15",), name='quark service24')
    p25 = Process(target=task, args=("safly16",), name='quark service25')
    p26 = Process(target=task, args=("safly15",), name='quark service26')

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()
    p17.start()
    p18.start()
    p19.start()
    p20.start()
    p21.start()
    p22.start()
    p23.start()
    p24.start()
    p25.start()
    p26.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()
    p17.join()
    p18.join()
    p19.join()
    p20.join()
    p21.join()
    p22.join()
    p23.join()
    p24.join()
    p25.join()
    p26.join()

    print("main")

    print(p1.name)

    print(p2.name)

    print(p3.name)

    end = time.time()

    print(end - start)