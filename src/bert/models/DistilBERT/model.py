from transformers import AutoTokenizer
from transformers import DataCollatorWithPadding


tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
data_collator = DataCollatorWithPadding(tokenizer=tokenizer) 

def tokenize_function(text):
    return tokenizer(text['text'], padding = 'max_length', truncation = True)

tokenized_datasets = dataset.map(tokenize_function, batched = True)

small_train_dataset = tokenized_datasets['train'].shuffle(seed=42).select(range(1000))
small_eval_dataset = tokenized_datasets['test'].shuffle(seed=42).select(range(1000))

