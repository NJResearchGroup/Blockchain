# Blockchain
## 加密算法实现
<br> symmetric cryptography.py 文件基于Anaconda anaconda3-4.1.0 中Crypto.Cipher包里的AES方法进行对称加密
<br> asymmetric cryptography.py 文件基于Anaconda anaconda3-4.1.0 中rsa包里的方法进行非对称加密
### 1. 首先，需要安装Python3.5+版本的Python解释器，或者直接使用内嵌Python解释器的Anaconda3 科学计算工具；
<br> 使用PyCharm 2018.1.4 (Professional Edition)作为实验的集成开发环境进行调试。
### 2. 安装Crypto:
<br> a. 首先
```pip install Crypto```
<br> b. 接下来
```pip install pycrypto```
<br> c. 最后尝试
```from Crypto.Cipher import AES```
<br> 如果成功，就说明安装成功，同时可以在本地调用AES包对代码进行测试。
### 3. 安装rsa
<br> 安装rsa时，只需在命令行中
```pip install rsa```
<br> 在工具全部安装好之后，即可进行对asymmetric cryptography.py和symmetric cryptography.py文件的测试
<br> 代码与函数具体功能代码注释中已标明

## 在geth客户端上搭建私有链
<br> [Solidity在线IDE](http://remix.ethereum.org/)
<br> msg_to_Tony.sol 使用solidity实现传输信息的智能合约，以Tony用户为例。
<br> solidity脚本在Remix上编译成功后，将编译后的js代码拷贝至在geth客户端上的以太坊私有链的JavaScript Console中，实现智能合约的布置。

## 智能合约实验说明

### 实验环境：
<br> 操作系统 Ubuntu 18.04 LTS
<br> go version go1.10.1 linux/amd64
<br> geth version: 1.8.11-stable
<br> Truffle v4.1.12 (core: 4.1.12)
<br> Solidity v0.4.23 (solc-js)

### 1.安装Go
```sudo add-apt-repository ppa:gophers/go sudo apt-get update sudo apt-get install golang-stable```

### 2.安装Geth
<br>从geth项目源码中构建
<br>将github上的geth项目仓库克隆到本地目录中
```$ git clone https://github.com/ethereum/go-ethereum```

<br> (上一步如果没有安装git语言需要先安装
```
$ sudo add-apt-repository ppa:git-core/ppa
$ sudo apt-get update
$ sudo apt-get install git)
```
<br> 安装Go和C编辑器
```$ sudo apt-get install -y build-essential golang```

<br> 构建geth
```
$ cd go-ethereum
$ make geth
```

### 3.私有链搭建
<br> 启动geth客户端（JavaScript Console）
```$ geth --datadir testNet --dev --rpc  console 2>> test.log```

<br>这里 –dev代表进入开发者模式，--rpc代表开启本地rpc端口8545，后面编辑truffle.js文件需要用到。

<br>配置创世块genesis.json
```
{
 "nonce":"0x0000000000000048",
 "mixhash":"0x0000000000000000000000000000000000000000000000000000000000000000",
 "difficulty": "0x200000",
 "alloc": {},
 "coinbase":"0x0000000000000000000000000000000000000000",
 "timestamp": "0x00",
 "parentHash":"0x0000000000000000000000000000000000000000000000000000000000000000",
 "extraData": "",
 "gasLimit":"0xffffffff",
 "config":{
	 "chainID":10,
	 "homesteadBlock":0,
	 "eip155Block":0,
	 "eip158Block":0
 }
}
```

<br>config.chainID: 区块链的ID，在 geth 命令中的 --networkid 参数需要与 chainId 的值一致。
<br>config.homesteadBlock: Homestead 硬分叉区块高度，不需要关注。
<br>config.eip155Block: EIP 155 硬分叉高度，不需要关注。
<br>config.eip158Block: EIP 158 硬分叉高度，不需要关注。
<br>coinbase: 矿工账号，第一个区块挖出后将给这个矿工账号发送奖励的以太币。
<br>difficulty: 难度值，越大越难。
<br>extraData: 附加信息随便填。
<br>gasLimit: gas 的消耗总量限制，用来限制区块能包含的交易信息总和。这里我们填最大值0xffffffff，与后面智能合约被部署到链上后能否被挖到有关联。<br>nonce: 一个 64 位随机数。
<br>mixhash: 与 nonce 配合用于挖矿，由上一个区块的一部分生成的 hash。
<br>parentHash: 上一个区块的 hash 值。
<br>alloc: 预设账号以及账号的以太币数量，私有链挖矿比较容易可以不配置。

<br>当私有链网络的初始状态在JSON文件中定义好之后，我们就可以初始化私有链
```$ geth init /home/supreme_daryl/eth/genesis.json```
            <br>（这里可以根据自己的创世块配置文件路径自己修改。）
<br>私有链搭建成功。

### 4.智能合约开发框架搭建

<br> 配置安装Truffle框架
```$ npm install -g truffle```

<br> 因为防火墙的原因，从源安装truffle可能会很慢，这时可以先设置一个淘宝源再下载安装
```
$ npm config set registry https://registry.npm.taobao.org
$ npm install -g truffle
```

<br>（如果上一步没有安装npm和nodejs需要先安装npm和nodejs
<br> 先上官网https://nodejs.org/dist/下载相应版本的安装包
```
$ tar xvf node-v9.8.0.tar.gz
$ cd node-v9.8.0
$ ./configure
$ make
$ make install）
```

<br> solidity是以太坊智能合约的开发语言，开发测试智能合约，需要安装solc
```
$ sudo add-apt-repository ppa:ethereum/ethereum
$ sudo apt-get update
$ sudo apt-get install solc
```

### 5.Geth客户端准备
<br> 启动geth客户端
```$ geth --datadir testNet --dev --rpc  console 2>> test.log （将运行日志记录到test.log中）```

<br> 查看网络中的账户结点
```$ eth.accounts```

<br> 新建账户
```$ personal.newAccount("daryl")```

<br> 解锁账户
```
$ personal.unlockAccount(eth.accounts[1], "daryl", 15000)
$ personal.unlockAccount(eth.accounts[0], "", 15000)
```

<br> 开始挖矿
```$ miner.start()```
<br> 这里通常会出现返回值为null的bug，目前网上和各大论坛中没有较好较成熟的解决方案，大家都在讨论解决，且Geth客户端的—dev开发者版本目前也没有一个明确的官网文档指导。
<br> 目前摸索出的可行的方案是，将创世区块中的gasLimit设置为最大值即0xffffffff。

<br> 过一会会看到账户地址的余额增加，将账户地址赋值给变量acc0，便于后续操作
```$ acc0 = web3.eth.accounts[0]```

### 6.创建，编译，部署合约

<br> 首先创建智能合约的本地目录
```
$ sudo mkdir msg_to_Kevin
$ cd msg_to_Kevin
```

<br> 初始化一个智能合约项目
```$ sudo truffle init```

<br> 初始化成功后，在本地将拥有如下目录
<br> contracts 智能合约目录
<br> migrations 发布脚本目录
<br> test 存放测试文件
<br> truffle.js Truffle的配置文件

<br> 创建一个msg_to_Kevin合约并编译，在contracts目录中新建一个msg_to_Tony.sol文件，编写代码如下
```
pragma solidity ^0.4.24;


contract Msg_to_Tony {
 
  //say msg to Tony
  function key() public pure returns (string) {
      return "3ae07527e5564346cb3ed92547175d0779cebb2f4788726af070086c7e71bae5e32ddba3c759ed6006af0b84b01f1deaae311a7855bcf4e1bc33258d3c0fefa6";
  }
  function A() public pure returns (string) {
    return "164872f0a0f63e828a62c9457f232d6f2895e18dc71c4a80595f3321c65a45770d2bce9cd2d9c04912dfbd4171821b8b96c11eaf1141e6bce993625e838c48b7";
  }
  function D() public pure returns (string) {
    return "3df5b836aa19193ebc0c391a90f837ec00c173def06fea1ec662dc525dae4c15" ;
  }
}
```
<br> 编辑migrations目录中的1_initial_migration.js部署脚本，将我们刚才创建的msg_to_Tony.sol文件设置到发布配置文件中，内容如下：
```
var Migrations = artifacts.require("./Migrations.sol");
var msg_to_Kevin = artifacts.require("./msg_to_Kevin.sol");
module.exports = function(deployer) {
deployer.deploy(Migrations);
deployer.deploy(msg_to_Kevin);
};
```
<br> 使用truffle compile命令编译合约msg_to_Kevin.sol，编译后的文件是msg_to_Kevin.json文件，存放于新生成的./build/contracts目录中
```$ truffle compile```

<br> 部署智能合约，编辑truffle.js配置文件，设置我们稍后要部署智能合约的位置（即搭建好的私有链），内容如下:
```
module.exports = {
    networks: {
        development: {
          host: "localhost",
          port: 8545,//这里就是当初我们进入Geth客户端时打开的rpc端口，即通过这个端口将写好的智//能合约部署到我们的私有链上
          network_id: "*"
        }
    }
};
```
<br> 执行部署
```$ truffle migrate```

### 7.在Geth中部署合约并调用
<br> 打开合约编译后的msg_to_Kevin.json文件，取出abi部分并进行JSON转义，然后将JSON后的内容赋值给mshk_abi变量。接下来，找到msg_to_Kevin.json文件中的bytecode部分，在geth中将其赋值给mshk_bytecode变量，最后评估创建合约需要的手续费。此时解锁账户并开启挖矿，进行合约的部署。
```
personal.unlockAccount(eth.accounts[0], "", 15000)
miner.start()
mshk_Contract = web3.eth.contract(mshk_abi);
mshk_hello = mshk_Contract.new({from:acc0, data:mshk_bytecode, gas:300000}, function(e, contract){
if(!e) {
if(!contract.address) {
console.log("Contract transaction send: TransactionHash: " + contract.transactionHash + " waiting to be mined...");
} else {
console.log("Contract mined! Address: " + contract.address);
console.log(contract);
}
}
});
```
<br> 合约被成功部署到geth中并被挖出，确认，存放于区块中
<br> 此时测试部属的合约
```
> msg_to_tony.key()
"3ae07527e5564346cb3ed92547175d0779cebb2f4788726af070086c7e71bae5e32ddba3c759ed6006af0b84b01f1deaae311a7855bcf4e1bc33258d3c0fefa6"
> msg_to_tony.A()
"164872f0a0f63e828a62c9457f232d6f2895e18dc71c4a80595f3321c65a45770d2bce9cd2d9c04912dfbd4171821b8b96c11eaf1141e6bce993625e838c48b7"
> msg_to_tony.D()
"3df5b836aa19193ebc0c391a90f837ec00c173def06fea1ec662dc525dae4c15"
```

<br> 实现合约的调用。



