# HTTP Server 

Creating a simple HTTP server with Python's standard library is straightforward thanks to the http.server module, which provides the classes for building basic web servers.

To enhance the simple HTTP server and turn it into a more versatile CLI tool that can serve a directory (including an index.html file if present), you can use Python's argparse module for command-line argument parsing. This approach allows users to specify the port and directory to serve when they start the server.

### Example

```bash
python http_server.py --port 8080 --directory /path/to/your/directory
```

### Using http module without the script from the offical documentation

http.server can also be invoked directly using the -m switch of the interpreter. Similar to the previous example, this serves files relative to the current directory:

```python 
python -m http.server
```

The server listens to port 8000 by default. The default can be overridden by passing the desired port number as an argument:

```python
python -m http.server 9000
```

By default, the server binds itself to all interfaces. The option -b/--bind specifies a specific address to which it should bind. Both IPv4 and IPv6 addresses are supported. For example, the following command causes the server to bind to localhost only:

```python
python -m http.server --bind 127.0.0.1
```

Changed in version 3.4: Added the --bind option.

Changed in version 3.8: Support IPv6 in the --bind option.

By default, the server uses the current directory. The option -d/--directory specifies a directory to which it should serve the files. For example, the following command uses a specific directory:

```python
python -m http.server --directory /tmp/
```

Changed in version 3.7: Added the --directory option.

By default, the server is conformant to HTTP/1.0. The option -p/--protocol specifies the HTTP version to which the server is conformant. For example, the following command runs an HTTP/1.1 conformant server:

```python
python -m http.server --protocol HTTP/1.1
```

Changed in version 3.11: Added the --protocol option.


