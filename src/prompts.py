"""
===========================================
        Module: Prompts collection
===========================================
"""
# Note: Precise formatting of spacing and indentation of the prompt template is important for Llama-2-7B-Chat,
# as it is highly sensitive to whitespace changes. For example, it could have problems generating
# a summary from the pieces of context if the spacing is not done correctly

qa_template = """Utiliza la siguiente información para responder a la pregunta del usuario sobre un pueblo llamado Villa Francia.
El pueblo tambien se llama Coronel Granada.
Si no conoce la respuesta, simplemente diga que no la conoce.
Si la pregunta no está relacionada con Villa Francia o Coronel Granada no responda.

Context: {context}
Question: {question}
"""
