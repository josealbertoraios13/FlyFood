import platform

import psutil

import subprocess


class InfoPC:
    @staticmethod
    def perguntar_exibir_info():
        resposta = input("\nDeseja exibir as informações do PC? (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            print()
            InfoPC.info_pc()

    @staticmethod
    def info_pc() -> None:
        sistema = platform.system()

        print(f"Sistema Operacional: {sistema}")
        print(f"Versão do Sistema: {platform.version()}\n")

        if sistema == "Linux":
            cpu = subprocess.check_output(
                ["lscpu", "-p=MODELNAME"],
                text=True
            ).strip()

            modelo_cpu = next(
                linha for linha in cpu.splitlines() if not linha.startswith("#")
            )
        elif sistema == "Darwin":     
            modelo_cpu = subprocess.check_output(
                ["sysctl", "-n", "machdep.cpu.brand_string"],
                text=True
            ).strip()
        else:
            modelo_cpu = platform.processor()

        print(f"CPU: {modelo_cpu}")
        print(f"Arquitetura: {platform.machine()}")
        print(f"Núcleos físicos: {psutil.cpu_count(logical=False)}")
        print(f"Núleos virtuais: {psutil.cpu_count(logical=True)}")
        
        frequencia = psutil.cpu_freq()

        if frequencia:
            print(f"Clock: {frequencia.current / 1000:.2f} GHz\n")

        memoria = psutil.virtual_memory()
        print(f"RAM: {memoria.total / (1024**3):.2f} GB\n")

        processos = len(list(psutil.process_iter()))
        print(f"Quantidades de processos no OS: {processos}")