# The following imports NEED to be in the exact order
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor

# Simulation configs, input any new simulations here

from sir import config
from seir import config
from seird import config
from stochastic_seir import config

from cadCAD import configs
import pandas as pd


def run(drop_midsteps: bool=True) -> pd.DataFrame:
    """
    Run all experiments and return their output on the dataset column.
    Each line represents an iteration of the parameter-sweep combinations.
    """
    exec_mode = ExecutionMode()

    multi_mode_ctx = ExecutionContext(context=exec_mode.multi_mode)
    run = Executor(exec_context=multi_mode_ctx, configs=configs)
    raw_result, tensor_field, sessions = run.execute()
    results = pd.DataFrame(raw_result)
    return results
