# SUMUWW · 文件

使用一筆 1 SMW 的輸入時，手續費會隨是否需要找零而改變。假設輸入和輸出都是 P2WPKH，費率為 1 yugeon/vB，傳送 0.99999890 SMW 時不用找零，手續費為 110 yugeon。用同一筆輸入傳送 0.8 SMW 時，會多一個找零輸出，手續費為 141 yugeon。扣除手續費後，餘額達到找零的最低金額，錢包才會找零。這項門檻將日後花用這筆找零的成本也算在內。低於門檻的餘額會計入送出前顯示的手續費。估算原生隔離見證（P2WPKH）錢包輸入的大小時，簽章連同雜湊類型最多以 71 位元組計算。

SUMUWW PC 0.57.51 · 節點負責驗證、儲存、傳播與查詢鏈上資料。

## 簽章格式

選用的原始碼 SDK 不需金鑰或網路即可組合交易並驗證傳入的簽章。它不是簽署程式，也不是節點指令。P2WPKH 支付限制只針對範例格式，不針對節點。原有個人錢包仍可使用。

## RPC 與 HTTP API

validateaddress 檢查校驗碼與所選網路。decoderawtransaction 的 decoded_only 僅表示解析，不代表簽章有效或交易已確認。OP_RETURN 輸出可儲存供外部程式讀取的資料。 節點新增費用查詢、廣播前檢查、RBF 替換狀態，以及依區塊順序讀取資料紀錄的功能。替換交易通過驗證後，才會移除原有待確認交易。多重簽章與鎖定輸出已實作，供獨立環境進行啟用測試，目前尚未在公開網路啟用。

## 查驗

安裝相依套件後，從原始碼執行 python examples/node_contract.py。公開測試金鑰與暫時 regtest 驗證提交、拒絕、確認、鏈重組及資料保存，不使用真實資金、使用者設定檔或硬體簽署器。

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[節點介面](EXCHANGE_INTEGRATION.html) · [RPC 與 HTTP API](RPC_API.html) · [節點運作](NETWORK_RUNBOOK.html) · [版本說明](RELEASE_NOTES.html) · [查驗](EXCHANGE_EXAMPLES.html)

[英文詳細參考](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## 交易手續費、確認內容與相容性

手續費等於輸入金額總和減去輸出金額總和。只有錢包實際建立符合門檻的找零時，估算才會計入找零輸出的大小。低於錢包找零門檻的餘額會併入手續費，確認前會顯示最終手續費與總扣款。費率單位為 yugeon/vB；虛擬大小等於交易權重除以四後無條件進位。

錢包只選擇一次輸入與輸出，並依同一筆交易計畫產生簽章。確認後提交的是已儲存的簽署交易，不會重新組合交易或重算手續費。報價逾期或輸入已被花費時，必須重新核對。進入本機待處理佇列，並不代表已獲得區塊確認。

一般 P2WPKH 轉帳使用 low-R、low-S 簽章，連同 SIGHASH_ALL 位元組在內最多 71 位元組。這是錢包的簽章與大小估算政策，並非對其他有效簽章新增的共識限制。簽章較短時，實際虛擬大小可能小於估算值。

<!-- /payment-policy-20261116 -->
