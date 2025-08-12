from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["selenium", "openpyxl", "customtkinter", "tkinter"],
    "includes": ["os", "sys"]
}

executables = [Executable("app.py", base="Win32GUI")]

setup(
    name="AutomatizadorSistema",
    version="0.1",
    description="Descrição",
    options={"build_exe": build_exe_options},
    executables=executables
)