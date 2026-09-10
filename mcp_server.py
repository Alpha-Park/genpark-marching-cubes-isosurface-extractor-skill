import sys
import json
from client import MarchingCubes2D

mc = MarchingCubes2D()

def handle_call(name, arguments):
    if name == "extract":
        g = arguments["grid"]
        iso = arguments.get("isovalue", 0.5)
        return {"segments": mc.extract_isolines(g, iso)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
