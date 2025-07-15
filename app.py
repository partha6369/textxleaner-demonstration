# app.py

import os
import gradio as gr
import random
import spacy
import subprocess
from textcleaner_partha import preprocess, get_tokens

# Ensure spaCy model is available in HF Space environment
try:
    spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"], check=True)
    
# 25 Sample texts for Examples tab
example_texts = [
    "Hey! How r u doing today? 😊",
    "Check out this link: <a href='https://example.com'>example</a>",
    "It's raining cats & dogs! Don't u think so?",
    "I can't go 2 d party 2nite. Got work.",
    "LOL that was gr8! Let's meet tmrw.",
    "The flight's ETA is 5 p.m. PST.",
    "He said he's gonna do it, but IDK when.",
    "Thx for ur help. Really appreciate it!",
    "OMG!!! This is unbelievable 😱",
    "They've been working on AI/ML solutions.",
    "Tbh, I'm not sure what to do rn.",
    "Call me ASAP when u reach the station.",
    "FYI: The doc was updated yesterday.",
    "This place is lit 🔥🔥🔥",
    "Your balance is ₹500.00 as of 10-July.",
    "Is this legit or a scam? 🤔",
    "Welcome to the party, bro!",
    "Pls fill out the form b4 5pm.",
    "The GDP growth is projected at 6.8%.",
    "She's working @ the new cafe.",
    "U gotta be kidding me 😒",
    "BTW, the meeting was rescheduled.",
    "I’ll b there in 10 mins.",
    "Here's the <div>HTML</div> you requested.",
    "Gonna chill with Netflix n snacks 🍿",
    "IDK what happened last night, but I woke up with like 57 unread msgs & 3 missed calls from mom 😅",
    "BTW, the CEO's AMA session is live rn! LMK if u wanna join — it's all about GenAI n the future of work.",
    "LOL, this guy just sent me a 2-page email with 'pls revert ASAP' in bold. I'm crying 😂",
    "Just got my COVID booster 💉✨ Now chillin’ at Starbucks with a caramel latte n browsing memes.",
    "Hey, do u hv any idea y the Wi-Fi's dead again? Been buffering for like 20 mins on Netflix 🙄",
    "Reminder: ur appointment is at 4pm tmrw @ Apollo Clinic. Pls arrive 10 mins early & bring ur ID.",
    "Wanna meet @ the cafe on 5th Ave? They’ve got free Wi-Fi, gr8 coffee, and lowkey amazing bagels 🥯☕",
    "OMG bro u won't believe it — I accidentally sent a 😘 emoji to my boss instead of a thumbs-up!",
    "Tbh, this policy doc is 78 pages of gibberish. Can't we get a TL;DR version with highlights?",
    "Ugh, my Uber driver just went the wrong way again. ETA changed from 7 mins to 18 🚗😤",
    "Here’s the snippet u asked 4: <script>alert('Hello!');</script>. Looks shady af, pls check.",
    "ATM my mind’s blank. Like fr, I was gonna write the essay but TikTok got me again 😬",
    "Heads up: the HRMS portal will be down 4 maintenance frm 1am–4am IST on 17th Jul.",
    "Dude, this game is fire! 🔥🔥 I'm at level 45 already. You gotta try it out, fr fr.",
    "ICYMI: The deadline’s moved to Fri 3pm. Pls send ur final copy b4 EOD Thu.",
    "FYI: We hv a team call @ 11.30 tmrw. Agenda: Q2 targets, OKRs, and release roadmap.",
    "No cap, that series finale was wild. Like, I’m still processing that plot twist 🤯",
    "I'm tryna finish this ppt deck b4 10, but Canva's acting up & my ideas r mid 💀",
    "Soz 4 the late reply. Been caught up with work & mom's bday prep 🎉🎂",
    "Hey there 👋 Just checking in. Haven't heard from u in ages — hope all's well 🙏",
    "She was like, 'brb', and then ghosted me for 3 days. I mean… what?!",
    "Just dropped 5k on my CC for that iPhone 15 Pro. Rly hoping it’s worth it 📱💸",
    "TL;DR: Gr8 content, but delivery was meh. Next time, pls include action points.",
    "Gtg now, catch ya on Zoom l8r. Text me if there’s any change in schedule 📅",
    "Woke up at 3am, couldn't sleep. Ended up watching 2 docu-series & ordering Maggi 🍜📺"
]

# Function to preprocess based on user config
def clean_text(
    text,
    lowercase,
    remove_stopwords,
    remove_html,
    remove_emoji,
    remove_whitespaces,
    remove_punctuations,
    expand_contraction,
    expand_abbrev,
    correct_spelling,
    lemmatise,
):
    return preprocess(
        text=text,
        lowercase=lowercase,
        remove_stopwords=remove_stopwords,
        remove_html=remove_html,
        remove_emoji=remove_emoji,
        remove_whitespace=remove_whitespaces,
        remove_punct=remove_punctuations,
        expand_contraction=expand_contraction,
        expand_abbrev=expand_abbrev,
        correct_spelling=correct_spelling,
        lemmatise=lemmatise,
        verbose=True
    )

# Function to get tokens based on user config
def get_tokens_for_text(
    text,
    lowercase,
    remove_stopwords,
    remove_html,
    remove_emoji,
    remove_whitespaces,
    remove_punctuations,
    expand_contraction,
    expand_abbrev,
    correct_spelling,
    lemmatise,
):
    return get_tokens(
        text=text,
        lowercase=lowercase,
        remove_stopwords=remove_stopwords,
        remove_html=remove_html,
        remove_emoji=remove_emoji,
        remove_whitespace=remove_whitespaces,
        remove_punct=remove_punctuations,
        expand_contraction=expand_contraction,
        expand_abbrev=expand_abbrev,
        correct_spelling=correct_spelling,
        lemmatise=lemmatise,
        verbose=True
    )

# Function to clear Try Yourself tab
def clear_all():
    return gr.update(value=""), True, True, True, True, True, True, True, True, True, True, gr.update(value="")

# Function for Examples tab
def random_example():
    text = random.choice(example_texts)
    checkbox_states = [random.choice([True, False]) for _ in range(10)]
    result = preprocess(
        text,
        lowercase=checkbox_states[0],
        remove_stopwords=checkbox_states[1],
        remove_html=checkbox_states[2],
        remove_emoji=checkbox_states[3],
        remove_whitespace=checkbox_states[4],
        remove_punct=checkbox_states[5],
        expand_contraction=checkbox_states[6],
        expand_abbrev=checkbox_states[7],
        correct_spelling=checkbox_states[8],
        lemmatise=checkbox_states[9],
        verbose=True
    )
    return (
        text,
        *checkbox_states,
        result
    )

# Function for get_tokens Examples tab
def random_example_get_tokens():
    text = random.choice(example_texts)
    checkbox_states = [random.choice([True, False]) for _ in range(10)]
    result = get_tokens(
        text,
        lowercase=checkbox_states[0],
        remove_html=checkbox_states[1],
        remove_stopwords=checkbox_states[2],
        remove_emoji=checkbox_states[3],
        remove_whitespace=checkbox_states[4],
        remove_punct=checkbox_states[5],
        expand_contraction=checkbox_states[6],
        expand_abbrev=checkbox_states[7],
        correct_spelling=checkbox_states[8],
        lemmatise=checkbox_states[9],
        verbose=True
    )
    return (
        text,
        *checkbox_states,
        result
    )

# Try to load the PayPal URL from the environment; if missing, use a placeholder
paypal_url = os.getenv("PAYPAL_URL", "https://www.paypal.com/donate/dummy-link")

APP_TITLE = "🧼 textcleaner-partha Demonstration"
APP_DESCRIPTION = (
    "This app allows you to test the <strong>textcleaner-partha</strong> Python library, developed by <em>Dr. Partha Majumdar</em>. "
    "You can try out the preprocessing and token extraction steps or explore examples"
)

# Build the Gradio app
with gr.Blocks(title="textcleaner-partha by Dr. Partha Majumdar") as app:
    # Title and Description
    gr.HTML(
        f"""
        <p style='text-align: center; font-size: 40px; font-weight: bold;'>{APP_TITLE}</p>
        <p style='text-align: center; font-size: 20px; color: #555;'><sub>{APP_DESCRIPTION}</sub></p>
        <hr>
        """
    )


    with gr.Tabs():
        with gr.TabItem("preprocess()"):
            
            with gr.Tabs():
                with gr.TabItem("Examples"):
                    with gr.Row():
                        example_input = gr.Textbox(label="Example Input Text", lines=6)
                        example_output = gr.Textbox(label="Processed Output Text", lines=6)
        
                    with gr.Row():
                        ex_lowercase = gr.Checkbox(label="Lowercase")
                        ex_remove_stopwords = gr.Checkbox(label="Remove Stop Words")
                        ex_remove_html = gr.Checkbox(label="Remove HTML tags")
                        ex_remove_emoji = gr.Checkbox(label="Remove Emojis")
                        ex_remove_whitespaces = gr.Checkbox(label="Remove White Spaces")
                        ex_remove_punctuations = gr.Checkbox(label="Remove Punctuations")
                        ex_expand_contraction = gr.Checkbox(label="Expand Contractions")
                        ex_expand_abbrev = gr.Checkbox(label="Expand Abbreviations")
                        ex_correct_spelling = gr.Checkbox(label="Correct Spellings")
                        ex_lemmatise = gr.Checkbox(label="Lemmatise")
        
                    example_button = gr.Button("Try an Example")
        
                    example_button.click(
                        fn=random_example,
                        inputs=[],
                        outputs=[
                            example_input,
                            ex_lowercase,
                            ex_remove_stopwords,
                            ex_remove_html,
                            ex_remove_emoji,
                            ex_remove_whitespaces,
                            ex_remove_punctuations,
                            ex_expand_contraction,
                            ex_expand_abbrev,
                            ex_correct_spelling,
                            ex_lemmatise,
                            example_output,
                        ]
                    )
        
                with gr.TabItem("Try Yourself"):
                    with gr.Row():
                        with gr.Column():
                            lowercase = gr.Checkbox(label="Lowercase", value=True)
                            remove_stopwords = gr.Checkbox(label="Remove Stop Words", value=True)
                            remove_html = gr.Checkbox(label="Remove HTML tags", value=True)
                            remove_emoji = gr.Checkbox(label="Remove Emojis", value=True)
                            remove_whitespaces = gr.Checkbox(label="Remove White Spaces", value=True)
                            remove_punctuations = gr.Checkbox(label="Remove Punctuations", value=True)
                            expand_contraction = gr.Checkbox(label="Expand Contractions", value=True)
                            expand_abbrev = gr.Checkbox(label="Expand Abbreviations", value=True)
                            correct_spelling = gr.Checkbox(label="Correct Spellings", value=True)
                            lemmatise = gr.Checkbox(label="Lemmatise", value=True)
                        with gr.Column():
                            input_text = gr.Textbox(label="Enter your text", lines=8, placeholder="Paste text here...")
                            output_text = gr.Textbox(label="Processed text", lines=8)
        
                            with gr.Row():
                                submit_btn = gr.Button("Submit")
                                clear_btn = gr.Button("Clear")
        
                    submit_btn.click(
                        fn=clean_text,
                        inputs=[
                            input_text,
                            lowercase,
                            remove_stopwords,
                            remove_html,
                            remove_emoji,
                            remove_whitespaces,
                            remove_punctuations,
                            expand_contraction,
                            expand_abbrev,
                            correct_spelling,
                            lemmatise,
                        ],
                        outputs=output_text
                    )
        
                    clear_btn.click(
                        fn=clear_all,
                        inputs=[],
                        outputs=[
                            input_text,
                            lowercase,
                            remove_stopwords,
                            remove_html,
                            remove_emoji,
                            remove_whitespaces,
                            remove_punctuations,
                            expand_contraction,
                            expand_abbrev,
                            correct_spelling,
                            lemmatise,
                            output_text,
                        ]
                    )
                    
        with gr.TabItem("get_tokens()"):
            
            with gr.Tabs():
                with gr.TabItem("Examples"):
                    with gr.Row():
                        example_input_gt = gr.Textbox(label="Example Input Text", lines=6)
                        example_output_gt = gr.Textbox(label="Extracted Tokens", lines=6)
        
                    with gr.Row():
                        ex_lowercase_gt = gr.Checkbox(label="Lowercase")
                        ex_remove_stopwords_gt = gr.Checkbox(label="Remove Stop Words")
                        ex_remove_html_gt = gr.Checkbox(label="Remove HTML tags")
                        ex_remove_emoji_gt = gr.Checkbox(label="Remove Emojis")
                        ex_remove_whitespaces_gt = gr.Checkbox(label="Remove White Spaces")
                        ex_remove_punctuations_gt = gr.Checkbox(label="Remove Punctuations")
                        ex_expand_contraction_gt = gr.Checkbox(label="Expand Contractions")
                        ex_expand_abbrev_gt = gr.Checkbox(label="Expand Abbreviations")
                        ex_correct_spelling_gt = gr.Checkbox(label="Correct Spellings")
                        ex_lemmatise_gt = gr.Checkbox(label="Lemmatise")
        
                    example_button_gt = gr.Button("Try an Example")
        
                    example_button_gt.click(
                        fn=random_example_get_tokens,
                        inputs=[],
                        outputs=[
                            example_input_gt,
                            ex_lowercase_gt,
                            ex_remove_stopwords_gt,
                            ex_remove_html_gt,
                            ex_remove_emoji_gt,
                            ex_remove_whitespaces_gt,
                            ex_remove_punctuations_gt,
                            ex_expand_contraction_gt,
                            ex_expand_abbrev_gt,
                            ex_correct_spelling_gt,
                            ex_lemmatise_gt,
                            example_output_gt,
                        ]
                    )
        
                with gr.TabItem("Try Yourself"):
                    with gr.Row():
                        with gr.Column():
                            lowercase_gt = gr.Checkbox(label="Lowercase", value=True)
                            remove_stopwords_gt = gr.Checkbox(label="Remove Stop Words", value=True)
                            remove_html_gt = gr.Checkbox(label="Remove HTML tags", value=True)
                            remove_emoji_gt = gr.Checkbox(label="Remove Emojis", value=True)
                            remove_whitespaces_gt = gr.Checkbox(label="Remove White Spaces", value=True)
                            remove_punctuations_gt = gr.Checkbox(label="Remove Punctuations", value=True)
                            expand_contraction_gt = gr.Checkbox(label="Expand Contractions", value=True)
                            expand_abbrev_gt = gr.Checkbox(label="Expand Abbreviations", value=True)
                            correct_spelling_gt = gr.Checkbox(label="Correct Spellings", value=True)
                            lemmatise_gt = gr.Checkbox(label="Lemmatise", value=True)
                        with gr.Column():
                            input_text_gt = gr.Textbox(label="Enter your text", lines=8, placeholder="Paste text here...")
                            output_text_gt = gr.Textbox(label="Extracted Tokens", lines=8)
        
                            with gr.Row():
                                submit_btn_gt = gr.Button("Submit")
                                clear_btn_gt = gr.Button("Clear")
        
                    submit_btn_gt.click(
                        fn=get_tokens_for_text,
                        inputs=[
                            input_text_gt,
                            lowercase_gt,
                            remove_stopwords_gt,
                            remove_html_gt,
                            remove_emoji_gt,
                            remove_whitespaces_gt,
                            remove_punctuations_gt,
                            expand_contraction_gt,
                            expand_abbrev_gt,
                            correct_spelling_gt,
                            lemmatise_gt,
                        ],
                        outputs=output_text_gt
                    )
        
                    clear_btn_gt.click(
                        fn=clear_all,
                        inputs=[],
                        outputs=[
                            input_text_gt,
                            lowercase_gt,
                            remove_stopwords_gt,
                            remove_html_gt,
                            remove_emoji_gt,
                            remove_whitespaces_gt,
                            remove_punctuations_gt,
                            expand_contraction_gt,
                            expand_abbrev_gt,
                            correct_spelling_gt,
                            lemmatise_gt,
                            output_text_gt,
                        ]
                    )
    
    gr.HTML(f"""
        <a href="{paypal_url}" target="_blank">
            <button style="background-color:#0070ba;color:white;border:none;padding:10px 20px;
            font-size:16px;border-radius:5px;cursor:pointer;margin-top:10px;">
                ❤️ Support Research via PayPal
            </button>
        </a>
        """)

    # Triggered on load
    app.load(
        fn=random_example,
        inputs=[],
        outputs=[
            example_input,
            ex_lowercase,
            ex_remove_stopwords,
            ex_remove_html,
            ex_remove_emoji,
            ex_remove_whitespaces,
            ex_remove_punctuations,
            ex_expand_contraction,
            ex_expand_abbrev,
            ex_correct_spelling,
            ex_lemmatise,
            example_output,
        ]
    )

if __name__ == "__main__":
    # Determine if running on Hugging Face Spaces
    on_spaces = os.environ.get("SPACE_ID") is not None
    
    # Launch the app conditionally
    app.launch(share=not on_spaces, debug=True)