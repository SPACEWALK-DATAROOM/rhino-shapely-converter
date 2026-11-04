# Geometry conversion contracts

This aggregate keeps the ten original cases and four prior conversion-contract cases, then adds four unique boundary/topology cases against the actual checkout. Production source is unchanged and imported directly from `src/rhino_shapely_converter`, with no duplicate production package. The original fourteen IDs are rerun unchanged.

## Reproduce

```sh
python3.12 -m venv /absolute/path/to/offline-venv
/absolute/path/to/offline-venv/bin/python -m pip install -r scripts/offline/requirements.lock
/absolute/path/to/offline-venv/bin/python scripts/offline/run.py --output /absolute/path/to/evidence
```

Tests use real Shapely and the real rhino3dm geometry library. They do not launch Rhino/CAD, read/write project documents or call APIs/databases/deployment. Prior checks cover geometry conversion coordinates, default Z, polyline round-trip vertices/length and unsupported geometry errors. New cases check a closed 3D line's ring topology and length, empty LineString round-trip, empty Shapely MultiPoint to Rhino PointCloud, and the inverse empty Rhino PointCloud conversion. The last case currently fails: rhino3dm's empty `GetPoints()` is `None`, which the production converter maps without handling. `added-test-integrity.json` verifies the prior four test functions remain unchanged. Both original files remain byte-identical to base.

The runner explicitly selects those files, disables plugin auto-loading and enables pytest-mock. Its child receives a minimal environment and the offline audit hook rejects socket access. It records commands/environment, JUnit identities, subprocess/coverage exit codes, logs, branch coverage JSON, source/blob hashes, positive execution lines and artifact hashes. Tests or coverage export failing return a failure status. Output belongs outside the repository. The dependency lock describes this tested environment, not all supported historical dependency combinations.

`snapshot.json` pins `8a82d4e0d0d6c6dd3a8aa29ed495549512113f56` on main; all 12 audited blobs match. `source-fixes.json` is empty. `original-test-integrity.json` verifies original tests; `test-identities.json` maps exact observed identities to prior cases, including the old cross-repository module names. `verified-result.json` records actual results/source reach. Imports/definitions, function bodies and asserted behavior are distinct; no whole-repository/archive coverage or CAD design validity is claimed.

Full raw combined evidence is under `/home/josh/code-asset-test-improvement-20261029/evidence/rhino-shapely-converter/combined` on this machine; re-run for independent evidence. This is a local reversible test-only commit. No push/PR, production write or expectation relaxation is included.
