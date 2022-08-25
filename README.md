{{

:construction: This is a template git repository for a ml-model to be published
on [mlhub.earth](https://mlhub.earth). Create a repository using this template,
named as the model id, without the version suffix.

For example model id `model_unet_agri_western_cape_v1` would use:

* Github repository name for publishing: `model_unet_agri_western_cape`, release to be tagged as `v1`.
* Github repository name for Radiant internal development (if needed): `model_unet_agri_western_cape_dev`.

:warning: Remember: all text in all files this repo using `{{` mustache brackets `}}` should be
edited, or the text yanked out.

:pushpin: stac references are in reference to the ml-model extension: <https://github.com/stac-extensions/ml-model>

}}

# {{ stac.properties.title }}

{{ stac.properties.description }}

![{{stac.id}}](https://radiantmlhub.blob.core.windows.net/frontend-dataset-images/odk_sample_agricultural_dataset.png)

MLHub model id: `{{stac.id}}`. Browse on [Radiant MLHub](https://mlhub.earth/model/{{stac.id}}).

## ML Model Documentation

Please review the model architecture, license, applicable spatial and temporal extents
and other details in the [model documentation](/docs/index.md).

## System Requirements

* Git client
* [Docker](https://www.docker.com/) with
    [Compose](https://docs.docker.com/compose/) v1.28 or newer.

## Hardware Requirements

|Inferencing|Training|
|-----------|--------|
|{{int}}GB RAM | {{int}}GB RAM|
|           | NVIDIA GPU |

## Get Started With Inferencing

First clone this Git repository.

{{

(:pushpin: only include the following LFS section if a file > 100MB had to be
committed using LFS

<https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github>)

}}

{{

Please note: this repository uses
[Git Large File Support (LFS)](https://git-lfs.github.com/) to include the
model checkpoint file. Either install `git lfs` support for your git client,
use the official Mac or Windows GitHub client to clone this repository.

}}

```bash
git clone https://github.com/{{your_org_name}}/{{repository_name}}.git
cd {{repository_name}}/
```

After cloning the model repository, you can use the Docker Compose runtime
files as described below.

## Pull or Build the Docker Image

{{

:pushpin: Model developer: please build and publish your images to [Docker
Hub](https://hub.docker.com/). The images should be public, and should be
tagged as `model_id:version` and `model_id:version-gpu`.

For example model_id `model_unet_agri_western_cape_v1`
would have two docker image tags published on Docker Hub:

* `model_unet_agri_western_cape:1` for cpu inferencing
* `model_unet_agri_western_cape:1-gpu` for gpu inferencing

}}

Pull pre-built image from Docker Hub (recommended):

```bash
# cpu
docker pull docker.io/{{your_org_name}}/{{repository_name}}:1
# optional, for NVIDIA gpu
docker pull docker.io/{{your_org_name}}/{{repository_name}}:1-gpu

```

Or build image from source:

```bash
# cpu
docker build -t {{your_org_name}}/{{repository_name}}:1 -f Dockerfile_cpu .
# for NVIDIA gpu
docker build -t {{your_org_name}}/{{repository_name}}:1-gpu -f Dockerfile_gpu .

```

## Run Model to Generate New Inferences

{{

:pushpin: Model developer: do not commit training data to the data folder on
this repo, this is only a placeholder to run the model locally for inferencing.

}}

1. Prepare your input and output data folders. The `data/` folder in this repository
    contains some placeholder files to guide you.

    * The `data/` folder must contain:
        * `input/chips` {{ Landsat, Maxar Open-Data 30cm, Sentinel-2, etc. }} imagery chips for inferencing:
            * File name: {{ `chip_id.tif` }} e.g. {{ `0fec2d30-882a-4d1d-a7af-89dac0198327.tif` }}
            * File Format: {{ GeoTIFF, 256x256 }}
            * Coordinate Reference System: {{ WGS84, EPSG:4326 }}
            * Bands: {{ 3 bands per file:
                * Band 1 Type=Byte, ColorInterp=Red
                * Band 2 Type=Byte, ColorInterp=Green
                * Band 3 Type=Byte, ColorInterp=Blue
                }}
        * `/input/checkpoint` the model checkpoint {{ file | folder }}, `{{ checkpoint file or folder name }}`.
            Please note: the model checkpoint is included in this repository.
    * The `output/` folder is where the model will write inferencing results.

2. Set `INPUT_DATA` and `OUTPUT_DATA` environment variables corresponding with
    your input and output folders. These commands will vary depending on operating
    system and command-line shell:

    ```bash
    # change paths to your actual input and output folders
    export INPUT_DATA="/home/my_user/{{repository_name}}/data/input/"
    export OUTPUT_DATA="/home/my_user/{{repository_name}}/data/output/"
    ```

3. Run the appropriate Docker Compose command for your system:

    ```bash
    # cpu
    docker compose up {{stac.id}}_cpu
    # NVIDIA gpu driver
    docker compose up {{stac.id}}_gpu
    ```

4. Wait for the `docker compose` to finish running, then inspect the
`OUTPUT_DATA` folder for results.

## Understanding Output Data

Please review the model output format and other technical details in the [model
documentation](/docs/index.md).
