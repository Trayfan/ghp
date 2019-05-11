#coding: utf8
from ctypes import *
from my_debugger_defines import *

import sys
import time

kernel32 = windll.kernel32  # вызываем библиотеку windows kernel32

class debugger():
    def __init__(self):
        pass

    def load(self, path_to_exe):
        # dwCreation - определяет как процесс будет создан.
        # CREATE_NEW_CONSOLE - GUI
        # DEBUG_PROCESS - debugger
        dwCreation = DEBUG_PROCESS

        # инициализируем необходимые структуры
        lpStartupInfo = STARTUPINFOA()
        lpProcessInformation = PROCESS_INFORMATION()

        # настраиваем запуск
        lpStartupInfo.dwFlags = 0x00000001
        lpStartupInfo.wShowWindow = 0

        lpStartupInfo.cb = sizeof(lpStartupInfo)

        if kernel32.CreateProcessA( path_to_exe,
                                    None,
                                    None,
                                    None,
                                    None,
                                    dwCreation,
                                    None,
                                    None,
                                    byref(lpStartupInfo),
                                    byref(lpProcessInformation)):
            print("Процесс запущен!")
            print("ID процесса: {0}".format(lpProcessInformation.dwProcessId))

        else:
            print("Что-то пошло не так")

        