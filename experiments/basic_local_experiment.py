import myopt as opt

params = [
    opt.Hyperparameter("x", opt.Float(0, 1)),
    opt.Hyperparameter("y", opt.Float(0, 1)),
]

meta_dir = "results/local"
sge_runner = opt.LocalRunner(meta_dir, "./test.sh", ["default", "--argument=3"])

experiment = opt.Experiment(meta_dir, params, sge_runner)

experiment.runner.start({"a": 3})