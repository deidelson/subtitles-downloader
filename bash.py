import subprocess

def execute(command):
    procesoBash = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return procesoBash.communicate()

