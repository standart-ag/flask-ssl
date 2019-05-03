# Flask SSL require and redirect decorator

Easy to use package for Flask framework to check if request is served securely.

> Please note, that this package does not enable SSL directly in Flask app
> (however we support that) we recommend you to use reverse proxy or wsgi
> server with configured SSL params.

## Install

```bash
pip install flask-ssl
```

## Configuration

You should have working reverse proxy server with configured SSL and SSL header information.

> This plugin supports nginx and apache default configurations.

For example, for your `nginx` installation it will be:
```
server {
  ...
  
  location  / {
    ...
    
    proxy_set_header HTTPS on;
    proxy_set_header X-Forwarded-Ssl on;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
}
```

## Use
```python
from flask_ssl import *

# {...}

@ssl_require
@app.route('/your/url/that/should/be/available/only/with/ssl')
def func():
    return "Ok, served via SSL"
    
@ssl_redirect
@app.route('/your/url/that/should/be/redirected/to/ssl')
def func2():
    return "Ok, served via SSL"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

This software is developed inside Standart AG, LLC, 2019