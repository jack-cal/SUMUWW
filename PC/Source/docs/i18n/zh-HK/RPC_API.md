# SUMUWW · RPC 與 HTTP API

SUMUWW PC 0.57.51 · 節點負責驗證、儲存、傳播及查詢鏈上資料。

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

[文件](README.html) · [節點介面](EXCHANGE_INTEGRATION.html) · [節點運作](NETWORK_RUNBOOK.html) · [版本說明](RELEASE_NOTES.html) · [查驗](EXCHANGE_EXAMPLES.html)

[英文詳細參考](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## 交易手續費、確認內容與兼容性

手續費等於輸入金額總和減去輸出金額總和。只有錢包實際建立符合要求的找贖時，估算才計入找贖輸出的大小。低於錢包找贖門檻的餘額會計入手續費，確認前會顯示最終手續費與總扣款。費率單位為 yugeon/vB；虛擬大小是交易權重除以四後向上取整的數值。

錢包只選取一次輸入及輸出，並按同一交易方案產生簽署。確認後提交的是已儲存的簽署交易，不會重新組合交易或重算手續費。報價到期或輸入已被花費時，必須重新核對。進入本機待處理佇列，不代表已獲區塊確認。

一般 P2WPKH 轉賬使用 low-R、low-S 簽署，連同 SIGHASH_ALL 位元組在內最多為 71 位元組。這是錢包的簽署及大小估算政策，並非對其他有效簽署新增的共識限制。簽署較短時，實際虛擬大小可能小於估算值。建議費率仍按本機節點的待處理佇列計算；採用與 Bitcoin 相近的大小計算方式，不表示使用 Bitcoin 網絡的費率。

## Windows I2P 組件及安全檢查

Windows 套件包含官方 i2pd 3.0.0，並更新雜湊值及初始連線所需的憑證。在已記錄的檢查中，Defender 仍會偵測官方 I2P 執行檔及原始 ZIP。雜湊值與官方相符，並不能證明安全或確定是誤報。本機檔案排除設定只適用於登記設定的電腦，公開套件不會自動加入排除設定；其他電腦仍可能封鎖同一批檔案。

<!-- /payment-policy-20261116 -->
