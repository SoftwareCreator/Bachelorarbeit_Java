from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
java_backend = gateway.jvm.com.yourproject.JavaBackend()
response = java_backend.echo("Hello from Python via Py4J and Gradle!")
print("Python received:", response)
