# Tired of proofreading your long articles or texts? Then, you can try this automated script which will scan your text and correct grammar errors. This great script uses the Happtransformer module, which is a machine learning module trained to fix grammar errors in text.

# Grammer Fixer
# pip install happytransformer
from happytransformer import HappyTextToText as HappyTTT
from happytransformer import TTSettings

def Grammer_Fixer(Text):
    Grammer = HappyTTT("T5","prithivida/grammar_error_correcter_v1")
    config = TTSettings(do_sample=True, top_k=10, max_length=100)
    corrected = Grammer.generate_text(Text, args=config)
    print("Corrected Text: ", corrected.text)

Text = "This is smple tet we how know this"
Grammer_Fixer(Text)