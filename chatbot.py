
import openai
import os

# Defina a sua chave da API aqui
chave_api = "Sua chave da API"
openai.api_key = chave_api

# Função que envia a mensagem para a API GPT e recebe a resposta
def enviar_mensagem(mensagem, Lista_mensagens=[]):
    Lista_mensagens.append({"role": "user", "content": mensagem})

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=Lista_mensagens,
    )

    return resposta["choices"][0]["message"], Lista_mensagens

# Loop principal do chatbot
def iniciar_chatbot():
    print("(Digite 'sair' para encerrar)")
    Lista_mensagens = []

    while True:
        texto = input("Você: ")

        if texto.lower() == "sair":
            print("Encerrando o chatbot...")
            break
        else:
            try:
                resposta, Lista_mensagens = enviar_mensagem(texto, Lista_mensagens)
                print("Chatbot:", resposta["content"])
            except openai.error.OpenAIError as e:
                print(f"Ocorreu um erro: {e}")
                break

if __name__ == "__main__":
    iniciar_chatbot()
