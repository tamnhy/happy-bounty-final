import os
import shutil
os.makedirs("/output", exist_ok=True)
shutil.copy("happy.jpg", "/output/image.png")
print("Happy image ready")
