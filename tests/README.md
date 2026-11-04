# Offline geometry conversion tests

The aggregate patch retains the original ten cases and the prior four
conversion-contract cases, then adds four cases for closed 3D line topology and
empty LineString/point-cloud behavior.

From the repository root, create an isolated environment and run:

    python3.12 -m venv .venv-offline
    .venv-offline/bin/python -m pip install -r scripts/offline/requirements.lock
    .venv-offline/bin/python scripts/offline/run.py --output /absolute/path/to/evidence

The selected compatible runtime is Python 3.12.3, Shapely 2.1.2, rhino3dm
8.17.0 and NumPy 2.2.6 with the test tools in the lock file. The original
project declares Python ^3.9, Shapely ^2.0.7 and rhino3dm ^8.9.0; this run uses
newer compatible versions and does not represent RhinoHost. It executes the
actual converter functions with the real rhino3dm library and blocks network
socket/DNS access.

The closed-line case checks actual Rhino Polyline closure plus coordinate
order, Z ordinates and planar length after round-trip. Empty line and empty
MultiPoint paths are checked in both conversion directions. In the selected
rhino3dm runtime an empty Rhino PointCloud returns `None` from `GetPoints()`, so
the production forward converter currently raises `TypeError` instead of
returning an empty Shapely MultiPoint. That regression case is intentionally
retained as a failing assertion; no product code or expected value was changed.
Generated runtime evidence and virtual environments belong outside the patch.
