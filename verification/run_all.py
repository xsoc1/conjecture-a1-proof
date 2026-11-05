"""Run all finite exact checks and probes, preserving exit statuses and logs."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

SCRIPTS = ["conj.py", "conj2.py", "verify.py", "verify2.py", "structure.py",
           "probe2.py", "sharpness.py", "pureZ_check.py", "audit_checks.py"]


def main():
    if not __debug__:
        raise RuntimeError("Run without -O: assertions are part of the verifier")
    root = pathlib.Path(__file__).resolve().parent
    output = root / "audit-2026-11-05"
    output.mkdir(exist_ok=True)
    results = []
    for name in SCRIPTS:
        started = time.monotonic()
        try:
            result = subprocess.run([sys.executable, str(root/name)], capture_output=True,
                                    text=True, encoding="utf-8", errors="replace", timeout=180)
            transcript = result.stdout + "\nSTDERR:\n" + result.stderr
            log = output / (name + ".txt")
            log.write_text(transcript,encoding="utf-8")
            entry = {"script": name, "exit_code": result.returncode,
                     "seconds": round(time.monotonic()-started, 3),
                     "script_sha256": hashlib.sha256((root/name).read_bytes()).hexdigest(),
                     "log": log.name, "log_sha256": hashlib.sha256(log.read_bytes()).hexdigest()}
        except subprocess.TimeoutExpired:
            entry = {"script": name, "exit_code": None, "timeout_seconds": 180}
        results.append(entry)
        print(json.dumps(entry), flush=True)
    passed = all(item["exit_code"] == 0 for item in results)
    report = {"status": "PASS_FINITE_CHECKS" if passed else "FAIL", "python": sys.version,
              "executable": sys.executable, "results": results,
              "limitations": "Finite exact computations do not prove the universal conjecture or general sharpness."}
    (output/"results.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
