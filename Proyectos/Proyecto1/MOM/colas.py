class Queue:
    def __init__(self):
        # Creación de colas
        #para cada tópico una cola
        self.queueOne = Queue()
        self.queueTwo = Queue()
        self.queueThree = Queue()

#Determina si las colas están vacias (False) o no (True)
    def is_empty1(self):
        return not bool(self.queueOne)

    def is_empty2(self):
        return not bool(self.queueTwo)
    
    def is_empty3(self):
        return not bool(self.queueThree)

#Agrega un nuevo elemento a la cola
    def enqueue1(self, message, times):
        self.queueOne.append(message)
        print(f"El elemento {message} ha sido agregado {times} veces a la cola.")

    def enqueue2(self, message, times):
        self.queueTwo.append(message)
        print(f"El mensaje {message} ha sido agregado a la cola.")

    def enqueue3(self, message, times):
        self.queueThree.append(message)
        print(f"El mensaje {message} ha sido agregado a la cola.")

#elimina y devuelve con el pop el primer elemento de la cola
    def dequeue1(self):
        return self.queueOne.pop(0)
    
    def dequeue2(self):
        return self.queueTwo.pop(0)
    
    def dequeue3(self):
        return self.queueThree.pop(0)

#con el display se imprime la cola en consola
    def display1(self):
        print(self.queueOne)

    def display2(self):
        print(self.queueTwo)

    def display3(self):
        print(self.queueThree)


#Agregar un mensaje a la cola especificada 
    def QueueAddOne(self, queueOne, message):
        message = input("Ingrese un mensaje para agregar a la cola: ")
        times = int(input("Ingrese la cantidad de veces que desea agregar el mensaje: "))
        for i in range(times):
            queueOne.enqueue1(message)

    def QueueAddTwo(self, queueTwo, message):
        message = input("Ingrese un mensaje para agregar a la cola: ")
        times = int(input("Ingrese la cantidad de veces que desea agregar el mensaje: "))
        for i in range(times):
            queueTwo.enqueue2(message)

    def QueueAddThree(self, queueThree, message):
        message = input("Ingrese un mensaje para agregar a la cola: ")
        times = int(input("Ingrese la cantidad de veces que desea agregar el mensaje: "))
        for i in range(times):
            queueThree.enqueue3(message)

#esto es para coger un mensaje en particular de la cola y enviarlo a un usuario
    def get_message1(self, position):
        if position < 0 or position >= len(self.queueOne):
            raise IndexError("Index out of range")
        return self.queueOne[position]
    
    def get_message2(self, position):
        if position < 0 or position >= len(self.queueTwo):
            raise IndexError("Index out of range")
        return self.queueTwo[position]
    
    def get_message3(self, position):
        if position < 0 or position >= len(self.queueThree):
            raise IndexError("Index out of range")
        return self.queueThree[position]

#el usuario solicita el mensaje de la cola de su interes 
    def messageRequest1(self, queueOne, position):
        if queueOne.is_empty1():
            return "La cola está vacía"
        # Obtener el elemento de la cola en x posición
        MessageOne = self.get_message1(position)
        queueOne.dequeue1(MessageOne)
        return MessageOne

    def messageRequest2(self, queueTwo, position):
        if queueTwo.is_empty2():
            return "La cola está vacía"
        # Obtener el elemento de la cola en x posición
        MessageTwo = self.get_message1(position)
        queueTwo.dequeue2(MessageTwo)
        return MessageTwo
    
    def messageRequest3(self, queueThree, position):
        if queueThree.is_empty3():
            return "La cola está vacía"
        # Obtener el elemento de la cola en x posición
        MessageThree = self.get_message1(position)
        queueThree.dequeue3(MessageThree)
        return MessageThree
    
