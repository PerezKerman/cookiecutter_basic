import os

# Recoger el número de tests desde cookiecutter.json
number_of_tests = int("{{cookiecutter.number_of_tests}}")

# Ruta a la carpeta "tests"
tests_dir = os.path.join(os.getcwd(), "tests")

# Crear los archivos de prueba
for i in range(number_of_tests):
    test_file = os.path.join(tests_dir, f"numtest_{i}.py")
    with open(test_file, "w") as f:
        # Esto habría que cambiarlo!
        f.write(f"# This is test file numtest_{i}.py\n")

