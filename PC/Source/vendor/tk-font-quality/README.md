# Windows Tk font rendering repair

The Windows build includes Tk 8.6.12 with the one-line patch in
`tkWinFont-quality.patch`. Version 0.57.5 explicitly requests ClearType
rather than the grayscale antialiasing forced in 0.57.4. Font families,
point sizes, weights, text and colors are unchanged. Windows may choose a
fallback when ClearType is unavailable on the display.

DORA's GUI executable declares system DPI awareness so Windows does not
bitmap-stretch the entire window at the system display scale. Source entry
points select the same awareness before creating a Tk window. Neither action
changes system font smoothing, display settings or firewall rules.

The default quality mode caused indefinite GDI font realization waits on the
audited host. ClearType must pass the same native painting and functional
checks as well as screenshot review; passing functional tests alone does not
establish visual sharpness.

`SOURCES.json` records upstream archives, compiler and resulting DLL hashes.
The upstream license is retained in `LICENSE.txt`. This is a DORA-patched
build, not an unmodified upstream binary.

To rebuild with w64devkit on Windows AMD64:

1. Download and verify the Tcl/Tk 8.6.12 archives and compiler listed in
   `SOURCES.json`; extract them in a working directory without spaces.
2. Add the compiler's `bin` to PATH. Set `PATH_SEPARATOR=;`, `CC=gcc.exe`,
   `AR=ar.exe`, `RANLIB=ranlib.exe` and `RC=windres.exe` for its native shell.
3. In `tcl-core-8-6-12/win`, run `sh configure --host=x86_64-w64-mingw32
   --enable-threads --enable-64bit --prefix=<absolute-install-directory>`,
   then `make -j4`.
4. Apply `tkWinFont-quality.patch` to the Tk source. In its `win` directory,
   run the same configure command with
   `--with-tcl=<absolute-tcl-source-directory>/win`, then `make -j4`.
5. Copy the resulting `tk86.dll` here as `tk86t.dll`. The official Tk 8.6.12
   script library used by the frozen build must match the native DLL.
6. Rebuild DORA using the packaged Windows build specification, then run the
   full tests with the same DLL and verify the frozen artifact separately.

No system font installation, font substitution, system DLL replacement,
firewall change or administrator privilege is required.

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. Rate suggestions still use the local pending queue; matching Bitcoin's sizing approach does not mean using Bitcoin's fee rates.

## Windows I2P component and security checks

Windows packages include official i2pd 3.0.0 with matching hashes and reseed certificates. Defender still detects the upstream I2P executable and ZIP in the recorded test. A matching upstream hash does not prove safety or establish a false positive. Any local file exception applies only to the computer where it is registered and is not installed by the public package. Other computers may block the same files.

<!-- /payment-policy-20261116 -->
