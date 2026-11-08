# Progress

Last worked on: 2026-11-08 - Checks 1-5 passed; next is Check 6 (Azure)

## Phase 0 - Groundwork

### Setup
- [x] GitHub repo + folder skeleton
- [x] Repo at C:\hx-twin-cfd\digital-twin, venv rebuilt
- [x] Python packages installed (incl. PyFluent 0.43.0)
- [x] Fluent opens from launcher with no licence error
- [x] PyFluent connects to running Fluent (scripts\check_pyfluent.py)
- [ ] Azure credit loaded, resource group + budget alert
- [ ] ADT Explorer quickstart done

### Engineering
- [ ] Counterflow e-NTU derived by hand (photo in notes\derivations)
- [ ] Problem 1 - counterflow rating
- [ ] Problem 2 - shell-and-tube rating
- [ ] Problem 3 - e-NTU vs LMTD-F check
- [ ] Problem 4 - my SolidWorks CFD case (compare with Claude's values)
- [ ] One Fluent CHT tutorial done
- [ ] Decision log D-001 to D-004 reasons written

## Notes / blockers
- Fluent: start from the launcher, NOT from Python (Student licence error). Then /server/start-server in the console.
- Always close Fluent with File -> Exit (a stuck session blocks the licence).
- Fluent working directory: C:\hx-twin-cfd (outside the repo).
- Save packages with: pip freeze | Set-Content -Encoding ascii requirements.txt
- Moved or renamed the repo folder? Rebuild the venv.
