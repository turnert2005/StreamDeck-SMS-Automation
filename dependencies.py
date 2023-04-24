import sys
import subprocess
import pkg_resources

def check_required_packages():
    """Check if required Python packages are installed."""
    required_packages = ['flask', 'twilio', 'phonenumbers', 'python-dotenv']
    installed_packages = [pkg.key for pkg in pkg_resources.working_set]
    missing_packages = [pkg for pkg in required_packages if pkg not in installed_packages]
    if missing_packages:
        print(f"The following required packages are missing: {missing_packages}")
        print("Installing missing packages...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages], stdout=subprocess.DEVNULL)
        print("Packages installed.")
