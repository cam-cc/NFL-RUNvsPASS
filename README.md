# NFL Big Data Bowl 2025 - Pre-snap Analysis with 2D CNN 🏈🏆


https://www.kaggle.com/competitions/nfl-big-data-bowl-2025/overview

## Overview
This repository contains a 1D Convolutional Neural Network (CNN) implementation for analyzing NFL pre-snap player tracking data as part of the NFL Big Data Bowl 2025 competition. The model aims to identify patterns in pre-snap movements and formations to predict post-snap outcomes.

## Competition Context
The NFL Big Data Bowl 2025 focuses on what happens before the snap to generate insights into post-snap behavior. Teams have 40 seconds to run a play, during which both offensive and defensive units make strategic decisions through formations, motions, and alignments.

## Data Description
The dataset includes player tracking data from the NFL Next Gen Stats team and additional data from Pro Football Focus (PFF). Key data components:

- Player tracking data (10 fps)
- Game and play information
- Player metadata
- Pre-snap events and formations
- Post-snap outcomes ( not needed )

### Key Features
- Player position coordinates (x, y)
- Player speed and acceleration
- Player orientation and direction
- Pre-snap events (shifts, motions)
- Formation and personnel groupings

## Model Architecture

### 2D CNN Overview

The model employs a hybrid architecture that combines neural network components with convolutional processing. It processes input features through two parallel paths:

1. A feature group pathway that uses dense layers with batch normalization and dropout
2. A convolutional pathway that processes the reshaped input through 2D convolutions

The use of parallel processing paths is because some features are more meaningful when processed together. The goal of this hybrid approach is for the CNN pathway to capture formation-based patterns and the dense feature pathway can process situational features (down, distance, tendencies) This combination allows the model to weigh both structural and situational factors in its predictions

## Setup

### Requirements
```
python>=3.8
tensorflow>=2.8.0
pandas
numpy
scikit-learn
```

### Installation
```bash
git clone https://github.com/cam-cc/NFL-RUNvsPASS
cd NFL-RUNvsPASS
pip install -r requirements.txt
```

## Usage

## Project Structure
```
├── data/
│   ├── *.csv                    # Original competition data
├── models/
│   ├── bet_model.pth            # best model weights
├── metrics/
│   ├── eval_metrics.csv         # best model training and val losses
├── nfl-runvspass.ipynb           # Jupyter notebook
├── requirements.txt
└── README.md
```

## Evaluation
The competition evaluates submissions on:
- Football Score (30%): Practical applicability
- Data Science Score (30%): Technical correctness
- Report Score (20%): Documentation quality
- Data Visualization Score (20%): Visual communication

## Competition Rules
- Submissions must be made public on Kaggle
- Maximum 2,000 words and 10 tables/figures
- Must use provided tracking data
- Team size limited to 4 members

## License
This project follows competition guidelines for open-source sharing. See the [Competition Rules](https://www.kaggle.com/competitions/nfl-big-data-bowl-2025/rules) for detailed licensing information.

## Acknowledgments
- NFL Next Gen Stats for providing tracking data
- Pro Football Focus for additional game data
- Kaggle and NFL for hosting the competition
