class MachineACafe:
    def __init__(self):
        self.temperature_eau = 0

    def __chauffe_eau(self):
        self.temperature_eau = 100
        print("L'eau est chaude.")

    def __moud_cafe(self):
        print("Café moulu avec succès.")

    def fait_du_cafe(self):
        self.__moud_cafe()
        self.__chauffe_eau()
        print("Le café est prêt")


machine = MachineACafe()
machine.fait_du_cafe()