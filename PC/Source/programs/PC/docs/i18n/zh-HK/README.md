# SUMUWW · 文件

SUMUWW PC 0.57.51 · 節點負責驗證、儲存、傳播及查詢鏈上資料。

## 簽署格式

可選的原始碼 SDK 毋須密鑰或網絡即可組合交易並驗證傳入的簽署。它不是簽署程式，也不是節點指令。P2WPKH 付款限制只針對範例格式，並非節點。原有個人錢包仍可使用。

## RPC 與 HTTP API

validateaddress 檢查校驗碼及所選網絡。decoderawtransaction 的 decoded_only 只代表解析，不代表簽署有效或交易已確認。OP_RETURN 輸出可保存供外部程式讀取的資料。 節點新增費用查詢、廣播前檢查、RBF 替換狀態，以及按區塊次序讀取數據記錄的功能。替換交易通過驗證後，才會移除原有待確認交易。多重簽署及鎖定輸出已實作，供獨立環境測試啟用，目前尚未在公開網絡啟用。

## 查驗

安裝相依套件後，從原始碼執行 python examples/node_contract.py。公開測試密鑰及臨時 regtest 驗證提交、拒絕、確認、鏈重組及資料保存，不使用真實資金、用戶設定檔或硬件簽署器。

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[節點介面](EXCHANGE_INTEGRATION.html) · [RPC 與 HTTP API](RPC_API.html) · [節點運作](NETWORK_RUNBOOK.html) · [版本說明](RELEASE_NOTES.html) · [查驗](EXCHANGE_EXAMPLES.html)

[英文詳細參考](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## 交易手續費、確認內容與兼容性

手續費等於輸入金額總和減去輸出金額總和。只有錢包實際建立符合要求的找贖時，估算才計入找贖輸出的大小。低於錢包找贖門檻的餘額會計入手續費，確認前會顯示最終手續費與總扣款。費率單位為 yugeon/vB；虛擬大小是交易權重除以四後向上取整的數值。

錢包只選取一次輸入及輸出，並按同一交易方案產生簽署。確認後提交的是已儲存的簽署交易，不會重新組合交易或重算手續費。報價到期或輸入已被花費時，必須重新核對。進入本機待處理佇列，不代表已獲區塊確認。

一般 P2WPKH 轉賬使用 low-R、low-S 簽署，連同 SIGHASH_ALL 位元組在內最多為 71 位元組。這是錢包的簽署及大小估算政策，並非對其他有效簽署新增的共識限制。簽署較短時，實際虛擬大小可能小於估算值。

<!-- /payment-policy-20261116 -->
