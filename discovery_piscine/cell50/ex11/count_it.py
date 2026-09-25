#!/usr/bin/env python3
import sys

# ดึงพารามิเตอร์มาเก็บไว้ในตัวแปร args (ตัดชื่อไฟล์ที่ index 0 ออกไป)
args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")

    for arg in args:
        print(f"{arg}: {len(arg)}")