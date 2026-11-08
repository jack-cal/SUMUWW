# SUMUWW Android 0.6.98 · 版本說明

手機會連接運行 0.57.49 或更新版本的 SUMUWW 完整節點，在本機核對獎勵及計算工作量證明，毋須下載整條鏈的交易記錄。

API 規格描述內置節點核心。Android 應用程式沒有 RPC 設定畫面。

## RPC 與 HTTP API

validateaddress 檢查校驗碼及所選網絡。decoderawtransaction 的 decoded_only 只代表解析，不代表簽署有效或交易已確認。OP_RETURN 輸出可保存供外部程式讀取的資料。 節點新增費用查詢、廣播前檢查、RBF 替換狀態，以及按區塊次序讀取數據記錄的功能。替換交易通過驗證後，才會移除原有待確認交易。多重簽署及鎖定輸出已實作，供獨立環境測試啟用，目前尚未在公開網絡啟用。

[API_CONTRACT.json](../../../API_CONTRACT.json)
