# Replicable AI for Microplanning (Ramp) Bootstrap Model

The Replicable AI for Microplanning (Ramp) deep learning model is a semantic
segmentation one which detects buildings from satellite imagery and delineates
the footprints in low-and-middle-income countries (LMICs) using satellite
imagery and enables in-country users to build their own deep learning models
for their regions of interest. The architecture and approach were inspired by
the Eff-UNet model outlined in this
[CVPR 2020 Paper](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w22/Baheti_Eff-UNet_A_Novel_Architecture_for_Semantic_Segmentation_in_Unstructured_Environment_CVPRW_2020_paper.pdf).

![model_ramp_baseline_v1](https://radiantmlhub.blob.core.windows.net/frontend-ml-model-images/model_ramp_baseline_v1.png)

MLHub model id: `model_ramp_baseline_v1`. Browse on [Radiant MLHub](https://mlhub.earth/model/model_ramp_baseline_v1).

## ML Model Documentation

Please review the model architecture, license, applicable spatial and temporal extents
and other details in the [model documentation](/docs/index.md).

## System Requirements

* Git client
* [Docker](https://www.docker.com/) with
    [Compose](https://docs.docker.com/compose/) v1.28 or newer.

## Hardware Requirements

|            |Inferencing|Training|
|------------|-----------|--------|
| RAM        | 4 GB RAM    | [View Ramp model card](https://rampml.global/ramp-model-card/) |
| NVIDIA GPU | optional  | [required](https://rampml.global/ramp-model-card/) |

## Get Started With Inferencing

First clone this Git repository. Please note: this repository uses
[Git Large File Support (LFS)](https://git-lfs.github.com/) to include the
model checkpoint file. Either install `git lfs` support for your git client,
use the official Mac or Windows GitHub client to clone this repository.

```bash
git clone https://github.com/radiantearth/model_ramp_baseline.git
cd model_ramp_baseline/
```

After cloning the model repository, you can use the Docker Compose runtime
files as described below.

Please note: these command-line examples were tested on Linux and MacOS.
Windows and WSL users may need to substitute appropriate commands, especially
for setting environment variables.

## Pull or Build the Docker Image

Pull pre-built image from Docker Hub (recommended):

```bash
# cpu
docker pull docker.io/radiantearth/model_ramp_baseline:1
# optional, for NVIDIA gpu
docker pull docker.io/radiantearth/model_ramp_baseline:1-gpu

```

Or build image from source:

```bash
# cpu
docker build -t radiantearth/model_ramp_baseline:1 -f Dockerfile_cpu .
# for NVIDIA gpu
docker build -t radiantearth/model_ramp_baseline:1-gpu -f Dockerfile_gpu .

```

## Run Model to Generate New Inferences

1. Prepare your input and output data folders. The `data/` folder in this repository
    contains some placeholder files to guide you.

    * The `data/` folder must contain:
        * `input/chips` imagery chips for inferencing.
            [For example, Maxar ODP imagery](https://rampml.global/ramp-faqs/)
            * File name: `chip_id.tif` for example:
                `0fec2d30-882a-4d1d-a7af-89dac0198327.tif`.
            * File Format: GeoTIFF, 256x256
            * Coordinate Reference System: WGS84, EPSG:4326
            * Bands: 3 bands per file:
                * Band 1 Type=Byte, ColorInterp=Red
                * Band 2 Type=Byte, ColorInterp=Green
                * Band 3 Type=Byte, ColorInterp=Blue
        * `/input/checkpoint.tf` the model checkpoint folder in tensorflow format.
            Please note: the model checkpoint is included in this repository.
    * The `output/` folder is where the model will write inferencing results.

2. Set `INPUT_DATA` and `OUTPUT_DATA` environment variables corresponding with
    your input and output folders. These commands will vary depending on operating
    system and command-line shell:

    ```bash
    # change paths to your actual input and output folders
    export INPUT_DATA="/home/my_user/model_ramp_baseline/data/input/"
    export OUTPUT_DATA="/home/my_user/model_ramp_baseline/data/output/"
    ```

3. Run the appropriate Docker Compose command for your system:

    Use either `docker compose` or `docker-compose` depending on your system.

    ```bash
    # cpu
    docker compose up model_ramp_baseline_v1_cpu
    # NVIDIA gpu driver
    docker compose up model_ramp_baseline_v1_gpu
    ```

4. Wait for the `docker compose` to finish running, then inspect the
`OUTPUT_DATA` folder for results.

## Understanding Output Data

Please review the model output format and other technical details in the [model
documentation](/docs/index.md).
