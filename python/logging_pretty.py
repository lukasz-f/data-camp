import pprint
import logmatic


class PrettyJsonFormatter(logmatic.JsonFormatter):
    def __init__(self, fmt=None, datefmt=None, style='%', extra={}, *args, **kwargs):
        logmatic.JsonFormatter.__init__(self, fmt=fmt, datefmt=datefmt, extra=extra, style=style, *args, **kwargs)

    def jsonify_log_record(self, log_record):
        """Returns a json string of the log record with pretty print."""
        return pprint.pformat(dict(log_record), indent=4)
