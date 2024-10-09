#!/usr/bin/env python3

import datetime
import multiprocessing as mp
import random as rd

import psutil


def cal():
    r = rd.randint(99999999, 999999999999)
    b = r ** rd.random()
    return b


def work():
    while True:
        cal()


if __name__ == "__main__":
    cpu = mp.cpu_count()
    print(f"roasting pi with {cpu=}")

    for i in range(cpu):
        p = mp.Process(target=work)
        p.start()

    while True:
        # print cpu usage every 5 seconds
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"{t} cpu usage: {psutil.cpu_percent(interval=1)}",
            end="\r",
        )
