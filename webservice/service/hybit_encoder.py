import re
import sys

from toml.decoder import InlineTableDict
from toml.encoder import TomlEncoder, _dump_str

if sys.version_info >= (3,):
    unicode = str


# This class returns only one section deep, all inner elements are dumped following the dot-notation
# example:
# {"root": {"owner": {"name": "test"}, "access": 2}}
# [root]
# owner.name = "test"
# access = 2

class hyBitMetaEncoder(TomlEncoder):
    def __init__(self, _dict=dict):
        super(hyBitMetaEncoder, self).__init__(_dict)

    def dump_sections(self, o, sup):
        retstr = ""
        retdict = self._dict()
        for section in o:

            section = unicode(section)
            qsection = section

            if not re.match(r'^[A-Za-z0-9_-]+$', section):
                qsection = _dump_str(section)

            if not isinstance(o[section], dict):
                if o[section] is not None:
                    retstr += (qsection + " = " + unicode(self.dump_value(o[section])) + '\n')
            elif self.preserve and isinstance(o[section], InlineTableDict):
                retstr += (qsection + " = " + self.dump_inline_table(o[section]))
            else:
                # this is the main difference
                retdict[qsection] = o[section]

                if sup != "" and sup[-1] != ".":
                    rstr = self.dump_dict(o[section], section)
                    retstr += rstr

        if sup != "" and sup[-1] != ".":
            return retstr, {}

        return retstr, retdict

    def dump_dict(self, data, prefix):
        retstr = ""
        for section in data:
            section = unicode(section)

            if not isinstance(data[section], dict):
                if data[section] is not None:
                    retstr += (prefix + '.' + section + " = " + unicode(self.dump_value(data[section])) + '\n')
            else:
                retstr += self.dump_dict(data[section], prefix + '.' + section)

        return retstr
