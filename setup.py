from cx_Freeze import setup, Executable

# Replace 'your_script.pyw' with the name of your .pyw file
executables = [Executable("fmconverter.pyw", base="Win32GUI")]

setup(
    name="fmconverter",
    version="0.1",
    description="Simple gui converter for Feets and Meters",
    executables=executables
)
