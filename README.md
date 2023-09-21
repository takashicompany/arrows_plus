# Arrows PLUS

## 基板のバージョンの確認

基板のバージョンによって、機能や用いるファームウェアに小さい差異がございます。  
基板のバージョンは以下の緑枠部分で判別が可能です。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_6123_b.jpg?raw=true" width = "600px" />

|基板の記載|基板のバージョン|ロータリーエンコーダの搭載|
|:--|:--|:--|
|Arrows+ のみ|Rev1|可能|
|Arrows+(Rev2)|Rev2|不可|

## 組み立てに必要な部品

### 基本

|部品|個数|備考|
|:--|:--|:--|
|Arrows PLUS 基板|1||
|[XIAO RP2040](https://talpkeyboard.net/items/63534f58f5197322fceb6487)|1|[電子部品の取扱店](https://www.switch-science.com/products/7634)などでも購入可能です。|
|キースイッチ|5|Cherry MX互換スイッチ。|
|キーキャップ|5|Cherry MX互換スイッチ対応のキーキャップ。全て1u。|
|[ゴム足シール](https://shop.yushakobo.jp/products/a0800ur-01-6)|4||

### スイッチプレートを取り付ける場合

Arrows PLUSは基板をもう1枚用意し、加工することでスイッチプレート付きのキーボードとして組み立てることができます。  
以下の写真の左側が基板1枚で組んだもの、右側が基板2枚を用いてスイッチプレートを取り付けたものです。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_6128.jpg?raw=true" width = "400px" />  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_6131.jpg?raw=true" width = "400px" />

全体的な使用感に大きな違いはありませんが、キースイッチプレートを取り付けることでキースイッチがより固定され安定がさらに増します。

|部品|個数|備考|
|:--|:--|:--|
|Arrows PLUS 基板|1|もう1枚用意してスイッチプレートとして利用する。|
|[M2 スペーサー 3.5mm](https://shop.yushakobo.jp/products/a0800c2?variant=43940969316583)|5||
|[M2 ネジ 3mm](https://shop.yushakobo.jp/products/a0800n2)|10||

### ロータリーエンコーダを取り付ける場合

基板のバージョンによっては、ロータリーエンコーダを取り付けることが可能です。
2023年9月現在では **Rev1** 基板のみ取り付け可能です。

基板右奥側のキースイッチ取付箇所にロータリーエンコーダの用の穴が追加されていると取付が可能です。  
他のキースイッチ取付箇所より穴が多めに空いていることを確認してください。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5530_b.jpg?raw=true" width = "600px" />

対応してないバージョンは以下になります。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_6122.jpg?raw=true" width = "600px" />

|部品|個数|備考|
|:--|:--|:--|
|[ロータリーエンコーダ](https://shop.yushakobo.jp/products/3762)|1|基板のバージョンによっては取り付け不可能。|


## 組み立てに必要な道具

|道具|備考|
|:--|:--|
|ハンダごて|おすすめは[HAKKO FX-600](https://www.hakko.com/japan/products/hakko_fx600.html)です。[こて台](https://www.hakko.com/japan/products/hakko_kote_board.html)もあると、より作業をスムーズに進められます。|
|ハンダ|[こちら](https://www.goot.jp/products/detail/se_06008)などを使う方が多いようです。|
|ピンセット|100均などで手に入るものでも充分利用できるかと思います。|
|ニッパー|100均などで手に入るものでも充分利用できるかと思いますが、1000円程度ものを買っても損では無いかと思います。|

## あるとさらに完成度が高くなる道具
|道具|備考|
|:--|:--|
|棒ヤスリ|基板の縁にあるバリを削るのに使います。|
|サインペン|基板の縁を塗るとより美しくなります。|
|マスキングテープ|キースイッチをハンダ付けする際に役立ちます。|

## 組み立て方

### 1. 基板の表裏を確認する

表  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5530.jpg?raw=true" width = "600px" />

裏  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5531.jpg?raw=true" width = "600px" />

### 2. 基板の縁を整える

この項目は必ずしも組み立てに必須ではありませんが、完成度を高める効能があります。

ヤスリでロゴの奥側の凹凸を削ると見栄えが良くなります。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5536.jpg?raw=true" width = "600px" />

以下の写真程度削ると凹凸が目立たなくなります。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5538.jpg?raw=true" width = "600px" />

また、縁を基板と同色のサインペンで塗ると、見栄えがさらに良くなります。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5534.jpg?raw=true" width = "600px" />

縁を一周するように塗ります。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5536.jpg?raw=true" width = "600px" />

### 3. MCU(XIAO RP2040)の取り付け

MCU(Micro Controller Unit)とは、キーボードの頭脳部分です。  
Arrows PLUSはXIAO RP2040を用います。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5541.jpg?raw=true" width = "600px" />

基板にXIAO RP2040を配置します。  
この時、ハンダ付けがしやすいよう基板とXIAO RP2040の位置をあわせます。  
XIAO RP2040の両縁を基板とハンダ付けするので、両縁がハンダ付けしやすい位置に配置します。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5544.jpg?raw=true" width = "600px" />

位置がズレないようにマスキングテープで固定すると作業がスムーズに行なえます。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5546.jpg?raw=true" width = "600px" />

XIAO RP2040の縁と基板をハンダ付けします。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5547.jpg?raw=true" width = "600px" />

XIAO RP2040の両縁と基板をハンダ付けしたら完了です。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5548.jpg?raw=true" width = "600px" />

### 4. ファームウェアの書き込み
[KMK Firmware](https://github.com/KMKfw/kmk_firmware)を用いる場合です。  

[こちら](http://kmkfw.io/docs/Getting_Started/)のKMK Firmwareの導入手順も併せて読むと理解が深まると思います。

[こちら](https://circuitpython.org/board/seeeduino_xiao_rp2040/)から.uf2ファイルをダウンロードします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/47f0223c-b40d-4b95-8516-b403834db523" width = "600px" />

XIAO RP2040のUSB口とは反対側にある「B」と書かれたスイッチを押しながらUSBケーブルを差します。  
「RPI-RP2」という名前の外部デバイスが表示されれば成功です。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5548_b.jpg" width = "600px" />

ダウンロードした.uf2を「RPI-RP2」に書き込みます。ドラッグアンドドロップかコピーペーストで書き込めます。  
書き込み完了後、「CIRCUITPY」という名前の外部デバイスが表示されれば成功です。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/1edcd0e8-89cb-49ea-af4f-ae5e574fdd37" width = "600px" />

[KMK Firmwareのソースコードのzip](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip)をダウンロードします。  
解凍後、フォルダ内の`boot.py`と`kmkフォルダ`をCIRCUITPYにドラッグアンドドロップ or コピーペーストします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/7f36a17a-5073-4edc-b0dd-3008e8e5ef75" width = "600px" />

code.pyにキーマップ等を書き込みます。
基板のバージョンに応じて、用いるcode.pyは以下になります。

- [Rev1](https://github.com/takashicompany/arrows_plus/blob/master/firmware/kmk/rev1/code.py)
- [Rev2](https://github.com/takashicompany/arrows_plus/blob/master/firmware/kmk/rev2/code.py)

上述のKMK Firmware用のソースコード`code.py`をダウンロード、またはコピーしてCIRCUITPYにドラッグアンドドロップ　or ペーストをします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/0bfe6c1c-1bc5-4667-b853-cea94f43abf7" width = "600px" />

XIAO RP2040のハンダ付けと、ファームウェアの書き込みが成功しているかを確かめるために、ピンセットなどでキースイッチ穴同士を導通させます。  
キーが入力されたら成功です。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_6121.jpg?raw=true" width = "600px" />

### 5. スイッチプレートの取り付け

この項目は基板をもう一枚用意してスイッチプレートとして加工し組み立てる場合の項目です。  
基板を1枚のみで組み立てる場合は省略します。  

基板の点線部分をニッパーで切ります。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5554.jpg?raw=true" width = "600px" />

全部で5箇所をくり抜きます。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5555.jpg?raw=true" width = "600px" />

くり抜いた箇所にキースイッチがハマるかを確認します。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5557.jpg?raw=true" width = "600px" />

スペーサーとネジを用いてスイッチプレートと基板を固定します。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5560.jpg?raw=true" width = "600px" />

スペーサースイッチプレートの裏側に取り付けて、表側からネジで固定します。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5562.jpg?raw=true" width = "600px" />

表側からネジで固定した例が以下になります。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5563.jpg?raw=true" width = "600px" />

基板の裏側からネジを用いてスイッチプレートに刺したスペーサーと固定します。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5564.jpg?raw=true" width = "600px" />

### 6. キースイッチのハンダ付け

キースイッチをハンダ付けして基板と接続します。  
組み立て方で手順が少し異なりますが、最終的には基板とキースイッチをハンダ付けすることになります。

#### a. 基板1枚で組み立てる場合

基板にキースイッチを仮置きします。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5558.jpg?raw=true" width = "600px" />

マスキングテープなどで基板とキースイッチを固定すると作業がスムーズに行えます。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5559.jpg?raw=true" width = "600px" />

#### b. スイッチプレートを用いる場合

スイッチプレートの枠にキースイッチをはめ込みます。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5566.jpg?raw=true" width = "600px" />

---

以下の工程から共通となります。

基板の裏側から、キースイッチの足が出ていることを確認します。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5569.jpg?raw=true" width = "600px" />

キースイッチの足と基板をハンダ付けします。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5571.jpg?raw=true" width = "600px" />

キースイッチがズレないよう　& ハズれないようにハンダ付けを行います。
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5572.jpg?raw=true" width = "600px" />

各キースイッチ毎に2箇所ずつハンダ付けをします。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5573.jpg?raw=true" width = "600px" />

### 7. ロータリーエンコーダのハンダ付け

一部のバージョンの基板のみ、右奥にロータリーエンコーダを取り付けることができます。  
不要な場合はキースイッチを取り付けることとなります。  

<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5574.jpg?raw=true" width = "600px" />

ロータリーエンコーダの固定用の足が取り付けの際に基板と干渉する場合があります。  
必要に応じて、固定用の足を切るなどしてください。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5575.jpg?raw=true" width = "600px" />

以下は固定用の足をカットした例です。赤丸のニッパーで箇所を切り落としました。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5577.jpg?raw=true" width = "600px" />

キースイッチプレートを取り付けている場合、スイッチプレートのロータリーエンコーダ穴と足が干渉することがありますので、必要に応じてニッパーでスイッチプレートのロータリーエンコーダ穴を削ります。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5578.jpg?raw=true" width = "600px" />

以下は加工例です。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5579.jpg?raw=true" width = "600px" />

ロータリーエンコーダを基板の表側に載せます。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5580.jpg?raw=true" width = "600px" />

基板の裏側からロータリーエンコーダの足が出ているかを確認します。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5581.jpg?raw=true" width = "600px" />

基板とロータリーエンコーダの足をハンダ付けします。  
基板と足がしっかりとハンダ付けされていることを確認しながら作業を進めます。
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5582.jpg?raw=true" width = "600px" />

取り付けは以上です。作業完了後、問題なくロータリーエンコーダが動作しているかを確認してください。

### 8. ゴム足シールの取り付け

基板の底面にゴム足シールを貼り付けます。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5584.jpg?raw=true" width = "600px" />

個人の打鍵スタイルにあわせて取り付け位置を決めます。  
以下は参考例です。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5585.jpg?raw=true" width = "600px" />

### 9. キーキャップを取り付ける

キーキャップを取り付けて完成です。  
<img src = "https://github.com/takashicompany/arrows_plus/blob/master/images/build/IMG_5587.jpg?raw=true" width = "600px" />


### 10. 完成したら

完成しましたら、ぜひSNSなどに写真を投稿頂ければと思います。
Twitterのハッシュタグは [`#ArrowsPlus #自作キーボード`](https://twitter.com/search?q=%23%E8%87%AA%E4%BD%9C%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89%20%23ArrowsPlus&src=typed_query) を付けていただけると幸いです。
キットを組み立てた感想や、キーボードを使った所感などをお待ちしております！

また、毎週日曜日の１9時より実施されている自作キーボード写真コンテスト[「#KEEP_PD」](https://twitter.com/hashtag/KEEB_PD?f=live)に投稿頂くこともオススメです。  
開催の告知は[@KEEB_PD](https://twitter.com/KEEB_PD)にて行われております。

ご不明な点などございましたら、[@takashicompany](https://twitter.com/takashicompany)にメンションやDM頂ければ回答できるかと思います。
