# SUMUWW · 节点运行

节点通常建立 10 个出站连接，大部分用于中继区块和交易。它可以使用已验证的备用连接中继区块，也可以临时打开第 11 个连接来发现其他节点。连接总数上限为 125。入站连接最多 117 个，有 10 个出站连接时最多 115 个。 桌面版现在只显示已连接节点的总数。 每台挖矿设备自行构建区块。电脑节点转发已完成的区块，并拒绝手机发来的挖矿任务请求和计算结果。

重启后，节点从本地上次验证的区块继续，检查新区块。如果保存的验证记录缺失或不一致，节点会重新验证已保存的历史记录。

SUMUWW PC 0.57.61 · 节点负责验证、保存、传播和查询链上数据。

## 网络与地址

公开网络为 `sumuww`，内部别名为 `dora`。请核对下方创世区块哈希。原生地址采用 witness v0 P2WPKH，以及压缩 secp256k1 公钥的 HASH160。无需强制 memo 或 tag。应拒绝网络错误或校验和无效的地址。记录 HD 收款/找零分支及索引，不要假定与 Bitcoin 的派生路径相同。

## 认证与限制

明确启用 RPC，使用数字回环地址 `127.0.0.1:18443` 及私有 Bearer token。不提供钱包解锁或远程签名。通过本地服务或已认证隧道连接；拒绝浏览器 Origin/Referer 请求。JSON-RPC 使用 POST `/rpc`、对象/数组 `params` 及 `id`；通知返回 HTTP 204。限制：请求体 8004096 字节、头部 8192 字节、批量 16、并发 16、期限 10 秒；limit 1–1000、offset 0–1000000。共有 28 个方法及 11 条 REST 路由。

## 交易与区块查询

`getrawtransaction` 查询活跃链及内存池，不查询仅存在于孤立分支的交易。输入指向之前的输出，并非唯一发送地址。`getblock` 的 `verbose` 为布尔值；已保存的非活跃块为 `active=false`、`confirmations=-1`，仍可用区块哈希取得原始交易。`findspendingtransaction` 仅查活跃链上已确认的花费，null 不证明可用。还需查询 `include_mempool=true` 的 `gettxout`。确认数及活跃状态都可能随重组改变。

## 验证

安装依赖后，从源码运行 python examples/node_contract.py。公开测试密钥和临时 regtest 用于验证提交、拒绝、确认、链重组及数据持久性，不使用真实资金、用户配置或硬件签名器。

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[文档](README.html) · [节点接口](EXCHANGE_INTEGRATION.html) · [RPC 与 HTTP API](RPC_API.html) · [版本说明](RELEASE_NOTES.html) · [验证](EXCHANGE_EXAMPLES.html)

[英文详细参考](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## 交易手续费、确认内容与兼容性

手续费等于输入金额总和减去输出金额总和。只有钱包实际创建符合要求的找零时，估算才计入找零输出。低于钱包找零门槛的余额会计入手续费，确认前会显示最终手续费和总扣款。费率单位为 yugeon/vB；虚拟大小等于交易权重除以四后向上取整。

钱包只选择一次输入和输出，并按同一交易方案生成签名。确认后提交的是已保存的签名交易，不会重新构造交易或重算手续费。报价过期或输入已被花费时，必须重新核对。进入本地待处理队列并不代表已获得区块确认。

普通 P2WPKH 转账使用 low-R、low-S 签名，连同 SIGHASH_ALL 字节在内最多为 71 字节。这是钱包的签名和大小估算策略，并不是对其他有效签名新增的共识限制。签名较短时，实际虚拟大小可能小于估算值。

<!-- /payment-policy-20261116 -->

节点收到有效的版本响应后，会给对端留出发送确认消息的时间。如果两条出站连接通向同一节点，会保留可用路径，直到其中一条完成同步。 
