import tensorflow as tf
# adding logging
import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def get_sparse_categorical_accuracy_fn(cfg):
    return tf.keras.metrics.SparseCategoricalAccuracy()