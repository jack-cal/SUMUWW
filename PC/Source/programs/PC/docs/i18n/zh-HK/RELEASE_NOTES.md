# SUMUWW · 版本說明

節點通常會建立 10 個對外連線，大部分用來轉發區塊和交易。節點可透過已驗證的備用連線轉發區塊，亦可暫時開啟第 11 個連線來尋找其他節點。連線總數上限為 125。連入連線最多 117 個，有 10 個對外連線時則最多 115 個。 桌面版現只顯示已連接節點的總數。 每部挖礦裝置自行建立區塊。電腦節點會轉發已完成的區塊，並拒絕手機發出的挖礦工作要求及提交的計算結果。


SUMUWW PC 0.57.53 · 節點負責驗證、儲存、傳播及查詢鏈上資料。

## 簽署格式

可選的原始碼 SDK 毋須密鑰或網絡即可組合交易並驗證傳入的簽署。它不是簽署程式，也不是節點指令。P2WPKH 付款限制只針對範例格式，並非節點。原有個人錢包仍可使用。

## RPC 與 HTTP API

validateaddress 檢查校驗碼及所選網絡。decoderawtransaction 的 decoded_only 只代表解析，不代表簽署有效或交易已確認。OP_RETURN 輸出可保存供外部程式讀取的資料。 節點新增費用查詢、廣播前檢查、RBF 替換狀態，以及按區塊次序讀取數據記錄的功能。替換交易通過驗證後，才會移除原有待確認交易。多重簽署及鎖定輸出已實作，供獨立環境測試啟用，目前尚未在公開網絡啟用。

## 查驗

安裝相依套件後，從原始碼執行 python examples/node_contract.py。公開測試密鑰及臨時 regtest 驗證提交、拒絕、確認、鏈重組及資料保存，不使用真實資金、用戶設定檔或硬件簽署器。

[文件](README.html) · [節點介面](EXCHANGE_INTEGRATION.html) · [RPC 與 HTTP API](RPC_API.html) · [節點運作](NETWORK_RUNBOOK.html) · [查驗](EXCHANGE_EXAMPLES.html)

[英文詳細參考](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)
