import ctypes

def use_cdll():
    """
    cdll - вызов библиотек, которые используют стандарт cdecl.
    msvcrt - библиотека C (C:/windows/system32). 
    printf - функция этой библиотеки.
    """
    msvcrt = ctypes.cdll.msvcrt
    msvcrt.printf("qwe")
    msvcrt.close()

def test_union():
    """
    Предположим у нас есть библиотека, в которой описан формат данных barley_amount. 
    Он может представлять одно число тремя способами long, int и char.
    Тут мы инициализируем этот формат и представляем число 66 в нем.
    """
    class barley_amount(ctypes.Union):
        _fields_ = [
            ("barley_long", ctypes.c_long),
            ("barley_int", ctypes.c_int),
            ("barley_char", ctypes.c_char*8),
        ]
    
    my_barley = barley_amount(66)
    print("{0} {1} {2}".format(my_barley.barley_long, my_barley.barley_int, my_barley.barley_char))


"""
######## Описание регистров ########
EAX - accumulator. регистр аккумуляции. Используется для вычислений и для хранения результатов вызовов функций.
EDX - data. регистр данных. Дополнительное хранилище данных для EAX. Используется при сложных вычислениях.

ECX - counter. регистр счетчик. Используется в циклах.

ESI - source index. индекс источника. Хранит адресс входящего потока данных. (чтение данных)
EDI - destination index. индекс назначения. Хранит адресс с результатом обработки данных. (запись данных)

ESP - stack pointer
EBP - base pointer

EBX - дополнительное хранилище данных.
EIP - указывает на выполняемую в данный момент инструкцию.
"""

test_union()