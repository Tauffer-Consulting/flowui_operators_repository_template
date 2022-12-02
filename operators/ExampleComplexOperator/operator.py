from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel
import os


class ExampleComplexOperator(BaseOperator):
    """
    This Operator serves as a more complex example, using Dockerfile as dependency, from where you can start writing your own Operator.
    Remember to also change all other required files accordingly:
    - operator.py (this file)
    - models.py
    - metadata.json
    - requirements.txt or Dockerfile if needed
    """
    
    def operator_function(self, input_model: InputModel):

        # Input arguments are retrieved from the Input model object
        arg1 = input_model.arg1

        # If this Operator needs to use a Secret value, it can retrieve it from ENV
        operator_secret = os.environ.get("EXAMPLE_OPERATOR_SECRET_2", None)

        # Basic logging is done with print()
        print("Starting operator process...")

        # Here we add the Operator function logic
        message = ""
        result = ""

        # Finally, results should return as an Output model
        return OutputModel(
            message=message,
            result=result
        )