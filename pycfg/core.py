_PYCFG_OPTIONS = {}


class OptionSpecs(object):
    def __init__(self, fqn, default=None, required=False, description=""):
        self.fqn = fqn
        self.default = default
        self.required = required
        self.description = description


def define(option_name, required=False, default=None, description=""):
    _PYCFG_OPTIONS[option_name] = OptionSpecs(option_name, default, required, description)


def dump_default_config(location, format="json"):
    pass


if __name__ == '__main__':
    define("core.logging.level", default="info", description="The level of the logging")
    define("core.logging.format", default="%(message)s", description="The log format")
    define("core.logging.errorfile", default="errors.log")
    define("core.logging.logfile", default="default.log")

    import pprint

    pprint.pprint(_PYCFG_OPTIONS)

    dump_default_config("config.json")
