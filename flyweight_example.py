import weakref

class CarModel:
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model    
        return model

    def __init__(self, model_name, air=False):
        if not hasattr(self, "initted"):
          self.model_name = model_name
          self.air = air
          self.initted=True