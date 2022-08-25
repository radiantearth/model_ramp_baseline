
import os, re

def get_spacenet_file_number_hash(chip_or_label_dir):
    all_files = [filename for filename in os.listdir(chip_or_label_dir) if filename.endswith('.tif') or filename.endswith('.geojson')]
    basenames = [os.path.splitext(filename)[0] for filename in all_files]
    match_pattern = re.compile(r"img(?P<numbers>[0-9]+)$")
    file_matches = [match_pattern.search(basename) for basename in basenames]
    filenumbers = [int(file_match.group("numbers")) for file_match in file_matches]
    filenumber_dict = {}
    for file_number, filepath in zip(filenumbers, [os.path.join(chip_or_label_dir, filename) for filename in all_files]):
        filenumber_dict[file_number] = filepath
    return filenumber_dict


def spacenet_names_match(file1, file2):
    '''
    This will tell you whether two spacenet files have matching numbers. 
    The spacenet files can be any of jsons, image chips, or standard masks.
    Standard mask names are the same as the chip names, but with extension mask.tif instead of tif.
    '''

    # if full paths, get filename only
    file1 = os.path.split(file1)[1]
    file2 = os.path.split(file2)[1]

    # get base of filename without extensions
    fbase1 = os.path.splitext(file1)[0]
    fbase2 = os.path.splitext(file2)[0]

    # get the number of the base filenames.
    # this will match numbers in spacenet jsons, image chips, or masks with extension mask.tif.
    match_pattern = re.compile(r"img(?P<numbers>[0-9]+)(\.mask)?$")
    match1 = match_pattern.search(fbase1)
    match2 = match_pattern.search(fbase2)
    number1 = int(match1.group("numbers"))
    number2 = int(match2.group("numbers"))
    return number1 == number2

def construct_mask_filepath(mask_dir, path_to_chip):
    '''
    Constructs a standard mask file path given the mask directory and the chip filename.
    Standard masks have the name: (chip_basename).mask.tif.
    This means they will alphabetically sort the same way as the image chips did.
    '''

    chip_filename = os.path.split(path_to_chip)[1]
    chip_basename = os.path.splitext(chip_filename)[0]
    mask_file = chip_basename + '.mask.tif'
    return os.path.join(mask_dir, mask_file)


def get_tq_chip_label_pairs(chip_dir, label_dir):
    '''
    Get a list of pairs of matching chips and labels from TQ-delivered directories.
    Checks to be sure all chips matching delivered labels are present.

    Matched files are named (e.g.) 84930efd.tif and 84930efd.geojson.

    :param directory chip_dir: directory containing image chips
    :param directory label_dir: directory containing geojson vectors

    Returns: list of tuples of chip and label filename pairs.
    '''

    # construct list of matching image chips from json labels

    # get sorted geojson file names
    gj_files = sorted([gj_file for gj_file in os.listdir(label_dir) if gj_file.endswith('.geojson')])
    
    # get matching chip file names -- for TQ deliveries these have the same base filename 
    basenames = [os.path.splitext(gj_file)[0] for gj_file in gj_files]
    print(basenames[0])
    chip_files = [basename + '.tif' for basename in basenames]

    # get full pathnames to json and chip files
    json_paths = [os.path.join(label_dir, gj_file) for gj_file in gj_files]
    chip_paths = [os.path.join(chip_dir, chip_file) for chip_file in chip_files]

    # check to be sure the matching image chips are present
    for chip_path in chip_paths:
        if not os.path.exists(chip_path):
            raise FileNotFoundError(f'Missing: required image chip file {chip_path}')
    
    return list(zip(chip_paths, json_paths))


def get_sn_chip_label_pairs(chip_dir, label_dir):
    '''
    Get a list of pairs of matching chips and labels from Spacenet-2 downloads.
    Checks to be sure all matches are present.

    Matched spacenet files have basenames that end with the same strings: 
    e.g., RGB-PanSharpen_AOI_5_Khartoum_img1013.tif & buildings_AOI_5_Khartoum_img1013.geojson.

    :param directory chip_dir: directory containing image chips
    :param directory label_dir: directory containing geojson vectors

    Returns: list of tuples of chip and label filename pairs.
    '''

    # construct list of matching image chips from json labels
    # These don't sort alphabetically the same way! I am getting json file 100 matching chip file 1!

    # get sorted geojson file names
    label_hash = get_spacenet_file_number_hash(label_dir)
    chip_hash = get_spacenet_file_number_hash(chip_dir)

    chip_label_pairs = []
    for key in label_hash.keys():
        json_file = label_hash[key]
        try:
            chip_file = chip_hash[key]
        except KeyError:
            print(f"Chip file with ID {key} not found in {chip_dir}")
            raise
        if not spacenet_names_match(chip_file, json_file):
            print(f"Chip name: {chip_file}")
            print(f"Json name: {json_file}")
            raise RuntimeError("Chip and geojson file numbers do not match")
        chip_label_pairs.append((chip_file, json_file))

    return chip_label_pairs

    