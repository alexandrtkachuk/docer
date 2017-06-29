import subprocess

proc = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
tmp = proc.stdout.read()
print tmp
