# from transformers import AutoTokenizer, AutoModelForCausalLM

# # Laden Sie das Modell und den Tokenizer
# tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
# model = AutoModelForCausalLM.from_pretrained('mosaicml/mpt-7b-chat', trust_remote_code=True)

# # Ihr Eingabetext
# input_text = "Hallo, wie geht es dir?"

# # Tokenisieren Sie den Eingabetext
# input_ids = tokenizer.encode(input_text, return_tensors='pt')

# # Generieren Sie die Ausgabe des Modells
# output = model.generate(input_ids, max_length=100, temperature=0.7)

# # Dekodieren Sie die Ausgabe in lesbaren Text
# print(output)
# # output_text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

# # print(output_text)

# import transformers
# import torch

# config = transformers.AutoConfig.from_pretrained(
#   'mosaicml/mpt-7b-chat',
#   trust_remote_code=True
# )
# config.attn_config['attn_impl'] = 'triton'

# model = transformers.AutoModelForCausalLM.from_pretrained(
#   'mosaicml/mpt-7b-chat',
#   trust_remote_code=True,
#     config=config,
#     torch_dtype=torch.float16
# )

from llama_cpp import Llama

print("loading model...")
llm = Llama(model_path="F:/Dokumente/AI/Mosaic/models/Manticore-13B-Chat-Pyg.ggmlv3.q4_0.bin")
print("model loaded")

output = llm("I like to eat apples.")
print(output)