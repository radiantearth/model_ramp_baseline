# Ramp Baseline Model for Building Footprint Segmentation

The Replicable AI for Microplanning (Ramp) deep learning model is a semantic segmentation one which detects buildings from satellite imagery and delineates the footprints in low-and-middle-income countries (LMICs) using satellite imagery and enables in-country users to build their own deep learning models for their regions of interest. The architecture and approach were inspired by the Eff-UNet model outlined in this [CVPR 2020 Paper](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w22/Baheti_Eff-UNet_A_Novel_Architecture_for_Semantic_Segmentation_in_Unstructured_Environment_CVPRW_2020_paper.pdf). 

![model_ramp_baseline_v1](https://radiantmlhub.blob.core.windows.net/frontend-ml-model-images/model_ramp_baseline_v1.png)

MLHub model id: `model_ramp_baseline_v1`. Browse on [Radiant MLHub](https://mlhub.earth/model/model_ramp_baseline_v1).

## Training Data

- [Ghana Source](https://api.radiant.earth/mlhub/v1/collections/ramp_accra_ghana_source)
- [Ghana Labels](https://api.radiant.earth/mlhub/v1/collections/ramp_accra_ghana_labels)
- [India Source](https://api.radiant.earth/mlhub/v1/collections/ramp_karnataka_india_source)
- [India Labels](https://api.radiant.earth/mlhub/v1/collections/ramp_karnataka_india_labels)
- [Malawi Source](https://api.radiant.earth/mlhub/v1/collections/ramp_mzuzu_malawi_source)
- [Malawi Labels](https://api.radiant.earth/mlhub/v1/collections/ramp_mzuzu_malawi_labels)
- [Myanmar Source](https://api.radiant.earth/mlhub/v1/collections/ramp_hpa_an_myanmar_source)
- [Myanmar Labels](https://api.radiant.earth/mlhub/v1/collections/ramp_hpa_an_myanmar_labels)
- [Oman Source](https://api.radiant.earth/mlhub/v1/collections/ramp_muscat_oman_source)
- [Oman Labels](https://api.radiant.earth/mlhub/v1/collections/ramp_muscat_oman_labels)
- [Sierra Leone Source](https://api.radiant.earth/mlhub/v1/collections/ramp_manjama_sierra_leone_source)
- [Sierra Leone Labels](https://api.radiant.earth/mlhub/v1/collections/ramp_manjama_sierra_leone_labels)
- [South Sudan Source](https://api.radiant.earth/mlhub/v1/collections/ramp_bentiu_south_sudan_source)
- [South Sudan Labels](https://api.radiant.earth/mlhub/v1/collections/ramp_bentiu_south_sudan_labels)
- [St Vincent Source](https://api.radiant.earth/mlhub/v1/collections/ramp_mesopotamia_st_vincent_source)
- [St Vincent Labels](https://api.radiant.earth/mlhub/v1/collections/ramp_mesopotamia_st_vincent_labels)

## Related MLHub Dataset

[Ramp Building Footprint Datasets](https://mlhub.earth/datasets?search=ramp)

## Citation

DevGlobal (2022) “Ramp Baseline Model for Building Footprint Segmentation”, Version 1.0, Radiant MLHub. [Date Accessed]
Radiant MLHub. <https://doi.org/10.34911/rdnt.1xe81y>

## License

CC BY-NC 4.0

## Creator

[DevGlobal](https://dev.global/)

## Contact

info@dev.global

## Applicable Spatial Extent

```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      'geometry': {
        'coordinates': [
          [
            [-0.24987, 5.573258],
            [5.647172, 5.573258],
            [5.647172, -0.18988],
            [-0.24987, -0.18988],
            [-0.24987, 5.573258]
          ]
        ],
        'type': 'Polygon'
      },
      'id': 0,
      'properties': {
        'ID': 0
      },
      'type': 'Feature'
    },
    {
      'geometry': {
        'coordinates': [
          [
            [75.893292, 12.015134],
            [12.981374, 12.015134],
            [12.981374, 76.014896],
            [75.893292, 76.014896],
            [75.893292, 12.015134]
          ]
        ],
        'type': 'Polygon'
      },
      'id': 1,
      'properties': {
        'ID': 1
      },
      'type': 'Feature'
    },
    {
      'geometry': {
        'coordinates': [
          [
            [33.964771, -11.488537],
            [-11.390598, -11.488537],
            [-11.390598, 34.052217],
            [33.964771, 34.052217],
            [33.964771, -11.488537]
          ]
        ],
        'type': 'Polygon'
      },
      'id': 2,
      'properties': {
        'ID': 2
      },
      'type': 'Feature'
    },
    {
      'geometry': {
        'coordinates': [
          [
            [97.577051, 16.806055],
            [16.915819, 16.806055],
            [16.915819, 97.697025],
            [97.577051, 97.697025],
            [97.577051, 16.806055]
          ]
        ],
        'type': 'Polygon'
      },
      'id': 3,
      'properties': {
        'ID': 3
      },
      'type': 'Feature'
    },
    {
      'geometry': {
        'coordinates': [
          [
            [58.452592, 23.587606],
            [23.643006, 23.587606],
            [23.643006, 58.599653],
            [58.452592, 58.599653],
            [58.452592, 23.587606]
          ]
        ],
        'type': 'Polygon'
      },
      'id': 4,
      'properties': {
        'ID': 4
      },
      'type': 'Feature'
    },
    {
      'geometry': {
        'coordinates': [
          [
            [-11.772279, 7.921254],
            [7.98898, 7.921254],
            [7.98898, -11.698137],
            [-11.772279, -11.698137],
            [-11.772279, 7.921254]
          ]
        ],
        'type': 'Polygon'
      },
      'id': 5,
      'properties': {
        'ID': 5
      },
      'type': 'Feature'
    },
    {
      'geometry': {
        'coordinates': [
          [
            [29.777953, 9.228564],
            [9.342134, 9.228564],
            [9.342134, 29.831493],
            [29.777953, 29.831493],
            [29.777953, 9.228564]
          ]
        ],
        'type': 'Polygon'
      },
      'id': 6,
      'properties': {
        'ID': 6
      },
      'type': 'Feature'
    },
    {
      'geometry': {
        'coordinates': [
          [
            [-61.259591, 13.123114],
            [13.201815, 13.123114],
            [13.201815, -61.154656],
            [-61.259591, -61.154656],
            [-61.259591, 13.123114]
          ]
        ],
        'type': 'Polygon'
      },
      'id': 7,
      'properties': {
        'ID': 7
      },
      'type': 'Feature'
    }
  }
  ]
}
```

## Applicable Temporal Extent

| Start | End |
|-------|-----|
| 2007-10-01 | present |

## Learning Approach

Supervised

## Prediction Type

Segmentation

## Model Architecture

Eff-UNet

## Training Operating System

Linux

## Training Processor Type

GPU

## Model Inferencing

Review the [GitHub repository README](../README.md) to get started running
this model for new inferencing.

## Methodology

{{

Use this section to provide more information to the reader about the model. Be
as descriptive as possible. The suggested sub-sections are as following:

}}

### Training

{{

Explain training steps such as augmentations and preprocessing used on image
before training.

}}

### Model

{{

Expalin the model and why you chose the model in this section. A graphical representation
of the model architecture could be helpful to individuals or organizations who would 
wish to replicate the workflow and reproduce the model results or to change the model 
architecture and improve the results.  

}}

### Structure of Output Data

{{

Explain output file names and formats, interpretation, classes, etc.

}}
