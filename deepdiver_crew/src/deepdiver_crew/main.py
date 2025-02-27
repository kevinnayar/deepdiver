#!/usr/bin/env python
import sys
import warnings
from deepdiver_crew.crew import DeepdiverCrew

# Suppress pysbd escape sequence warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {"topic": "JWT Authentication"}

    try:
        DeepdiverCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
