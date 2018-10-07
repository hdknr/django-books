class JcbReceipt(object):

    @classmethod
    def get_fields_map(cls):
        return dict((f.verbose_name, f.name) for f in cls._meta.fields)