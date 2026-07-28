import sys
import ast
import importlib.util
import subprocess


BUILTINS = {
    "os",
    "sys",
    "time",
    "json",
    "math",
    "random",
    "re",
    "datetime",
    "pathlib",
    "subprocess",
    "shutil",
    "socket",
    "threading",
    "collections",
    "itertools",
    "functools",
    "statistics",
}


def find_imports(filename):
    with open(filename, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    imports = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for item in node.names:
                imports.add(item.name.split(".")[0])

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])

    return sorted(imports)


def check_package(package):
    if package in BUILTINS:
        return "built-in"

    if importlib.util.find_spec(package):
        return "installed"

    return "missing"


def install_packages(packages):
    print("\nInstalling:")
    print(" ".join(packages))

    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            *packages
        ]
    )

    print("\n✓ Installation complete!")


def create_requirements(packages):
    with open("requirements.txt", "w") as file:
        for package in packages:
            file.write(package + "\n")

    print("\n✓ Created requirements.txt")


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python dependency_checker.py file.py")
        print("python dependency_checker.py file.py --fix")
        print("python dependency_checker.py file.py --requirements")
        return


    filename = sys.argv[1]

    fix_mode = "--fix" in sys.argv
    requirements_mode = "--requirements" in sys.argv


    try:
        imports = find_imports(filename)

    except Exception as error:
        print("Could not read file:")
        print(error)
        return


    print("""
=========================
  Dependency Checker
=========================
""")

    print("File:")
    print(filename)

    print("\nDependencies:\n")


    missing = []
    external = []


    for package in imports:

        result = check_package(package)

        if result == "built-in":
            print(f"✓ {package} - Python built-in")

        elif result == "installed":
            print(f"✓ {package} - installed")
            external.append(package)

        else:
            print(f"✗ {package} - missing")
            missing.append(package)
            external.append(package)


    if requirements_mode:
        create_requirements(external)


    if missing:

        print("\nMissing packages:")

        for package in missing:
            print(f" - {package}")


        if fix_mode:

            answer = input(
                "\nInstall missing packages? (y/n): "
            )

            if answer.lower() == "y":
                install_packages(missing)

            else:
                print("Cancelled.")

        else:
            print("\nUse --fix to install missing packages.")

    elif not requirements_mode:
        print("\nEverything looks good! 🎉")


if __name__ == "__main__":
    main()
