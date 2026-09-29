import sys
print("=== PYTHON EXECUTABLE IN USE ===")
print(sys.executable)

try:
    import pandas
    print("\n=== PANDAS LOCATION ===")
    print(pandas.__file__)
    print("SUCCESS: Pandas is working!")
except ImportError as e:
    print("\n=== ERROR ===")
    print("ImportError:", e)