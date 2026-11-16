# SUMUWW · 節點介面

SUMUWW PC 0.57.51 · 節點負責驗證、儲存、傳播及查詢鏈上資料。

## 網絡與地址

公開網絡為 `sumuww`，內部別名為 `dora`。請核對下方創世區塊雜湊。原生地址採用 witness v0 P2WPKH，以及壓縮 secp256k1 公鑰的 HASH160。無須強制 memo 或 tag。應拒絕網絡錯誤或檢查碼無效的地址。記錄 HD 收款/找零分支及索引，不要假定與 Bitcoin 的衍生路徑相同。

## 簽署格式

可選的原始碼 SDK 毋須密鑰或網絡即可組合交易並驗證傳入的簽署。它不是簽署程式，也不是節點指令。P2WPKH 付款限制只針對範例格式，並非節點。原有個人錢包仍可使用。

## RPC 與 HTTP API

validateaddress 檢查校驗碼及所選網絡。decoderawtransaction 的 decoded_only 只代表解析，不代表簽署有效或交易已確認。OP_RETURN 輸出可保存供外部程式讀取的資料。 節點新增費用查詢、廣播前檢查、RBF 替換狀態，以及按區塊次序讀取數據記錄的功能。替換交易通過驗證後，才會移除原有待確認交易。多重簽署及鎖定輸出已實作，供獨立環境測試啟用，目前尚未在公開網絡啟用。

## 驗證與限制

明確啟用 RPC，使用數字回送地址 `127.0.0.1:18443` 及私有 Bearer token。不提供錢包解鎖或遠端簽署。透過本機服務或已驗證通道連線；拒絕瀏覽器 Origin/Referer 請求。JSON-RPC 使用 POST `/rpc`、物件/陣列 `params` 及 `id`；通知回傳 HTTP 204。限制：本文 8004096 位元組、標頭 8192、批次 16、同時請求 16、期限 10 秒；limit 1–1000、offset 0–1000000。共有 28 個方法及 11 條 REST 路由。

## 金額與可用輸出

`_units` 為最小單位整數，`_smw` 為 8 位小數字串，`_dora` 為相容別名。不存在 `_sumuww` 金額欄位。1 SMW = 100000000 單位。`gettxout` 沒有 `spendable`，可能回傳未成熟 coinbase 輸出。要在下一區塊花費，至少須 100 次確認。依 `spendable` 篩選 `listunspent`；`getaddressbalance` 的 available 金額排除未成熟及已被待處理交易占用的資金。記憶池新輸出不是已確認資金。分頁時檢查鏈頂並重新驗證所選輸入。

1 SMW = 100,000,000 yugeon。自動費用按本機觀測提供慢速、一般及快速選項，但不保證確認時間。你亦可手動輸入 yugeon/vB 費率。發送前請核對以 SMW 顯示的最終費用及總額。被拒絕的交易不會扣減餘額。

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

自動手續費按目前待處理數據量、區塊容量及交易優先次序計算，不採用過往區塊的手續費。待處理量較少時維持最低費率。預覽會更新，最後確認時固定手續費。觀測範圍是已連線的本機節點，並非所有節點。

重新啟動錢包後，本節點記錄的交易替換歷史仍會保留。已移除的交易不計入結餘。

挖礦紀錄分別顯示每個區塊的新增發行獎勵、交易手續費獎勵和總獎勵，錢包實際收到的金額會另外顯示。若只領取部分獎勵，系統不會自行推定兩類獎勵的分配。節點提供 28 個 RPC 方法，包括手續費估算，並驗證及轉發已簽署交易。

## 交易與區塊查詢

`getrawtransaction` 查詢有效鏈及記憶池，不查詢僅存在於孤立分支的交易。輸入指向之前的輸出，並非唯一傳送地址。`getblock` 的 `verbose` 為布爾值；已保存的非有效區塊為 `active=false`、`confirmations=-1`，仍可用區塊雜湊取得原始交易。`findspendingtransaction` 僅查有效鏈上已確認的花費，null 不證明可用。還須查詢 `include_mempool=true` 的 `gettxout`。確認數與有效狀態都可能隨重組改變。

## 查驗

安裝相依套件後，從原始碼執行 python examples/node_contract.py。公開測試密鑰及臨時 regtest 驗證提交、拒絕、確認、鏈重組及資料保存，不使用真實資金、用戶設定檔或硬件簽署器。

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[文件](README.html) · [RPC 與 HTTP API](RPC_API.html) · [節點運作](NETWORK_RUNBOOK.html) · [版本說明](RELEASE_NOTES.html) · [查驗](EXCHANGE_EXAMPLES.html)

[英文詳細參考](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## 交易手續費、確認內容與兼容性

手續費等於輸入金額總和減去輸出金額總和。只有錢包實際建立符合要求的找贖時，估算才計入找贖輸出的大小。低於錢包找贖門檻的餘額會計入手續費，確認前會顯示最終手續費與總扣款。費率單位為 yugeon/vB；虛擬大小是交易權重除以四後向上取整的數值。

錢包只選取一次輸入及輸出，並按同一交易方案產生簽署。確認後提交的是已儲存的簽署交易，不會重新組合交易或重算手續費。報價到期或輸入已被花費時，必須重新核對。進入本機待處理佇列，不代表已獲區塊確認。

一般 P2WPKH 轉賬使用 low-R、low-S 簽署，連同 SIGHASH_ALL 位元組在內最多為 71 位元組。這是錢包的簽署及大小估算政策，並非對其他有效簽署新增的共識限制。簽署較短時，實際虛擬大小可能小於估算值。建議費率仍按本機節點的待處理佇列計算；採用與 Bitcoin 相近的大小計算方式，不表示使用 Bitcoin 網絡的費率。

## Windows I2P 組件及安全檢查

Windows 套件包含官方 i2pd 3.0.0，並更新雜湊值及初始連線所需的憑證。在已記錄的檢查中，Defender 仍會偵測官方 I2P 執行檔及原始 ZIP。雜湊值與官方相符，並不能證明安全或確定是誤報。本機檔案排除設定只適用於登記設定的電腦，公開套件不會自動加入排除設定；其他電腦仍可能封鎖同一批檔案。

<!-- /payment-policy-20261116 -->
