INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["There is a fine house in the forest"]
    },
    "num_inference_steps": {
        'datatype': 'INT8',
        'required': True,
        'shape': [1],
        'example': [10]
    },
    "format": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["JPEG"]
    }
}
