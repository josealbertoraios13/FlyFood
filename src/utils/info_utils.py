import platform
import psutil

class InfoPC:
    @staticmethod
    def perguntar_exibir_info():
        resposta = input("\nDeseja exibir as informações do PC? (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            print()
            InfoPC.info_pc()

    @staticmethod
    def info_pc():
        print(f"Sistema Operacional: {platform.system()}")
        print(f"Versão do SO: {platform.version()}\n")

        print(f"CPU: {platform.processor()}")
        print(f"Uso da CPU: {psutil.cpu_percent()}\n")

        memoria = psutil.virtual_memory()
        print(f"RAM Total: {memoria.total / (1024**3):.2f} GB")
        print(f"Usada: {memoria.used / (1024**3):.2f} GB")
        print(f"Uso: {memoria.percent}%\n")

        for processo in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                print(
                    f"PID: {processo.info['pid']} | "
                    f"Nome: {processo.info['name']} | "
                    f"RAM: {processo.info['memory_percent']:.2f}%"
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass