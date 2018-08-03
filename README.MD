# Fomo3D-Terminator

![Demo](https://github.com/Umiiii/Fomo3D-Terminator/blob/master/demo.png)

[中文版本](#Fomo3D终结者)

Fomo3D-Terminator is a toolkit that can help you to buy the last key of Fomo3D games in the Ethereum. Web3 is used for interact with Ethereum contract interaction. Give me star if you like it.

*Warning* : This project is using private key to sign your transaction.  If you don't know what it is , don't use it.

## Environment

Python 3.5+ 

web3

Tested on macOS 10.13.6, Python 3.7, web3 4.4.1

Not sure if Windows also works.

## Instruction

1. `pip -m install requirements.txt`
2. Get your own RPC from infura.io, change `config.py`
3. Fill in with your address and private key in `config.py`
4. Set the number you want in `config.py`
5. `python main.py`
6. Sit down and wait for your ether.

## Hints

1. Fomo short version and other copycat version is also compatible, but you need to change ABI.
2. If you want to ask how to run this Terminator, send at least 0.05 ETH to this address with your contact. Also, donations are welcome : )

​       Address:0xA56D13fcA94aAaA908B5346b3693B21281d2a17A

## To do list

- [ ] Asynchronous transaction query.
- [ ] More safer ways to make transaction.
- [ ] Multiple RPC support.





## Fomo3D终结者

Fomo3D终结者是个帮你自动买Key的工具，使用了Web3作为与智能合约交互的库。如果这个项目帮到了你，不妨给我点个Star。

*警告*：该项目使用你的以太坊私钥来完成交易签名，如果你不知道这意味着什么，请不要使用这个程序。

## 环境

Python3.5+

web3

在 macOS 10.13.6, Python3.7, Web3 4.4.1下测试通过，没测试过 Windows 能不能跑，推荐挂 VPS

## 功能

1. 自动监测当前局势
2. 指定时间自动无限次抢 Key
3. （待实现）多线程同时抢 Key

## 使用指南

1. `pip -m install requirements.txt`
2. 去 infura.io 申请一个 RPC 地址, 然后填到 `config.py` 里面
3. 把你钱包的地址和私钥填到  `config.py`里面
4. 在 `config.py` 中修改 Gas, Gas Limit 和最后抢key时间
5. 运行`python main.py`
6. 坐等大奖到手。

## 提示

1. 该脚本也同样适用于*所有* Fomo3D的衍生版本，包括短版。你可能需要手动修改ABI

2. 任何部署的技术问题，请先自行百度/谷歌，作者已经与百度/谷歌达成战略合作，只需要将问题输入，即可获取答案。如果还是想问的话，请先发送至少0.05ETH到这个地址，附上你的联系方式，作者会联系你：）

   0xA56D13fcA94aAaA908B5346b3693B21281d2a17A