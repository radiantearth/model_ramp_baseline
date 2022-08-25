# {{ stac.properties.title }}

{{ stac.properties.description }}

![{{stac.id}}](https://radiantmlhub.blob.core.windows.net/frontend-dataset-images/odk_sample_agricultural_dataset.png)

MLHub model id: `{{stac.id}}`. Browse on [Radiant MLHub](https://mlhub.earth/model/{{stac.id}}).

## Related MLHub Dataset {{ (Optional) }}

{{

If this model was based on a dataset which is already published to MLHub, enter that link here.

[https://mlhub.earth/data/ref_african_crops_kenya_02](https://mlhub.earth/data/ref_african_crops_kenya_02)

}}

## Citation

{{

example:

Amer, K. (2022) “A Spatio-Temporal Deep Learning-Based Crop Classification
Model for Satellite Imagery”, Version 1.0, Radiant MLHub. [Date Accessed]
Radiant MLHub. <https://doi.org/10.34911/rdnt.h28fju>

}}

## License

{{

example: CC-BY-4.0

(update the LICENSE file in this repository to match the license)

}}

## Creator{{s}}

{{

example: Model creators and links go here (examples: Radiant Earth Foundation, Microsoft
AI for Good Research Lab).

}}

## Contact

{{

Contact email goes here (example: ml@radiant.earth)

}}

## Applicable Spatial Extent

{{

Here please provide the applicable spatial extent, for new inferencing (this
may be the same, or different than the spatial extent of the training data).
Please provide the spatial extent bounding box as WKT text or GEOJSON text.

```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "properties": {
        "ID": 0
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
              [-90,35],
              [-90,30],
              [-85,30],
              [-85,35],
              [-90,35]
          ]
        ]
      }
    }
  ]
}
```

<https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-geojson-and-topojson-maps>

}}

## Applicable Temporal Extent

{{

The recommended start/end date of imagery for new inferencing. Example:

| Start | End |
|-------|-----|
| 2000-01-01 | present |

}}

## Learning Approach

{{

The learning approach used to train the model. It is recommended that you use
one of the values below, but other values are allowed.

* Supervised
* Unsupervised
* Semi-supervised
* Reinforcement-learning
* Other (explain)

Explain training steps such as augmentations and preprocessing used on image
before training.

A graphical representation of the model architecture within the documentation
could be helpful to individuals or organizations who would wish to replicate
workflow and reproduce same or even similar benchmark model results as well
make specific changes within the architecture in an attempt to further improve
it.

}}

## Prediction Type

{{

The type of prediction that the model makes. It is recommended that you use one
of the values below, but other values are allowed.

* Object-detection
* Classification
* Segmentation
* Regression
* Other (explain)

}}

## Model Architecture

{{

Identifies the architecture employed by the model. This may include any string
identifiers, but publishers are encouraged to use well-known identifiers
whenever possible. More details than just “it’s a CNN”!

}}

## Training Operating System

{{

Identifies the operating system on which the model was trained.

* Linux
* Windows (win32)
* Windows (cygwin)
* MacOS (darwin)
* Other (explain)

}}

## Training Processor Type

{{

The type of processor used during training. Must be one of "cpu" or "gpu".

* cpu
* gpu

}}

## Model Inferencing

Review the [GitHub repository README](../README.md) to get started running
this model for new inferencing.

## Structure of Output Data

{{

Explain output file names and formats, interpretation, classes, etc.

}}
