from TarjetaCredito import TarjetaCredito

# Tarjeta 1: 2 compras y un pago, cobrar intereses y mostrar
tarjeta1 = TarjetaCredito(1000, 0.1)
tarjeta1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 2: 3 compras y 2 pagos, cobrar intereses y mostrar
tarjeta2 = TarjetaCredito(1500, 0.05)
tarjeta2.compra(300).compra(200).compra(250).pago(100).pago(50).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 3: 5 compras que exceden el límite de crédito, mostrar info
tarjeta3 = TarjetaCredito(500, 0.02)
tarjeta3.compra(100).compra(150).compra(200).compra(100).compra(100).mostrar_info_tarjeta()

# todas las tarjetas creadas
print("\nResumen de todas las tarjetas creadas:")
TarjetaCredito.mostrar_todas_las_tarjetas()


