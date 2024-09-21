import openai

class OpenAIGateway:
    @staticmethod
    def generate_embeddings(text):
        # Aqui usamos a API do OpenAI para gerar embeddings
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response['data'][0]['embedding']
