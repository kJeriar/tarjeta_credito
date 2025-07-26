class TarjetaCredito:
    tarjetas_creadas = []

    def __init__(self, limite_credito, intereses, saldo_pagar= 0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas_creadas.append(self)

    def compra(self, monto):
    #aumenta el saldo a pagar
        if self.saldo_pagar + monto <= self.limite_credito:
           self.saldo_pagar += monto
        else:
           print("No se puede comprar con esta tarjeta, tiene muchas deudas")
        return self

    def pago(self, monto):
    #disminuye el saldo
        self.saldo_pagar -= monto
        return self
  
    def mostrar_info_tarjeta(self):
    #imprimir saldo
        print (f"Tienes una deuda de ${self.saldo_pagar:.2f}")
        return self

    def cobrar_interes(self):
    #saldo + intereses
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("Información de todas las tarjetas:")
        for i, tarjeta in enumerate(cls.tarjetas_creadas, start=1):
            print(f"Tarjeta {i}: Deuda = ${tarjeta.saldo_pagar:.2f}, Límite = ${tarjeta.limite_credito}, Interés = {tarjeta.intereses}")