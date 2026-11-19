# Maintaining translated integration documents

 The `exchange/` directory contains directly authored
text for all 34 application languages, including separate Traditional Chinese
regional editions and both Mongolian scripts. Do not replace an edition with
an English redirect or use an external automatic translation service.

Each catalog contains 19 navigation/section labels and 14 substantive paragraphs.
Their stable positions are defined by `TEXT_HEADINGS` in
`packaging/generate_exchange_documents.py`. Apply factual corrections to every
catalog before rendering. Literal API names, JSON keys, executable commands and
test vectors are shared and must remain byte-identical across editions.

From the source root, run the generator with the documentation-only dependency
`Markdown==3.7`. This dependency is not needed by the node or wallet runtime.

```powershell
python packaging/generate_exchange_documents.py
```

The generator writes six current-update topics in Markdown and HTML into both
`docs/i18n/` and `programs/PC/docs/i18n/`, an English default index, metadata and a
file-hash manifest. The extended English references remain at their original
paths. The translated scope covers the current integration update, not all
historical whitepapers or release history. Repackage documentation alongside the
unchanged verified executable when only documentation changes.

<!-- payment-policy-20261116 -->

## Payment fees, reviewed transactions and compatibility

The fee is the sum of inputs minus the sum of outputs. A payment quote includes a change output only when the wallet will actually create viable change. A remainder below the wallet's change threshold is added to the fee, and the resulting fee and total debit are shown for review. Rates are expressed in yugeon/vB; virtual size is transaction weight divided by four, rounded up.

The wallet selects the inputs and outputs once and signs that same payment plan. Confirmation submits the stored signed transaction without rebuilding it or recalculating its fee. An expired quote or inputs spent in the meantime require a new review. Submission to the local queue is not confirmation in a block.

For ordinary P2WPKH payments, the wallet generates low-R, low-S signatures of at most 71 bytes including the SIGHASH_ALL byte. This is a signing and size-estimation policy, not a new consensus limit on other valid signatures. Shorter signatures can make the actual virtual size smaller than the estimate. 

<!-- /payment-policy-20261116 -->
