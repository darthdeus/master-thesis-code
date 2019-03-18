import os
import sys
import yaml

import bopt
from bopt.cli.util import handle_cd, ensure_meta_yml, acquire_lock


def run(args) -> None:
    handle_cd(args)

    with acquire_lock(), ensure_meta_yml():
        experiment = bopt.Experiment.deserialize(".")

        # TODO: unify naming run_params vs model_params
        model_params = vars(args).copy()
        del model_params["bopt"]
        del model_params["func"]
        if "dir" in model_params:
            del model_params["dir"]

        __import__('ipdb').set_trace()

        experiment.manual_run(bopt.ModelConfig.default(), ".",
                model_params, bopt.ModelParameters.for_manual_run())
