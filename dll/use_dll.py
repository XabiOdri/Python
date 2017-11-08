from ctypes import *

dll = CDLL('example.dll')

ReadDLLVersion = dll.ReadDLLVersion
ReadDLLVersion.restype = c_long # tipo ctypes del resultado
#CloseCommunicationPort.argtypes = [] # lista de tipos de los argumentos

#SomeFunction = dll.SomeFunction
#CloseCommunicationPort.restype = ctypes.c_void_p # tipo ctypes del resultado
#SomeFunction.argtypes = [c_char_p] # lista de tipos de los argumentos

ReadDLLDate = dll.ReadDLLDate
ReadDLLDate.restype = c_long # tipo ctypes del resultado


if __name__ == "__main__":

	version = ReadDLLVersion()
	print(version)
	date = ReadDLLDate()
	print(date)
	#CloseCommunicationPort()
	#SomeFunction("Hola mundo!\n")
