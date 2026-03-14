# from app.chains.inspection_chain import run_inspection

# def evaluate_image(image):

#     result = run_inspection(image)

#     # return result
import json
from app.chains.inspection_chain import run_inspection


def evaluate_image(image):

    result = run_inspection(image)

    # Remove markdown json formatting
    result = result.replace("```json", "")
    result = result.replace("```", "")

    result = result.strip()

    return json.loads(result)