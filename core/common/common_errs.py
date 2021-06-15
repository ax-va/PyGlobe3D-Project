from pyglobe3d.core.core_errs import CoreError


class CommonError(CoreError):
    pass


class ConstantAttributeRewriteError(CommonError):
    def __init__(self, attribute_name):
        self.message = f'The attribute {attribute_name} is constant and cannot be rewritten'
        super().__init__(self, self.message)