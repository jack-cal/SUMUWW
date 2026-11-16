"""Sign an APK with the separately stored 2026-11-16 release identity."""
import argparse, os, subprocess
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('apk',type=Path)
p.add_argument('output',type=Path)
a=p.parse_args()
private=Path(os.environ['SUMUWW_SIGNING_DIR'])
sdk=Path(os.environ['ANDROID_SDK_ROOT'])
tool=sdk/'build-tools/35.0.0/apksigner.bat'
subprocess.run([str(tool),'sign','--ks',str(private/'sumuww-release-20261116.p12'),
 '--ks-key-alias','sumuww-release','--ks-pass','file:'+str(private/'password.txt'),
 '--v4-signing-enabled','false','--out',str(a.output),str(a.apk)],check=True)
subprocess.run([str(tool),'verify','--verbose','--print-certs',str(a.output)],check=True)
