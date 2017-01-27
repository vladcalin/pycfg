pycfg
=====

Library for manipulating configuration values for your applications with ease.

Installation
------------

Not yet.

Usage
-----

Suggested usage (initial draft)

::

    import pycfg

    pycfg.define("app.logging.level", default="info", choices=("debug", "info", "warning", "error", "critical"))
    pycfg.define("app.logging.format", default="%(message)s")

    pycfg.define("app.server.host", default="127.0.0.1", description="The address of the server")
    pycfg.define("app.server.port", default=8000, description="The port of the server")

    pycfg.define("app.backend.db_driver", default="mysql", choices=("mysql", "postgresql", "sqlite", "mongodb"))
    pycfg.define("app.backend.username", required=True)
    pycfg.define("app.backend.password", required=True, secret=True)

    pycfg.dump_defaults_to_json("myapp.json")
    """
    {
        "app.logging.level": "info",
        "app.logging.format": "%(message)s",
        "app.server.host": "127.0.0.1",
        "app.server.port": 8000,
        "app.backend.db_driver": "mysql",
        "app.backend.username": null,
        "app.backend.password": null
    }
    """

    pycfg.dump_defaults_to_ini("myapp.ini")
    """
    [app]

    ; Supported values: debug, info, warning, error, critical
    logging.level = info
    logging.format = %(message)s

    ; The address of the server
    server.host = 127.0.0.1

    ; The port of the server
    server.port = 8000

    ; Supported values: mysql, postgresql, sqlite, mongodb
    backend.db_driver = mysql

    ; Required
    backend.username =

    ; Required and secret
    backend.password =
    """

    pycfg.dump_defaults_to_module("myappconf.py")
    """
    # TODO
    """

    pycfg.load_from_json("conf.json")
    pycfg.load_from_ini("conf.ini")
    pycfg.load_from_module("mymodule.py")
    pycfg.load_from_object("myapp.conf.settings")
    pycfg.load_from_env()

    pycfg.get_option("app.logging.level")
    # debug
    pycfg.get_option("app.logging.format")
    # %(message)s
    pycfg.get_option("app.backend.db_driver")
    # mysql

    pycfg.save_state(".confstate")
In other process

::

    import pycfg
    pycfg.load_state(".confstate")
    pycfg.get_option("app.logging.level")
    # debug


