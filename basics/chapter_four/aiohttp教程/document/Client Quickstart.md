# Client Quickstart

Eager to get started? This page gives a good introduction in how to get started with aiohttp client API.

First, make sure that aiohttp is [installed](https://docs.aiohttp.org/en/stable/index.html#aiohttp-installation) and *up-to-date*

Let’s get started with some simple examples.

## Make a Request

Begin by importing the aiohttp module, and asyncio:

```pytho
import aiohttp
import asyncio
```

Now, let’s try to get a web-page. For example let’s query `http://httpbin.org/get`:

```python
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Now, we have a [`ClientSession`](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientSession) called `session` and a [`ClientResponse`](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientResponse) object called `resp`. We can get all the information we need from the response. The mandatory parameter of [`ClientSession.get()`](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientSession.get) coroutine is an HTTP *url* ([`str`](https://docs.python.org/3/library/stdtypes.html#str) or class:yarl.URL instance).

1. mandatory  /mænˈdeɪtəri/  adj. 强制的；法定的
2. parameter /pəˈræmɪtə(r)/  n. 范围 
3. coroutine n.协程

In order to make an HTTP POST request use [`ClientSession.post()`](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientSession.post)  coroutine:

```python
session.post(url, data=b'data')
```

Other HTTP methods are available as well:

```python
session.put('http://httpbin.org/put', data=b'data')
session.delete('http://httpbin.org/delete')
session.head('http://httpbin.org/get')
session.options('http://httpbin.org/get')
session.patch('http://httpbin.org/patch', data=b'data')
```

Note

Don’t create a session per request. Most likely you need a session per application which performs all requests altogether.

1. per prep .每

2. perform vt. 执行

3. altogether adv 完全地

   不要为每个请求创建一个对话。最可能得情况是，你需要为每个应用程序创建一个会话，以执行所有请求。

More complex cases may require a session per site, e.g. one for Github and other one for Facebook APIs. Anyway making a session for every request is a **very bad** idea.

1. complex adj 复杂的

A session contains a connection pool inside. Connection reusage and keep-alives (both are on by default) may speed up total performance.

1. reusage  重复使用
2. speed up vt 加速
3. total adv 完全
4. performance n. 性能

A session context manager usage is not mandatory but `await session.close()` method should be called in this case, e.g.:

```py
session = aiohttp.ClientSession()
async with session.get('...'):
    # ...
await session.close()
```

## Passing Parameters In URLs

You often want to send some sort of data in the URL’s query string. If you were constructing the URL by hand, this data would be given as key/value pairs in the URL after a question mark, e.g. `httpbin.org/get?key=val`. Requests allows you to provide these arguments as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict), using the `params` keyword argument. As an example, if you wanted to pass `key1=value1` and `key2=value2` to `httpbin.org/get`, you would use the following code:

```python
params = {'key1': 'value1', 'key2': 'value2'}
async with session.get('http://httpbin.org/get', params=params) as resp:
    expect = 'http://httpbin.org/get?key1=value1&key2=value2'
    assert str(resp.url) == expect
```

1. a question mark n 问号 	mark 符号
2. keyword n 关键字

You can see that the URL has been correctly encoded by printing the URL.

1. encode  vt. 编码

For sending data with multiple values for the same key [`MultiDict`](https://multidict.readthedocs.io/en/stable/multidict.html#multidict.MultiDict) may be used; the library support nested lists (`{'key': ['value1', 'value2']}`) alternative as well.

1. library n 程序库
2. alternative  /ɔːlˈtɜːnətɪv/  n 可选择
3. as well adv 也

It is also possible to pass a list of 2 item tuples as parameters, in that case you can specify multiple values for each key:

```python
params = [('key', 'value1'), ('key', 'value2')]
async with session.get('http://httpbin.org/get', params=params) as r:
    expect = 'http://httpbin.org/get?key=value2&key=value1'
    assert = str(r.url) == expect
```

You can also pass [`str`](https://docs.python.org/3/library/stdtypes.html#str) content as param, but beware – content is not encoded by library. Note that `+` is not encoded:

1. beware v 警告

```python
async with session.get('http://httpbin.org/get',
                       params='key=value+1') as r:
        assert str(r.url) == 'http://httpbin.org/get?key=value+1'
```

### Note

*aiohttp* internally performs URL canonicalization before sending request.

1. internally adv 内部

Canonicalization encodes *host* part by [IDNA](https://docs.aiohttp.org/en/stable/glossary.html#term-IDNA) codec and applies [requoting](https://docs.aiohttp.org/en/stable/glossary.html#term-requoting) to *path* and *query* parts.

For example `URL('http://example.com/путь/%30?a=%31')` is converted to `URL('http://example.com/%D0%BF%D1%83%D1%82%D1%8C/0?a=1')`.

Sometimes canonicalization is not desirable if server accepts exact representation and does not requote URL itself.

1. desirable adj 可取的
2. representation n. 描述
3. requote vt重复引用

To disable canonicalization use `encoded=True` parameter for URL construction:

```python
await session.get(URL('http://example.com/%30', encoded=True))
```

1. disable adj. 无效的
2. canonicalization n. 标准

__Warning__

Passing *params* overrides `encoded=True`, never use both options.

1. override 覆盖 覆盖了一个方法并且对其重写

## Response Content and Status Code

We can read the content of the server’s response and its status code. Consider the GitHub time-line again:

```python
async with aiohttp.ClientSession() as session:
    async with session.get('https://api.github.com/events') as resp:
        print(resp.status)
        print(await resp.text())
```

1. time-line

prints out something like:

```python
200
'[{"created_at":"2015-06-12T14:06:22Z","public":true,"actor":{...
```

`aiohttp` automatically decodes the content from the server. You can specify custom encoding for the [`text()`](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientResponse.text) method:

1. automatically adv 自动地
2. custom 自定义

```python
await resp.text(encoding='utf-8')
```

## Binary Response Content[¶](https://docs.aiohttp.org/en/stable/client_quickstart.html#binary-response-content)

You can also access the response body as bytes, for non-text requests:

```python
print(await resp.read())
```

```python
b'[{"created_at":"2015-06-12T14:06:22Z","public":true,"actor":{...
```

The `gzip` and `deflate` transfer-encodings are automatically decoded for you.

You can enable `brotli` transfer-encodings support, just install [brotlipy](https://github.com/python-hyper/brotlipy).



