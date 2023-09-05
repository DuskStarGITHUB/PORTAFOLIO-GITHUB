"""Titulo: |Generador QR|"""
#####################################################################################
# Descripción: <Genera qr con un enlace>
# Autor: <DuskStar>
# Fecha de creación: <04/09/2023>
# Nota: <Cambiar el enlace>
#####################################################################################

# LIBRERIAS
import qrcode

def generar_codigo_qr(enlace, nombre_archivo):
    """GENERADOR"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(enlace)
    qr.make(fit=True)

    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    imagen_qr.save(nombre_archivo)

if __name__ == "__main__":
    # Enlace a cambair
    LINK = "https://github.com/DuskStarGITHUB"
    # Nombre del archivo a generar
    NOMBRE = "codigo_qr.png"
    generar_codigo_qr(LINK, NOMBRE)
    print(f"El código QR ha sido generado y guardado en {NOMBRE}.")
