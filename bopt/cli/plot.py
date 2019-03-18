import os
import sys
import yaml
from tqdm import tqdm

from typing import List

import bopt
from bopt.cli.util import handle_cd, ensure_meta_yml, acquire_lock
from bopt.models.gpy_model import GPyModel

# TODO: co kdyz dostanu manual evaluation, zkusit precejenom fitnout model
#       ale do plotu napsat, ze ten model neni podle ceho byl vybrany?
def run(args) -> None:
    handle_cd(args)

    with acquire_lock(), ensure_meta_yml():
        experiment = bopt.Experiment.deserialize(".")

        processed_samples: List[bopt.Sample] = []

        for sample in tqdm(experiment.samples):
            if sample.model.model_name == GPyModel.model_name:
                sample_col = bopt.SampleCollection(processed_samples, ".")
                X, Y = sample_col.to_xy()

                model = GPyModel.from_model_params(sample.model, X, Y)

                experiment.plot_current(model, ".", sample.to_x())

            processed_samples.append(sample)
