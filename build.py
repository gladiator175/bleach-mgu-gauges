#!/usr/bin/env python3
"""Build source with the store manifest, then expose a stable package path."""
import json, os, pathlib, shutil, subprocess, sys, tarfile, zipfile
root = pathlib.Path(__file__).resolve().parent
app_id = sys.argv[1] if len(sys.argv) > 1 else 'bleach_hollow'
if app_id != 'bleach_hollow':
    raise SystemExit('Unknown app: ' + app_id)
spec_path = root / 'apps' / app_id / 'app.json'
spec = json.loads(spec_path.read_text())
work = root / '.bleach-build'
if work.exists():
    shutil.rmtree(work)
work.mkdir()
with zipfile.ZipFile(root / 'source.zip') as archive:
    for item in archive.infolist():
        target = (work / item.filename).resolve()
        if os.path.commonpath([str(target), str(work.resolve())]) != str(work.resolve()):
            raise ValueError('Unsafe archive path')
    archive.extractall(work)
# The manifest selected by the store is authoritative, including its version.
shutil.copy2(spec_path, work / 'apps' / app_id / 'app.json')
sdk = root / 'oap-sdk'
if not sdk.exists():
    raise SystemExit('MGU Store must supply the owner unit SDK')
(work / 'oap-sdk').symlink_to(sdk, target_is_directory=True)
subprocess.run([sys.executable, str(work / 'kit/tools/build.py'), app_id], cwd=work, check=True)
package = work / 'dist' / (app_id + '@' + spec['version'] + '.tgz')
if not package.is_file():
    raise SystemExit('Builder did not produce ' + str(package))
with tarfile.open(package, 'r:gz') as archive:
    metadata = json.load(archive.extractfile('package/package.json'))
    if metadata['name'] != app_id or metadata['version'] != spec['version']:
        raise SystemExit('Built package identity does not match store manifest')
out = root / 'dist'
out.mkdir(exist_ok=True)
shutil.copy2(package, out / (app_id + '.tgz'))
shutil.copy2(package, out / package.name)
print('Store output: dist/' + app_id + '.tgz (version ' + spec['version'] + ')')
