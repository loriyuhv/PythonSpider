# Client Reference

## Client Session

Client session is the recommended interface for making HTTP requests.

1. reference  /ˈrefrəns/  n. 参考书
2. recommend  /ˌrekəˈmend/  vt.推荐
3. interface n. 接口

Session encapsulates a *connection pool* (*connector* instance) and supports keepalives by default. Unless you are connecting to a large, unknown number of different servers over the lifetime of your application, it is suggested you use a single session for the lifetime of your application to benefit from connection pooling.

1. encapsulate  /ɪnˈkæpsjuleɪt/ vt. 简述
2. pool /puːl/ n.池
3. instance n.实例；实体
4.  keepalives 运维生存时间
5. benefit from/by sth v 得益于

Usage example:

1. usage /ˈjuːsɪdʒ/ n. 用法

```python
url = 'http://python.org'
async def fetch(client):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.text()


async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

```

The client session supports the context manager protocol for self closing.

1. the context manager protocol 上下文管理协议

*class* aiohttp__.ClientSession__(__*__, *connector=None*, *loop=None*, *cookies=None*, *headers=None*, *skip_auto_headers=None*, *auth=None*, *json_serialize=json.dumps*, *version=aiohttp.HttpVersion11*, *cookie_jar=None*, *read_timeout=None*, *conn_timeout=None*, *timeout=sentinel*, *raise_for_status=False*, *connector_owner=True*, *auto_decompress=True*, *read_bufsize=2 ** 16*, *requote_redirect_url=False*, *trust_env=False*, *trace_configs=None*)

The class for creating client sessions and making requests.

__Parameters__

- **connector** ([*aiohttp.BaseConnector*](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.BaseConnector)) – BaseConnector sub-class instance to support connection pooling.

- **loop** –

  [event loop](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop) used for processing HTTP requests. If *loop* is `None` the constructor borrows it from *connector* if specified.

  1. process vt.处理
  2. constructor n. 构造函数，构造器
  3. borrow vt. 引用
  4. specify vi.指定

  [`asyncio.get_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop) is used for getting default event loop otherwise. *Deprecated since version 2.0.*

  1. otherwise adv 除此之外
  2. deprecate  /ˈdeprəkeɪt/ vt 反对

- **cookies ** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Cookies to send with the request (optional)

  1. optional adj 可选的

- **headers** –

  HTTP Headers to send with every request (optional).

  May be either *iterable of key-value pairs* or [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping) (e.g. [`dict`](https://docs.python.org/3/library/stdtypes.html#dict), [`CIMultiDict`](https://multidict.readthedocs.io/en/stable/multidict.html#multidict.CIMultiDict)).

  1. iterable adj. 迭代的

- **skip_auto_headers** –

  set of headers for which autogeneration should be skipped.

  *aiohttp* autogenerates headers like `User-Agent` or `Content-Type` if these headers are not explicitly passed. Using `skip_auto_headers` parameter allows to skip that generation. Note that `Content-Length` autogeneration can’t be skipped.Iterable of [`str`](https://docs.python.org/3/library/stdtypes.html#str) or `istr` (optional)

  1. explicitly adv 明确地
  2. pass vt 传递

- **auth** ([*aiohttp.BasicAuth*](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.BasicAuth)) – an object that represents HTTP Basic Authorization (optional)

- **version** – supported HTTP version, `HTTP 1.1` by default.

- **cookie_jar** –Cookie Jar, `AbstractCookieJar` instance.By default every session instance has own private cookie jar for automatic cookies processing but user may redefine this behavior by providing own jar implementation.One example is not processing cookies at all when working in proxy mode.If no cookie processing is needed, a [`aiohttp.DummyCookieJar`](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.DummyCookieJar) instance can be provided.

- **json_serialize** (*callable*) –Json *serializer* callable.By default [`json.dumps()`](https://docs.python.org/3/library/json.html#json.dumps) function.

- **raise_for_status** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) –

  Automatically call [`ClientResponse.raise_for_status()`](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientResponse.raise_for_status) for each response, `False` by default. This parameter can be overridden when you making a request, e.g.:

  ```python
  client_session = aiohttp.ClientSession(raise_for_status=False)
  resp = await client_session.get(url, raise_for_status=False)
  async with resp:
      assert resp.status == 200
  ```

  1. automatically adv自动地
  2. call 调用
  3. overridde /ˌəʊvəˈraɪd/  vt. 否决

  Set the parameter to `True` if you need `raise_for_status` for most of cases but override `raise_for_status` for those requests where you need to handle responses with status 400 or higher.

- j

  