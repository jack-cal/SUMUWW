# SUMUWW Android 0.6.103 · RPC 與 HTTP API

SUMUWW Android 0.6.103 · 節點負責驗證、儲存、傳播與查詢鏈上資料。

API 規格描述內建節點核心。Android 應用程式沒有 RPC 設定畫面。

## RPC 與 HTTP API

validateaddress 檢查校驗碼與所選網路。decoderawtransaction 的 decoded_only 僅表示解析，不代表簽章有效或交易已確認。OP_RETURN 輸出可儲存供外部程式讀取的資料。 節點新增費用查詢、廣播前檢查、RBF 替換狀態，以及依區塊順序讀取資料紀錄的功能。替換交易通過驗證後，才會移除原有待確認交易。多重簽章與鎖定輸出已實作，供獨立環境進行啟用測試，目前尚未在公開網路啟用。

## 金額與可用輸出

`_units` 為最小單位整數，`_smw` 為 8 位小數字串，`_dora` 為相容別名。不存在 `_sumuww` 金額欄位。1 SMW = 100000000 單位。`gettxout` 沒有 `spendable`，可能回傳未成熟 coinbase 輸出。要在下一區塊花費，至少須 100 次確認。依 `spendable` 篩選 `listunspent`；`getaddressbalance` 的 available 金額排除未成熟及已被待處理交易占用的資金。記憶池新輸出不是已確認資金。分頁時檢查鏈頂並重新驗證所選輸入。

1 SMW = 100,000,000 yugeon。自動費用依本機觀測提供慢速、一般與快速選項，但不保證確認時間。也可手動輸入 yugeon/vB 費率。傳送前請核對以 SMW 顯示的最終費用與總額。遭拒絕的交易不會扣減餘額。

`1 yugeon = 0.00000001 SMW` · `1 SMW = 100000000 yugeon`

| API / wallet | yugeon / SMW |
|---|---|
| minimum relay | 1 yugeon/vB |
| automatic cap | 0.01 SMW |
| manual cap | 1 SMW |
| manual rate | 1–100000 yugeon/vB |

自動手續費依目前待處理資料量、區塊容量和交易優先順序計算，不使用歷史區塊的手續費。待處理量較少時維持最低費率。預覽會更新，最終確認時固定手續費。觀測範圍是已連線的本機節點，並非所有節點。

重新啟動錢包後，本節點記錄的交易替換歷史仍會保留。已移除的交易不計入餘額。

挖礦紀錄分別顯示每個區塊的新增發行獎勵、交易手續費獎勵及總獎勵，錢包實際收到的金額另行顯示。若只領取部分獎勵，不會擅自推定兩類獎勵的分配。節點提供 28 個 RPC 方法，包括手續費估算，並驗證及轉發已簽署交易。

## 交易與區塊查詢

`getrawtransaction` 查詢有效鏈及記憶池，不查詢僅存在於孤立分支的交易。輸入指向之前的輸出，並非唯一傳送地址。`getblock` 的 `verbose` 為布林值；已保存的非有效區塊為 `active=false`、`confirmations=-1`，仍可用區塊雜湊取得原始交易。`findspendingtransaction` 僅查有效鏈上已確認的花費，null 不證明可用。還須查詢 `include_mempool=true` 的 `gettxout`。確認數與有效狀態都可能隨重組改變。

| method | params |
|---|---|
| `getblockchaininfo` | `{} / []` |
| `gethtlcinfo` | `{} / []` |
| `getspendinginfo` | `{} / []` |
| `getdatarecords` | `blockhash, offset=0, limit=100` |
| `decodescript` | `hex` |
| `gettxout` | `txid, index, include_mempool=true` |
| `findspendingtransaction` | `txid, index, start_height=0` |
| `getnetworkinfo` | `{} / []` |
| `getblockcount` | `{} / []` |
| `getbestblockhash` | `{} / []` |
| `getblockhash` | `height` |
| `getblock` | `hash, verbose=true` |
| `getrawmempool` | `{} / []` |
| `getmempoolinfo` | `{} / []` |
| `getmempoolpolicy` | `{} / []` |
| `estimatefee` | `vsize=140, mode=normal` |
| `testmempoolaccept` | `hex` |
| `getmempoolentry` | `txid` |
| `gettransactionstatus` | `txid` |
| `getrawtransaction` | `txid, verbose=true` |
| `decoderawtransaction` | `hex` |
| `validateaddress` | `address` |
| `listunspent` | `address, limit=100, offset=0` |
| `getaddressbalance` | `address` |
| `sendrawtransaction` | `hex` |
| `submitblock` | `hex` |
| `getblocktemplate` | `address` |
| `help` | `{} / []` |

| HTTP | URI | JSON |
|---|---|---|
| `GET` | `/api/v1/info` | `—` |
| `GET` | `/api/v1/network` | `—` |
| `GET` | `/api/v1/mempool` | `—` |
| `GET` | `/api/v1/mempool/info` | `—` |
| `GET` | `/api/v1/blocks/{height-or-hash}` | `—` |
| `GET` | `/api/v1/transactions/{txid}` | `—` |
| `GET` | `/api/v1/addresses/{address}/balance` | `—` |
| `GET` | `/api/v1/addresses/{address}/utxos?limit=100&offset=0` | `—` |
| `POST` | `/api/v1/transactions` | `{"hex":"..."}` |
| `POST` | `/api/v1/blocks` | `{"hex":"..."}` |
| `POST` | `/api/v1/mining/template` | `{"address":"..."}` |

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## 交易手續費、確認內容與相容性

手續費等於輸入金額總和減去輸出金額總和。只有錢包實際建立符合門檻的找零時，估算才會計入找零輸出的大小。低於錢包找零門檻的餘額會併入手續費，確認前會顯示最終手續費與總扣款。費率單位為 yugeon/vB；虛擬大小等於交易權重除以四後無條件進位。

錢包只選擇一次輸入與輸出，並依同一筆交易計畫產生簽章。確認後提交的是已儲存的簽署交易，不會重新組合交易或重算手續費。報價逾期或輸入已被花費時，必須重新核對。進入本機待處理佇列，並不代表已獲得區塊確認。

一般 P2WPKH 轉帳使用 low-R、low-S 簽章，連同 SIGHASH_ALL 位元組在內最多 71 位元組。這是錢包的簽章與大小估算政策，並非對其他有效簽章新增的共識限制。簽章較短時，實際虛擬大小可能小於估算值。建議費率仍依本機節點的待處理佇列計算；採用與 Bitcoin 相近的大小計算方式，不表示沿用 Bitcoin 網路的費率。

## Android 簽章相容性

錢包檔案格式、地址及既有代幣均未變更。可以在新應用程式中還原原有的加密錢包備份，繼續使用同一個錢包。 Android 節點 0.6.103 與錢包 1.1.14 使用新產生的發行簽章金鑰，無法覆蓋安裝至使用不同金鑰簽署的舊版本。請先保留舊應用程式及資料，確認已取得錢包的加密備份與有效的復原方式。不要只為強行安裝更新而解除安裝舊應用程式。

<!-- /payment-policy-20261116 -->
