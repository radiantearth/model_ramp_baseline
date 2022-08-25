import tensorflow as tf

def get_adam_optimizer(cfg):
    adam_parms = cfg["optimizer"]["optimizer_fn_parms"]
    return tf.keras.optimizers.Adam(**adam_parms)