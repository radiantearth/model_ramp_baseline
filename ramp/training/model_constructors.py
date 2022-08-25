

def get_effunet_model(cfg):
    from ..models.effunet_1 import get_effunet 
    parms = cfg["model"]["model_fn_parms"]
    return get_effunet(**parms)






