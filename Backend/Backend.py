#from py4j.java_gateway import JavaGateway
#from py4j.java_gateway import GatewayServer

#gateway = JavaGateway()
#java_frontend = gateway.entry_point

#gateway.jvm.System.out.println("Hello from python to java")
#random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
#number1 = random.nextInt(10)              # call the Random.nextInt method
#number2 = random.nextInt(10)
#print(number1, number2)

# Test the connection
#response = java_frontend.toString()  # Java's default `toString()` method
#print("Python received:", response)

# Example: Call a method on Micropolis (assuming `getGameLevel()` exists)
#return_value = java_frontend.getDataLog()
#print("Java says:", return_value)




#from py4j.java_gateway import JavaGateway

#def receiveDataFromJava(dataLog):
#  print("hello")
#  print(dataLog)

#class Java:
#  implements = ['micropolisj.engine.javaPyCallInt']

#if __name__ == '__main__':
    #logger = logging.getLogger("py4j")
    #logger.setLevel(logging.DEBUG)
    #logger.addHandler(logging.StreamHandler())
#    gateway = JavaGateway(start_callback_server=True)
    #Fromjava = receiveDataFromJava(dataLog)   
#    Fromjava_ex = gateway.jvm.micropolisj.engine.Micropolis()
#    Fromjava_ex.SendDataToPython(receiveDataFromJava)




#from py4j.java_gateway import JavaGateway

# Define a Python class that implements the Java interface
#class PythonCallback:
#    def receiveDataFromJava(self, dataLog):
#        print("hello")
#        print(dataLog)

# Start Py4J gateway
#if __name__ == '__main__':
#    gateway = JavaGateway(start_callback_server=True)
    
    # Create an instance of the callback class
#    python_callback_instance = PythonCallback()
    
    # Get the Java object
#    Fromjava_ex = gateway.jvm.micropolisj.engine.Micropolis()
    
    # Pass the instance, not a raw function
#    Fromjava_ex.SendDataToPython(python_callback_instance)



'''
from py4j.java_gateway import JavaGateway, CallbackServerParameters

# Define a Python class that implements the Java interface
class PythonCallback:
    def receiveDataFromJava(self, dataLog):
        print("hello")
        print(dataLog)

    # This tells Py4J that this class implements a Java interface
    def _py4j_get_interfaces(self):
        return ["micropolisj.engine.javaPyCallInt"]

# Start Py4J gateway
if __name__ == '__main__':
    gateway = JavaGateway(
        callback_server_parameters=CallbackServerParameters()  # Ensure callbacks work
    )
    
    # Create an instance of the callback class
    python_callback_instance = PythonCallback()

    # Register the instance with Py4J so Java can call it
    gateway.entry_point = python_callback_instance  

    # Get the Java object
    Fromjava_ex = gateway.jvm.micropolisj.engine.Micropolis()
    
    # Pass the callback instance to Java
    Fromjava_ex.SendDataToPython(python_callback_instance)
    '''