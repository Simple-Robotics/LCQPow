from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import typing
__all__: list[str] = ['AlgorithmStatus', 'C_STATIONARY_SOLUTION', 'FAILED_SWITCH_TO_DENSE', 'FAILED_SWITCH_TO_SPARSE', 'FAILED_SYM_COMPLEMENTARITY_MATRIX', 'INDEX_OUT_OF_BOUNDS', 'INITIAL_SUBPROBLEM_FAILED', 'INNER_LOOP_ITERATES', 'INVALID_ARGUMENT', 'INVALID_COMPLEMENTARITY_MATRIX', 'INVALID_COMPLEMENTARITY_TOLERANCE', 'INVALID_CONSTRAINT_MATRIX', 'INVALID_ETA_VALUE', 'INVALID_INDEX_ARRAY', 'INVALID_INDEX_POINTER', 'INVALID_INITIAL_PENALTY_VALUE', 'INVALID_LOWER_COMPLEMENTARITY_BOUND', 'INVALID_MAX_ITERATIONS_VALUE', 'INVALID_MAX_RHO_VALUE', 'INVALID_NUMBER_OF_COMP_VARS', 'INVALID_NUMBER_OF_CONSTRAINT_VARS', 'INVALID_NUMBER_OF_OPTIM_VARS', 'INVALID_OBJECTIVE_LINEAR_TERM', 'INVALID_OSQP_BOX_CONSTRAINTS', 'INVALID_PENALTY_UPDATE_VALUE', 'INVALID_PRINT_LEVEL_VALUE', 'INVALID_QPSOLVER', 'INVALID_RHO_OPT', 'INVALID_STATIONARITY_TOLERANCE', 'INVALID_TOTAL_ITER_COUNT', 'INVALID_TOTAL_OUTER_ITER', 'IVALID_SUBPROBLEM_ITER', 'LCQPOBJECT_NOT_SETUP', 'LCQProblem', 'MAX_ITERATIONS_REACHED', 'MAX_PENALTY_REACHED', 'M_STATIONARY_SOLUTION', 'NONE', 'NOT_YET_IMPLEMENTED', 'OSQP_INITIAL_DUAL_GUESS_FAILED', 'OSQP_INITIAL_PRIMAL_GUESS_FAILED', 'OSQP_SPARSE', 'OSQP_WORKSPACE_NOT_SET_UP', 'OUTER_LOOP_ITERATES', 'Options', 'OutputStatistics', 'PROBLEM_NOT_SOLVED', 'PrintLevel', 'QPOASES_DENSE', 'QPOASES_SPARSE', 'QPSolver', 'ReturnValue', 'SUBPROBLEM_SOLVER_ERROR', 'SUCCESSFUL_RETURN', 'S_STATIONARY_SOLUTION', 'UNABLE_TO_READ_FILE', 'W_STATIONARY_SOLUTION', 'cscWrapper']
class AlgorithmStatus:
    """
    Members:
    
      PROBLEM_NOT_SOLVED
    
      W_STATIONARY_SOLUTION
    
      C_STATIONARY_SOLUTION
    
      M_STATIONARY_SOLUTION
    
      S_STATIONARY_SOLUTION
    """
    C_STATIONARY_SOLUTION: typing.ClassVar[AlgorithmStatus]  # value = <AlgorithmStatus.C_STATIONARY_SOLUTION: 2>
    M_STATIONARY_SOLUTION: typing.ClassVar[AlgorithmStatus]  # value = <AlgorithmStatus.M_STATIONARY_SOLUTION: 3>
    PROBLEM_NOT_SOLVED: typing.ClassVar[AlgorithmStatus]  # value = <AlgorithmStatus.PROBLEM_NOT_SOLVED: 0>
    S_STATIONARY_SOLUTION: typing.ClassVar[AlgorithmStatus]  # value = <AlgorithmStatus.S_STATIONARY_SOLUTION: 4>
    W_STATIONARY_SOLUTION: typing.ClassVar[AlgorithmStatus]  # value = <AlgorithmStatus.W_STATIONARY_SOLUTION: 1>
    __members__: typing.ClassVar[dict[str, AlgorithmStatus]]  # value = {'PROBLEM_NOT_SOLVED': <AlgorithmStatus.PROBLEM_NOT_SOLVED: 0>, 'W_STATIONARY_SOLUTION': <AlgorithmStatus.W_STATIONARY_SOLUTION: 1>, 'C_STATIONARY_SOLUTION': <AlgorithmStatus.C_STATIONARY_SOLUTION: 2>, 'M_STATIONARY_SOLUTION': <AlgorithmStatus.M_STATIONARY_SOLUTION: 3>, 'S_STATIONARY_SOLUTION': <AlgorithmStatus.S_STATIONARY_SOLUTION: 4>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LCQProblem:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, nV: typing.SupportsInt, nC: typing.SupportsInt, nComp: typing.SupportsInt) -> None:
        ...
    def getDualSolution(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]:
        ...
    def getNumberOfDuals(self) -> int:
        ...
    def getOutputStatistics(self, arg0: OutputStatistics) -> None:
        ...
    def getPrimalSolution(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]:
        ...
    @typing.overload
    def loadLCQP(self, Q: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, n]", "flags.f_contiguous"], g: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"], L: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, n]", "flags.f_contiguous"], R: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, n]", "flags.f_contiguous"], lbL: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., ubL: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., lbR: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., ubR: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., A: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, n]", "flags.f_contiguous"] = ..., lbA: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., ubA: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., lb: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., ub: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., x0: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., y0: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ...) -> ReturnValue:
        ...
    @typing.overload
    def loadLCQP(self, Q: cscWrapper, g: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"], L: cscWrapper, R: cscWrapper, lbL: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., ubL: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., lbR: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., ubR: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., A: cscWrapper = ..., lbA: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., ubA: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., lb: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., ub: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., x0: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ..., y0: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"] = ...) -> ReturnValue:
        ...
    @typing.overload
    def loadLCQP(self, Q_file: str, g_file: str, L_file: str, R_file: str, lbL_file: str = None, ubL_file: str = None, lbR_file: str = None, ubR_file: str = None, A_file: str = None, lbA_file: str = None, ubA_file: str = None, lb_file: str = None, ub_file: str = None, x0_file: str = None, y0_file: str = None) -> ReturnValue:
        ...
    def runSolver(self) -> ReturnValue:
        ...
    def setOptions(self, arg0: Options) -> None:
        ...
class Options:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, rhs: Options) -> None:
        ...
    def getComplementarityTolerance(self) -> float:
        ...
    def getEtaDynamicPenalty(self) -> float:
        ...
    def getInitialPenaltyParameter(self) -> float:
        ...
    def getMaxIterations(self) -> int:
        ...
    def getMaxPenaltyParameter(self) -> float:
        ...
    def getNDynamicPenalty(self) -> int:
        ...
    def getPenaltyUpdateFactor(self) -> float:
        ...
    def getPrintLevel(self) -> PrintLevel:
        ...
    def getQPSolver(self) -> QPSolver:
        ...
    def getSolveZeroPenaltyFirst(self) -> bool:
        ...
    def getStationarityTolerance(self) -> float:
        ...
    def getStoreSteps(self) -> bool:
        ...
    def setComplementarityTolerance(self, arg0: typing.SupportsFloat) -> ReturnValue:
        ...
    def setEtaDynamicPenalty(self, arg0: typing.SupportsFloat) -> ReturnValue:
        ...
    def setInitialPenaltyParameter(self, arg0: typing.SupportsFloat) -> ReturnValue:
        ...
    def setMaxIterations(self, arg0: typing.SupportsInt) -> ReturnValue:
        ...
    def setMaxPenaltyParameter(self, arg0: typing.SupportsFloat) -> ReturnValue:
        ...
    def setNDynamicPenalty(self, arg0: typing.SupportsInt) -> ReturnValue:
        ...
    def setPenaltyUpdateFactor(self, arg0: typing.SupportsFloat) -> ReturnValue:
        ...
    @typing.overload
    def setPrintLevel(self, arg0: PrintLevel) -> ReturnValue:
        ...
    @typing.overload
    def setPrintLevel(self, arg0: typing.SupportsInt) -> ReturnValue:
        ...
    @typing.overload
    def setQPSolver(self, arg0: QPSolver) -> ReturnValue:
        ...
    @typing.overload
    def setQPSolver(self, arg0: typing.SupportsInt) -> ReturnValue:
        ...
    def setSolveZeroPenaltyFirst(self, arg0: bool) -> ReturnValue:
        ...
    def setStationarityTolerance(self, arg0: typing.SupportsFloat) -> ReturnValue:
        ...
    def setStoreSteps(self, arg0: bool) -> ReturnValue:
        ...
    def setToDefault(self) -> None:
        ...
class OutputStatistics:
    def __init__(self) -> None:
        ...
    def getAccuSubproblemIters(self) -> list[int]:
        ...
    def getInnerIters(self) -> list[int]:
        ...
    def getIterOuter(self) -> int:
        ...
    def getIterTotal(self) -> int:
        ...
    def getMeritVals(self) -> list[float]:
        ...
    def getObjVals(self) -> list[float]:
        ...
    def getPhiVals(self) -> list[float]:
        ...
    def getQPSolverExitFlag(self) -> int:
        ...
    def getRhoOpt(self) -> float:
        ...
    def getSolutionStatus(self) -> AlgorithmStatus:
        ...
    def getStatVals(self) -> list[float]:
        ...
    def getStepLength(self) -> list[float]:
        ...
    def getStepSize(self) -> list[float]:
        ...
    def getSubproblemIter(self) -> int:
        ...
    def getSubproblemIters(self) -> list[int]:
        ...
class PrintLevel:
    """
    Members:
    
      NONE
    
      OUTER_LOOP_ITERATES
    
      INNER_LOOP_ITERATES
    """
    INNER_LOOP_ITERATES: typing.ClassVar[PrintLevel]  # value = <PrintLevel.INNER_LOOP_ITERATES: 2>
    NONE: typing.ClassVar[PrintLevel]  # value = <PrintLevel.NONE: 0>
    OUTER_LOOP_ITERATES: typing.ClassVar[PrintLevel]  # value = <PrintLevel.OUTER_LOOP_ITERATES: 1>
    __members__: typing.ClassVar[dict[str, PrintLevel]]  # value = {'NONE': <PrintLevel.NONE: 0>, 'OUTER_LOOP_ITERATES': <PrintLevel.OUTER_LOOP_ITERATES: 1>, 'INNER_LOOP_ITERATES': <PrintLevel.INNER_LOOP_ITERATES: 2>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class QPSolver:
    """
    Members:
    
      QPOASES_DENSE
    
      QPOASES_SPARSE
    
      OSQP_SPARSE
    """
    OSQP_SPARSE: typing.ClassVar[QPSolver]  # value = <QPSolver.OSQP_SPARSE: 2>
    QPOASES_DENSE: typing.ClassVar[QPSolver]  # value = <QPSolver.QPOASES_DENSE: 0>
    QPOASES_SPARSE: typing.ClassVar[QPSolver]  # value = <QPSolver.QPOASES_SPARSE: 1>
    __members__: typing.ClassVar[dict[str, QPSolver]]  # value = {'QPOASES_DENSE': <QPSolver.QPOASES_DENSE: 0>, 'QPOASES_SPARSE': <QPSolver.QPOASES_SPARSE: 1>, 'OSQP_SPARSE': <QPSolver.OSQP_SPARSE: 2>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ReturnValue:
    """
    Members:
    
      NOT_YET_IMPLEMENTED
    
      SUCCESSFUL_RETURN
    
      INVALID_ARGUMENT
    
      INVALID_PENALTY_UPDATE_VALUE
    
      INVALID_COMPLEMENTARITY_TOLERANCE
    
      INVALID_INITIAL_PENALTY_VALUE
    
      INVALID_MAX_ITERATIONS_VALUE
    
      INVALID_STATIONARITY_TOLERANCE
    
      INVALID_NUMBER_OF_OPTIM_VARS
    
      INVALID_NUMBER_OF_COMP_VARS
    
      INVALID_NUMBER_OF_CONSTRAINT_VARS
    
      INVALID_QPSOLVER
    
      INVALID_OSQP_BOX_CONSTRAINTS
    
      INVALID_TOTAL_ITER_COUNT
    
      INVALID_TOTAL_OUTER_ITER
    
      IVALID_SUBPROBLEM_ITER
    
      INVALID_RHO_OPT
    
      INVALID_PRINT_LEVEL_VALUE
    
      INVALID_OBJECTIVE_LINEAR_TERM
    
      INVALID_CONSTRAINT_MATRIX
    
      INVALID_COMPLEMENTARITY_MATRIX
    
      INVALID_ETA_VALUE
    
      OSQP_INITIAL_PRIMAL_GUESS_FAILED
    
      OSQP_INITIAL_DUAL_GUESS_FAILED
    
      INVALID_LOWER_COMPLEMENTARITY_BOUND
    
      INVALID_MAX_RHO_VALUE
    
      MAX_ITERATIONS_REACHED
    
      MAX_PENALTY_REACHED
    
      INITIAL_SUBPROBLEM_FAILED
    
      SUBPROBLEM_SOLVER_ERROR
    
      FAILED_SYM_COMPLEMENTARITY_MATRIX
    
      FAILED_SWITCH_TO_SPARSE
    
      FAILED_SWITCH_TO_DENSE
    
      OSQP_WORKSPACE_NOT_SET_UP
    
      LCQPOBJECT_NOT_SETUP
    
      INDEX_OUT_OF_BOUNDS
    
      UNABLE_TO_READ_FILE
    
      INVALID_INDEX_POINTER
    
      INVALID_INDEX_ARRAY
    """
    FAILED_SWITCH_TO_DENSE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.FAILED_SWITCH_TO_DENSE: 206>
    FAILED_SWITCH_TO_SPARSE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.FAILED_SWITCH_TO_SPARSE: 205>
    FAILED_SYM_COMPLEMENTARITY_MATRIX: typing.ClassVar[ReturnValue]  # value = <ReturnValue.FAILED_SYM_COMPLEMENTARITY_MATRIX: 204>
    INDEX_OUT_OF_BOUNDS: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INDEX_OUT_OF_BOUNDS: 301>
    INITIAL_SUBPROBLEM_FAILED: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INITIAL_SUBPROBLEM_FAILED: 202>
    INVALID_ARGUMENT: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_ARGUMENT: 100>
    INVALID_COMPLEMENTARITY_MATRIX: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_COMPLEMENTARITY_MATRIX: 118>
    INVALID_COMPLEMENTARITY_TOLERANCE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_COMPLEMENTARITY_TOLERANCE: 102>
    INVALID_CONSTRAINT_MATRIX: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_CONSTRAINT_MATRIX: 117>
    INVALID_ETA_VALUE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_ETA_VALUE: 119>
    INVALID_INDEX_ARRAY: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_INDEX_ARRAY: 401>
    INVALID_INDEX_POINTER: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_INDEX_POINTER: 400>
    INVALID_INITIAL_PENALTY_VALUE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_INITIAL_PENALTY_VALUE: 103>
    INVALID_LOWER_COMPLEMENTARITY_BOUND: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_LOWER_COMPLEMENTARITY_BOUND: 120>
    INVALID_MAX_ITERATIONS_VALUE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_MAX_ITERATIONS_VALUE: 104>
    INVALID_MAX_RHO_VALUE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_MAX_RHO_VALUE: 121>
    INVALID_NUMBER_OF_COMP_VARS: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_NUMBER_OF_COMP_VARS: 107>
    INVALID_NUMBER_OF_CONSTRAINT_VARS: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_NUMBER_OF_CONSTRAINT_VARS: 108>
    INVALID_NUMBER_OF_OPTIM_VARS: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_NUMBER_OF_OPTIM_VARS: 106>
    INVALID_OBJECTIVE_LINEAR_TERM: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_OBJECTIVE_LINEAR_TERM: 116>
    INVALID_OSQP_BOX_CONSTRAINTS: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_OSQP_BOX_CONSTRAINTS: 110>
    INVALID_PENALTY_UPDATE_VALUE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_PENALTY_UPDATE_VALUE: 101>
    INVALID_PRINT_LEVEL_VALUE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_PRINT_LEVEL_VALUE: 115>
    INVALID_QPSOLVER: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_QPSOLVER: 109>
    INVALID_RHO_OPT: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_RHO_OPT: 114>
    INVALID_STATIONARITY_TOLERANCE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_STATIONARITY_TOLERANCE: 105>
    INVALID_TOTAL_ITER_COUNT: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_TOTAL_ITER_COUNT: 111>
    INVALID_TOTAL_OUTER_ITER: typing.ClassVar[ReturnValue]  # value = <ReturnValue.INVALID_TOTAL_OUTER_ITER: 112>
    IVALID_SUBPROBLEM_ITER: typing.ClassVar[ReturnValue]  # value = <ReturnValue.IVALID_SUBPROBLEM_ITER: 113>
    LCQPOBJECT_NOT_SETUP: typing.ClassVar[ReturnValue]  # value = <ReturnValue.LCQPOBJECT_NOT_SETUP: 300>
    MAX_ITERATIONS_REACHED: typing.ClassVar[ReturnValue]  # value = <ReturnValue.MAX_ITERATIONS_REACHED: 200>
    MAX_PENALTY_REACHED: typing.ClassVar[ReturnValue]  # value = <ReturnValue.MAX_PENALTY_REACHED: 201>
    NOT_YET_IMPLEMENTED: typing.ClassVar[ReturnValue]  # value = <ReturnValue.NOT_YET_IMPLEMENTED: -1>
    OSQP_INITIAL_DUAL_GUESS_FAILED: typing.ClassVar[ReturnValue]  # value = <ReturnValue.OSQP_INITIAL_DUAL_GUESS_FAILED: 209>
    OSQP_INITIAL_PRIMAL_GUESS_FAILED: typing.ClassVar[ReturnValue]  # value = <ReturnValue.OSQP_INITIAL_PRIMAL_GUESS_FAILED: 208>
    OSQP_WORKSPACE_NOT_SET_UP: typing.ClassVar[ReturnValue]  # value = <ReturnValue.OSQP_WORKSPACE_NOT_SET_UP: 207>
    SUBPROBLEM_SOLVER_ERROR: typing.ClassVar[ReturnValue]  # value = <ReturnValue.SUBPROBLEM_SOLVER_ERROR: 203>
    SUCCESSFUL_RETURN: typing.ClassVar[ReturnValue]  # value = <ReturnValue.SUCCESSFUL_RETURN: 0>
    UNABLE_TO_READ_FILE: typing.ClassVar[ReturnValue]  # value = <ReturnValue.UNABLE_TO_READ_FILE: 302>
    __members__: typing.ClassVar[dict[str, ReturnValue]]  # value = {'NOT_YET_IMPLEMENTED': <ReturnValue.NOT_YET_IMPLEMENTED: -1>, 'SUCCESSFUL_RETURN': <ReturnValue.SUCCESSFUL_RETURN: 0>, 'INVALID_ARGUMENT': <ReturnValue.INVALID_ARGUMENT: 100>, 'INVALID_PENALTY_UPDATE_VALUE': <ReturnValue.INVALID_PENALTY_UPDATE_VALUE: 101>, 'INVALID_COMPLEMENTARITY_TOLERANCE': <ReturnValue.INVALID_COMPLEMENTARITY_TOLERANCE: 102>, 'INVALID_INITIAL_PENALTY_VALUE': <ReturnValue.INVALID_INITIAL_PENALTY_VALUE: 103>, 'INVALID_MAX_ITERATIONS_VALUE': <ReturnValue.INVALID_MAX_ITERATIONS_VALUE: 104>, 'INVALID_STATIONARITY_TOLERANCE': <ReturnValue.INVALID_STATIONARITY_TOLERANCE: 105>, 'INVALID_NUMBER_OF_OPTIM_VARS': <ReturnValue.INVALID_NUMBER_OF_OPTIM_VARS: 106>, 'INVALID_NUMBER_OF_COMP_VARS': <ReturnValue.INVALID_NUMBER_OF_COMP_VARS: 107>, 'INVALID_NUMBER_OF_CONSTRAINT_VARS': <ReturnValue.INVALID_NUMBER_OF_CONSTRAINT_VARS: 108>, 'INVALID_QPSOLVER': <ReturnValue.INVALID_QPSOLVER: 109>, 'INVALID_OSQP_BOX_CONSTRAINTS': <ReturnValue.INVALID_OSQP_BOX_CONSTRAINTS: 110>, 'INVALID_TOTAL_ITER_COUNT': <ReturnValue.INVALID_TOTAL_ITER_COUNT: 111>, 'INVALID_TOTAL_OUTER_ITER': <ReturnValue.INVALID_TOTAL_OUTER_ITER: 112>, 'IVALID_SUBPROBLEM_ITER': <ReturnValue.IVALID_SUBPROBLEM_ITER: 113>, 'INVALID_RHO_OPT': <ReturnValue.INVALID_RHO_OPT: 114>, 'INVALID_PRINT_LEVEL_VALUE': <ReturnValue.INVALID_PRINT_LEVEL_VALUE: 115>, 'INVALID_OBJECTIVE_LINEAR_TERM': <ReturnValue.INVALID_OBJECTIVE_LINEAR_TERM: 116>, 'INVALID_CONSTRAINT_MATRIX': <ReturnValue.INVALID_CONSTRAINT_MATRIX: 117>, 'INVALID_COMPLEMENTARITY_MATRIX': <ReturnValue.INVALID_COMPLEMENTARITY_MATRIX: 118>, 'INVALID_ETA_VALUE': <ReturnValue.INVALID_ETA_VALUE: 119>, 'OSQP_INITIAL_PRIMAL_GUESS_FAILED': <ReturnValue.OSQP_INITIAL_PRIMAL_GUESS_FAILED: 208>, 'OSQP_INITIAL_DUAL_GUESS_FAILED': <ReturnValue.OSQP_INITIAL_DUAL_GUESS_FAILED: 209>, 'INVALID_LOWER_COMPLEMENTARITY_BOUND': <ReturnValue.INVALID_LOWER_COMPLEMENTARITY_BOUND: 120>, 'INVALID_MAX_RHO_VALUE': <ReturnValue.INVALID_MAX_RHO_VALUE: 121>, 'MAX_ITERATIONS_REACHED': <ReturnValue.MAX_ITERATIONS_REACHED: 200>, 'MAX_PENALTY_REACHED': <ReturnValue.MAX_PENALTY_REACHED: 201>, 'INITIAL_SUBPROBLEM_FAILED': <ReturnValue.INITIAL_SUBPROBLEM_FAILED: 202>, 'SUBPROBLEM_SOLVER_ERROR': <ReturnValue.SUBPROBLEM_SOLVER_ERROR: 203>, 'FAILED_SYM_COMPLEMENTARITY_MATRIX': <ReturnValue.FAILED_SYM_COMPLEMENTARITY_MATRIX: 204>, 'FAILED_SWITCH_TO_SPARSE': <ReturnValue.FAILED_SWITCH_TO_SPARSE: 205>, 'FAILED_SWITCH_TO_DENSE': <ReturnValue.FAILED_SWITCH_TO_DENSE: 206>, 'OSQP_WORKSPACE_NOT_SET_UP': <ReturnValue.OSQP_WORKSPACE_NOT_SET_UP: 207>, 'LCQPOBJECT_NOT_SETUP': <ReturnValue.LCQPOBJECT_NOT_SETUP: 300>, 'INDEX_OUT_OF_BOUNDS': <ReturnValue.INDEX_OUT_OF_BOUNDS: 301>, 'UNABLE_TO_READ_FILE': <ReturnValue.UNABLE_TO_READ_FILE: 302>, 'INVALID_INDEX_POINTER': <ReturnValue.INVALID_INDEX_POINTER: 400>, 'INVALID_INDEX_ARRAY': <ReturnValue.INVALID_INDEX_ARRAY: 401>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class cscWrapper:
    def __init__(self, m: typing.SupportsInt, n: typing.SupportsInt, nnx: typing.SupportsInt, x: typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"], i: collections.abc.Sequence[typing.SupportsInt], p: collections.abc.Sequence[typing.SupportsInt]) -> None:
        ...
    @property
    def m(self) -> int:
        ...
    @property
    def n(self) -> int:
        ...
    @property
    def nz(self) -> int:
        ...
    @property
    def nzmax(self) -> int:
        ...
C_STATIONARY_SOLUTION: AlgorithmStatus  # value = <AlgorithmStatus.C_STATIONARY_SOLUTION: 2>
FAILED_SWITCH_TO_DENSE: ReturnValue  # value = <ReturnValue.FAILED_SWITCH_TO_DENSE: 206>
FAILED_SWITCH_TO_SPARSE: ReturnValue  # value = <ReturnValue.FAILED_SWITCH_TO_SPARSE: 205>
FAILED_SYM_COMPLEMENTARITY_MATRIX: ReturnValue  # value = <ReturnValue.FAILED_SYM_COMPLEMENTARITY_MATRIX: 204>
INDEX_OUT_OF_BOUNDS: ReturnValue  # value = <ReturnValue.INDEX_OUT_OF_BOUNDS: 301>
INITIAL_SUBPROBLEM_FAILED: ReturnValue  # value = <ReturnValue.INITIAL_SUBPROBLEM_FAILED: 202>
INNER_LOOP_ITERATES: PrintLevel  # value = <PrintLevel.INNER_LOOP_ITERATES: 2>
INVALID_ARGUMENT: ReturnValue  # value = <ReturnValue.INVALID_ARGUMENT: 100>
INVALID_COMPLEMENTARITY_MATRIX: ReturnValue  # value = <ReturnValue.INVALID_COMPLEMENTARITY_MATRIX: 118>
INVALID_COMPLEMENTARITY_TOLERANCE: ReturnValue  # value = <ReturnValue.INVALID_COMPLEMENTARITY_TOLERANCE: 102>
INVALID_CONSTRAINT_MATRIX: ReturnValue  # value = <ReturnValue.INVALID_CONSTRAINT_MATRIX: 117>
INVALID_ETA_VALUE: ReturnValue  # value = <ReturnValue.INVALID_ETA_VALUE: 119>
INVALID_INDEX_ARRAY: ReturnValue  # value = <ReturnValue.INVALID_INDEX_ARRAY: 401>
INVALID_INDEX_POINTER: ReturnValue  # value = <ReturnValue.INVALID_INDEX_POINTER: 400>
INVALID_INITIAL_PENALTY_VALUE: ReturnValue  # value = <ReturnValue.INVALID_INITIAL_PENALTY_VALUE: 103>
INVALID_LOWER_COMPLEMENTARITY_BOUND: ReturnValue  # value = <ReturnValue.INVALID_LOWER_COMPLEMENTARITY_BOUND: 120>
INVALID_MAX_ITERATIONS_VALUE: ReturnValue  # value = <ReturnValue.INVALID_MAX_ITERATIONS_VALUE: 104>
INVALID_MAX_RHO_VALUE: ReturnValue  # value = <ReturnValue.INVALID_MAX_RHO_VALUE: 121>
INVALID_NUMBER_OF_COMP_VARS: ReturnValue  # value = <ReturnValue.INVALID_NUMBER_OF_COMP_VARS: 107>
INVALID_NUMBER_OF_CONSTRAINT_VARS: ReturnValue  # value = <ReturnValue.INVALID_NUMBER_OF_CONSTRAINT_VARS: 108>
INVALID_NUMBER_OF_OPTIM_VARS: ReturnValue  # value = <ReturnValue.INVALID_NUMBER_OF_OPTIM_VARS: 106>
INVALID_OBJECTIVE_LINEAR_TERM: ReturnValue  # value = <ReturnValue.INVALID_OBJECTIVE_LINEAR_TERM: 116>
INVALID_OSQP_BOX_CONSTRAINTS: ReturnValue  # value = <ReturnValue.INVALID_OSQP_BOX_CONSTRAINTS: 110>
INVALID_PENALTY_UPDATE_VALUE: ReturnValue  # value = <ReturnValue.INVALID_PENALTY_UPDATE_VALUE: 101>
INVALID_PRINT_LEVEL_VALUE: ReturnValue  # value = <ReturnValue.INVALID_PRINT_LEVEL_VALUE: 115>
INVALID_QPSOLVER: ReturnValue  # value = <ReturnValue.INVALID_QPSOLVER: 109>
INVALID_RHO_OPT: ReturnValue  # value = <ReturnValue.INVALID_RHO_OPT: 114>
INVALID_STATIONARITY_TOLERANCE: ReturnValue  # value = <ReturnValue.INVALID_STATIONARITY_TOLERANCE: 105>
INVALID_TOTAL_ITER_COUNT: ReturnValue  # value = <ReturnValue.INVALID_TOTAL_ITER_COUNT: 111>
INVALID_TOTAL_OUTER_ITER: ReturnValue  # value = <ReturnValue.INVALID_TOTAL_OUTER_ITER: 112>
IVALID_SUBPROBLEM_ITER: ReturnValue  # value = <ReturnValue.IVALID_SUBPROBLEM_ITER: 113>
LCQPOBJECT_NOT_SETUP: ReturnValue  # value = <ReturnValue.LCQPOBJECT_NOT_SETUP: 300>
MAX_ITERATIONS_REACHED: ReturnValue  # value = <ReturnValue.MAX_ITERATIONS_REACHED: 200>
MAX_PENALTY_REACHED: ReturnValue  # value = <ReturnValue.MAX_PENALTY_REACHED: 201>
M_STATIONARY_SOLUTION: AlgorithmStatus  # value = <AlgorithmStatus.M_STATIONARY_SOLUTION: 3>
NONE: PrintLevel  # value = <PrintLevel.NONE: 0>
NOT_YET_IMPLEMENTED: ReturnValue  # value = <ReturnValue.NOT_YET_IMPLEMENTED: -1>
OSQP_INITIAL_DUAL_GUESS_FAILED: ReturnValue  # value = <ReturnValue.OSQP_INITIAL_DUAL_GUESS_FAILED: 209>
OSQP_INITIAL_PRIMAL_GUESS_FAILED: ReturnValue  # value = <ReturnValue.OSQP_INITIAL_PRIMAL_GUESS_FAILED: 208>
OSQP_SPARSE: QPSolver  # value = <QPSolver.OSQP_SPARSE: 2>
OSQP_WORKSPACE_NOT_SET_UP: ReturnValue  # value = <ReturnValue.OSQP_WORKSPACE_NOT_SET_UP: 207>
OUTER_LOOP_ITERATES: PrintLevel  # value = <PrintLevel.OUTER_LOOP_ITERATES: 1>
PROBLEM_NOT_SOLVED: AlgorithmStatus  # value = <AlgorithmStatus.PROBLEM_NOT_SOLVED: 0>
QPOASES_DENSE: QPSolver  # value = <QPSolver.QPOASES_DENSE: 0>
QPOASES_SPARSE: QPSolver  # value = <QPSolver.QPOASES_SPARSE: 1>
SUBPROBLEM_SOLVER_ERROR: ReturnValue  # value = <ReturnValue.SUBPROBLEM_SOLVER_ERROR: 203>
SUCCESSFUL_RETURN: ReturnValue  # value = <ReturnValue.SUCCESSFUL_RETURN: 0>
S_STATIONARY_SOLUTION: AlgorithmStatus  # value = <AlgorithmStatus.S_STATIONARY_SOLUTION: 4>
UNABLE_TO_READ_FILE: ReturnValue  # value = <ReturnValue.UNABLE_TO_READ_FILE: 302>
W_STATIONARY_SOLUTION: AlgorithmStatus  # value = <AlgorithmStatus.W_STATIONARY_SOLUTION: 1>
