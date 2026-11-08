"""Quick setup check for hx-twin. Run: python scripts\status.py"""
import importlib
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CFD_DIR = Path(r"C:\hx-twin-cfd")


def check(label, ok, hint=""):
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {label}" + ("" if ok else f"  ->  {hint}"))


print("\n=== hx-twin status ===\n")

# 1 - Python is running from the project venv
in_venv = str(REPO / ".venv").lower() in sys.prefix.lower()
check("Running inside project venv", in_venv,
      r"run .\.venv\Scripts\Activate.ps1 first")

# 2 - Required packages import
for pkg in ["numpy", "scipy", "matplotlib", "pandas", "pytest", "ansys.fluent.core"]:
    try:
        importlib.import_module(pkg)
        check(f"Package {pkg}", True)
    except ImportError:
        check(f"Package {pkg}", False, "pip install -r requirements.txt")

# 3 - Git: uncommitted changes?
result = subprocess.run(["git", "status", "--porcelain"], cwd=REPO,
                        capture_output=True, text=True)
clean = result.returncode == 0 and result.stdout.strip() == ""
check("Git working tree clean", clean, "commit or review changes (git status)")

# 4 - Expected files exist
files = {
    "PROGRESS.md": REPO / "PROGRESS.md",
    "Decision log": REPO / "notes" / "decision-log.md",
    "PyFluent check script": REPO / "scripts" / "check_pyfluent.py",
}
for label, path in files.items():
    check(label, path.exists(), f"missing: {path}")

# 5 - Phase 0 engineering work present
derivations = [p for p in (REPO / "notes" / "derivations").glob("*") if p.name != ".gitkeep"]
check("Derivation uploaded to notes\\derivations", bool(derivations),
      "not started yet - see PROGRESS.md")
notebooks = list((REPO / "notebooks").glob("*.ipynb"))
check("Phase 0 problem notebooks", bool(notebooks), "no notebooks yet")

# 6 - Fluent server file (only while Fluent's server is running)
check("Fluent server_info.txt present", (CFD_DIR / "server_info.txt").exists(),
      "only needed for PyFluent: start Fluent + /server/start-server")

print("\nOpen PROGRESS.md for the full checklist.\n")
