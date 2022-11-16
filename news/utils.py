class MyMixin(object):
    mixin_prob = ''
    def get_prob(self):
        return self.mixin_prob.upper()
    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()