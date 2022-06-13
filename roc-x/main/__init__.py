# COLOR_VALUE

BLUE = '\33[94m'
LIGHT_BLUE = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = "\033[0;92m"
CYAN = "\033[96m"
END = '\033[0m'
BLACK = "\033[0;30m"


class Services:
    @staticmethod
    def install_requirements(packages: list):
        """
        Install requirements.
        :param packages: A list of packages to install.
        :return: None.
        """
        import subprocess
        for package in packages:
            try:
                print(GREEN)
                subprocess.call(["pip", "install", package])
                exec(f"import {package}")
                print(f"\n{GREEN}[+] {YELLOW}{package}{GREEN} installed.")
            except ModuleNotFoundError:
                print(f"\n{RED}[-] {YELLOW}{package}{RED} not installed.")
            except Exception:
                print(f"\n{RED}[-] {YELLOW}{package}{RED} not installed.")

    @staticmethod
    def check_requirements(packages: list):
        """
        Check requirements.
        :param packages: A list of packages to check.
        :return: None if all requirements are met, otherwise packages list that are not met.
        """
        not_met = []
        for package in packages:
            try:
                exec("import " + package)
            except ImportError:
                not_met.append(package)

        if not_met:
            return not_met
        else:
            return None

    @staticmethod
    def must_require(packages: list):
        """
        Check requirements.
        :param packages: A list of packages to check.
        :return: None if all requirements are met, otherwise an error will be raised.
        """
        not_met = []
        for package in packages:
            try:
                exec("import " + package)
            except ImportError:
                not_met.append(package)

        if not_met:
            raise Exception(f"\n{RED}[-] {YELLOW}{not_met}{RED} not installed. Try to install manually.")
        else:
            return None
