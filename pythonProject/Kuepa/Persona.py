class Persona:
#Constructor
    def __init__(self, nom, sex, eda, pes, alt, com, sue, cam):
        self.nombre = nom
        self.sexo = sex
        self.edad = eda
        self.peso = pes
        self.altura = alt
        self.comida = com
        self.sueño = sue
        self.camina = cam

#Metodo para mostrar los atributos
    def atributos(self):
        print('\nMostramos los atribitos del objeto\n')
        print('nombre: ', self.nombre,
              '\nSexo: ', self.sexo,
              '\nEdad: ', self.edad,
              '\nPeso: ', self.peso,
              '\nAltura: ', self.altura)

#creamos metodos con diferentes acciones
    def comer(self):
        print(self.nombre, self.comida)
    def dormir(self):
        print(self.nombre, self.sueño)
    def caminar(self):
        print(self.nombre, self.camina)

#creamos un metodo para  impriman todos los metodos anteriores juntos
    def acciones(self):
        print('\nAhora mostraremos los metodos\n')
        self.comer()
        self.dormir()
        self.caminar()

#Creamos un objeto
emmanuel = Persona('Emmanuel', 'Masculino', '34 años', '70kg', '1.70m', 'come pescado', 'duerme 8 horas', 'camina mucho')

#mandamos a llamar a los metodos para que se muestren en consola
emmanuel.atributos()
emmanuel.acciones()