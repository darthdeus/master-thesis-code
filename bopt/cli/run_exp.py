import os
import sys
import yaml

import bopt

def run(args) -> None:
    meta_fname = os.path.join(
        args.DIR,
        "meta.yml"
    )

    if os.path.exists(meta_fname):

        print("Found existing meta.yml, resuming experiment.")
        experiment = bopt.Experiment.deserialize(args.DIR)

        # TODO
        experiment.run_loop(bopt.models.gpy_model.GPyModel(), args.DIR, n_iter=args.n_iter)
    else:
        print(f"There is no `meta.yml` at {meta_fname}.")
        sys.exit(1)
