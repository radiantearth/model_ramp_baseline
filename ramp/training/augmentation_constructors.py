import albumentations as A
import cv2
import re

# adding logging
import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def get_augmentation_fn(cfg):
    aug_name_list = cfg["augmentation"]["aug_list"]
    aug_parms_list = cfg["augmentation"]["aug_parms"]

    # construct augmentation functions
    aug_fn_list = []
    for augment_name, aug_parms in zip(aug_name_list, aug_parms_list):
        aug_fn = getattr(A, augment_name)

        # some of these values are cv2 flag strings that have to be converted
        flag_parms = { k: getattr(cv2,v) for (k,v) in aug_parms.items() 
            if (isinstance(v, str) and hasattr(cv2, v))}
        aug_parms = {k: v for (k,v) in aug_parms.items() if not isinstance(v, str)}
        aug_parms.update(flag_parms)
    aug_fn_list.append(aug_fn(**aug_parms))
    return A.Compose(aug_fn_list)

        
# def get_augparm(parameter_name):
#     '''
#     splits the augmentation and parameter part of a 
#     parameter in the augmentation.aug_parms group of the config file.
#     examples: 
#     colorjitter_p -> colorjitter, p
#     rotate_mask_value -> rotate, mask_value
#     '''
#     # 'aug' named group matches everything up to the first _ (underline)
#     rex = re.compile(r'(?P<aug>[^_]*)_(?P<parm>.*)')
#     m = rex.search(parameter_name)
#     assert m is not None, f'parameter name {parameter_name} is malformed'
#     return m["aug"], m['parm']

# def get_aug_parm_list(augment_name, cfg):
#     '''
#     filter out only parameters relevant to the specific augmentation
#     relevant parameters begin with the lowercased augmentation name
#     '''
#     all_aug_parms = cfg["augmentation"]["aug_parms"]

#     aug_parms =  {get_augparm(k)[1]:v for (k,v) in all_aug_parms.items() if k.startswith(augment_name.lower())}
    
#     # some of these values are cv2 flag strings that have to be converted
#     flag_parms = { k: getattr(cv2,v) for (k,v) in aug_parms.items() 
#         if (isinstance(v, str) and hasattr(cv2, v))}
#     aug_parms = {k: v for (k,v) in aug_parms.items() if not isinstance(v, str)}
#     aug_parms.update(flag_parms)

#     log.debug(f"augmentation parameters for {augment_name}:{aug_parms}")
#     return aug_parms



