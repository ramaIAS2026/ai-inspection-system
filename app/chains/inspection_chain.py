import base64
from io import BytesIO
from langchain.schema import HumanMessage
from app.models.vision_model import get_llm
from app.prompts.inspection_prompt import INSPECTION_PROMPT


def encode_image(image):
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode()


def run_inspection(image):

    llm = get_llm()

    base64_image = encode_image(image)

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": INSPECTION_PROMPT
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    )

    response = llm.invoke([message])

    return response.content