from py4j.java_gateway import JavaGateway
#from py4j.java_gateway import GatewayServer

gateway = JavaGateway()
java_frontend = gateway.entry_point

random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
number1 = random.nextInt(10)              # call the Random.nextInt method
number2 = random.nextInt(10)
print(number1, number2)

# Test the connection
response = java_frontend.toString()  # Java's default `toString()` method
print("Python received:", response)

# Example: Call a method on Micropolis (assuming `getGameLevel()` exists)
return_value = java_frontend.testMethod()
print("Java says:", return_value)


#class PythonBackend:
#    def process_data(self, java_array):
#        python_list = list(java_array)
#        return sum(python_list)  # Example calculation

#backend = PythonBackend()
#server = GatewayServer(backend)
#server.start()
#print("Python GatewayServer Started...")