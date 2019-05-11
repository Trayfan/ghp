#coding: utf8
from ctypes import *

# определение типов p 38
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPSTR = POINTER(c_char)
HANDLE = c_void_p

# константы
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# инициализация структур для CreateProcessA https://docs.microsoft.com/ru-ru/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa
class STARTUPINFOA(Structure):
    _fields_ = [
        ("cb", DWORD),
        ("lpReserved", LPSTR),
        ("lpDesktop", LPSTR),
        ("lpTitle", LPSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
    ]

class PROCESS_INFORMATION(Structure):
    __fields__ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
    ]