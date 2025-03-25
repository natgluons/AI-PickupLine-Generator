from pathlib import Path
import subprocess
import sys

def setup():
    # Install dependencies
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Install npm dependencies and build Next.js app
    subprocess.check_call(["npm", "install"])
    subprocess.check_call(["npm", "run", "build"])

def main():
    # Start the Next.js server
    subprocess.check_call(["npm", "start"])

if __name__ == "__main__":
    setup()
    main() 