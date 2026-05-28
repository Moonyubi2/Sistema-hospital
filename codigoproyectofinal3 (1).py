import os
import numpy as np
from datetime import datetime


def cargarPersonalSistema() -> dict:

    try:

        personalSistemaDict = {}

        archivoPersonalSistema = open("personal.txt", "r", encoding="utf-8")

        for lineaPersonal in archivoPersonalSistema:

            datosPersonalLista = lineaPersonal.strip().split(",")

            if len(datosPersonalLista) == 3:

                nombreUsuarioSistema = datosPersonalLista[0]

                claveUsuarioSistema = datosPersonalLista[1]

                rolUsuarioSistema = datosPersonalLista[2]

                personalSistemaDict[nombreUsuarioSistema] = {"clave": claveUsuarioSistema, "rol": rolUsuarioSistema}

        archivoPersonalSistema.close()

        return personalSistemaDict

    except FileNotFoundError as errorArchivo:

        raise FileNotFoundError(f"Error cargando archivo personal.txt - {errorArchivo}")

    except Exception as errorCargaPersonal:

        raise Exception(f"Error cargando personal del sistema - {errorCargaPersonal}")


def cargarEstadoHabitaciones() -> tuple:

    try:

        matrizHabitacionesTipoA = np.empty((10, 1), dtype=object)

        matrizHabitacionesTipoB = np.empty((20, 2), dtype=object)

        for filaHabitacionTipoA in range(10):

            matrizHabitacionesTipoA[filaHabitacionTipoA][0] = ["disponible", ""]

        for filaHabitacionTipoB in range(20):

            for columnaCamaTipoB in range(2):

                matrizHabitacionesTipoB[filaHabitacionTipoB][columnaCamaTipoB] = ["disponible", ""]

        archivoEstadoCamas = open("estado_camas.txt", "r", encoding="utf-8")

        for lineaEstadoCama in archivoEstadoCamas:

            datosEstadoCamaLista = lineaEstadoCama.strip().split(",")

            if len(datosEstadoCamaLista) == 5:

                tipoHabitacionArchivo = datosEstadoCamaLista[0]

                numeroHabitacionArchivo = int(datosEstadoCamaLista[1])

                numeroCamaArchivo = int(datosEstadoCamaLista[2])

                estadoCamaArchivo = datosEstadoCamaLista[3]

                documentoPacienteArchivo = datosEstadoCamaLista[4]

                if tipoHabitacionArchivo == "A":

                    matrizHabitacionesTipoA[numeroHabitacionArchivo][0] = [estadoCamaArchivo, documentoPacienteArchivo]

                elif tipoHabitacionArchivo == "B":

                    matrizHabitacionesTipoB[numeroHabitacionArchivo][numeroCamaArchivo] = [estadoCamaArchivo, documentoPacienteArchivo]

        archivoEstadoCamas.close()

        return matrizHabitacionesTipoA, matrizHabitacionesTipoB

    except FileNotFoundError as errorArchivo:

        raise FileNotFoundError(f"Error cargando estado_camas.txt - {errorArchivo}")

    except Exception as errorEstadoHabitaciones:

        raise Exception(f"Error cargando estado habitaciones - {errorEstadoHabitaciones}")


def guardarEstadoHabitaciones(matrizHabitacionesTipoA: np.ndarray, matrizHabitacionesTipoB: np.ndarray) -> bool:

    try:

        archivoEstadoCamas = open("estado_camas.txt", "w", encoding="utf-8")

        for filaHabitacionTipoA in range(10):

            estadoCamaTipoA = matrizHabitacionesTipoA[filaHabitacionTipoA][0][0]

            documentoPacienteTipoA = matrizHabitacionesTipoA[filaHabitacionTipoA][0][1]

            archivoEstadoCamas.write("A," + str(filaHabitacionTipoA) + ",0," + estadoCamaTipoA + "," + documentoPacienteTipoA + "\n")

        for filaHabitacionTipoB in range(20):

            for columnaCamaTipoB in range(2):

                estadoCamaTipoB = matrizHabitacionesTipoB[filaHabitacionTipoB][columnaCamaTipoB][0]

                documentoPacienteTipoB = matrizHabitacionesTipoB[filaHabitacionTipoB][columnaCamaTipoB][1]

                archivoEstadoCamas.write("B," + str(filaHabitacionTipoB) + "," + str(columnaCamaTipoB) + "," + estadoCamaTipoB + "," + documentoPacienteTipoB + "\n")

        archivoEstadoCamas.close()

        return True

    except Exception as errorGuardarEstado:

        raise Exception(f"Error guardando estado habitaciones - {errorGuardarEstado}")


def iniciarSesionSistema(nombreUsuarioIngresado: str, claveUsuarioIngresada: str, personalSistemaDict: dict) -> tuple:

    try:

        if nombreUsuarioIngresado in personalSistemaDict:

            if personalSistemaDict[nombreUsuarioIngresado]["clave"] == claveUsuarioIngresada:

                rolUsuarioLogueado = personalSistemaDict[nombreUsuarioIngresado]["rol"]

                return True, rolUsuarioLogueado

            else:

                return False, 1

        else:

            return False, 2

    except Exception as errorInicioSesion:

        raise Exception(f"Error iniciando sesión - {errorInicioSesion}")


def verificarPacienteHospitalizado(documentoPacienteVerificar: str, matrizHabitacionesTipoA: np.ndarray, matrizHabitacionesTipoB: np.ndarray) -> bool:

    try:

        for filaHabitacionTipoA in range(10):

            if matrizHabitacionesTipoA[filaHabitacionTipoA][0][1] == documentoPacienteVerificar:

                return True

        for filaHabitacionTipoB in range(20):

            for columnaCamaTipoB in range(2):

                if matrizHabitacionesTipoB[filaHabitacionTipoB][columnaCamaTipoB][1] == documentoPacienteVerificar:

                    return True

        return False

    except Exception as errorPacienteHospitalizado:

        raise Exception(f"Error verificando paciente hospitalizado - {errorPacienteHospitalizado}")


def crearArchivoHistoriaClinica(documentoPacienteNuevo: str) -> bool:

    try:

        nombreArchivoHistoriaClinica = "historia_" + documentoPacienteNuevo + ".txt"

        archivoHistoriaClinica = open(nombreArchivoHistoriaClinica, "w", encoding="utf-8")

        archivoHistoriaClinica.write("HISTORIA CLINICA DEL PACIENTE " + documentoPacienteNuevo + "\n")

        archivoHistoriaClinica.close()

        return True

    except Exception as errorHistoriaClinica:

        raise Exception(f"Error creando historia clínica - {errorHistoriaClinica}")


def ingresarNuevoPaciente(documentoPacienteNuevo: str, tipoHabitacionSeleccionada: str, numeroHabitacionSeleccionada: int, numeroCamaSeleccionada: int, matrizHabitacionesTipoA: np.ndarray, matrizHabitacionesTipoB: np.ndarray) -> int:

    try:

        pacienteHospitalizado = verificarPacienteHospitalizado(documentoPacienteNuevo, matrizHabitacionesTipoA, matrizHabitacionesTipoB)

        if pacienteHospitalizado == True:

            return 1

        if tipoHabitacionSeleccionada == "A":

            if matrizHabitacionesTipoA[numeroHabitacionSeleccionada][0][0] == "disponible":

                matrizHabitacionesTipoA[numeroHabitacionSeleccionada][0] = ["ocupada", documentoPacienteNuevo]

                crearArchivoHistoriaClinica(documentoPacienteNuevo)

                return 2

            else:

                return 3

        elif tipoHabitacionSeleccionada == "B":

            if matrizHabitacionesTipoB[numeroHabitacionSeleccionada][numeroCamaSeleccionada][0] == "disponible":

                matrizHabitacionesTipoB[numeroHabitacionSeleccionada][numeroCamaSeleccionada] = ["ocupada", documentoPacienteNuevo]

                crearArchivoHistoriaClinica(documentoPacienteNuevo)

                return 4

            else:

                return 5

        else:

            return 6

    except Exception as errorIngresoPaciente:

        raise Exception(f"Error ingresando nuevo paciente - {errorIngresoPaciente}")


def visualizarHistoriaClinica(documentoPacienteBuscar: str) -> str | bool:

    try:

        nombreArchivoHistoriaClinica = "historia_" + documentoPacienteBuscar + ".txt"

        archivoHistoriaClinica = open(nombreArchivoHistoriaClinica, "r", encoding="utf-8")

        contenidoHistoriaClinica = archivoHistoriaClinica.read()

        archivoHistoriaClinica.close()

        return contenidoHistoriaClinica

    except FileNotFoundError:

        return False

    except Exception as errorHistoriaClinica:

        raise Exception(f"Error visualizando historia clínica - {errorHistoriaClinica}")


def verificarPacienteFacturado(documentoPacienteVerificar: str) -> bool:

    try:
        nombreArchivoFactura = "factura_" + documentoPacienteVerificar + ".txt"

        if os.path.exists(nombreArchivoFactura):

            return True

        return False

    except Exception as errorVerificarFactura:

        raise Exception(f"Error verificando factura paciente - {errorVerificarFactura}")


def actualizarHistoriaClinicaPaciente(documentoPacienteActualizar: str, nombreUsuarioLogueado: str, rolUsuarioLogueado: str, tipoRegistroHistoria: str, descripcionRegistroHistoria: str) -> bool:

    try:

        if verificarPacienteFacturado(documentoPacienteActualizar) == True:

            return False

        if verificarAltaMedicaPaciente(documentoPacienteActualizar) == True:

            return False

        fechaHoraActualSistema = datetime.now()

        fechaRegistroHistoria = fechaHoraActualSistema.strftime("%d/%m/%Y")

        horaRegistroHistoria = fechaHoraActualSistema.strftime("%H:%M:%S")

        nombreArchivoHistoriaClinica = "historia_" + documentoPacienteActualizar + ".txt"

        archivoHistoriaClinica = open(nombreArchivoHistoriaClinica, "a", encoding="utf-8")

        archivoHistoriaClinica.write("[" + fechaRegistroHistoria + "] [" + horaRegistroHistoria + "] [" + nombreUsuarioLogueado + "] [" + rolUsuarioLogueado + "] : [" + tipoRegistroHistoria + "] " + descripcionRegistroHistoria + "\n")

        archivoHistoriaClinica.close()

        return True

    except Exception as errorActualizarHistoria:

        raise Exception(f"Error actualizando historia clínica - {errorActualizarHistoria}")


def registrarAltaMedica(documentoPacienteAlta: str, nombreUsuarioMedico: str) -> bool:

    try:

        fechaHoraActualSistema = datetime.now()

        fechaAltaMedica = fechaHoraActualSistema.strftime("%d/%m/%Y")

        horaAltaMedica = fechaHoraActualSistema.strftime("%H:%M:%S")

        nombreArchivoHistoriaClinica = "historia_" + documentoPacienteAlta + ".txt"

        archivoHistoriaClinica = open(nombreArchivoHistoriaClinica, "a", encoding="utf-8")

        archivoHistoriaClinica.write("[" + fechaAltaMedica + "] [" + horaAltaMedica + "] [" + nombreUsuarioMedico + "] [medico] : ALTA MEDICA\n")

        archivoHistoriaClinica.close()

        return True

    except Exception as errorAltaMedica:

        raise Exception(f"Error registrando alta médica - {errorAltaMedica}")


def verificarAltaMedicaPaciente(documentoPacienteFacturacion: str) -> bool:

    try:

        nombreArchivoHistoriaClinica = "historia_" + documentoPacienteFacturacion + ".txt"

        archivoHistoriaClinica = open(nombreArchivoHistoriaClinica, "r", encoding="utf-8")

        for lineaHistoriaClinica in archivoHistoriaClinica:

            if "ALTA MEDICA" in lineaHistoriaClinica:

                archivoHistoriaClinica.close()

                return True

        archivoHistoriaClinica.close()

        return False

    except Exception as errorAltaMedica:

        raise Exception(f"Error verificando alta médica - {errorAltaMedica}")


def liberarHabitacionPaciente(documentoPacienteLiberar: str, matrizHabitacionesTipoA: np.ndarray, matrizHabitacionesTipoB: np.ndarray) -> bool:

    try:

        for filaHabitacionTipoA in range(10):

            if matrizHabitacionesTipoA[filaHabitacionTipoA][0][1] == documentoPacienteLiberar:

                matrizHabitacionesTipoA[filaHabitacionTipoA][0] = ["disponible", ""]

        for filaHabitacionTipoB in range(20):

            for columnaCamaTipoB in range(2):

                if matrizHabitacionesTipoB[filaHabitacionTipoB][columnaCamaTipoB][1] == documentoPacienteLiberar:

                    matrizHabitacionesTipoB[filaHabitacionTipoB][columnaCamaTipoB] = ["disponible", ""]

        return True

    except Exception as errorLiberarHabitacion:

        raise Exception(f"Error liberando habitación - {errorLiberarHabitacion}")


def generarFacturaPaciente(documentoPacienteFactura: str, valorTotalFactura: int) -> bool:

    try:

        nombreArchivoFactura = "factura_" + documentoPacienteFactura + ".txt"

        archivoFacturaPaciente = open(nombreArchivoFactura, "w", encoding="utf-8")

        archivoFacturaPaciente.write("FACTURA HOSPITALARIA\n")
        archivoFacturaPaciente.write("Paciente: " + documentoPacienteFactura + "\n")
        archivoFacturaPaciente.write("Total pagar: $" + str(valorTotalFactura) + "\n")

        archivoFacturaPaciente.close()

        return True

    except Exception as errorFactura:

        raise Exception(f"Error generando factura - {errorFactura}")


def facturarPacienteHospital(documentoPacienteFacturacion: str, cantidadDiasHospitalizacion: int, matrizHabitacionesTipoA: np.ndarray, matrizHabitacionesTipoB: np.ndarray) -> int | bool:

    try:

        pacienteAltaMedica = verificarAltaMedicaPaciente(documentoPacienteFacturacion)

        if pacienteAltaMedica == False:

            return False

        costoHabitacionTipoA = 150000

        costoHabitacionTipoB = 250000

        valorTotalFactura = 0

        for filaHabitacionTipoA in range(10):

            if matrizHabitacionesTipoA[filaHabitacionTipoA][0][1] == documentoPacienteFacturacion:

                valorTotalFactura = cantidadDiasHospitalizacion * costoHabitacionTipoA

        for filaHabitacionTipoB in range(20):

            for columnaCamaTipoB in range(2):

                if matrizHabitacionesTipoB[filaHabitacionTipoB][columnaCamaTipoB][1] == documentoPacienteFacturacion:

                    valorTotalFactura = cantidadDiasHospitalizacion * costoHabitacionTipoB

        generarFacturaPaciente(documentoPacienteFacturacion, valorTotalFactura)

        liberarHabitacionPaciente(documentoPacienteFacturacion, matrizHabitacionesTipoA, matrizHabitacionesTipoB)

        guardarEstadoHabitaciones(matrizHabitacionesTipoA, matrizHabitacionesTipoB)

        return valorTotalFactura

    except Exception as errorFacturacion:

        raise Exception(f"Error facturando paciente - {errorFacturacion}")


def generarReporteHospital(matrizHabitacionesTipoA: np.ndarray, matrizHabitacionesTipoB: np.ndarray, personalSistemaDict: dict) -> tuple | bool:


    try:

        cantidadHabitacionesTipoAOcupadas = 0

        cantidadCamasTipoBOcupadas = 0

        for filaHabitacionTipoA in range(10):

            if matrizHabitacionesTipoA[filaHabitacionTipoA][0][0] == "ocupada":

                cantidadHabitacionesTipoAOcupadas += 1

        for filaHabitacionTipoB in range(20):

            for columnaCamaTipoB in range(2):

                if matrizHabitacionesTipoB[filaHabitacionTipoB][columnaCamaTipoB][0] == "ocupada":

                    cantidadCamasTipoBOcupadas += 1

        porcentajeOcupacionTipoA = (cantidadHabitacionesTipoAOcupadas * 100) / 10

        porcentajeOcupacionTipoB = (cantidadCamasTipoBOcupadas * 100) / 40

        totalDiasEstadia = 0

        cantidadPacientesAlta = 0

        carpetaArchivo = "./"

        pacientesPorMedico = {}

        for nombreUsuario in personalSistemaDict:

            if personalSistemaDict[nombreUsuario]["rol"] == "medico":

                pacientesPorMedico[nombreUsuario] = 0

        if os.path.exists(carpetaArchivo):

            listaArchivosHistoria = os.listdir(carpetaArchivo)

            for nombreArchivoHistoria in listaArchivosHistoria:

                if nombreArchivoHistoria.startswith("historia_") and nombreArchivoHistoria.endswith(".txt"):

                    rutaArchivoHistoria = carpetaArchivo + nombreArchivoHistoria

                    try:

                        archivoHistoriaReporte = open(rutaArchivoHistoria, "r", encoding="utf-8")

                        fechaIngresoHistoria = ""

                        fechaAltaHistoria = ""

                        medicoAltaHistoria = ""

                        for lineaHistoriaReporte in archivoHistoriaReporte:

                            if lineaHistoriaReporte.startswith("Fecha ingreso:"):

                                fechaIngresoHistoria = lineaHistoriaReporte.strip().split(":", 1)[1].strip()

                            if "ALTA MEDICA" in lineaHistoriaReporte:

                                partesLineaAlta = lineaHistoriaReporte.strip().split("]")

                                if len(partesLineaAlta) >= 3:

                                    fechaAltaHistoria = partesLineaAlta[0].replace("[", "").strip()

                                    medicoAltaHistoria = partesLineaAlta[2].replace("[", "").strip()

                        archivoHistoriaReporte.close()

                        if fechaIngresoHistoria != "" and fechaAltaHistoria != "":

                            try:

                                fechaIngresoDatetime = datetime.strptime(fechaIngresoHistoria, "%d/%m/%Y")

                                fechaAltaDatetime = datetime.strptime(fechaAltaHistoria, "%d/%m/%Y")

                                diasEstadia = (fechaAltaDatetime - fechaIngresoDatetime).days

                                if diasEstadia < 1:

                                    diasEstadia = 1

                                totalDiasEstadia += diasEstadia

                                cantidadPacientesAlta += 1

                            except Exception as errorFechaReporte:

                                cantidadPacientesAlta += 1

                        if medicoAltaHistoria != "" and medicoAltaHistoria in pacientesPorMedico:

                            pacientesPorMedico[medicoAltaHistoria] += 1

                    except Exception as errorArchivoReporte:

                        raise Exception(f"Error leyendo archivo reporte - {errorArchivoReporte}")

        if cantidadPacientesAlta > 0:

            estadiaPromedio = totalDiasEstadia / cantidadPacientesAlta

        else:

            estadiaPromedio = 0

        return cantidadHabitacionesTipoAOcupadas, cantidadCamasTipoBOcupadas, porcentajeOcupacionTipoA, porcentajeOcupacionTipoB, estadiaPromedio, cantidadPacientesAlta, pacientesPorMedico

    except Exception as errorReporte:

        raise Exception(f"Error generando reporte hospitalario - {errorReporte}")


try:

    # DATOS DE ENTRADA

    respuestaInicioSistema = ""
    nombreUsuarioIngresado = ""
    claveUsuarioIngresada = ""
    opcionMenuSistema = ""
    respuestaContinuarSistema = ""

    # DATOS DE SALIDA

    mensajeSistema = ""

    # VARIABLES ADICIONALES

    sistemaHospitalActivo = False

    personalSistemaDict = {}

    matrizHabitacionesTipoA = np.empty((10, 1),dtype=object)

    matrizHabitacionesTipoB = np.empty((20, 2),dtype=object)

    nombreUsuarioLogueado = ""

    rolUsuarioLogueado = ""

    # PROCESO

    respuestaInicioSistema = input("¿Desea iniciar el sistema hospitalario? (si/no): ").lower().strip()

    while respuestaInicioSistema not in ["si", "no"]:

        print("\nError: Debe ingresar 'si' o 'no'")

        respuestaInicioSistema = input("¿Desea iniciar el sistema hospitalario? (si/no): ").lower().strip()

    if respuestaInicioSistema == "si":

        sistemaHospitalActivo = True

        personalSistemaDict = cargarPersonalSistema()

        matrizHabitacionesTipoA, matrizHabitacionesTipoB = cargarEstadoHabitaciones()

        while sistemaHospitalActivo == True:

            accesoSistemaCorrecto = False

            while accesoSistemaCorrecto == False:

                print("\n========== LOGIN DEL SISTEMA ==========")

                nombreUsuarioIngresado = input("Ingrese nombre usuario: ")

                if nombreUsuarioIngresado in personalSistemaDict:

                    claveUsuarioIngresada = input("Ingrese clave usuario: ")

                    resultadoInicioSesion = iniciarSesionSistema(nombreUsuarioIngresado, claveUsuarioIngresada, personalSistemaDict)

                    if resultadoInicioSesion[0] == True:

                        accesoSistemaCorrecto = True

                        nombreUsuarioLogueado = nombreUsuarioIngresado

                        rolUsuarioLogueado = resultadoInicioSesion[1]

                        print("\nInicio sesión exitoso")

                    else:

                        print("\nError: Clave incorrecta")

                else:

                    print("\nError: Usuario no encontrado")

            sesionActiva = True

            while sesionActiva == True:

                print("\n========== SISTEMA HOSPITALARIO ==========")

                if rolUsuarioLogueado == "admin":

                    print("1. Mostrar habitaciones")
                    print("2. Ingresar paciente")
                    print("3. Facturar paciente")
                    print("4. Generar reporte")
                    print("5. Cerrar sesión")

                    opcionMenuSistema = input("Seleccione opción: ")

                    if opcionMenuSistema == "1":

                        print("\n========== HABITACIONES TIPO A ==========\n")

                        for filaImpresionA in range(10):

                            estadoImpresionA = matrizHabitacionesTipoA[filaImpresionA][0][0]

                            documentoImpresionA = matrizHabitacionesTipoA[filaImpresionA][0][1]

                            print("Hab A" + str(filaImpresionA) + ": ['" + estadoImpresionA + "', '" + documentoImpresionA + "']")

                        print("\n========== HABITACIONES TIPO B ==========\n")

                        for filaImpresionB in range(10):

                            filaMostrarB = ""

                            for columnaImpresionB in range(2):

                                estadoImpresionB = matrizHabitacionesTipoB[filaImpresionB][columnaImpresionB][0]

                                documentoImpresionB = matrizHabitacionesTipoB[filaImpresionB][columnaImpresionB][1]

                                filaMostrarB += "['" + estadoImpresionB + "', '" + documentoImpresionB + "']  "

                            print("Hab B" + str(filaImpresionB) + ": " + filaMostrarB)

                    elif opcionMenuSistema == "2":

                        regresarMenuAdmin = False

                        while True:

                            documentoPacienteNuevo = input("Ingrese documento paciente (o '0' para regresar al menú): ")

                            if documentoPacienteNuevo == "0":

                                regresarMenuAdmin = True

                                break

                            elif documentoPacienteNuevo.isdigit() == False:

                                print("\nError: El documento solo debe contener números")

                            elif len(documentoPacienteNuevo) != 10:

                                print("\nError: El documento debe tener exactamente 10 dígitos")

                            else:

                                break

                        if regresarMenuAdmin == False and verificarPacienteHospitalizado(documentoPacienteNuevo, matrizHabitacionesTipoA, matrizHabitacionesTipoB) == True:

                            print("\nError: El paciente ya está hospitalizado")

                        elif regresarMenuAdmin == False:

                            while True:

                                tipoHabitacionSeleccionada = input("Ingrese tipo habitación (A/B): ").upper()

                                if tipoHabitacionSeleccionada in ["A", "B"]:

                                    break

                                else:

                                    print("\nError: El tipo de habitación debe ser 'A' o 'B'")

                            if tipoHabitacionSeleccionada == "A":

                                while True:

                                    numeroHabitacionSeleccionadaTexto = input("Ingrese número habitación (0-9): ")

                                    if numeroHabitacionSeleccionadaTexto.isdigit() == False:

                                        print("\nError: El número de habitación debe ser un valor numérico")

                                    elif int(numeroHabitacionSeleccionadaTexto) < 0 or int(numeroHabitacionSeleccionadaTexto) > 9:

                                        print("\nError: El número de habitación debe estar entre 0 y 9")

                                    else:

                                        break

                                numeroHabitacionSeleccionada = int(numeroHabitacionSeleccionadaTexto)

                                numeroCamaSeleccionada = 0

                            elif tipoHabitacionSeleccionada == "B":

                                while True:

                                    numeroHabitacionSeleccionadaTexto = input("Ingrese número habitación (0-19): ")

                                    if numeroHabitacionSeleccionadaTexto.isdigit() == False:

                                        print("\nError: El número de habitación debe ser un valor numérico")

                                    elif int(numeroHabitacionSeleccionadaTexto) < 0 or int(numeroHabitacionSeleccionadaTexto) > 19:

                                        print("\nError: El número de habitación debe estar entre 0 y 19")

                                    else:

                                        break

                                numeroHabitacionSeleccionada = int(numeroHabitacionSeleccionadaTexto)

                                while True:

                                    numeroCamaSeleccionadaTexto = input("Ingrese número cama (0-1): ")

                                    if numeroCamaSeleccionadaTexto.isdigit() == False:

                                        print("\nError: El número de cama debe ser un valor numérico")

                                    elif int(numeroCamaSeleccionadaTexto) < 0 or int(numeroCamaSeleccionadaTexto) > 1:

                                        print("\nError: El número de cama debe ser 0 o 1")

                                    else:

                                        break

                                numeroCamaSeleccionada = int(numeroCamaSeleccionadaTexto)

                            else:

                                numeroHabitacionSeleccionada = 0

                                numeroCamaSeleccionada = 0

                            resultadoIngresoPaciente = ingresarNuevoPaciente(documentoPacienteNuevo, tipoHabitacionSeleccionada, numeroHabitacionSeleccionada, numeroCamaSeleccionada, matrizHabitacionesTipoA, matrizHabitacionesTipoB)

                            if resultadoIngresoPaciente == 2:

                                guardarEstadoHabitaciones(matrizHabitacionesTipoA, matrizHabitacionesTipoB)

                                print("\nPaciente ingresado correctamente")

                            elif resultadoIngresoPaciente == 3:

                                print("\nError: Habitación ocupada")

                            elif resultadoIngresoPaciente == 4:

                                guardarEstadoHabitaciones(matrizHabitacionesTipoA, matrizHabitacionesTipoB)

                                print("\nPaciente ingresado correctamente")

                            elif resultadoIngresoPaciente == 5:

                                print("\nError: Cama ocupada")

                            elif resultadoIngresoPaciente == 6:

                                print("\nError: Tipo habitación inválido")

                            else:

                                print("\nError en ingreso paciente")

                    elif opcionMenuSistema == "3":

                        regresarMenuFacturacion = False

                        documentoPacienteFacturacion = ""

                        while True:

                            documentoPacienteFacturacion = input("Ingrese documento paciente (o '0' para regresar al menú): ")

                            if documentoPacienteFacturacion == "0":

                                regresarMenuFacturacion = True

                                break

                            elif documentoPacienteFacturacion.isdigit() == False:

                                print("\nError: El documento solo debe contener números")

                            elif len(documentoPacienteFacturacion) != 10:

                                print("\nError: El documento debe tener exactamente 10 dígitos")

                            else:

                                break

                        if regresarMenuFacturacion == False:

                            while True:

                                cantidadDiasHospitalizacionTexto = input("Ingrese cantidad días hospitalización: ")

                                if cantidadDiasHospitalizacionTexto.isdigit() == False:

                                    print("\nError: La cantidad de días debe ser un valor numérico entero")

                                elif int(cantidadDiasHospitalizacionTexto) < 1:

                                    print("\nError: La cantidad de días debe ser al menos 1")

                                else:

                                    break

                            cantidadDiasHospitalizacion = int(cantidadDiasHospitalizacionTexto)

                            resultadoFacturaPaciente = facturarPacienteHospital(documentoPacienteFacturacion, cantidadDiasHospitalizacion, matrizHabitacionesTipoA, matrizHabitacionesTipoB)

                            if resultadoFacturaPaciente == False:

                                print("\nError: Paciente sin alta médica")

                            else:

                                print("\nFactura generada correctamente")

                                print("Valor total factura:", resultadoFacturaPaciente)

                    elif opcionMenuSistema == "4":
                        resultadoReporteHospital = generarReporteHospital(matrizHabitacionesTipoA, matrizHabitacionesTipoB, personalSistemaDict)

                        if resultadoReporteHospital != False:

                            print("\n========== REPORTE HOSPITAL ==========\n")

                            print("Habitaciones Tipo A ocupadas:", resultadoReporteHospital[0])

                            print("Camas Tipo B ocupadas:", resultadoReporteHospital[1])

                            print("Porcentaje ocupación Tipo A:", resultadoReporteHospital[2], "%")

                            print("Porcentaje ocupación Tipo B:", resultadoReporteHospital[3], "%")

                            print("Estadía promedio (pacientes alta):", resultadoReporteHospital[4], "días")

                            print("Total pacientes dados de alta:", resultadoReporteHospital[5])

                            print("\nPacientes atendidos por médico:")

                            for nombreMedicoReporte in resultadoReporteHospital[6]:

                                print("  " + nombreMedicoReporte + ": " + str(resultadoReporteHospital[6][nombreMedicoReporte]) + " alta(s)")

                        else:

                            print("\nError generando reporte")

                    elif opcionMenuSistema == "5":

                        sesionActiva = False

                    else:

                        print("\nError: Opción inválida")

                elif rolUsuarioLogueado == "medico" or rolUsuarioLogueado == "enfermera":

                    print("1. Ver historia clínica")
                    print("2. Actualizar historia clínica")

                    if rolUsuarioLogueado == "medico":

                        print("3. Dar alta médica")
                        print("4. Cerrar sesión")

                    else:

                        print("3. Cerrar sesión")

                    opcionMenuSistema = input("Seleccione opción: ")

                    if opcionMenuSistema == "1":

                        while True:

                            documentoPacienteBuscar = input("Ingrese documento paciente (o '0' para regresar al menú): ")

                            if documentoPacienteBuscar == "0":

                                break

                            elif documentoPacienteBuscar.isdigit() == False:

                                print("\nError: El documento solo debe contener números")

                            elif len(documentoPacienteBuscar) != 10:

                                print("\nError: El documento debe tener exactamente 10 dígitos")

                            else:

                                contenidoHistoriaClinica = visualizarHistoriaClinica(documentoPacienteBuscar)

                                if contenidoHistoriaClinica != False:

                                    print("\n========== HISTORIA CLINICA ==========\n")

                                    print(contenidoHistoriaClinica)

                                    break

                                else:

                                    print("\nError: Historia clínica no encontrada")

                                    reintentoVerHistoria = input("¿Desea intentar con otro documento? (si/no): ").lower().strip()

                                    while reintentoVerHistoria not in ["si", "no"]:

                                        print("\nError: Debe ingresar 'si' o 'no'")

                                        reintentoVerHistoria = input("¿Desea intentar con otro documento? (si/no): ").lower().strip()

                                    if reintentoVerHistoria == "no":

                                        break

                    elif opcionMenuSistema == "2":

                        documentoValidoParaActualizar = False

                        documentoPacienteActualizar = ""

                        while documentoValidoParaActualizar == False:

                            documentoPacienteActualizar = input("Ingrese documento paciente (o '0' para regresar al menú): ")

                            if documentoPacienteActualizar == "0":

                                documentoPacienteActualizar = ""

                                documentoValidoParaActualizar = True

                            elif documentoPacienteActualizar.isdigit() == False:

                                print("\nError: El documento solo debe contener números")

                            elif len(documentoPacienteActualizar) != 10:

                                print("\nError: El documento debe tener exactamente 10 dígitos")

                            elif visualizarHistoriaClinica(documentoPacienteActualizar) == False:

                                print("\nError: Historia clínica no encontrada")

                                reintentoActualizarHistoria = input("¿Desea intentar con otro documento? (si/no): ").lower().strip()

                                while reintentoActualizarHistoria not in ["si", "no"]:

                                    print("\nError: Debe ingresar 'si' o 'no'")

                                    reintentoActualizarHistoria = input("¿Desea intentar con otro documento? (si/no): ").lower().strip()

                                if reintentoActualizarHistoria == "no":

                                    documentoValidoParaActualizar = True

                                    documentoPacienteActualizar = ""

                            elif verificarPacienteFacturado(documentoPacienteActualizar) == True:

                                print("\nError: No se puede actualizar la historia clínica de un paciente ya facturado")

                            elif verificarAltaMedicaPaciente(documentoPacienteActualizar) == True:

                                print("\nError: No se puede actualizar la historia clínica de un paciente con alta médica")

                            else:

                                documentoValidoParaActualizar = True

                        while documentoPacienteActualizar != "" and True:

                            print("\n1. Prescripción")
                            print("2. Suministro Medicamento")
                            print("3. Evolución")

                            opcionTipoRegistro = input("Seleccione tipo entrada: ")

                            if opcionTipoRegistro in ["1", "2", "3"]:

                                break

                            else:

                                print("\nError: Debe seleccionar una opción válida (1, 2 o 3)")

                        descripcionRegistroHistoria = input("Ingrese información clínica: ")

                        while descripcionRegistroHistoria.strip() == "":

                            print("\nError: La información clínica no puede estar vacía")

                            descripcionRegistroHistoria = input("Ingrese información clínica: ")

                        tipoRegistroHistoria = ""

                        if opcionTipoRegistro == "1":

                            tipoRegistroHistoria = "Prescripción"

                        elif opcionTipoRegistro == "2":

                            tipoRegistroHistoria = "Suministro Medicamento"

                        elif opcionTipoRegistro == "3":

                            tipoRegistroHistoria = "Evolución"

                        resultadoActualizarHistoria = actualizarHistoriaClinicaPaciente(documentoPacienteActualizar, nombreUsuarioLogueado, rolUsuarioLogueado, tipoRegistroHistoria, descripcionRegistroHistoria)

                        if resultadoActualizarHistoria == True:

                            print("\nHistoria clínica actualizada correctamente")

                        else:

                            print("\nError actualizando historia clínica")

                    elif opcionMenuSistema == "3" and rolUsuarioLogueado == "medico":

                        while True:

                            documentoPacienteAlta = input("Ingrese documento paciente (o '0' para regresar al menú): ")

                            if documentoPacienteAlta == "0":

                                break

                            elif documentoPacienteAlta.isdigit() == False:

                                print("\nError: El documento solo debe contener números")

                            elif len(documentoPacienteAlta) != 10:

                                print("\nError: El documento debe tener exactamente 10 dígitos")

                            elif visualizarHistoriaClinica(documentoPacienteAlta) == False:

                                print("\nError: Historia clínica no encontrada")

                                reintentoAltaMedica = input("¿Desea intentar con otro documento? (si/no): ").lower().strip()

                                while reintentoAltaMedica not in ["si", "no"]:

                                    print("\nError: Debe ingresar 'si' o 'no'")

                                    reintentoAltaMedica = input("¿Desea intentar con otro documento? (si/no): ").lower().strip()

                                if reintentoAltaMedica == "no":

                                    break

                            else:

                                resultadoAltaMedica = registrarAltaMedica(documentoPacienteAlta, nombreUsuarioLogueado)

                                if resultadoAltaMedica == True:

                                    print("\nAlta médica registrada correctamente")

                                else:

                                    print("\nError registrando alta médica")

                                break

                    elif opcionMenuSistema == "3" and rolUsuarioLogueado == "enfermera":

                        sesionActiva = False

                    elif opcionMenuSistema == "4" and rolUsuarioLogueado == "medico":

                        sesionActiva = False

                    else:

                        print("\nError: Opción inválida")

                respuestaContinuarSistema = input("\n¿Desea continuar usando el sistema? (si/no): ").lower()

                while respuestaContinuarSistema not in ["si", "no"]:

                    print("\nError: Debe ingresar 'si' o 'no'")

                    respuestaContinuarSistema = input("¿Desea continuar usando el sistema? (si/no): ").lower()

                if respuestaContinuarSistema == "no":

                    sistemaHospitalActivo = False

                    sesionActiva = False

    else:

        print("\nSistema no iniciado")

except ValueError as errorValor:

    print("\nError de valor:", errorValor)

except FileNotFoundError as errorArchivo:

    print("\nError archivo no encontrado:", errorArchivo)

except Exception as errorGeneralSistema:

    print("\nError general sistema:", errorGeneralSistema)

else:

    print("\nSistema ejecutado correctamente")

finally:

    print("\nGracias por usar el sistema hospitalario")