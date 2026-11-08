# SUMUWW · 版本說明

節點通常建立 10 個對外連線，大部分用來轉送區塊和交易。節點可以透過已驗證的備用連線轉送區塊，也可以暫時開啟第 11 個連線來尋找其他節點。連線總數上限為 125。連入連線最多 117 個，有 10 個對外連線時則最多 115 個。 桌面版現在只顯示已連線節點的總數。 每台挖礦裝置自行建立區塊。電腦節點會轉送已完成的區塊，並拒絕手機提出的挖礦工作請求及送出的計算結果。

重新啟動後，節點會從上次在本機驗證的區塊繼續，檢查新區塊。如果儲存的驗證紀錄遺失或資料不符，節點會重新驗證已儲存的歷史紀錄。


SUMUWW PC 0.57.54 · 節點負責驗證、儲存、傳播與查詢鏈上資料。

## 簽章格式

選用的原始碼 SDK 不需金鑰或網路即可組合交易並驗證傳入的簽章。它不是簽署程式，也不是節點指令。P2WPKH 支付限制只針對範例格式，不針對節點。原有個人錢包仍可使用。

## RPC 與 HTTP API

validateaddress 檢查校驗碼與所選網路。decoderawtransaction 的 decoded_only 僅表示解析，不代表簽章有效或交易已確認。OP_RETURN 輸出可儲存供外部程式讀取的資料。 節點新增費用查詢、廣播前檢查、RBF 替換狀態，以及依區塊順序讀取資料紀錄的功能。替換交易通過驗證後，才會移除原有待確認交易。多重簽章與鎖定輸出已實作，供獨立環境進行啟用測試，目前尚未在公開網路啟用。

## 查驗

安裝相依套件後，從原始碼執行 python examples/node_contract.py。公開測試金鑰與暫時 regtest 驗證提交、拒絕、確認、鏈重組及資料保存，不使用真實資金、使用者設定檔或硬體簽署器。

[文件](README.html) · [節點介面](EXCHANGE_INTEGRATION.html) · [RPC 與 HTTP API](RPC_API.html) · [節點運作](NETWORK_RUNBOOK.html) · [查驗](EXCHANGE_EXAMPLES.html)

[英文詳細參考](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
