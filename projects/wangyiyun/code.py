# # 1. 找到未加密的参数                               # window.arsea(参数, xxxx, xxxx)
# # 2. 想办法把参数进行加密（必须参考网易的逻辑）， params => encText, encSecKey => encSecKey
# # 3. 请求到网易，拿到评论信息
#
#
# from Crypto.C
# data = {
#     "csrf_token": "",
#     "cursor": "-1",
#     "offset": "0",
#     "orderType": "1",
#     "pageNo": "1",
#     "pageSize": "20",
#     "rid": "R_SO_4_1325905146",
#     "threadId": "R_SO_4_1325905146"
# }
# e = "010001"
# f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# g = "0CoJUm6Qyw8W8jud"
# i = "hLEy9sLlcXxJfVTq"
#
#
# def get_encSecKey():
#     return "7ffbe257392eeea7acc2960a38850731c75c7cd6026472e5ce94abd5d6acfb46c032351fef18aa121571b33a448f0c73791d4edf0d00af0f83d6bd641d9ce30da5c6ed46cacce065e9af27ac739687736ffb30c960d06a09fbfdfe0950969afa78e41b29e70555ed622793c064406d97616098392fd7b353181a326ae25575f0"
#
#
# def get_parms(data): # 默认这里收到的是字符串
#     first = enc_params(data, g)
#     second = enc_params(first, i)
#     return second
#
#
# def enc_params(data, key): # 加密过程
#
#     pass
# # 处理加密过程
# """
#     function a(a) { # 随机的16位字符串
#         var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
#         for (d = 0; a > d; d += 1) # 循环16次
#             e = Math.random() * b.length, # 随机数 1.2345
#             e = Math.floor(e), # 取整 1
#             c += b.charAt(e);  # 去字符串中的xx位值 b
#         return c
#     }
#     function b(a, b) {
#         var c = CryptoJS.enc.Utf8.parse(b) //  b就是密钥
#           , d = CryptoJS.enc.Utf8.parse("0102030405060708") //
#           , e = CryptoJS.enc.Utf8.parse(a) //e是数据
#           , f = CryptoJS.AES.encrypt(e, c, { // c 加密的密钥
#             iv: d, // 偏移量
#             mode: CryptoJS.mode.CBC // 模式 cbc
#         });
#         return f.toString()
#     }
#     function c(a, b, c) {
#         var d, e;
#         return setMaxDigits(131),
#         d = new RSAKeyPair(b,"",c),
#         e = encryptedString(d, a)
#     }
#     function d(d, e, f, g) {    d:数据， e: 010001 f:很长 g:0CoJUm6Qyw8W8jud
#         var h = {} #空对象
#           , i = a(16);  # i就是一个16位的随机值
#         return h.encText = b(d, g), // g就是密钥
#         h.encText = b(h.encText, i), # 返回的就是params
#         h.encSecKey = c(i, e, f),     # 得到的就是encSecKey, e和f是定死的， 如果此时我把i固定
#         h
#     }
# """
