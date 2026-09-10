from client import MarchingCubes2D

def main():
    print("=== Testing Marching Cubes Isosurface Extractor ===")
    mc = MarchingCubes2D()
    scalar_field = [
        [0.0, 0.0, 0.0],
        [0.0, 2.5, 0.0],
        [0.0, 0.0, 0.0]
    ]

    isolines = mc.extract_isolines(scalar_field, isovalue=1.0)
    print(f"Extracted {len(isolines)} isocontour crossing segments:")
    for s in isolines:
        print(" ", s)

    assert len(isolines) > 0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
